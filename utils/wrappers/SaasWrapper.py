# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'Saas.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'libsaas.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'libsaas.dylib'

def LoadSaasDll():
   """ LoadSaasDll() -- Loads Saas.dll from the PATH or LD_LIBRARY_PATH
   depending on Operating System and returns the object type.
   for each of its functions.

   Return Value
   an object which can be used to access the dll.""" 

   # load the dll
   try:
      dllObj = CDLL(DLL_NAME)
   except:
      print("Unable to load " + DLL_NAME)
      sys.exit(1)
   # set parameter list and return type for each function


   # Notes: This function has been deprecated since v9.0. 
   # Initializes Saas dll for use in the program
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.SaasInit.restype = c_int
   dllObj.SaasInit.argtypes = [c_longlong]


   # Returns information about the current version of Saas.dll. The information is placed in the
   # string parameter passed-in
   # infoStr: A string to hold information about the Saas.dll (out-Character[128])
   dllObj.SaasGetInfo.restype = None
   dllObj.SaasGetInfo.argtypes = [c_char_p]


   # SaasGetResults executes SAAS (Satellite Attack Assessment Software) also known as DA ASAT
   #   (Direct Ascent Anti-Satellite). 
   # 
   # 
   # SAAS software description:
   # 
   #   SaasGetResults executes SAAS (Satellite Attack Assessment Software) also known as DA ASAT
   #   (Direct Ascent Anti-Satellite). Developed by HQ SpOC, SAAS assesses attack opportunities
   #   for a direct ascent ASAT attack, similar to F-15 ASAT of the 1980's.  By its use of SGP4
   #   propagation, SAAS is designed as a high-speed screening tool to identify potential target
   #   objects in vulnerable orbits relative to the specified missile site/capability; however it
   #   should not be considered a precision analysis model.
   # 
   # 
   # SAAS algorithm:
   # 
   #   SAAS computes a ring of potential intercept points around a launch site.  The size of the
   #   ring (also known as 'the kill ring') is based on the altitude limit and missile profile
   #   specified for the direct ascent booster.  Each target altitude has a unique kill ring with
   #   two intercept points, defined as 'pierce/entry' and exit.  The ring of potential intercept
   #   points span over 360 degrees azimuth above the launch site.  The ring of intercept points
   #   is circumscribed by a cone looking up from the launch site.  Target orbits are flown
   #   (propagated by SGP4) over a specified period of interest and penetrations of the launch site
   #   cone determine a viable intercept passes.  The time of the cone penetration, and/or cone
   #   exit, are the 'intercept times'.  (Note that as the target altitude decreases, the intercept
   #   point moves farther down-range from the launch site; then it moves up-range after the
   #   specified missile max range is reached.) The azimuth from the launch site to the cone
   #   penetration point is the launch azimuth.  Lastly, the launch time is determined as the cone
   #   penetration time minus the missile time-of-flight to the target.
   # 
   # 
   # INPUTS include:
   # 
   # 
   #   table
   #   (a) a set of target input SGP4 two-line element sets (TLEs)
   #   (b) coefficient-based missile profile used for the direct ascent attack trajectory
   #   (c) missile profile limits including min and max height, maximum sun angle, and maximum
   #        attack angle
   #   (d) ground missile location(s) including N. latitude, E. longitude, and height for one or
   #        more test sites
   #   (e) a specified evaluation period of interest for assessment
   # 
   # 
   # 
   # OUTPUTS include:
   #   (a) attack launch time, launch azimuth, and intercept time, for each viable target pass over
   #        a launch site within the specified period of interest
   # 
   # Order of elements in the input xa_msl array:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #   0 missile profile minimum height limit [km]
   #   1 missile profile maximum height limit [km]
   #   2 maximum allowed solar aspect angle [deg], pass qualifies 
   #   3 maximum allowed missile attack angle [deg], pass qualifies only 
   #   4 rejection flag*: -1=reject negative; 0=reject neither negative nor positive; 1=reject positive. 
   #   5 missile profile time coefficient for the X^2 term
   #   6 missile profile time coefficient for the X term
   #   7 missile profile time constant for the C term
   #   8 missile profile range coefficient for the X^2 term
   #   9 missile profile range coefficient for the X term
   #  10 missile profile range constant for the C term
   #  11-31 unused at this time
   #    
   #  (*) The missile rejection flag designation is used by SAAS to check for sign of the desired
   #      attack angles in the results.  It evaluates the sign (+ or -) of the computed attack
   #      angle vs. the maximum allowed attack angle.  For example if set to -1, only positive
   #      attack angles less than the max attack angle will be returned.  If set to 0, either a
   #      positive or negative computed attack angle is acceptable as long as long it is less
   #      than the max allowed attack angle.  If set to 1, only negative attack angles less than
   #      the maximum will be accepted and returned.
   # 
   # Order of elements in the input xa_ls array:   
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #  0 launch test site's latitude (+North, -South)
   #  1 launch test site longitude (+East, -West)
   #  2 launch test site local height above Earth average equatorial radius (meters). 
   #  3-7 unused at this time
   #    
   # 
   # Order of elements in the input xa_saasRun array:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #  0 Maximum number of penetration points allowed. 
   #  1 SAAS assessment period-of-interest (POI) start time in fractional days since 1950, UTC
   #  2 SAAS assessment period-of-interest (POI) stop time in fractional days since 1950, UTC. 
   # 								 Note: if a stop time is not specified, it is defaulted by SAAS to 1 day after the specified start
   # 								 time
   #  3 Specified half-angle of attack cone, where if set to 0, SAAS will automatically determine the attack cone half angle. 
   #   								 Note:  if a input cone angle is > 90 degrees, it is defaulted by SAAS to 90
   #   								 degrees
   #  4-7 unused at this time
   #    
   # 
   # Order of elements in the returned in the first dimension of xa_satPen array (second array
   #  dimension allows similar same results Elements for other viable penetration solutions at
   #  different times during the assessment period of interest):
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #  0 impact time in fractional days since 1950, UTC
   #  1 missile launch time in fractional days since 1950, UTC
   #  2 satellite penetration azimuth [deg]
   #  3 satellite penetration elevation [deg]
   #  4 satellite penetration range [km]
   #  5 satellite penetration range rate [km/s]
   #  6 satellite penetration solar aspect angle [deg]
   #  7 satellite penetration attack angle [deg]
   #  8 satellite height at penetration [km] 
   #  9 ring penetration indicator:  0 = impact time is an 'entry' time; 1 = ring penetration is an 'exit'
   # time
   #  10-15 unused at this time
   #    
   # 
   # Order of elements in the output xa_Ret array:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #  0 number of potential viable attack penetrations (opportunities) identified vs. the target set within the
   # POI
   #  1-15 unused at this time
   #    
   # 
   # xa_saasRet(16) - other saas output:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   #    
   #  0  number of actual satellite penetrations found
   #  1  satellite apogee height (km)
   #  2  satellite perigee height (km)
   #  3  autocone minimum cone half angle (deg)
   #  4  autocone maximum cone half angle (deg)
   #  5-15  not used at this time
   #    
   # satKey: The satellite's unique key (in-Long)
   # xa_saasrun: run parameters (in-Double[8])
   # xa_msl: missile profile data.  see XA_MSL_? (in-Double[32])
   # xa_ls: launch site data.  see XA_LS_? (in-Double[8])
   # xa_satPen: array that stores data of satellite penetrations.  see XA_SATPEN_? (out-Double[*, 16])
   # xa_saasRet: array that stores other SAAS output.  see XA_SAASRET_? (out-Double[16])
   dllObj.SaasGetResults.restype = c_int
   dllObj.SaasGetResults.argtypes = [c_longlong, c_double * 8, c_double * 32, c_double * 8, c_void_p, c_double * 16]


   # Computes auto cone size based on satellite height and missile profile      
   # satHeight: satelite height (km) (in-Double)
   # xa_msl: missile profile data.  see XA_MSL_? (in-Double[32])
   dllObj.SaasAutoConeSize.restype = c_double
   dllObj.SaasAutoConeSize.argtypes = [c_double, c_double * 32]


   # Computes missile time of flight based on satellite height and missile profile  
   # satHeight: satellite height (km) (in-Double)
   # xa_msl: missile profile data.  see XA_MSL_? (in-Double[32])
   dllObj.SaasMissileFlightTime.restype = c_double
   dllObj.SaasMissileFlightTime.argtypes = [c_double, c_double * 32]


   # Computes launch orbital plane (inclination and node) based on the launch data
   # xa_lnch: The input launch data (see XA_LNCH_? for array arrangement) (in-Double[8])
   # incli: The output planer's inclination (deg) (out-Double)
   # node: The output planer's node (deg) (out-Double)
   dllObj.ComputeLnchOrbPlane.restype = None
   dllObj.ComputeLnchOrbPlane.argtypes = [c_double * 8, c_double_p, c_double_p]


   # Compares a satellite elset against a new launch to find planer intersection time and associated data
   # satKey: The satellite's unique key (in-Long)
   # xa_plnr: The input new launch and time of flight data.  see XA_PLNR_? (in-Double[16])
   # xa_intxn: The output planer intersection data.  see XA_INTXN_? (out-Double[16])
   dllObj.FindPlanerIntersection.restype = c_int
   dllObj.FindPlanerIntersection.argtypes = [c_longlong, c_double * 16, c_double * 16]

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj

