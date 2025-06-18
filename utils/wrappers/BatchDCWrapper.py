# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'BatchDC.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'libbatchdc.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'libbatchdc.dylib'

def LoadBatchDCDll():
   """ LoadBatchDCDll() -- Loads BatchDC.dll from the PATH or LD_LIBRARY_PATH
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
   # Initializes BatchDC DLL for use in the program
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.BatchDCInit.restype = c_int
   dllObj.BatchDCInit.argtypes = [c_longlong]


   # Returns information about the current version of BatchDC DLL. 
   # The information is placed in the string parameter passed in.
   # infoStr: A string to hold the information about BatchDC.dll (out-Character[128])
   dllObj.BatchDCGetInfo.restype = None
   dllObj.BatchDCGetInfo.argtypes = [c_char_p]


   # Read/Load BatchDC input data from an input file
   # batchDCInputFile: The name of the file containing BatchDC-related parameters (in-Character[512])
   dllObj.BatchDCLoadFile.restype = c_int
   dllObj.BatchDCLoadFile.argtypes = [c_char_p]


   # Loads BatchDC control parameters and all BatchDC related data (environment, time, elsets, sensors) from an input text file
   # batchDCInputFile: The name of the file containing BatchDC and BatchDC-related parameters (in-Character[512])
   dllObj.BatchDCLoadFileAll.restype = c_int
   dllObj.BatchDCLoadFileAll.argtypes = [c_char_p]


   # Read/Load BatchDC-typed input data from an input card
   # card: BatchDC-type input card (in-Character[512])
   dllObj.BatchDCLoadCard.restype = c_int
   dllObj.BatchDCLoadCard.argtypes = [c_char_p]


   # Builds and returns the DC parameter card (1P-Card) from the current DC settings
   # dcPCard: the resulting DC 1P-Card (out-Character[512])
   dllObj.BatchDCGetPCard.restype = None
   dllObj.BatchDCGetPCard.argtypes = [c_char_p]


   # Saves any currently loaded BatchDC-related settings to a file
   # batchDCFile: The name of the file in which to save the settings (in-Character[512])
   # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
   # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for future) (in-Integer)
   dllObj.BatchDCSaveFile.restype = c_int
   dllObj.BatchDCSaveFile.argtypes = [c_char_p, c_int, c_int]


   # Gets BatchDC parameter data (P Card) - all fields
   # 
   # The table below shows the structure of the integer array xai_ctrl:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0DC print option
   #     1Apply biases from sensor file
   #     2Weighed DC flag
   #     3Epoch placement control
   #     4Element correction flag - Ag
   #     5Element correction flag - Af
   #     6Element correction flag - Psi
   #     7Element correction flag - Chi
   #     8Element correction flag - L
   #     9Element correction flag - N
   #     10Element correction flag - B* (SGP4) B (SP)
   #     11Element correction flag - Agom (SP)
   #     12Correction order
   #     13Correct by the specified correction order for 1 iteration only
   #     14Flag specifies which residuals are used for RMS calculation and convergence
   #     15Flag; if set, produce sensor performance analysis summary
   #     16Flag; if set, deweight according to # of obs per track
   #     17Iteration summary control
   #     18Partials method
   #     19Light time correction control
   #     20Number of iteration to allow no auto rejection of residuals
   #     21Propagation method
   #     22Flag; if set, correct B* vs X
   #     23Max # of iterations before declaring divergence
   #     24Use predicted RMS versus previous RMS for convergence testing
   # 
   # 
   # The table below shows the structure of the real array xar_ctrl:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0RMS multiplier
   #     1Time of specified epoch
   #     2Convergence criteria on time correction (%)
   #     3First pass delta-t rejection criteria
   #     4Convergence criteria on 7-elt correction (%)
   #     5Reset value for B term in subset correction
   # 
   # xai_ctrl: Array contains integer BatchDC parameters, see XAI_CTRL_? for array arrangement (out-Integer[256])
   # xar_ctrl: Array contains double BatchDC parameters, see XAR_CTRL_? for array arrangement (out-Double[256])
   # xas_ctrl: BatchDC parameters in character string format - not yet used (out-Character[512])
   dllObj.BatchDCGetParams.restype = None
   dllObj.BatchDCGetParams.argtypes = [c_int * 256, c_double * 256, c_char_p]


   # Sets BatchDC parameter data (P Card) - all fields
   # See BatchDCGetParams for the structure of the xai_ctrl and xar_ctrl arrays.
   # xai_ctrl: Array contains integer BatchDC parameters, see XAI_CTRL_? for array arrangement (in-Integer[256])
   # xar_ctrl: Array contains double BatchDC parameters, see XAR_CTRL_? for array arrangement (in-Double[256])
   # xas_ctrl: BatchDC parameters in character string format - not yet used (in-Character[512])
   dllObj.BatchDCSetParams.restype = None
   dllObj.BatchDCSetParams.argtypes = [c_int * 256, c_double * 256, c_char_p]


   # Returns DC control parameters using array format
   # xa_dcCtrl: Output DC control parameters, see XA_DCCTRL_? for array arrangement (out-Double[64])
   dllObj.BatchDCGetCtrlArr.restype = None
   dllObj.BatchDCGetCtrlArr.argtypes = [c_double * 64]


   # Sets DC control parameters using array format
   # xa_dcCtrl: Input DC control parameters, see XA_DCCTRL_? for array arrangement (in-Double[64])
   dllObj.BatchDCSetCtrlArr.restype = c_int
   dllObj.BatchDCSetCtrlArr.argtypes = [c_double * 64]


   # Initializes DC parameters for the satellite
   # See BatchDCGetParams for the structure of the xai_dcElts and xar_dcElts arrays.
   # satKey: The satellite's unique key (in-Long)
   # numObs: Actual number of obs being selected to be used in the DC (out-Integer)
   # obsKeys: The array in which to store the obsKeys (out-Long[*])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCInitSat.restype = c_int
   dllObj.BatchDCInitSat.argtypes = [c_longlong, c_int_p, c_void_p, c_int * 256, c_double * 256, c_char_p]


   # Initializes DC parameters for the satellite using only the provided/preselected obsKeys (not all loaded obs) (Thread-Safe)
   # See BatchDCGetParams for the structure of the xai_dcElts and xar_dcElts arrays.
   # satKey: The satellite's unique key (in-Long)
   # xa_dcCtrl: Input DC control parameters (in-Double[64])
   # numObs: Actual number of obs being selected to be used in the DC (in-Integer)
   # obsKeys: The array contains preselected obsKeys (in-Long[*])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCInitSatObsKeys.restype = c_int
   dllObj.BatchDCInitSatObsKeys.argtypes = [c_longlong, c_double * 64, c_int, c_void_p, c_int * 256, c_double * 256, c_char_p]


   # Initializes DC parameters for the satellite using only obs that match the provided obs selection criteria (not all loaded obs) (Thread-Safe)
   # See BatchDCGetParams for the structure of the xai_dcElts and xar_dcElts arrays.
   # Note: This can be accomplished by using ObsGetSelected() and BatchDCInitSatObsKeys() as well
   # satKey: The satellite's unique key (in-Long)
   # xa_dcCtrl: Input DC control parameters (in-Double[64])
   # xa_selob: Input obs selection criteria for the DC of this satellite, see XA_SELOB_? for array arrangement (in-Double[128])
   # numObs: Actual number of obs being selected (matching the specified obs selection criteria) to be used in the DC (out-Integer)
   # obsKeys: The array in which to store the obsKeys (out-Long[*])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCInitSatObsSel.restype = c_int
   dllObj.BatchDCInitSatObsSel.argtypes = [c_longlong, c_double * 64, c_double * 128, c_int_p, c_void_p, c_int * 256, c_double * 256, c_char_p]


   # Performs batch-least-square differential corrections to the specified satellite and
   # return the corrected elements and related data - using all loaded obs
   # 
   # Note: The input satellite must be intialized by calling BatchDCInitSat() prior to calling this routine
   # 
   # See BatchDCGetParams for the structure of the xai_dcElts array.
   # 
   # The table below shows the structure of the integer array xar_dcElts:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0elset's epoch time in days since 1950 UTC
   #     1n-dot/2  (for SGP, eph-type = 0)
   #     2n-double-dot/6  (for SGP, eph-type = 0)
   #     3either SGP4 bStar (1/er) or SP bTerm (m2/kg)
   #     4SP agom (m**2/kg)
   #     5SP outgassing parameter (km/s**2)
   #     6semi major axis (km)
   #     7eccentricity
   #     8inclination (deg)
   #     9mean anamoly (deg)
   #     10right ascension of the ascending node (deg)
   #     11argument of perigee (deg)
   #     12AF
   #     13AG
   #     14CHI
   #     15PSI
   #     16mean longitude (deg)
   #     17mean motion (revs/day)
   #     18ECI posX (km)
   #     19ECI posY (km)
   #     20ECI posZ (km)
   #     21ECI velX (km/s)
   #     22ECI velY (km/s)
   #     23ECI velZ (km/s)
   #     
   #     40RMS (km)
   #     41unweighted RMS (km)
   #     42delta T RMS (min)
   #     43beta RMS (deg)
   #     44delta height RMS (km)
   #     45convergence value (km)
   #     46predicted RMS (km)
   #     
   #     60covariance diagonal L
   #     61covariance diagonal N
   #     62covariance diagonal CHI
   #     63covariance diagonal PSI
   #     64covariance diagonal AF
   #     65covariance diagonal AG
   #     66covariance diagonal BTERM
   #     67covariance not used
   #     68covariance diagonal AGOM
   #     
   #     200-244equinoctial covariance matrix - the lower triangular half 200-244
   # 
   # satKey: The satellite's unique key (in-Long)
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCSolve.restype = c_int
   dllObj.BatchDCSolve.argtypes = [c_longlong, c_int * 256, c_double * 256, c_char_p]


   # Performs batch-least-square differential corrections to the specified satellite and
   # return the corrected elements and related data - using only the provided obsKeys (not all loaded obs)
   # Note: The input satellite must be intialized by calling BatchDCInitSat() prior to calling this routine
   # See BatchDCGetParams for the structure of the xai_dcElts array.
   # See BatchDCSolve for the structure of the xar_dcElts array.
   # satKey: The satellite's unique key (in-Long)
   # obsKeys: The array of obs keys that wil be used in the DC (in-Long[*])
   # numObs: The size of the obsKeys array (in-Integer)
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCSolveSelObs.restype = c_int
   dllObj.BatchDCSolveSelObs.argtypes = [c_longlong, c_void_p, c_int, c_int * 256, c_double * 256, c_char_p]


   # Removes a satellite, represented by the satKey, from BatchDC's memory
   # satKey: The unique key of the satellite to be removed (in-Long)
   dllObj.BatchDCRemoveSat.restype = c_int
   dllObj.BatchDCRemoveSat.argtypes = [c_longlong]


   # Iterates DC for the satellite
   # 
   # xa_ObsRes size is [numObs, 100].  xa_rejFlg size is [numObs, 32].
   # 
   # The table below shows the values contained in xa_ObsRes for each ob:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #      0  Azimuth residual (deg)
   #      1  Elevation residual (deg)
   #      2  Range residual (km)
   #      3  Height residual (deg)
   #      4  Beta residual (deg)
   #      5  Delta T residual (min)
   #      6  Vector magnitude (km)
   #      7  Time since epoch (days)
   #      8  True argument of latitude (deg)
   #      9  Revolution number  
   #     10  Range rate residual (km/sec)
   #     11  observation ASTAT
   #     12  observation type
   #     13  satellite true anomaly (deg)
   #     14  satellite elevation (deg)
   #     15  satellite maintenance category
   #     16  obs time in ds50UTC
   #     17  obs azimuth (deg)
   #     18  obs elevation (deg)
   #     19  Velocity angle residual (deg)
   #     20  Angular momentum residual (deg)
   #     21  Right ascension residual (deg) (for ob types 5, 9, 19)
   #     22  Declination residual (deg) (for ob types 5, 9, 19)
   #     23  Delta X position (km)
   #     24  Delta Y position (km)
   #     25  Delta Z position (km)
   #     26  Delta X velocity (km/sec)
   #     27  Delta Y velocity (km/sec)
   #     28  Delta Z velocity (km/sec)
   #     29  Angle only obs computed range (km)
   #     30  obs azimuth (deg)
   #     31  obs elevation (deg)
   # 
   # 
   # See BatchDCGetParams for the structure of the xai_dcElts array.
   # 
   # See BatchDCSolve for the structure of the xar_dcElts array.
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[*, 100])
   # xa_rejFlg: Obs rejection flag array, see XA_REJFLG_? for array arrangement (out-Integer[*, 32])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.BatchDCIterate.restype = c_int
   dllObj.BatchDCIterate.argtypes = [c_longlong, c_void_p, c_void_p, c_int * 256, c_double * 256, c_char_p]


   # Returns a concatenated string representation of a VCM generated by a successful DC
   # satKey: The satellite's unique key (in-Long)
   # vcmLines: The resulting concatenated string representation of the VCM, (out-Character[4000])
   dllObj.BatchDCGetVcm.restype = c_int
   dllObj.BatchDCGetVcm.argtypes = [c_longlong, c_char_p]


   # Returns the full file name of the output SP Vector file that was specified using "SPVOUT = " 
   # in the main input file or using the BatchDCSetSpVOutFileName() function call
   # spVOutFile: The output file that stores SP output message (out-Character[512])
   dllObj.BatchDCGetSpVOut.restype = None
   dllObj.BatchDCGetSpVOut.argtypes = [c_char_p]


   # Sets the full file name of the SP Vector output file which will be used to store the generated SP vector data
   # spVOutFile: The output file that stores SP vector output (VCM message) (in-Character[512])
   dllObj.BatchDCSetSpVOut.restype = None
   dllObj.BatchDCSetSpVOut.argtypes = [c_char_p]


   # Resets all BatchDC control parameters back to their default values and empties the DC binary tree (objects created by BatchDCInitSat)
   dllObj.BatchDCResetAll.restype = None
   dllObj.BatchDCResetAll.argtypes = []


   # Returns DC acceptance criteria data for the specified satellite
   # satKey: The satellite's unique key (in-Long)
   # xa_ac: acceptance criteria values in an array, see XA_AC_? for array arrangement (out-Double[64])
   dllObj.BatchDCGetAccptCrit.restype = c_int
   dllObj.BatchDCGetAccptCrit.argtypes = [c_longlong, c_double * 64]


   # Performs batch-least-square differential corrections to the specified satellite (VCM/SPVEC) and
   # returns the corrected SGP4/SGP4-XP elements and related data
   # Note: No need to initialize VCM before calling this method
   # satKey: The satellite's unique key of the specified satellite (must be VCM or SPVEC) (in-Long)
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.SpToEGP.restype = c_int
   dllObj.SpToEGP.argtypes = [c_longlong, c_double * 64, c_int * 256, c_double * 256, c_char_p]


   # Performs batch-least-square differential corrections to the specified satellite (VCM/SPVEC) and
   # returns the corrected elements SGP4/SGP4-XP in form of a TLE
   # Note: No need to initialize VCM before calling this method
   # satKey: The satellite's unique key of the specified satellite (must be VCM or SPVEC) (in-Long)
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # line1: Returned first line of a TLE. (out-Character[512])
   # line2: Returned second line of a TLE (out-Character[512])
   dllObj.SpToTle.restype = c_int
   dllObj.SpToTle.argtypes = [c_longlong, c_double * 64, c_char_p, c_char_p]


   # Combines SpToEGP and SpToTle functions into just one function call
   # Note: No need to initialize VCM before calling this method
   # satKey: The satellite's unique key of the specified satellite (must be VCM or SPVEC) (in-Long)
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # line1: Returned first line of a TLE. (out-Character[512])
   # line2: Returned second line of a TLE (out-Character[512])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.SpToTleComb.restype = c_int
   dllObj.SpToTleComb.argtypes = [c_longlong, c_double * 64, c_char_p, c_char_p, c_int * 256, c_double * 256, c_char_p]


   # Performs batch-least-square differential corrections to the specified satellite (VCM/SPVEC) and
   # returns the corrected elements SGP4/SGP4-XP in form of a TLE
   # Note: No need to initialize VCM before calling this method
   # satKey: The satellite's unique key (in-Long)
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # csvLine: A string to hold the TLE in csv format. (out-Character[512])
   dllObj.SpToCsv.restype = c_int
   dllObj.SpToCsv.argtypes = [c_longlong, c_double * 64, c_char_p]


   # Combines SpToEGP and SpToCsv functions into just one function call
   # Note: No need to initialize VCM before calling this method
   # satKey: The satellite's unique key (in-Long)
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # csvLine: A string to hold the TLE in csv format. (out-Character[512])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.SpToCsvComb.restype = c_int
   dllObj.SpToCsvComb.argtypes = [c_longlong, c_double * 64, c_char_p, c_int * 256, c_double * 256, c_char_p]


   # Performs batch-least-square differential corrections using the input external ephemeris and treating them as observations and
   # returns the corrected SGP4/SGP4-XP elements and related data
   # extEphFile: The name of the file containing external ephemeris data to be used in EGP (in-Character[512])
   # xa_egpCtrl: Array (in/out) containing settings for SpToEGP conversion, see XA_EGPCTRL_? for array arrangement (inout-Double[64])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.ExtEphemToEGP.restype = c_int
   dllObj.ExtEphemToEGP.argtypes = [c_char_p, c_double * 64, c_int * 256, c_double * 256, c_char_p]


   # Performs IOMOD/IODET and then batch-least-square differential corrections on the input observations via their obsKeys (Thread-Safe) 
   # numObs: Number of preselected obs to be used in IOMOD and then DC (in-Integer)
   # obsKeys: The array contains preselected obsKeys (in-Long[*])
   # xa_iomdc: Array containing settings for the DC, see XA_IOMDC_? for array arrangement (in-Double[64])
   # xai_dcElts: Array of integers containing resulting BatchDC data, see XAI_DCELTS_? for array arrangement (out-Integer[256])
   # xar_dcElts: Array of doubles containing resulting BatchDC data, see XAR_DCELTS_? for array arrangement (out-Double[256])
   # xas_dcElts: String containing resulting BatchDC data, see XAS_DCELTS_? for substring arrangement (out-Character[512])
   dllObj.IomodDC.restype = c_int
   dllObj.IomodDC.argtypes = [c_int, c_void_p, c_double * 64, c_int * 256, c_double * 256, c_char_p]

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj
# Different DC propagation method
# DC propagator method is GP
DCPROPTYPE_GP =  0
# DC propagator method is SGP4-XP
DCPROPTYPE_XP =  4
# DC propagator method is SP
DCPROPTYPE_SP = 99

# DC iterating returned code
# DC was successful
ITERCODE_DONE      = 0
# DC has error
ITERCODE_ERROR     = 1
# DC is still iterating
ITERCODE_ITERATING = 2
# DC diverged but trying to recover
ITERCODE_DIVERGED  = 3

# indexes represent epoch placement options
# Nodal crossing nearest latest obs
EPFLG_NODALXINGLATESTOB = 0
# Exact time of latest obs
EPFLG_LATESTOB          = 1
# Nodal crossing closest to specified time
EPFLG_NODALXINGATTIME   = 2
# Do not change epoch
EPFLG_ATEPOCH           = 3
# Exact at specified time
EPFLG_ATSPECIFIEDTIME   = 4
# Middle of obs span
EPFLG_MIDDLEOBSSPAN     = 5
# Exact time of earliest obs
EPFLG_EARLIESTOB        = 6
# Beginning of day of Epoch, good for eGP
EPFLG_BEGINDAYEPOCH     = 7
# Beginning of day of Last obs
EPFLG_BEGINDAYLATESTOB  = 8
# Nodal crossing nearest epoch, good for eGP
EPFLG_NODALXINGEPOCH    = 9

# Different correction types
CORT_TIME   = 0,
CORT_PLANE  = 1,
CORT_7ELT   = 2,
CORT_INTRK  = 3,
CORT_8ELT   = 4,
CORT_SUBELT = 5

# Different element correction order
# 7-element only [default]
CORORD_7ELT       = 0
# time (SP: L, n, B), then 7-element
CORORD_TIM7ELT    = 1
# time, plane, then 7-element (SGP4) or 7-elt only; pht/pi vs Af/Ag (SP)
CORORD_TIMPLN7ELT = 2
# plane, time, then 7-element (SGP4) or 7-elt only; e/pi vs Af/Ag (SP)
CORORD_PLNTIM7ELT = 3
# plane, then 7-element (SGP4) or L, n, B, then 7-elt, with pht/pi vs Af/Ag (SP)
CORORD_PLN7ELT    = 4
# n-only, then 7-element
CORORD_N7ELT      = 5
# L-only, then 7-element
CORORD_L7ELT      = 6
# L & n only, then 7-element
CORORD_LN7ELT     = 7
# Af/Ag, L, n only, then 7-element
CORORD_AFAGLN7ELT = 8
# 6-element, then 7-element
CORORD_6ELT7ELT   = 9


# indexes for EGP control parameters for input VCM/SPVEC-typed elsets or external ephemeris file
# Not being used yet
XA_EGPCTRL_OPTION     =  0
# DC element type: 0=SPG4, 4=SGP4-XP
XA_EGPCTRL_DCELTTYPE  =  1
# Fit span start time (minutes since VCM's epoch/specified new epoch) (set start/stop = 0 to auto select)
XA_EGPCTRL_STARTMSE   =  2
# Fit span stop time (minutes since VCM's epoch/specified new epoch) (set start/stop = 0 to auto select)
XA_EGPCTRL_STOPMSE    =  3
# Step size in minutes (how often obs are generated) (set to zero to auto select and then actual step size will be returned)
XA_EGPCTRL_STEPMIN    =  4
# Drag correction: 0=no correction, 1=correct BStar(SGP4)/BTerm(SGP4-XP), 2=correct X(SGP4 only)
XA_EGPCTRL_DRAGCOR    =  5
# agom correction: 0=no correction, 1=correct agom (only when DC element = SGP4-XP)
XA_EGPCTRL_AGOMCOR    =  6
# Epoch placement flag - see EPFLG_? for available options
XA_EGPCTRL_EPFLG      =  7
# Time of specified Epoch in Ds50UTC (only for XA_EGPCTRL_EPFLG = 2 or 4)                 *
XA_EGPCTRL_NEWEPOCH   =  8

# Addtional option if input is external ephemeris file - BStar(SGP4)/BTerm(SGP4-XP) if XA_EGPCTRL_DRAGCOR is set (= 1)
XA_EGPCTRL_BVAL       =  9
# Addtional option if input is external ephemeris file - agom value if XA_EGPCTRL_AGOMCOR is set (= 1)
XA_EGPCTRL_AGOMVAL    = 10

# correction order
XA_EGPCTRL_ORDERCOR   = 11
# Max # of iterations before declaring divergence [10]
XA_EGPCTRL_MAXOFITERS = 12

# satellite number
XA_EGPCTRL_SATNUM     = 63

XA_EGPCTRL_SIZE       = 64



# DC setting parameters

MAX_PARAMS = 256


# DC print options
# print first and last iteration
DC_PRINT_FIRSTBEST   =  0
# print every pass and summary
DC_PRINT_ALLPASS     =  1
# print summary only
DC_PRINT_SUMONLY     =  2
# print output elemenets only
DC_PRINT_ELTONLY     =  3
# do not print anything
DC_PRINT_NONE        =  4

# Iteration summary options
# print summary every iteration in Keplerian elts
ITER_SUM_KEP         =  1
# print summary every iteration in Equinoctial elts
ITER_SUM_EQNX        =  2

# indexes for integer data fields
# DC print option
XAI_CTRL_PRINTOPTION  =  0
# Apply biases from sensor file
XAI_CTRL_DEBIASOBS    =  1
# Weighed DC flag
XAI_CTRL_WEIGHTEDDC   =  2
# Epoch placement flag - see EPFLG_? for available options
XAI_CTRL_EPOCHOPTION  =  3
# Element correction flag - Ag
XAI_CTRL_CORRECT_AG   =  4
# Element correction flag - Af
XAI_CTRL_CORRECT_AF   =  5
# Element correction flag - Psi
XAI_CTRL_CORRECT_PSI  =  6
# Element correction flag - Chi
XAI_CTRL_CORRECT_CHI  =  7
# Element correction flag - L
XAI_CTRL_CORRECT_L    =  8
# Element correction flag - N
XAI_CTRL_CORRECT_N    =  9
# Element correction flag - B* (SGP4) B (SP)
XAI_CTRL_CORRECT_B    = 10
# Element correction flag - Agom (SP)
XAI_CTRL_CORRECT_AGOM = 11
# Correction order
XAI_CTRL_CORRECTORDER = 12
# Correct by the specified correction order for 1 iteration only
XAI_CTRL_FOR1ITERONLY = 13
# Flag specifies which residuals are used for RMS calculation and convergence
XAI_CTRL_RESIDSELECT  = 14
# Flag; if set, produce sensor performance analysis summary
XAI_CTRL_SENPERFORM   = 15
# Flag; if set, deweight according to # of obs per track
XAI_CTRL_DWOBSPERTRCK = 16
# Iteration summary control
XAI_CTRL_ITERSUMOPT   = 17
# Partials method
XAI_CTRL_PARTIALMETH  = 18
# Light time correction control
XAI_CTRL_LTC          = 19
# Number of iteration to allow no auto rejection of residuals
XAI_CTRL_BRUCE        = 20
# Propagation method - GP=0, XP=4, SP=99
XAI_CTRL_PROPMETHOD   = 21
# Flag; if set, correct B* vs X
XAI_CTRL_CORRECTBVSX  = 22
# Max # of iterations before declaring divergence
XAI_CTRL_MAXOFITERS   = 23
# Use predicted RMS versus previous RMS for convergence testing
XAI_CTRL_USEPREDRMS   = 24
# Residual computation method (GP only): DELTA/427M=1, SPADOC4=2
XAI_CTRL_RESCOMPMETH  = 25
# Flag; if set, use angle rates (obstypes = 4, 11)
XAI_CTRL_USEANGRATES  = 26

XAI_CTRL_SIZE         = 256



# indexes for real data fields
# RMS multiplier
XAR_CTRL_RMSMULT        =   0
# Time of specified epoch
XAR_CTRL_USEREPOCH      =   1
# Convergence criteria on time correction (%)
XAR_CTRL_CNVCRITONT     =   2
# First pass delta-t rejection criteria
XAR_CTRL_1STPASDELTAT   =   3
# Convergence criteria on 7-elt correction (%)
XAR_CTRL_CNVCRITON7ELT  =   4
# reset value for B term in subset correction
XAR_CTRL_BRESET         =   5
XAR_CTRL_SIZE           = 256


# indexes for accessing DC's integer data
# satellite number
XAI_DCELTS_SATNUM       =   0
# elset number
XAI_DCELTS_ELSETNUM     =   1
# elset's orbital/element type - see ELTTYPE_ constants for a list of possible values
XAI_DCELTS_ORBTYPE      =   2
# propagation method - see PROPTYPE_ constants for a list of possible values (GP=1, SP=2, External Ephemeris=3)
XAI_DCELTS_PROPTYPE     =   3
# spectr mode
XAI_DCELTS_SPECTR       =   4
# epoch revolution number
XAI_DCELTS_REVNUM       =   5
# correction type: 0=TIME, 1=PLANE", 2=7-ELT, 3=IN-TRK, 4=8-ELT, 5=SUBELT; see CORT_? for available values
XAI_DCELTS_CORRTYPE     =   6

# total iteration count
XAI_DCELTS_ITERCOUNT    =  10
# sub iteration count
XAI_DCELTS_SUBITER      =  11
# # residual accepted
XAI_DCELTS_RESACC       =  12
# # residual rejected
XAI_DCELTS_RESREJ       =  13

# 20-28 correction element flags
XAI_DCELTS_CORRFLGS     =  20

XAI_DCELTS_SIZE         = 256

# indexes for accessing DC's real data
# elset's epoch time in days since 1950 UTC
XAR_DCELTS_EPOCHDS50UTC =   0
# n-dot/2  (for SGP, eph-type = 0)
XAR_DCELTS_NDOT         =   1
# n-double-dot/6  (for SGP, eph-type = 0)
XAR_DCELTS_N2DOT        =   2
# either SGP4 bStar (1/er) or SGP4-XP/SP bTerm (m2/kg)
XAR_DCELTS_BFIELD       =   3
# SGP4-XP/SP agom (m**2/kg)
XAR_DCELTS_AGOM         =   4
# SP outgassing parameter (km/s**2)
XAR_DCELTS_OGPARM       =   5
# semi major axis (km)
XAR_DCELTS_KEP_A        =   6
# eccentricity
XAR_DCELTS_KEP_E        =   7
# inclination (deg)
XAR_DCELTS_KEP_INCLI    =   8
# mean anamoly (deg)
XAR_DCELTS_KEP_MA       =   9
# right ascension of the ascending node (deg)
XAR_DCELTS_KEP_NODE     =  10
# argument of perigee (deg)
XAR_DCELTS_KEP_OMEGA    =  11
# AF
XAR_DCELTS_EQNX_AF      =  12
# AG
XAR_DCELTS_EQNX_AG      =  13
# CHI
XAR_DCELTS_EQNX_CHI     =  14
# PSI
XAR_DCELTS_EQNX_PSI     =  15
# mean longitude (deg)
XAR_DCELTS_EQNX_L       =  16
# mean motion (revs/day)
XAR_DCELTS_EQNX_N       =  17
# ECI posX (km)
XAR_DCELTS_POSX         =  18
# ECI posY (km)
XAR_DCELTS_POSY         =  19
# ECI posZ (km)
XAR_DCELTS_POSZ         =  20
# ECI velX (km/s)
XAR_DCELTS_VELX         =  21
# ECI velY (km/s)
XAR_DCELTS_VELY         =  22
# ECI velZ (km/s)
XAR_DCELTS_VELZ         =  23

# RMS (km)
XAR_DCELTS_RMS          =  40
# unweighted RMS (km)
XAR_DCELTS_RMSUNWTD     =  41
# delta T RMS (min)
XAR_DCELTS_DELTATRMS    =  42
# beta RMS (deg)
XAR_DCELTS_BETARMS      =  43
# delta height RMS (km)
XAR_DCELTS_DELTAHTRMS   =  44
# convergence value (km)
XAR_DCELTS_CONVQLTY     =  45
# predicted RMS (km)
XAR_DCELTS_RMSPD        =  46

# covariance diagonal L
XAR_DCELTS_COVL         =  60
# covariance diagonal N
XAR_DCELTS_COVN         =  61
# covariance diagonal CHI
XAR_DCELTS_COVCHI       =  62
# covariance diagonal PSI
XAR_DCELTS_COVPSI       =  63
# covariance diagonal AF
XAR_DCELTS_COVAF        =  64
# covariance diagonal AG
XAR_DCELTS_COVAG        =  65
# covariance diagonal BTERM
XAR_DCELTS_COVBTERM     =  66
# covariance not used
XAR_DCELTS_COVNA        =  67
# covariance diagonal AGOM
XAR_DCELTS_COVAGOM      =  68

# max partial residual (km)
XAR_DCELTS_XMAX         =  70
# max velocity resid (km/sec)
XAR_DCELTS_XMAX2        =  71
# max beta residual (deg)
XAR_DCELTS_XMAX3        =  72
# max delta-t residual (min)
XAR_DCELTS_XMAX4        =  73
# low argument of latitude coverage (deg)
XAR_DCELTS_PATCL        =  74
# high argument of latitude coverage (deg)
XAR_DCELTS_PATCH        =  75

# equinoctial covariance matrix - the lower triangular half 200-244
XAR_DCELTS_EQNXCOVMTX   = 200

XAR_DCELTS_SIZE         = 256

# indexes for accessing obs rejection flags
# satellite has decayed at the time of obs
XA_REJFLG_DECAYED      =   0
# obs residual computation error code
XA_REJFLG_ERROR        =   1
# right ascension residual rejected
XA_REJFLG_RA           =   2
# beta residual rejected
XA_REJFLG_BETA         =   3
# declination residual rejected
XA_REJFLG_DEC          =   4
# delta h residual rejected
XA_REJFLG_HEIGHT       =   5
# range residual rejected
XA_REJFLG_RANGE        =   6
# range rate residual rejected
XA_REJFLG_RR           =   7
# delta t residual rejected
XA_REJFLG_TIME         =   8

XA_REJFLG_SIZE         =  32

# indexes for accessing DC's acceptance criteria data
# standard - days from epoch
XA_AC_STD_EPOCH    =   0
# standard - number of residuals
XA_AC_STD_NORES    =   1
# standard - percent residual
XA_AC_STD_PRCNTRES =   2
# standard - RMS (km)
XA_AC_STD_RMS      =   3
# standard - obs span (days)
XA_AC_STD_OBSSPAN  =   4
# standard - change in plan (deg)
XA_AC_STD_DELTAW   =   5
# standard - change in abar
XA_AC_STD_DELTAABAR=   6
# standard - change in N (rev/day)
XA_AC_STD_DELTAN   =   7
# standard - change in B term
XA_AC_STD_DELTAB   =   8

# actual - days from epoch
XA_AC_ACT_EPOCH    =  20
# actual - number of residuals
XA_AC_ACT_NORES    =  21
# actual - percent residual
XA_AC_ACT_PRCNTRES =  22
# actual - RMS (km)
XA_AC_ACT_RMS      =  23
# actual - obs span (days)
XA_AC_ACT_OBSSPAN  =  24
# actual - change in plan (deg)
XA_AC_ACT_DELTAW   =  25
# actual - change in abar
XA_AC_ACT_DELTAABAR=  26
# actual - change in N (rev/day)
XA_AC_ACT_DELTAN   =  27
# actual - change in B term
XA_AC_ACT_DELTAB   =  28

XA_AC_SIZE         =  64


# indexes for accessing DC's string character data - index to index of a substring
# satellite's international designator
XAS_DCELTS_SATNAME_0TO7 =   0

XAS_DCELTS_SIZE         = 512

# Different DC control modes
# Use DC global settings settings
DCCTRL_MODE_GLOBAL   = 0
# Use provided/local DC settings
DCCTRL_MODE_LOCAL    = 1


# indexes of DC control parameters
# DC control mode: 0= use global settings (ignore the rest), 1= use the provided/local settings (thread-safe) - N/A for BatchDC(Get/Set)CtrlArr()
XA_DCCTRL_MODE             =  0
# propagation method: SGP4 = 0, SP = 99, XP = 4, or see DCPROPTYPE_? for available options
XA_DCCTRL_PROPMETHOD 		=  1
# debias obs flag: 0= do not debias obs, 1= debias obs
XA_DCCTRL_DEBIASOBS    		=  2
# element correction order
XA_DCCTRL_CORRECTORDER		=  3
# epoch placement flag - see EPFLG_? for available options
XA_DCCTRL_EPOCHOPTION  		=  4
# use predicted RMS versus previous RMS for convergenece testing
XA_DCCTRL_USEPREDRMS		   =  5
# residual computation selection
XA_DCCTRL_RESIDSELECT      =  6
# correct by the specified correction order for 1 iteration only
XA_DCCTRL_FOR1ITERONLY		=  7
# max # of iterations before declaring divergence
XA_DCCTRL_MAXOFITERS       =  8
# apply weighed DC flag
XA_DCCTRL_WEIGHTEDDC		   =  9
# light time correction control
XA_DCCTRL_LTC              = 10
# number of iteration to allow no auto rejection of residuals
XA_DCCTRL_BRUCE            = 11
# flag; if set, deweight according to # of obs per track
XA_DCCTRL_DWOBSPERTRCK     = 12
# partials method
XA_DCCTRL_PARTIALMETH      = 13
# Element correction flag - Ag
XA_DCCTRL_CORRECT_AG    	= 20
# Element correction flag - Af
XA_DCCTRL_CORRECT_AF    	= 21
# Element correction flag - Psi
XA_DCCTRL_CORRECT_PSI   	= 22
# Element correction flag - Chi
XA_DCCTRL_CORRECT_CHI   	= 23
# Element correction flag - L
XA_DCCTRL_CORRECT_L     	= 24
# Element correction flag - N
XA_DCCTRL_CORRECT_N     	= 25
# Element correction flag - B* (SGP4) B (SP)
XA_DCCTRL_CORRECT_B     	= 26
# Element correction flag - Agom (SP)
XA_DCCTRL_CORRECT_AGOM  	= 27
# Convergence criteria on time (%) [5.0%]
XA_DCCTRL_CNVCRITONT       = 30
# First pass delta-t rejection criteria Convergence criteria on time correction (min) [20 minutes]
XA_DCCTRL_1STPASDELTAT     = 31
# Convergence criteria on 7-elt correction (%) [1.0%]
XA_DCCTRL_CNVCRITON7ELT    = 32
# RMS multiplier [4.0]
XA_DCCTRL_RMSMULT          = 33
# reset value for B term in subset correction [0.01]
XA_DCCTRL_BRESET           = 34
# user's specified epoch - only when epoch placement option = 4 exact at specified time
XA_DCCTRL_USEREPOCH        = 35
# SP only - density consider parameter
XA_DCCTRL_CONSIDER         = 40
# GP only - residual computation method
XA_DCCTRL_GPRCM 			   = 40
# GP only - SGP4: correct B* vs X, SGP4-XP: correct B
XA_DCCTRL_CORRECTBVSX		= 41

XA_DCCTRL_SIZE             = 64

# Indexes of paramters using in IomodDC()
# Iomod/DC control mode (not yet used)
XA_IOMDC_MODE           =  0
# DC element type, see DCPROPTYPE_? for available options
XA_IOMDC_DCELTTYPE      =  1
# Epoch placement flag - see EPFLG_? for available options
XA_IOMDC_EPFLG          =  2
# Time of specified Epoch in Ds50UTC (only for XA_EGPCTRL_EPFLG = 2 or 4)
XA_IOMDC_NEWEPOCH       =  3
# Correction order
XA_IOMDC_ORDERCOR       =  4
# IOMOD obs selection mode: 0= auto select, 1= use first 3 obs in the provided list of obs (see OBSSELMODE_? for available options)
XA_IOMDC_OBSSELMODE     =  5
# residual computation selection
XA_IOMDC_RESIDSELECT    =  6
# correct by the specified correction order for 1 iteration only
XA_IOMDC_FOR1ITERONLY   =  7
# max # of iterations before declaring divergence
XA_IOMDC_MAXOFITERS     =  8
# apply weighed DC flag
XA_IOMDC_WEIGHTEDDC		=  9
# light time correction control
XA_IOMDC_LTC            = 10
# number of iteration to allow no auto rejection of residuals
XA_IOMDC_BRUCE          = 11
# flag; if set, deweight according to # of obs per track
XA_IOMDC_DWOBSPERTRCK   = 12
# partials method
XA_IOMDC_PARTIALMETH    = 13
# debias obs flag: 0= do not debias obs, 1= debias obs
XA_IOMDC_DEBIASOBS    	= 14
# use predicted RMS versus previous RMS for convergenece testing
XA_IOMDC_USEPREDRMS		= 15

# Element correction flag - Ag
XA_IOMDC_CORRECT_AG    	= 20
# Element correction flag - Af
XA_IOMDC_CORRECT_AF    	= 21
# Element correction flag - Psi
XA_IOMDC_CORRECT_PSI   	= 22
# Element correction flag - Chi
XA_IOMDC_CORRECT_CHI   	= 23
# Element correction flag - L
XA_IOMDC_CORRECT_L     	= 24
# Element correction flag - N
XA_IOMDC_CORRECT_N     	= 25
# Element correction flag - B* (SGP4) B (SP)
XA_IOMDC_CORRECT_B     	= 26
# Element correction flag - Agom (SP)
XA_IOMDC_CORRECT_AGOM  	= 27
# Convergence criteria on time (%) [5.0%]
XA_IOMDC_CNVCRITONT     = 30
# First pass delta-t rejection criteria Convergence criteria on time correction (min) [20 minutes]
XA_IOMDC_1STPASDELTAT   = 31
# Convergence criteria on 7-elt correction (%) [1.0%]
XA_IOMDC_CNVCRITON7ELT  = 32
# RMS multiplier [4.0]
XA_IOMDC_RMSMULT        = 33
# reset value for B term in subset correction [0.01]
XA_IOMDC_BRESET         = 34
# SP only - density consider parameter
XA_IOMDC_CONSIDER       = 40
# GP only - residual computation method
XA_IOMDC_GPRCM 			= 40
# GP only - SGP4: correct B* vs X, SGP4-XP: correct B
XA_IOMDC_CORRECTBVSX		= 41

# see IOMDC_METHOD_? for available options
XA_IOMDC_METHOD         = 50
# The below parameters only apply when XA_IOMDC_METHOD is set to 2 (use customized Gooding settings)
# number of half revolutions [0]
XA_IOMDC_NHREV          = 51
# solution number [0]
XA_IOMDC_IND            = 52
# maximum number of iterations [20]
XA_IOMDC_MAXIT          = 53
# the range guess to first observation (km) [36000]
XA_IOMDC_RNG1           = 54
# the range guess to third observation (km) [36000]
XA_IOMDC_RNG3           = 55
# partial derivative increment [1e-5]
XA_IOMDC_PDINC          = 56
# convergence criterion [1e-9]
XA_IOMDC_CONVCR         = 57

# IOMOD/DC parameter list size
XA_IOMDC_SIZE           = 64

# Different options for doing IOMOD/DC
# Default option which uses Herrick-Gibbs for all obs types
IOMDC_METHOD_HB      = 0
# Use Gooding (with default settings) for angle only type obs and Herrick-Gibbs for other obs types
IOMDC_METHOD_GDDEFLT = 1
# Use Gooding (with customized settings) for angle only type obs and Herrick-Gibbs for other obs types
IOMDC_METHOD_GDSPEC  = 2

# ========================= End of auto generated code ==========================
