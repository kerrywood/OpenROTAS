# ###############################################################################
# MIT License
import ctypes
from dnd.math.linalg.vectors._vector_3d import Vector3D

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

def plot_trajectories(sat1_positions, sat2_positions):
    import numpy as np
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot the satellite trajectories
    ax.plot(sat1_positions.apply(lambda x: x[0]).iloc[::10],
                       sat1_positions.apply(lambda x: x[1]).iloc[::10],
                       sat1_positions.apply(lambda x: x[2]).iloc[::10], label='Satellite 1', color='blue')
    ax.plot(sat2_positions.apply(lambda x: x[0]).iloc[::10],
                       sat2_positions.apply(lambda x: x[1]).iloc[::10],
                       sat2_positions.apply(lambda x: x[2]).iloc[::10], label='Satellite 2', color='red')

    # Plot Earth as a sphere (for reference)
    r_earth = 6371  # Earth's radius in km
    u, v = np.mgrid[0:2 * np.pi:50j, 0:np.pi:25j]
    x = r_earth * np.cos(u) * np.sin(v)
    y = r_earth * np.sin(u) * np.sin(v)
    z = r_earth * np.cos(v)
    ax.plot_surface(x, y, z, color='lightblue', alpha=0.3)

    #for i in range(0, len(sat1_positions), 10):  # every 10th time step
    for i in range(50,100):
        pos1 = sat1_positions.iloc[i]
        pos2 = sat2_positions.iloc[i]
        ax.plot([pos1[0], pos2[0]],
                [pos1[1], pos2[1]],
                [pos1[2], pos2[2]],
                color='gray', linestyle='--', linewidth=0.5)

    # Labels and legend
    ax.set_xlabel('X (km)')
    ax.set_ylabel('Y (km)')
    ax.set_zlabel('Z (km)')
    ax.set_title('Satellite Trajectories in ECI Frame')
    ax.legend()
    ax.grid(True)

    # Equal aspect ratio
    max_range = np.array([sat2_positions.apply(lambda x: x[0]).max() - sat2_positions.apply(lambda x: x[0]).min(),
                          sat2_positions.apply(lambda x: x[1]).max() - sat2_positions.apply(lambda x: x[1]).min(),
                          sat2_positions.apply(lambda x: x[2]).max() - sat2_positions.apply(lambda x: x[2]).min()]).max() / 2.0

    mid_x = (sat2_positions.apply(lambda x: x[0]).max() + sat2_positions.apply(lambda x: x[0]).min()) * 0.5
    mid_y = (sat2_positions.apply(lambda x: x[1]).max() + sat2_positions.apply(lambda x: x[1]).min()) * 0.5
    mid_z = (sat2_positions.apply(lambda x: x[2]).max() + sat2_positions.apply(lambda x: x[2]).min()) * 0.5

    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)

    plt.show()


def create_observation(X, snsr_pos_efg, INTERFACE):
    c_class = ctypes.c_char("U".encode())
    c_sat_no = ctypes.c_int(4881)
    c_sen_no = ctypes.c_int(504)
    c_epoch = ctypes.c_double(X.ds50_utc_sensor)
    c_dec = ctypes.c_double(X.XA_TOPO_DEC)
    c_ra = ctypes.c_double(X.XA_TOPO_RA)
    c_obs_type = ctypes.c_char("9".encode())
    c_vel = Vector3D.null_pointer()
    c_ext_arr = (ctypes.c_double * 128)()
    c_snsr_pos = Vector3D(snsr_pos_efg[0], snsr_pos_efg[1], snsr_pos_efg[2]).to_c_array()


    obKey = INTERFACE.ObsDll.ObsAddFrFields(
        c_class,
        c_sat_no,
        c_sen_no,
        c_epoch,
        c_dec,
        c_ra,
        ctypes.c_double(0), # range
        ctypes.c_double(0), # range rate
        ctypes.c_double(0), # el rate
        ctypes.c_double(0), # az rate
        ctypes.c_double(0), # range accel
        c_obs_type,
        ctypes.c_int(3), # track ind
        ctypes.c_int(2), # astat
        ctypes.c_int(4881), # site tag
        ctypes.c_int(4881), # spadoc tag
        c_snsr_pos,
        c_vel,
        c_ext_arr,
    )

    '''
    ob = looks.iloc[0]
    c_double_64 = ctypes.c_double * 64
    xa_obs = c_double_64()
    xa_obs[0] = ctypes.c_double(1)  # classification 1 = Unclassified, 2 = Confidential, 3 = SECRET
    xa_obs[1] = ctypes.c_double(4881)  # satellite number
    xa_obs[2] = ctypes.c_double(504)  # sensor number
    xa_obs[3] = ctypes.c_double(ob.ds50_utc_sensor)  # observation time in days since 1950 UTC
    xa_obs[11] = ctypes.c_double(9)  # ob type
    xa_obs[4] = ctypes.c_double(ob.XA_TOPO_DEC)  # declination
    xa_obs[5] = ctypes.c_double(ob.XA_TOPO_RA)  # right ascension
    xa_obs[16] = ctypes.c_double(snsr_pos_efg[0])
    xa_obs[17] = ctypes.c_double(snsr_pos_efg[1])
    xa_obs[18] = ctypes.c_double(snsr_pos_efg[2])
    # Create an Obs object from the array
    obKey = harness.ObsDll.ObsAddFrArray(xa_obs)
    '''

    return obKey


