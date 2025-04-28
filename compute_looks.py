import ctypes 
import numpy as np
import pandas as pd
from astrostandards.utils import helpers

# -----------------------------------------------------------------------------------------------------
def get_looks(     df_sensor : pd.DataFrame,
                   df_object : pd.DataFrame,
                   INTERFACE ):
    '''
    those frames must be time-aligned; that's up to you
    
    each row must have 
        ds50_utc 
        
        '''
    # we need a data holder for the output of ECIToTopoComps
    TOPO = helpers.astrostd_named_fields( INTERFACE.AstroFuncDll, prefix='XA_TOPO_' )
    
    # check that the dates are aligned
    for A,B in zip( df_object['ds50_utc'].values, df_sensor['ds50_utc'].values) : 
        assert np.isclose(A,B,.0000001)
    
    tdf = pd.concat( (df_sensor.add_suffix('_sensor'), df_object.add_suffix('_object')), 
                    axis=1 )
    
    def calcLooks( R ):
        lst = np.radians( R['lon_sensor'] ) + R['theta_sensor']
        if 'eci_v_object' in R: 
            eci_v_object = (ctypes.c_double * 3)( *R['eci_v_object'] )
        else: 
            eci_v_object = (ctypes.c_double * 3)(0,0,0)
        INTERFACE.AstroFuncDll.ECIToTopoComps( lst, 
                                               R['lat_sensor'], 
                                               (ctypes.c_double * 3) (*R['eci_p_sensor']), 
                                               (ctypes.c_double * 3) (*R['eci_p_object']), 
                                               eci_v_object, 
                                               TOPO.data )
        # INTERFACE.AstroFuncDll.ECIToTopoComps( lst, lat, sen_eci, sun_p, fake_v, SUN_TOPO.data )
        return TOPO.toDict()    

    ans =  pd.DataFrame.from_records( tdf.apply( calcLooks, axis=1 ) )
    return pd.concat( (tdf,ans), axis=1 )


# =====================================================================================================
if __name__ == "__main__":
    from datetime import datetime,timedelta,timezone
    from astrostandards.utils import load_utils as harness
    import time_helpers
    import sensor_helper

    # init all the Dll's
    harness.init_all()

    # use the TimeFunc to load the time parameters file (need to upate this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(  harness.Cstr('./full_time_constants.dat',512) )

    # generate some test data
    now   = datetime.now( timezone.utc )
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    # ---------------- SENSOR FRAME ----------------
    # now that we have a time frame, copy it and make sensor objects
    sensor_f = dates_f.copy()
    # this is a ground sensor, so we need to set the position information
    sensor_f['lat']    = 0
    sensor_f['lon']    = 0
    sensor_f['height'] = 0
    # and the key field is the position...
    sensor_f           = sensor_helper.llh_to_eci( sensor_f, harness )

    # ---------------- TARGET FRAME ----------------
    # same dates... required
    target_f = dates_f.copy()
    # pick a target; in this case.. the sun
    target_f['eci_p'] = sensor_helper.sun_at_time( target_f, harness )

    # calculate the looks    
    results = get_looks( sensor_f, target_f, harness )
    print( results )
    # look at the elevation
    print( results['XA_TOPO_EL']) 
    # find those entries when the sun is down
    print( results[ results['XA_TOPO_EL'] < 0 ] )