#*******************************************************************************

# Missile Profile
# missile profile's minimum height limit (km)
XA_MSL_MINHGT  =  0
# missile profile's maximum height limit (km)
XA_MSL_MAXHGT  =  1
# maximum allowed solar aspect angle (deg)
XA_MSL_MAXSA   =  2
# maximum allowed missile attack angle (deg)
XA_MSL_ANGMAX  =  3
# rejection flag (-1: reject negative, 0: reject neg and pos, 1: reject pos)
XA_MSL_REJFLG  =  4
# missile trajectory time coefficient for the *X**2 term [sec]
XA_MSL_TIMCOE1 =  5
# missile trajectory time coefficient for the *X term [sec]
XA_MSL_TIMCOE2 =  6
# missile trajectory time constant for the C term [sec]
XA_MSL_TIMCOE3 =  7
# missile trajectory range coefficient *X**2 term [km]
XA_MSL_RNGCOE1 =  8
# missile trajectory range coefficient *X term [km]
XA_MSL_RNGCOE2 =  9
# missile trajectory range constant for the C term [km]
XA_MSL_RNGCOE3 = 10

XA_MSL_SIZE    = 32

#*******************************************************************************

# Launch site location
# launch site's latitude (deg)  (+N) (-S)
XA_LS_LAT     = 0
# launch site's longitude (deg) (+E) (-W)
XA_LS_LON     = 1
# launch site's height(m)
XA_LS_HEIGHT  = 2

