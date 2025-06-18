# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'Fov.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'libfov.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'libfov.dylib'

def LoadFovDll():
   """ LoadFovDll() -- Loads Fov.dll from the PATH or LD_LIBRARY_PATH
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
   # Initializes Fov dll for use in the program
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.FovInit.restype = c_int
   dllObj.FovInit.argtypes = [c_longlong]


   # Returns information about the current version of Fov.dll. The information is placed in the string parameter you pass in
   # infoStr: A string to hold the information about Fov.dll. (out-Character[128])
   dllObj.FovGetInfo.restype = None
   dllObj.FovGetInfo.argtypes = [c_char_p]


   # Loads Fov-related parameters (1P/2P/3P cards, and Fov parameter free format) from an input text file
   # fovInputFile: The name of the file containing Fov-related parameters (in-Character[512])
   dllObj.FovLoadFile.restype = c_int
   dllObj.FovLoadFile.argtypes = [c_char_p]


   # Loads Fov-related parameters (1P/2P/3P cards, and Fov parameter free format) from an input text file
   # fovInputFile: The name of the file containing Fov-related parameters (in-Character[512])
   dllObj.FovLoadFileAll.restype = c_int
   dllObj.FovLoadFileAll.argtypes = [c_char_p]


   # Loads a single Fov-typed card
   # card: Fov-type input card (in-Character[512])
   dllObj.FovLoadCard.restype = c_int
   dllObj.FovLoadCard.argtypes = [c_char_p]


   # Saves any currently loaded Fov-related settings to a file
   # fovFile: The name of the file in which to save the settings (in-Character[512])
   # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
   # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for future) (in-Integer)
   dllObj.FovSaveFile.restype = c_int
   dllObj.FovSaveFile.argtypes = [c_char_p, c_int, c_int]


   # This function retrieves various FOV input data being entered from input flat files (various FOV cards)
   # xa_fovCtrl: FOV control parameters, see XA_FOVCTRL_? for array arrangement (out-Double[8])
   # numOfWindows: Number of specified start/stop windows (out-Integer)
   # startStopTimes: Array of start/stop times in days since 1950 UTC (even idxs=start times, odd idxs=stop times) (out-Double[256])
   # numOfSources: Number of sources (out-Integer)
   # xa_fovSrc_Arr: Array of source records, see XA_FOVSRC_? for array arrangement (out-Double[128, 8])
   # numOfTargets: Number of targets (out-Integer)
   # xa_fovTgt_Arr: Array of target records, see XA_FOVTGT_? for array arrangement (out-Double[128, 8])
   # numVicSats: Number of specified potential victims (out-Integer)
   # vicSatNums: Array of satellite numbers of the specified potential victims (out-Integer[128])
   dllObj.FovGetDataFrInputFiles.restype = None
   dllObj.FovGetDataFrInputFiles.argtypes = [c_double * 8, c_int_p, c_double * 256, c_int_p, c_void_p, c_int_p, c_void_p, c_int_p, c_int * 128]


   # This function screens the specified start/end time window and returns passes when the target satellite can be seen (passed all limit checks) by the source 
   # startTimeDs50UTC: window start time in days since 1950 UTC (in-Double)
   # stopTimeDs50UTC: window stop time in days since 1950 UTC (in-Double)
   # srcSenKey: the source sensor key (in-Long)
   # tgtSatKey: the targeted satellite's unique key (in-Long)
   # tgtPassesArr: array of entry/exit times (in Ds50TAI) of each pass; the size of the array should match the specified value in XA_FOVRUN_MAXPASSES (out-Double[*, 2])
   # numOfPasses: number of passes that target satellite can be seen (passed all limit checks) by the source sensor (out-Integer)
   dllObj.FovFindTargetPasses.restype = c_int
   dllObj.FovFindTargetPasses.argtypes = [c_double, c_double, c_longlong, c_longlong, c_void_p, c_int_p]


   # This function screens a potential victim satellite for penetrating the illumination cone between a source and a target (target is an elset).
   # 
   # The xa_emeDat array size is [numObs, 3].  The penetration time indexes are:
   # 
   # table
   # 
   # Name
   # Index
   # Index Interpretation
   # 
   #  0 entry time (ds50UTC)
   #  1 minimum time (ds50UTC)
   #  2 exit time (ds50UTC)
   # 
   # 
   # See FovGetDataFrInputFiles for a description of the XA_FOVSRC parameter values.
   # xa_fovRun: fov run parameters, see XA_FOVRUN_? for array arrangement (in-Double[8])
   # xa_fovSrc: source data, see XA_FOVSRC_? for array arrangement (in-Double[8])
   # tgtSatKey: the targeted satellite's unique key (in-Long)
   # vicSatKey: the victim satellite's unique key (in-Long)
   # xa_emeDat: array of entry/minimum/exit (in Ds50TAI) times of each pass (out-Double[*, 3])
   # numOfPasses: number of passes found (out-Integer)
   dllObj.FovTargetElset.restype = c_int
   dllObj.FovTargetElset.argtypes = [c_double * 8, c_double * 8, c_longlong, c_longlong, c_void_p, c_int_p]


   # This function returns a look angle from the source to the potential victim satellite at the specified time (target is an elset)
   # 
   # If actual number of passes exceeds the set limit in XA_FOVRUN_MAXPASSES, an error is returned. However, the data in xa_emeDat is still valid.
   # currDs50TAI: Time, in ds50TAI, for which to compute the look angle (in-Double)
   # xa_fovSrc: source data, see XA_FOVSRC_? for array arrangement (in-Double[8])
   # vicSatKey: the victim satellite's unique key (in-Long)
   # xa_look: look angle data, see XA_LOOK_? for array arrangement (out-Double[8])
   dllObj.FovTargetElsetLook.restype = c_int
   dllObj.FovTargetElsetLook.argtypes = [c_double, c_double * 8, c_longlong, c_double * 8]


   # This function screens a potential victim satellite for penetrating the illumination cone between a source and a target (target is a vector: AZ/EL or RA/DEC).
   # See FovTargetElset for a description of the xa_emeDat array.
   # If actual number of passes exceeds the set limit in XA_FOVRUN_MAXPASSES, an error is returned. However, the data in xa_emeDat is still valid 
   # xa_fovRun: fov run parameters, see XA_FOVRUN_? for array arrangement (in-Double[8])
   # xa_fovSrc: source data, see XA_FOVSRC_? for array arrangement (in-Double[8])
   # xa_fovTgt: target data, see XA_FOVTGT_? for array arrangement (in-Double[8])
   # vicSatKey: the victim satellite's unique key (in-Long)
   # xa_emeDat: array of entry/minimum/exit (in Ds50TAI) times of each pass (out-Double[*, 3])
   # numOfPasses: number of passes found (out-Integer)
   dllObj.FovTargetVec.restype = c_int
   dllObj.FovTargetVec.argtypes = [c_double * 8, c_double * 8, c_double * 8, c_longlong, c_void_p, c_int_p]


   # This function returns a look angle from the source to the potential victim satellite at the specified time (target is a vector: AZ/EL or RA/DEC).
   # See FovGetDataFrInputFiles for a description of the XA_FOVSRC and XA_FOVTGT parameter values.
   # See FovTargetElsetLook for a description of the XA_LOOK parameter values.
   # currDs50TAI: Time, in ds50TAI, for which to compute the look angle (in-Double)
   # xa_fovSrc: source data, see XA_FOVSRC_? for array arrangement (in-Double[8])
   # xa_fovTgt: target data, see XA_FOVTGT_? for array arrangement (in-Double[8])
   # vicSatKey: the victim satellite's unique key (in-Long)
   # xa_look: look angle data, see XA_LOOK_? for array arrangement (out-Double[8])
   dllObj.FovTargetVecLook.restype = c_int
   dllObj.FovTargetVecLook.argtypes = [c_double, c_double * 8, c_double * 8, c_longlong, c_double * 8]


   # Resets all FOV control parameters back to their default values
   dllObj.FovReset.restype = None
   dllObj.FovReset.argtypes = []

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj

# Fov run parameters
# Maximum number of passes (entry/minimum/exit times) that FOV returns in one start/stop time
XA_FOVRUN_MAXPASSES= 0
# FOV start time in days since 1950, UTC
XA_FOVRUN_START    = 1
# FOV stop time in days since 1950, UTC
XA_FOVRUN_STOP     = 2
# Cone half angle (deg) (0=auto) (0-45)
XA_FOVRUN_HALFCONE = 3
# Search interval (min)
XA_FOVRUN_INTERVAL = 4

XA_FOVRUN_SIZE     = 8

# FOV source types
# Source is sensor
FOV_SRCTYPE_SEN = 1
# Source is lat lon height
FOV_SRCTYPE_LLH = 2
# Source is EFG
FOV_SRCTYPE_EFG = 3
# Source is XYZ
FOV_SRCTYPE_XYZ = 4

# FOV source types
# Target is elset
FOV_TGTTYPE_ELSET = 1
# Target is constant Az/El
FOV_TGTTYPE_AZEL  = 2
# Target is RA/Dec (STAR)
FOV_TGTTYPE_RADEC = 3

# FOV source specification
# 1=SEN   | 2=LLH       | 3=EFG      | 4=XYZ
XA_FOVSRC_TYPE  = 0
# Sensor# | Source ID   | Source ID  | Source ID
XA_FOVSRC_ID    = 1
# | N lat (deg) | EFG: E (m) | X (m)
XA_FOVSRC_ELEM1 = 2
# | E lon (deg) | EFG: F (m) | Y (m)
XA_FOVSRC_ELEM2 = 3
# | height (m)  | EFG: G (m) | Z (m)
XA_FOVSRC_ELEM3 = 4
# |             |            | time of position in Ds50UTC
XA_FOVSRC_ELEM4 = 5

XA_FOVSRC_SIZE  = 8


# FOV target specification
# 1=ELSET | 2=AZEL    | 3=RADEC
XA_FOVTGT_TYPE  = 0
# Elset#  | Target ID | Target ID
XA_FOVTGT_ID    = 1
# | az (deg)  | RA (deg)
XA_FOVTGT_ELEM1 = 2
# | el (deg)  | Dec (deg)
XA_FOVTGT_ELEM2 = 3
# |           | equinox indicator
XA_FOVTGT_ELEM3 = 4

XA_FOVTGT_SIZE  = 8

# entry/minimum/exit time data
# entry time (ds50UTC)
XA_EMEDAT_ENTRY = 0
# minimum time (ds50UTC)
XA_EMEDAT_MIN   = 1
# exit time (ds50UTC)
XA_EMEDAT_EXIT  = 2

XA_EMEDAT_SIZE  = 3

# FOV parameters
# Cone half angle (deg) (0=auto) (0-45)
XA_FOVCTRL_HALFCONE = 0
# Search interval (min)
XA_FOVCTRL_INTERVAL = 1
# Print option
XA_FOVCTRL_PRTOPT   = 2

XA_FOVCTRL_SIZE     = 8


# maximum number of windows/potential, victims/sources/targets allowed to be entered via an input file
FOVMAXNUM = 128

# ========================= End of auto generated code ==========================
