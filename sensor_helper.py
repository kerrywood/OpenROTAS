import ctypes 
import numpy as np
import pandas as pd
from astrostandards.utils import helpers

# -----------------------------------------------------------------------------------------------------
def llh_to_eci( lat : float,
                lon : float,
                alt : float,
                df : list[ float ],
                INTERFACE ) :
    '''
    given a lat / lon / alt tuple and a set of astrostandard epoch'd dates,
    give back the ECI position (TEME)
    '''
    sen_eci = (ctypes.c_double * 3)()
    llh = (ctypes.c_double * 3)( lat, lon, alt )
    def getECI( ds50u ):
        INTERFACE.AstroFuncDll.LLHToXYZTime( ds50u, llh, sen_eci )
        return list( sen_eci )
    return [ getECI(X) for X in df['ds50_utc'] ]


# -----------------------------------------------------------------------------------------------------
def sun_at_time(  df : pd.DataFrame, # must have the times set
                  INTERFACE ):
    sun_v  = (ctypes.c_double * 3)()
    sun_m  = ctypes.c_double()
    # the routine gives us a look vector and magnitude
    sun_p = (ctypes.c_double * 3)( * (np.array( sun_v ) * sun_m ) )
    # compute the sun location at times 
    def getSun( X ):
        INTERFACE.AstroFuncDll.CompSunPos( X, sun_v, sun_m ) 
        return list( (ctypes.c_double * 3)( * (np.array( sun_v ) * sun_m ) ) )
    return [ getSun(X)  for X in df['ds50_et'] ]

# -----------------------------------------------------------------------------------------------------
def moon_at_time(  df : pd.DataFrame, # must have the times set
                  INTERFACE ):
    sun_v  = (ctypes.c_double * 3)()
    sun_m  = ctypes.c_double()
    # the routine gives us a look vector and magnitude
    sun_p = (ctypes.c_double * 3)( * (np.array( sun_v ) * sun_m ) )
    # compute the sun location at times 
    def getMoon( X ):
        INTERFACE.AstroFuncDll.CompMoonPos( X, sun_v, sun_m ) 
        return list( (ctypes.c_double * 3)( * (np.array( sun_v ) * sun_m ) ) )
    return [ getMoon(X)  for X in df['ds50_et'] ]



# =====================================================================================================
if __name__ == "__main__":
    from datetime import datetime,timedelta
    from astrostandards.utils import load_utils as harness
    import time_helpers

    # init all the Dll's
    harness.init_all()

    # use the TimeFunc to load the time parameters file (need to upate this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(  harness.Cstr('./full_time_constants.dat',512) )

    # generate some test data
    now   = datetime.utcnow()
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]

    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )


    # test the llh_to_eci function
    dates_f['sensor_eci'] = llh_to_eci( 0, 0, 0, dates_f, harness )
    print(dates_f)

    print( sun_at_time( dates_f, harness ) )
    print( moon_at_time( dates_f, harness ) )