XA_LS_SIZE    = 8

#*******************************************************************************

# Saas run parameters
# Maximum number of penetration points that are allowed
XA_SAASRUN_MAXPENS  = 0
# SAAS start time in days since 1950, UTC
XA_SAASRUN_START    = 1
# SAAS stop time in days since 1950, UTC
XA_SAASRUN_STOP     = 2
# Half angle of attack cone (0=auto)
XA_SAASRUN_HALFCONE = 3

XA_SAASRUN_SIZE     = 8

#*******************************************************************************

# Satellite penetration data
# impact time in days since 1950, UTC
XA_SATPEN_IMPTIME  =  0
# msl launch time in days since 1950, UTC
XA_SATPEN_LAUTIME  =  1
# azimuth (deg)
XA_SATPEN_AZ       =  2
# elevation (deg)
XA_SATPEN_EL       =  3
# range (km)
XA_SATPEN_RANGE    =  4
# range rate (km/s)
XA_SATPEN_RNGRATE  =  5
# solar aspect angle (deg)
XA_SATPEN_SOLANG   =  6
# attack angle (deg)
XA_SATPEN_ATTCKANG =  7
# satellite's height (km)
XA_SATPEN_SATHGHT  =  8
# ring penetration entry or exit time (0=entry, 1=exit)
XA_SATPEN_EN0EX1   =  9

XA_SATPEN_SIZE     = 16

#*******************************************************************************

# SAAS ouput data
# number of actual satellite penetrations
XA_SAASRET_NUMOFPENS =  0
# satellite apogee height (km)
XA_SAASRET_SATAHT    =  1
# satellite perigee height (km)
XA_SAASRET_SATPHT    =  2
# autocone minimum cone half angle (deg)
XA_SAASRET_MINCONE   =  3
# autocone maximum cone half angle (deg)
XA_SAASRET_MAXCONE   =  4




XA_SAASRET_SIZE     = 16

#*******************************************************************************

# predefined values for different orbit types used in planer program
# orbit type LEO
ORBTYPE_LEO = 1
# orbit type MEO
ORBTYPE_MEO = 2
# orbit type GEO
ORBTYPE_GEO = 3

#*******************************************************************************

# indexes of fields specifying parameters for planer intersection program
# launch site latitude (deg)
XA_LNCH_LAT     = 0
# launch site longitude (deg)
XA_LNCH_LON     = 1
# injection azimuth (deg)
XA_LNCH_INJAZ   = 2
# launch time in days since 1950 UTC
XA_LNCH_DS50UTC = 3

XA_LNCH_SIZE    = 8

#*******************************************************************************

# indexes of fields specifying parameters for planer intersection program
# orbital type (LEO = 1, MEO = 2, GEO = 3)
XA_PLNR_ORBTYPE  = 0
# launch site latitude (deg)
XA_PLNR_LSLAT    = 1
# launch site longitude (deg)
XA_PLNR_LSLON    = 2
# launch time in days since 1950 UTC
XA_PLNR_DS50UTC  = 4
# time of flight start (min)
XA_PLNR_TOFFR    = 5
# time of flight end (min)
XA_PLNR_TOFTO    = 6
# planer's inclination (deg)
XA_PLNR_INCLI    = 7
# planer's node (deg)
XA_PLNR_NODE     = 8

XA_PLNR_SIZE     = 16

#*******************************************************************************

# indexes of output data returned by planer intersection program
# time of intersection in days since 1950 UTC
XA_INTXN_DS50UTC = 0
# satellite inclination (deg)
XA_INTXN_INCLI   = 1
# satellite latitude (deg) at the time of the intersection
XA_INTXN_LAT     = 2
# satellite longitude (deg) at the time of the intersection
XA_INTXN_LON     = 3
# satellite height (km) at the time of the intersection
XA_INTXN_HEIGHT  = 4
# time of flight (min) since launch time
XA_INTXN_TOF     = 5
# coplaner angle (deg)
XA_INTXN_COPLANG = 6

XA_INTXN_SIZE    = 16

#*******************************************************************************

# ========================= End of auto generated code ==========================
