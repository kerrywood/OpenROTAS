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
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from datetime import datetime,timedelta,timezone
    import pandas as pd
    
    from astrostandards.utils import load_utils as harness
    from OpenROTAS import time_helpers
    from OpenROTAS import sgp4_prop
    from OpenROTAS import sensor_helper
    from OpenROTAS import compute_looks


    ## STEP 1 : set up the AstroStandards DLL's and init the time constants
    # init all the Dll's
    harness.init_all()
    # use the TimeFunc to load the time parameters file (need to upate this periodically)
    harness.TimeFuncDll.TimeFuncLoadFile(  harness.Cstr('./full_time_constants.dat',512) )
    
    ## STEP 2 : setup some dates that we'll investigate
    # generate some test data
    now   = datetime(year=2025,month=4,day=30)
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    
    # STEP 3 : generate ephem for our two satellites, setup frames with necessary data
    iss_ephem = sgp4_prop.sgp4_prop( 
                                    '1 25544U 98067A   25119.19035294  .00013779  00000-0  25440-3 0  9996',
                                    '2 25544  51.6352 189.7367 0002491  81.0639 279.0631 15.49383308507563',
                                    dates_f['ds50_utc'] , 
                                    harness )
    iss_df = pd.concat( (dates_f.copy(), iss_ephem), axis=1 )
    iss_df = sensor_helper.eci_to_llh( iss_df, harness )
    
    tdrs_ephem = sgp4_prop.sgp4_prop( 
                                    '1 27566U 02055A   25119.03837147 -.00000224  00000-0  00000+0 0  9997',
                                    '2 27566   9.5417  47.8538 0008706 288.8984 161.9044  1.00666936 82076',
                                    dates_f['ds50_utc'] , 
                                    harness )
    tdrs_df = pd.concat( (dates_f.copy(), tdrs_ephem), axis=1 )
    tdrs_df = sensor_helper.eci_to_llh( tdrs_df, harness )
    
    ## STEP 4 : compute looks from LEO to GEO
    looks = compute_looks.compute_looks( iss_df, tdrs_df, harness )
    # dates are duplicated because we fused the frames for looks, "sensor" is the sensor column
    print(looks[['datetime_sensor','XA_TOPO_RANGE','XA_TOPO_AZ','XA_TOPO_EL','XA_TOPO_RA','XA_TOPO_DEC']] )
    print(looks.columns)