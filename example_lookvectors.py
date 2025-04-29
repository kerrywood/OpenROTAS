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

# =====================================================================================================
if __name__ == '__main__':
    from datetime import datetime,timedelta,timezone
    import pandas as pd
    
    from astrostandards.utils import load_utils as harness
    import time_helpers
    import sgp4_prop
    import sensor_helper
    import compute_looks


    ## STEP 1 : set up the AstroStandards DLL's and init the time constants
    # init all the Dll's
    harness.init_all()
    # use the TimeFunc to load the time parameters file (need to upate this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(  harness.Cstr('./full_time_constants.dat',512) )
    
    ## STEP 2 : setup some dates that we'll investigate
    # generate some test data
    now   = datetime.now( timezone.utc )
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    ## STEP 3 : propagate a TLE to the dates we setup
    # some test TLE data
    L1='1 99999U 00000A   23038.45547454 +.00000000 +46171+0 +33000-1 4 99992'
    L2='2 99999   9.7332 113.4837 7006332 206.5371  38.9576 01.00149480000003'
    # generate some ephemeris
    ephem_f = sgp4_prop.sgp4_prop( L1, L2, dates_f['ds50_utc'] , harness )
    # concat those frames so that dates and eph work together
    ephem_f = pd.concat( (dates_f.copy(),ephem_f), axis=1 )
    
    # STEP 4 : setup a ground sensor
    sensor_f = dates_f.copy()
    # the ground sensor never moves...
    sensor_f ['lat']    = 0
    sensor_f ['lon']    = 0
    sensor_f ['height'] = 0
    # but we need that ECI position to use the look vec calculator
    sensor_f = sensor_helper.llh_to_eci( sensor_f, harness )
    
    ## FINAL step : compute the look vectors to the satellite at that time
    looks = compute_looks.compute_looks( sensor_f, ephem_f, harness )
    print(looks)