# =====================================================================================================
if __name__ == '__main__':
    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    from datetime import datetime,timedelta,timezone
    import numpy as np
    import pandas as pd

    from OpenROTAS import time_helpers
    from OpenROTAS import sgp4_prop
    from OpenROTAS import sensor_helper
    from OpenROTAS import compute_looks


    ## STEP 1 : set up the AstroStandards DLL's and init the time constants
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
    
    ## STEP 2 : setup some dates that we'll investigate
    # generate some test data
    now   = datetime(year=2025,month=4,day=30)
    dates = [ now + timedelta( minutes=X ) for X in range(0,1440) ]
    # use the time_helpers to initialize the dataframe with times
    dates_f = time_helpers.convert_times( dates, harness )
    
    
    # STEP 3 : generate ephem for our two satellites, setup frames with necessary data
    iss_key, iss_ephem = sgp4_prop.sgp4_prop(
                                    '1 25544U 98067A   25119.19035294  .00013779  00000-0  25440-3 0  9996',
                                    '2 25544  51.6352 189.7367 0002491  81.0639 279.0631 15.49383308507563',
                                    dates_f['ds50_utc'],
                                    harness )
    iss_df = pd.concat( (dates_f.copy(), iss_ephem), axis=1 )
    iss_df = sensor_helper.eci_to_llh( iss_df, harness )
    
    tdrs_key, tdrs_ephem = sgp4_prop.sgp4_prop(
                                    '1 27566U 02055A   25119.03837147 -.00000224  00000-0  00000+0 0  9997',
                                    '2 27566   9.5417  47.8538 0008706 288.8984 161.9044  1.00666936 82076',
                                    dates_f['ds50_utc'] , 
                                    harness )
    tdrs_df = pd.concat( (dates_f.copy(), tdrs_ephem), axis=1 )
    tdrs_df = sensor_helper.eci_to_llh( tdrs_df, harness )
    tdrs_df = sensor_helper.llh_to_efg( tdrs_df, harness )
    
    ## STEP 4 : compute looks from LEO to GEO
    looks = compute_looks.compute_looks( iss_df, tdrs_df, harness )

    looks_reversed = compute_looks.compute_looks(tdrs_df, iss_df, harness)
    # dates are duplicated because we fused the frames for looks, "sensor" is the sensor column
    #print(looks[['datetime_sensor','XA_TOPO_RANGE','XA_TOPO_AZ','XA_TOPO_EL','XA_TOPO_RA','XA_TOPO_DEC']] )
    #print(looks.columns)


    # Create an xa_obs array for a type 8 ob (azimuth, elevation, sensor location)
    snsr_pos_efg = tdrs_df.iloc[0].efg_p
    obKey = create_observation(looks.iloc[0], snsr_pos_efg, harness)

    # Check that the ob was created
    posx = ctypes.create_string_buffer(513)
    harness.ObsDll.ObsGetField(obKey, 19, posx)
    print('Ob snsr position X:', posx.value)

    # JW - code block for debugging
    # Perturb the ra/dec measurements until we find something that associates
    ras = np.arange(-180, 181, 0.1)
    decs = np.arange(-90, 91, 0.1)
    for ra in ras:
        for dec in decs:
            harness.ObsDll.ObsSetField(obKey, ctypes.c_int(8), harness.Cstr(str(ra), 512))
            harness.ObsDll.ObsSetField(obKey, ctypes.c_int(6), harness.Cstr(str(dec), 512))
            astat_bool = harness.RotasDll.RotasHasASTAT(obKey, iss_key)
            if astat_bool: break
        if astat_bool: break

    # Hopefully there's a combination of ra/dec that generated an association, printing to screen
    print("RA:", ra, "Dec:", dec)

    # Check to see if a single ob associates
    astat_bool = harness.RotasDll.RotasHasASTAT(obKey, iss_key)

    # JW - function for debugging
    # Plotting the trajectory of the sensor and object to ensure LOS
    #plot_trajectories(iss_ephem.teme_p, tdrs_ephem.teme_p)

    # Create variables to hold the ROTAS output info
    c_double_100 = ctypes.c_double * 100
    c_double_9 = ctypes.c_double * 9
    xa_ObsRes = c_double_100()
    satElts = c_double_9()
    obElts = c_double_9()

    # Compute ROTAS residuals
    error_code = harness.RotasDll.RotasComputeObsResiduals(obKey, iss_key, xa_ObsRes, satElts, obElts)
    print(error_code)
    print('xa_ObsRes:', xa_ObsRes[0:10])
    print()