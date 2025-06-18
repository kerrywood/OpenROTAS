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
import sys
import ctypes 
import pandas as pd
from datetime import datetime
from utils.astrostds import AstroStds
from utils.wrappers.AstroUtils import *


# ------------------------------------------------------------------------------------------
def sgp4_prop(   line1      : str,            # TLE line1
                 line2      : str,            # TLE line2
                 ds50_utc   : list[ float ],  # astrostandard epoch (UTC)
                 INTERFACE ):

    INTERFACE.TleDll.TleRemoveAllSats()
    INTERFACE.Sgp4PropDll.Sgp4RemoveAllSats()

    # load the TLE and init SGP4
    tleid = INTERFACE.TleDll.TleAddSatFrLines(
                                          INTERFACE.Cstr(line1, 512),
                                          INTERFACE.Cstr(line2, 512))
    
    # assert that TLE was added 
    assert tleid > 0

    # init the TLE
    assert INTERFACE.Sgp4PropDll.Sgp4InitSat( tleid ) == 0

    # holders for output
    pos = (ctypes.c_double * 3)()
    vel = (ctypes.c_double * 3)()
    llh = (ctypes.c_double * 3)()

    def doProp( X ):
        INTERFACE.Sgp4PropDll.Sgp4PropDs50UtcPosVel(
            tleid,
            X,
            pos,
            vel)

        # return np.hstack( (list(pos), list(vel) ) )
        return { 'teme_p' : list(pos), 'teme_v' : list(vel) }

    #datestr = [ ds50_to_str(X) for X in ds50 ]
    return tleid, pd.DataFrame([doProp(X) for X in ds50_utc ] )
    
# ------------------------------------------------------------------------------------------
# def sgp4proc_interval(      line1 : str,            # TLE line1
#                             line2 : str,            # TLE line2
#                             start_date : datetime,
#                             end_date   : datetime,
#                             step       : float ):   # minutes

#     total_steps = (end_date - start_date).total_seconds() / 60  # in minutes
#     isot = [ start_date + timedelta(minutes=step*X) for X in range( int(total_steps) + 1 ) ]
#     return sgp4proc( line1, line2, isot )


# =====================================================================================================
if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

    from datetime import datetime,timedelta,timezone
    import time_helpers

    # init all the Dll's
    if sys.platform.startswith('linux'):
        from astrostandards.utils import load_utils as harness
        harness.init_all()
    elif sys.platform.startswith('win'):
        from utils.astrostds import AstroStds
        harness = AstroStds()
    else:
        raise OSError(f"Unsupported operating system: {sys.platform}")

    # use the TimeFunc to load the time parameters file (need to update this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(harness.Cstr('./full_time_constants.dat', 512))

    # generate some test data
    now   = datetime.now( timezone.utc )
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    # some test TLE data
    L1='1 99999U 00000A   23038.45547454 +.00000000 +46171+0 +33000-1 4 99992'
    L2='2 99999   9.7332 113.4837 7006332 206.5371  38.9576 01.00149480000003'

    key = harness.TleDll.TleAddSatFrLines(L1.encode('utf-8'),L2.encode('utf-8'))

    print(key)

    #L1 = '1 99999U F0078521 23129.36741898 0.00000000 +71470-1 +36483-1 4 00003'
    #L2 = '2 99999  11.1157 135.4398 4764778 123.8103 223.8499  1.83169650000003'

    # ISS May 31 2025
    L1 = '1 25544U 98067A   25151.88784326  .00010887  00000-0  19918-3 0  9995'
    L2 = '2 25544  51.6366  27.8423 0001867 174.0070 186.0942 15.49897373512639'
    
    # generate some ephemeris
    satKey, ephemeris = sgp4_prop( L1, L2, dates_f['ds50_utc'] , harness )
    
    # concat those frames so that dates and eph work together
    ephemeris = pd.concat( (dates_f,ephemeris), axis=1 )
    print( ephemeris )