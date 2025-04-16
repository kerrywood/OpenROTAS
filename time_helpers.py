from datetime import datetime 
import pandas as pd
from astrostandards.utils import helpers

# -----------------------------------------------------------------------------------------------------
def convert_times( datetimes : list[ datetime ] ,
                   INTERFACE ):
    
    # convert the datetimes to astrostandard epochs
    ds50_utc = [ helpers.datetime_to_ds50( X, INTERFACE.TimeFuncDll ) for X in datetimes ]

    return pd.DataFrame( 
           [ { 'datetime' : X,
               'theta'    : INTERFACE.TimeFuncDll.ThetaGrnwchFK5( Y ),
               'ds50_utc' : Y,
               'ds50_et'  : INTERFACE.TimeFuncDll.UTCToET( Y ),
               'ds50_ut1' : INTERFACE.TimeFuncDll.UTCToUT1( Y ) } for X,Y in zip(datetimes,ds50_utc) ])


# ==================================================================================================
if __name__ == '__main__':
    from datetime import timedelta
    from astrostandards.utils import load_utils as harness

    # init all the Dll's
    harness.init_all()

    # use the TimeFunc to load the time parameters file (need to upate this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(  harness.Cstr('./full_time_constants.dat',512) )

    # generate some test data
    now   = datetime.utcnow()
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    print(dates)
    print(convert_times( dates, harness) )

