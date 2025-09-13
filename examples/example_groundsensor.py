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
    
    import public_astrostandards as harness
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
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440*5) ]
    print()
    print('Selecting some dates : {} -- {}, {} total timesteps'.format( 
                                                                       dates[0], dates[-1], len(dates) ) )
    print()
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    # STEP 3 : compute our frames
    # generate our sensor frame (we'll do this manually)
    sensor_f           = dates_f.copy()   # make a copy of the dates
    sensor_f['lat']    = 38.83
    sensor_f['lon']    = -104.82
    sensor_f['height'] = 1.832 
    # get the ECI for each of those rows
    sensor_f           = sensor_helper.llh_to_eci( sensor_f, harness )

    # generate our TARGET frame
    print('Propagating two TLE to those dates (aligned) and then annotating with LLH (for looks)')
    iss_ephem = sgp4_prop.sgp4_prop( 
                                    '1 25544U 98067A   25119.19035294  .00013779  00000-0  25440-3 0  9996',
                                    '2 25544  51.6352 189.7367 0002491  81.0639 279.0631 15.49383308507563',
                                    dates_f,
                                    harness )
    iss_df = pd.concat( (dates_f.copy(), iss_ephem), axis=1 )
    iss_df = sensor_helper.eci_to_llh( iss_df, harness )
    
    ## STEP 4 : compute looks from LEO to GEO
    # compute looks arguments are <from> <to> <harness> (where from is your observer)
    looks = compute_looks.compute_looks( sensor_f , iss_df, harness )
    # dates are duplicated because we fused the frames for looks, "sensor" is the sensor column
    print('Looks dataframe has columns : {}'.format( looks.columns.values.tolist() ) )
    print()
    COLS = ['datetime_sensor','XA_TOPO_RANGE','XA_TOPO_AZ','XA_TOPO_EL','XA_TOPO_RA','XA_TOPO_DEC']
    print(looks[ COLS ] )

    # EXTRA CREDIT
    # compute the sun and the moon and see where those are.. fuse the answers
    # (you can do this for the moon as well (note that you can re-use sun/moon position if you have multiple calls)
    sun_f           = dates_f.copy()   # make a copy of the dates
    sun_f['teme_p'] = sensor_helper.sun_at_time( sun_f , harness )  # compute where the sun is in ECI, and store it for futher calls
    sun_f           = sensor_helper.eci_to_llh( sun_f, harness )    # annotate those rows with the LLA values (for looks)
    sun_looks       = compute_looks.compute_looks( sensor_f, sun_f, harness ) # compute the looks

    # now fuse them together
    looks = pd.concat( ( looks.add_suffix('_target'),
                         sun_looks.add_suffix('_sun') ), 
                      axis=1)

    # now we can print when ISS is overhead and the sun is down
    good_looks = looks[ ( looks['XA_TOPO_EL_target'] > 0 ) & ( looks['XA_TOPO_EL_sun'] < 0) ]
    NEWCOLS = [X+'_target' for X in COLS]
    print(good_looks[ NEWCOLS ] )
