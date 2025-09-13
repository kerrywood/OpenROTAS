import ctypes 
import numpy as np
import pandas as pd
# from astrostandards.utils import helpers

# -----------------------------------------------------------------------------------------------------
def llh_to_eci( df : pd.DataFrame,
                INTERFACE ) :
    '''
    assume that the dataframe "df" has lat / lon / height and ds50_utc (from time_helpers)

    this will annotate the frame with the LLA for each row entry
    '''
    sen_eci = (ctypes.c_double * 3)()
    def getECI( R ):
        llh = (ctypes.c_double * 3)( R['lat'], R['lon'], R['height'] )
        INTERFACE.AstroFuncDll.LLHToXYZTime( R['ds50_utc'], llh, sen_eci )
        return list( sen_eci )
    df['teme_p'] =  df.apply( getECI, axis=1 )
    return df


# -----------------------------------------------------------------------------------------------------
def eci_to_llh( df : pd.DataFrame,
                INTERFACE ) :
    '''
    assuming dataframe "df" has "teme_p" and ds50_utc in each row (TEME position vector and ds50 from time_helpers)
    annotate the frame with the lat lon height of each of those rows
    '''
    llh  = (ctypes.c_double * 3)()
    
    def getLLH( R ):
        eci = (ctypes.c_double * 3)( *R['teme_p'] )
        INTERFACE.AstroFuncDll.XYZToLLHTime( R['ds50_utc'], eci, llh ) 
        return list( llh )
    
    tv = df.apply( getLLH, axis=1 )
    df['lat']    = [ T[0] for T in tv ]
    df['lon']    = [ T[1] for T in tv ]
    df['height'] = [ T[2] for T in tv ]
    return df

# -----------------------------------------------------------------------------------------------------
def sun_at_time(  df : pd.DataFrame, # must have the times set
                  INTERFACE ):
    '''
    assume that df has been prepared like time_helpers outputs

    return the position of the sun at those times (do NOT annotate frame)
    '''
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
    '''
    assume that df has been prepared like time_helpers outputs

    return the position of the moon at those times (do NOT annotate frame)
    '''
    moon_v  = (ctypes.c_double * 3)()
    moon_m  = ctypes.c_double()
    # the routine gives us a look vector and magnitude
    moon_p = (ctypes.c_double * 3)( * (np.array( moon_v ) * sun_m ) )
    # compute the moon location at times 
    def getMoon( X ):
        INTERFACE.AstroFuncDll.CompMoonPos( X, moon_v, moon_m ) 
        return list( (ctypes.c_double * 3)( * (np.array( moon_v ) * moon_m ) ) )
    return [ getMoon(X)  for X in df['ds50_et'] ]



# =====================================================================================================
if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

    from datetime import datetime,timedelta
    import public_astrostandards as harness
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
    dates_f ['lat']    = 0
    dates_f ['lon']    = 0
    dates_f ['height'] = 0
    dates_f = llh_to_eci( dates_f, harness )
    print(dates_f)

    # annotate that dataframe wih the sun position
    dates_f['sun_teme_p']  = sun_at_time( dates_f, harness ) 
    dates_f['moon_teme_p'] = moon_at_time( dates_f, harness ) 
    
    dates_f['eci_p'] = dates_f['sun_teme_p']
    eci_to_llh( dates_f, harness )
    
    print(dates_f)
    

