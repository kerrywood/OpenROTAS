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

# -----------------------------------------------------------------------------------------------------
# KNW : make sure to add a sensor that corresponds to your obs.. because AstroStandards
def add_sensor( sensor_number , harness):
    # this can be nonsensical because you're going to use type-9
    posECR = (ctypes.c_double * 3)(0.,0.,0.)
    # need a name
    sensor_name = ctypes.create_string_buffer( 24 )
    sensor_name.value = 'SUPERCOOLSENSOR'.encode()

    return harness.SensorDll.SensorSetLocAll(   
                                        sensor_number,
                                        0.,
                                        0.,
                                        posECR,
                                        sensor_name, 
                                        99999,
                                        ctypes.c_char(b'U'))
# -----------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------
def addTLE( L1  : str, L2 : str, harness ):
    # load the TLE and init SGP4
    tleid = harness.TleDll.TleAddSatFrLines(
                                          harness.Cstr(L1, 512),
                                          harness.Cstr(L2, 512))
    # assert that TLE was added 
    assert tleid > 0
    # init the TLE
    assert harness.Sgp4PropDll.Sgp4InitSat( tleid ) == 0
    return tleid

# -----------------------------------------------------------------------------------------------------

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
        c_ext_arr
    )

    return obKey


def plot_residuals(datetimes, res1, res1_name, res2, res2_name, astats):
    import matplotlib.pyplot as plt
    import matplotlib.lines as mlines

    # Define marker styles for each discrete value
    marker_map = {
        0: ('x', 'ASTAT 0'),
        1: ('o', 'ASTAT 1'),
        2: ('s', 'ASTAT 2'),
        3: ('^', 'ASTAT 3'),
        4: ('D', 'ASTAT 4'),
    }

    # Color palette
    color1 = '#1f77b4'  # Blue
    color2 = '#ff7f0e'  # Orange

    x = datetimes
    y1 = np.array(res1)
    y2 = np.array(res2)

    # Create plot with primary y-axis
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # Apply grid
    ax1.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)

    # Plot y1 with marker styles based on marker_type
    for val in np.unique(astats):
        (marker, _) = marker_map[val]
        mask = astats == val
        ax1.scatter(x[mask], y1[mask], marker=marker, color=color1, s=10)

    ax1.set_ylabel(res1_name, color=color1, fontsize=12, fontweight='bold')
    #ax1.tick_params(axis='y', labelcolor=color1)
    ax1.set_xlabel('Times', fontsize=12, fontweight='bold')

    # Create secondary y-axis
    ax2 = ax1.twinx()

    # Plot y2 with marker styles based on marker_type
    for val in np.unique(astats):
        (marker, _) = marker_map[val]
        mask = astats == val
        ax2.scatter(x[mask], y2[mask], marker=marker, color=color2, s=10)
    ax2.set_ylabel(res2_name, color=color2, fontsize=12, fontweight='bold')
    #ax2.tick_params(axis='y', labelcolor=color2)

    # Custom legend with one entry per marker type
    legend_handles = [
        mlines.Line2D([], [], color='black', marker=marker, linestyle='None', markersize=8, label=label)
        for marker, label in marker_map.values()
    ]

    fig.legend(legend_handles, [label for _, label in marker_map.values()],
               loc='upper center', bbox_to_anchor=(0.5, 0.95), ncol=5, frameon=False, fontsize=10)

    plt.tight_layout()
    y1_max = max(y1)
    y2_max = max(y2)
    y_max = max(y1_max,y2_max)
    ax1.set_ylim(top=y_max * 1.4)
    ax2.set_ylim(top=y_max * 1.4)
    plt.show()


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

    from utils.wrappers.RotasWrapper import (
        XA_OBSRES_AGE,
        XA_OBSRES_ASTAT,
        XA_OBSRES_AZ,
        XA_OBSRES_BETA,
        XA_OBSRES_DEC,
        XA_OBSRES_DELTAT,
        XA_OBSRES_HEIGHT,
        XA_OBSRES_POSU,
        XA_OBSRES_POSV,
        XA_OBSRES_POSW,
        XA_OBSRES_RA,
        XA_OBSRES_SIZE
    )


    ## STEP 1 : set up the AstroStandards DLL's and init the time constants
    # init all the Dll's
    if sys.platform.startswith('linux'):
        #from astrostandards.utils import load_utils as harness
        import load_utils as harness
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
    iss_df = sensor_helper.llh_to_efg(iss_df, harness)
    
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

    # -----------------------------------------------------------------------------------------------------
    # KNW : add in the sensor
    add_sensor( 504, harness )
    # -----------------------------------------------------------------------------------------------------

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # JAW: Turns out, we didn't need this block
    # KNW : so, that sgp4_prop routine removes all TLE's when it is called; since you did two TLE's, you blew
    # the first one away and it is no longer loaded in the astrostandards
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #print('Re-setting, reloading, and init-ing TLE')
    #harness.TleDll.TleRemoveAllSats()
    #harness.Sgp4PropDll.Sgp4RemoveAllSats()
    #iss_key = addTLE(
    #                '1 25544U 98067A   25119.19035294  .00013779  00000-0  25440-3 0  9996',
    #                '2 25544  51.6352 189.7367 0002491  81.0639 279.0631 15.49383308507563',
    #                harness )
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # Calculate the residuals for each ob
    astats, ra_res, dec_res, t_res, beta_res = [], [], [], [], []

    # JW - function for debugging
    # Plotting the trajectory of the sensor and object to ensure LOS
    # plot_trajectories(iss_ephem.teme_p, tdrs_ephem.teme_p)

    for ob_idx in range(len(looks)):

        # Create an xa_obs array for a type 8 ob (azimuth, elevation, sensor location)
        snsr_pos_efg = iss_df.iloc[ob_idx].efg_p
        obKey = create_observation(looks.iloc[ob_idx], snsr_pos_efg, harness)

        # Check to see if a single ob associates
        astat_bool = harness.RotasDll.RotasHasASTAT(obKey, tdrs_key)

        # Create variables to hold the ROTAS output info
        xa_ObsRes = (ctypes.c_double * XA_OBSRES_SIZE)()
        satElts = (ctypes.c_double * 9)()
        obElts = (ctypes.c_double * 9)()

        # Compute ROTAS residuals
        if astat_bool:
            error_code = harness.RotasDll.RotasComputeObsResiduals(obKey, tdrs_key, xa_ObsRes, satElts, obElts)
            if not error_code:
                astats.append(xa_ObsRes[XA_OBSRES_ASTAT])
                ra_res.append(xa_ObsRes[XA_OBSRES_RA])
                dec_res.append(xa_ObsRes[XA_OBSRES_DEC])
                t_res.append(xa_ObsRes[XA_OBSRES_DELTAT])
                beta_res.append(xa_ObsRes[XA_OBSRES_BETA])
            else:
                print('Error calculating resiudals!')

    # Plot RA/DEC residuals
    plot_residuals(looks.datetime_object, ra_res, 'Right Ascension Residuals [deg]', dec_res, 'Declination Residuals [deg]', astats)

    # Plot Beta and deltaT residuals
    plot_residuals(looks.datetime_object, t_res, 'deltaT', beta_res, 'Beta', astats)

    # Plot Beta slope and deltaT slope residuals