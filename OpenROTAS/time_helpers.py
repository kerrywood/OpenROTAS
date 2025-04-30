# ###############################################################################
# MIT License

# Copyright (c) 2025 Kerry N. Wood (kerry.wood@asterism.ai)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ###############################################################################

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
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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

