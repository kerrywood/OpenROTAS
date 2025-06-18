# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'SpProp.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'libspprop.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'libspprop.dylib'

def LoadSpPropDll():
   """ LoadSpPropDll() -- Loads SpProp.dll from the PATH or LD_LIBRARY_PATH
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
   # Initializes SpProp DLL for use in the program
   # If this function returns an error, it is recommended that the users stop the program immediately. The error occurs if the users forget to load and initialize all the prerequisite DLLs, as listed in the DLL Prerequisites section, before using this DLL. 
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.SpInit.restype = c_int
   dllObj.SpInit.argtypes = [c_longlong]


   # Returns information about the current version of SpProp DLL. The information is placed in the string parameter you pass in
   # The returned string provides information about the version number, build date, and the platform of the Sp DLL. 
   # infoStr: A string to hold the information about SpProp.dll (out-Character[128])
   dllObj.SpGetInfo.restype = None
   dllObj.SpGetInfo.argtypes = [c_char_p]


   # Loads SP-related parameters (SP application controls, prediction controls, numerical integration controls) from a text file
   # spInputFile: The name of the file containing SP-related parameters (in-Character[512])
   dllObj.SpLoadFile.restype = c_int
   dllObj.SpLoadFile.argtypes = [c_char_p]


   # Loads SP-related parameters (SP application controls, prediction controls, numerical integration controls) and SP elsets from a text file
   # spInputFile: The name of the file containing SP-related parameters and SP elsets (in-Character[512])
   dllObj.SpLoadFileAll.restype = c_int
   dllObj.SpLoadFileAll.argtypes = [c_char_p]


   # Saves currently loaded SP-related parameters (SP application controls, prediction controls, integration controls) to a file
   # The purpose of this function is to save the current SP-related settings, usually used in GUI applications, for future use.
   # spFile: The name of the file in which to save the settings (in-Character[512])
   # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
   # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for future) (in-Integer)
   dllObj.SpSaveFile.restype = c_int
   dllObj.SpSaveFile.argtypes = [c_char_p, c_int, c_int]


   # Initializes an SP satellite from an SP TLE, SPVEC, or VCM
   # Internally, when this function is called, the SpProp DLL will look into the right binary tree, based on the vector type extracted from the satKey, and search for the satKey. If found, the SpProp DLL will use the associated SP data to create an SP object for this satellite in its own binary tree. Subsequent calls to propagate this satellite will use the data in the SP object to compute the satellite's new state.
   # 
   # The users need to call this routine only once for each satellite they want to propagate or every time the satellite data, from which it was initialized, is changed. The call needs to be placed before any calls to the SP propagate routines (SpPropMse, SpPropDs50UTC...).
   # satKey: The satellite's unique key (in-Long)
   dllObj.SpInitSat.restype = c_int
   dllObj.SpInitSat.argtypes = [c_longlong]


   # Initializes an SP satellite from an SP TLE, SPVEC, or VCM (thread-safe)
   # Internally, when this function is called, the SpProp DLL will look into the right binary tree, based on the vector type extracted from the satKey, and search for the satKey. If found, the SpProp DLL will use the associated SP data to create an SP object for this satellite in its own binary tree. Subsequent calls to propagate this satellite will use the data in the SP object to compute the satellite's new state.
   # 
   # The users need to call this routine only once for each satellite they want to propagate or every time the satellite data, from which it was initialized, is changed. The call needs to be placed before any calls to the SP propagate routines (SpPropMse, SpPropDs50UTC...).
   # satKey: The satellite's unique key (in-Long)
   # xa_spParms: SP parameters for the initialized satellite (in-Double[32])
   dllObj.SpInitSat_MT.restype = c_int
   dllObj.SpInitSat_MT.argtypes = [c_longlong, c_double * 32]


   # Removes a satellite, represented by the satKey, from the set of currently loaded satellites
   # Calling this function removes all satellites from the set maintained by SpProp.dll. However, the data loaded by Vcm.dll, Tle.dll, SpVec.dll, and ExtEphem.dll is unaffected.
   # If the users enter an invalid satKey - a non-existing satKey in memory, the function will return a non-zero value indicating an error.
   # satKey: The unique key of the satellite to be removed (in-Long)
   dllObj.SpRemoveSat.restype = c_int
   dllObj.SpRemoveSat.argtypes = [c_longlong]


   # Removes all currently loaded satellites from memory
   # Calling this function removes all satellites from the set maintained by SpProp.dll. However, the data loaded by Vcm.dll, Tle.dll, SpVec.dll, and ExtEphem.dll is unaffected.
   # The function returns zero if all the satellites were removed successfully from the SpProp DLL's binary tree.
   dllObj.SpRemoveAllSats.restype = c_int
   dllObj.SpRemoveAllSats.argtypes = []


   # Returns the number of SP objects currently created. 
   dllObj.SpGetCount.restype = c_int
   dllObj.SpGetCount.argtypes = []


   # Removes all SP-related data from memory (Geo models, Flux records, JPL, DCA, etc.)
   dllObj.SpReset.restype = None
   dllObj.SpReset.argtypes = []


   # Retrieves the value of an SP application control parameter
   # 
   # The table below shows the values for the xf_SpApp parameter:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   # 
   # 1 Geopotential directory path
   # 2 Buffer size
   # 3 Run mode
   # 4 Save partials data
   # 5 Specter compatibility mode
   # 6 Consider parameter
   # 7 Decay altitude
   # 8 Output coordinate system
   # 9 Additional VCM options
   # 
   # xf_SpApp: Predefined value specifying which application control parameter to retrieve (in-Integer)
   # valueStr: A string to hold the retrieved application control parameter (out-Character[512])
   dllObj.SpGetApCtrl.restype = None
   dllObj.SpGetApCtrl.argtypes = [c_int, c_char_p]


   # Retrieves all SP application control parameters with a single function call
   # geoDir: geopotential directory path (out-Character[512])
   # bufSize: buffer size [5000] (out-Integer)
   # runMode: run mode: 0=performance priority, [1]=memory priority (out-Integer)
   # savePartials: propagate covariance matrix: 0=don't propagate, 1=propagate covariance matrix (if VCM has it) (out-Integer)
   # isSpectr: spectr mode: 0=not compatible, 1=SPECTR compatible (out-Integer)
   # consider: consider parameter (set it to 12 to match operational system) (out-Double)
   # decayAlt: decay altitude (km) [10] (out-Integer)
   # outCoord: ouput cooridnate system: [0]=TEME of Date, 1=TEME of Epoch, 2=MEME of J2K (out-Integer)
   dllObj.SpGetApCtrlAll.restype = None
   dllObj.SpGetApCtrlAll.argtypes = [c_char_p, c_int_p, c_int_p, c_int_p, c_int_p, c_double_p, c_int_p, c_int_p]


   # Sets an SP application control parameter
   # See SpGetApCtrl for a list of the values for the xf_SpApp parameter.
   # xf_SpApp: predefined value specifying which application control parameter to set (in-Integer)
   # valueStr: the new value of the specified parameter, expressed as a string (in-Character[512])
   dllObj.SpSetApCtrl.restype = None
   dllObj.SpSetApCtrl.argtypes = [c_int, c_char_p]


   # Sets all SP application control parameters with a single function call
   # geoDir: geopotential directory path (in-Character[512])
   # bufSize: buffer size [5000] (in-Integer)
   # runMode: run mode: 0=performance priority, [1]=memory priority (in-Integer)
   # savePartials: propagate covariance matrix: 0=don't propagate, 1=propagate covariance matrix (if VCM has it) (in-Integer)
   # isSpectr: spectr mode: 0=not compatible, 1=SPECTR compatible (in-Integer)
   # consider: consider parameter (set it to 12 to match operational system) (in-Double)
   # decayAlt: decay altitude (km) [10] (in-Integer)
   # outCoord: ouput cooridnate system: [0]=TEME of Date, 1=TEME of Epoch, 2=MEME of J2K (in-Integer)
   dllObj.SpSetApCtrlAll.restype = None
   dllObj.SpSetApCtrlAll.argtypes = [c_char_p, c_int, c_int, c_int, c_int, c_double, c_int, c_int]


   # Retrieves the value of a numerical integration control parameter
   # 
   # The table below shows the values for xf_4P parameter:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   # 
   # 1   Geopotential model to use
   # 2   Earth gravity pertubations flag
   # 3   Drag pertubations flag 
   # 4   Radiation pressure pertubations flag
   # 5   Lunar/Solar pertubations flag
   # 6   F10 value
   # 7   F10 average value
   # 8   Ap value
   # 9   Geopotential truncation order/degree/zonals
   # 10  Corrector step convergence criterion; exponent of 1/10; default = 10
   # 11  Outgassing pertubations flag
   # 12  Solid earth ocean tide pertubations flag
   # 13  Input vector coordinate system
   # 14  Nutation terms
   # 15  Recompute pertubations at each corrector step
   # 16  Variable of intergration control
   # 17  Variable step size control
   # 18  Initial step size
   # 21  DCA file name
   # 22  Solar flux file name
   # 23  Geopotential file name
   # 24  JPL file name
   # 25  JPL start time
   # 26  JPL stop time
   # 
   # xf_4P: Predefined value specifying which application control parameter to retrieve (in-Integer)
   # valueStr: A string to hold the retrieved application control parameter (out-Character[512])
   dllObj.SpGet4P.restype = None
   dllObj.SpGet4P.argtypes = [c_int, c_char_p]


   # Sets the value of a numerical integration control parameter
   # See SpGet4P for a list of the values for the xf_4P parameter.
   # For flux, dca, and jpl file settings, the actual file loading happens when the first SpSatInit() is called. 
   # If the user needs to load these files instantly, please call the SpLoadFile() instead
   # xf_4P: predefined value specifying which application control parameter to set (in-Integer)
   # valueStr: the new value of the specified parameter, expressed as a string (in-Character[512])
   dllObj.SpSet4P.restype = None
   dllObj.SpSet4P.argtypes = [c_int, c_char_p]


   # Retrieves prediction control parameters
   # startFrEpoch: start time flag: 0=in days since 1950 UTC, 1=in minutes since epoch (out-Integer)
   # stopFrEpoch: stop time flag : 0=in days since 1950 UTC, 1=in minutes since epoch (out-Integer)
   # startTime: start time value (out-Double)
   # stopTime: stop time value (out-Double)
   # interval: step size (min) (out-Double)
   dllObj.SpGetPredCtrl.restype = None
   dllObj.SpGetPredCtrl.argtypes = [c_int_p, c_int_p, c_double_p, c_double_p, c_double_p]


   # Sets prediction control parameters
   # startFrEpoch: start time flag: 0=in days since 1950 UTC, 1=in minutes since epoch (in-Integer)
   # stopFrEpoch: stop time flag : 0=in days since 1950 UTC, 1=in minutes since epoch (in-Integer)
   # startTime: start time value (in-Double)
   # stopTime: stop time value (in-Double)
   # interval: step size (min) (in-Double)
   dllObj.SpSetPredCtrl.restype = None
   dllObj.SpSetPredCtrl.argtypes = [c_int, c_int, c_double, c_double, c_double]


   # Retrieves the value of a field of an SP satellite
   # 
   # The table below shows the values for the xf_SpSat parameter:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   # 
   # 1  Satellite number I5
   # 2  Satellite's epoch time in days since 1950, UTC 
   # 3  Satellite's epoch time in days since 1950, TAI
   # 4  Mu value 
   # 5  Covariance Matrix flag
   # 6  Integration mode
   # 7  Nutation terms
   # 8  Specter compatibility mode
   # 
   # satKey: The satellite's unique key (in-Long)
   # xf_SpSat: Predefined number specifying which field to retrieve (in-Integer)
   # valueStr: A string containing the value of the specified field (out-Character[512])
   dllObj.SpGetSatData.restype = c_int
   dllObj.SpGetSatData.argtypes = [c_longlong, c_int, c_char_p]


   # Retrieves all fields of an SP satellite with a single function call
   # satKey: The satellite's unique key (in-Long)
   # satNum: Satellite number (out-Integer)
   # epochDs50UTC: Satellite's epoch time in days since 1950 UTC (out-Double)
   # epochDs50TAI: Satellite's epoch time in days since 1950 TAI (out-Double)
   # mu: mu value from Satellite's geopotential model (out-Double)
   # hasCovMtx: 0=This satellite doesn't have covariance matrix, 1=This satellite has covariance matrix (out-Integer)
   # integMode: Partials computation mode: 0=no partials, 1=numerical, 2=semi-analytic (out-Integer)
   # nTerms: number of nutation terms (out-Integer)
   # isSpectr: Spectr compatible mode: 0=not compatible, 1=compatible (out-Integer)
   dllObj.SpGetSatDataAll.restype = c_int
   dllObj.SpGetSatDataAll.argtypes = [c_longlong, c_int_p, c_double_p, c_double_p, c_double_p, c_int_p, c_int_p, c_int_p, c_int_p]


   # Propagates a satellite, represented by the satKey, to the time expressed in minutes since the 
   # satellite's epoch time
   # satKey: The satellite's unique key (in-Long)
   # mse: The requested time in minutes since the satellite's epoch time (in-Double)
   # xa_timeTypes: The output array that stores different time types, see XA_TIMETYPES_? for array arrangement (out-Double[5])
   # revNum: The resulting revolution number (out-Integer)
   # posJ2K: The resulting position vector (km) in MEME of J2K (out-Double[3])
   # velJ2K: The resulting velocity vector (km/s) in MEME of J2K (out-Double[3])
   dllObj.SpPropMse.restype = c_int
   dllObj.SpPropMse.argtypes = [c_longlong, c_double, c_double * 5, c_int_p, c_double * 3, c_double * 3]


   # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC. 
   # satKey: The satellite's unique key (in-Long)
   # ds50UTC: The requested time in days since 1950 UTC (in-Double)
   # xa_timeTypes: The output array that stores different time types, see XA_TIMETYPES_? for array arrangement (out-Double[5])
   # revNum: The resulting revolution number (out-Integer)
   # posJ2K: The resuling position vector (km) in MEME of J2K (out-Double[3])
   # velJ2K: The resulting velocity vector (km/s) in MEME of J2K (out-Double[3])
   dllObj.SpPropDs50UTC.restype = c_int
   dllObj.SpPropDs50UTC.argtypes = [c_longlong, c_double, c_double * 5, c_int_p, c_double * 3, c_double * 3]


   # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC. 
   # It only returns the latitude, longitude, and height at that time in coordinate system of Date
   # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to check for decay or low altitude, they can put that logic into their own code.
   # 
   # This function is built especially for application that plots ground trace.
   # satKey: The satellite's unique key (in-Long)
   # ds50UTC: The requested time in days since 1950 UTC (in-Double)
   # llh: The resulting array: 1=geodetic latitude (deg), 2=geodetic longitude (deg), 3=height (km) (out-Double[3])
   dllObj.SpPropDs50UtcLLH.restype = c_int
   dllObj.SpPropDs50UtcLLH.argtypes = [c_longlong, c_double, c_double * 3]


   # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC. 
   # It only returns the satellite's ECI position in TEME of DATE
   # It is the users' responsibility to decide what to do with the returned value. For example, if the users want to check for decay or low altitude, they can put that logic into their own code.
   # 
   # This function is built especially for application that plots satellites' positions in 3D.
   # satKey: The satellite's unique key (in-Long)
   # ds50UTC: The requested time in days since 1950 UTC (in-Double)
   # pos: The resulting ECI position (km) in TEME of Date (out-Double[3])
   dllObj.SpPropDs50UtcPos.restype = c_int
   dllObj.SpPropDs50UtcPos.argtypes = [c_longlong, c_double, c_double * 3]


   # Propagates a satellite, represented by the satKey, to the time expressed in either minutes since epoch or days since 1950, UTC. 
   # 
   # All propagation data is returned by this function.
   # satKey: The unique key of the satellite to propagate. (in-Long)
   # timeType: The propagation time type: 0 = minutes since epoch, 1 = days since 1950, UTC (in-Integer)
   # timeIn: The time to propagate to, expressed in either minutes since epoch or days since 1950, UTC. (in-Double)
   # covType: Covariance matrix type, if available: 0=don't propagate, 1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K (in-Integer)
   # xa_spOut: The array that stores all Sp propagation data, see XA_SPOUT_? for array arrangement (out-Double[128])
   dllObj.SpPropAll.restype = c_int
   dllObj.SpPropAll.argtypes = [c_longlong, c_int, c_double, c_int, c_double * 128]


   # Propagates a satellite, represented by the satKey, to the time expressed in days since 1950, UTC. 
   # It only returns the position and velocity in TEME of Date
   # satKey: The satellite's unique key (in-Long)
   # ds50UTC: The requested time in days since 1950 UTC (in-Double)
   # posDate: The resulting ECI position (km) in TEME of Date (out-Double[3])
   # velDate: The resulting ECI velocity (km/s) in TEME of Date (out-Double[3])
   dllObj.SpGetStateDs50UTC.restype = c_int
   dllObj.SpGetStateDs50UTC.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3]


   # Reepochs the state of an existing SP object associated with the satKey. 
   # Proper initialization is handled internally so no need to call SpSatInit() afterward 
   # satKey: The satellite's unique key (in-Long)
   # ds50UTC: The requested new epoch time in days since 1950 UTC (in-Double)
   # posDate: The initial ECI position (km) in TEME of Date (in-Double[3])
   # velDate: The initial ECI velocity (km/s) in TEME of Date (in-Double[3])
   dllObj.SpSetStateDs50UTC.restype = c_int
   dllObj.SpSetStateDs50UTC.argtypes = [c_longlong, c_double, c_double * 3, c_double * 3]


   # Updates an SP object associated with the satKey with the new input data stored in setDataArr. 
   # Then propagates the updated SP object to the requested time propTimeDs50UTC. 
   # Resulting propagated data will be stored in propDataArr.
   # satKey: The satellite's unique key (in-Long)
   # setDataArr: 0-2: posECI (km), 3-5: velECI (km/s), 6: bTerm (m2/kg), 7: agom (m2/kg) (in-Double[128])
   # propTimeDs50UTC: The requested time in days since 1950 UTC (in-Double)
   # propDataArr: 0-2: out posECI (km), 3-5: out velECI (km/s), 6-127: NA (out-Double[128])
   dllObj.SpSetAndProp.restype = c_int
   dllObj.SpSetAndProp.argtypes = [c_longlong, c_double * 128, c_double, c_double * 128]


   # This function is reserved for future use. The purpose is to return propagator output data based on user special requests that have not yet been determined
   # Use this function immediately after the call to SpPropMse or SpPropDs50UTC. 
   # satKey: The satellite's unique key (in-Long)
   # index: Index specified ouput data (in-Integer)
   # destArr: The resulting array (out-Double[*])
   dllObj.SpGetPropOut.restype = c_int
   dllObj.SpGetPropOut.argtypes = [c_longlong, c_int, c_void_p]


   # Returns the covariance matrix of a satellite
   # Use this function immediately after the call to SpPropMse or SpPropDs50UTC. 
   # satKey: The satellite's unique key (in-Long)
   # covType: Covariance matrix type: 1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K (in-Integer)
   # covMtx: Resulting covariance matrix 6x6 (out-Double[6, 6])
   dllObj.SpGetCovMtx.restype = c_int
   dllObj.SpGetCovMtx.argtypes = [c_longlong, c_int, c_void_p]


   # Computes the covariance sigma from the input covariance matrix
   # covMtx: Input covariance matrix (in-Double[6, 6])
   # covSigma: Resulting covariance sigma (out-Double[6])
   dllObj.SpCompCovSigma.restype = None
   dllObj.SpCompCovSigma.argtypes = [c_void_p, c_double * 6]


   # Sets all numerical integration control parameters with a single function call
   # geoIdx: geopotential model (in-Integer)
   # bulgePert: earth gravity flag (in-Integer)
   # dragPert: drag pertubation flag (in-Integer)
   # radPresPert: radiation pressure pertubation flag (in-Integer)
   # lunSolPert: lunar/solar pertubation flag (in-Integer)
   # f10: f10 value (in-Integer)
   # f10Avg: f10 average value (in-Integer)
   # ap: ap (in-Integer)
   # trunc: geo truncation order/degree/zonals (in-Integer)
   # incr: corrector step convergenece criterion (in-Integer)
   # ogPert: outgassing pertubation flag (in-Integer)
   # tidePert: solid earth + ocean tide pertubation flag (in-Integer)
   # inCoord: input vector coordinate system (in-Integer)
   # nTerms: nutation terms (in-Integer)
   # reEval: recompute pertubations at each corrector step (in-Integer)
   # integStepMode: variable of integration control (in-Integer)
   # stepSizeMethod: variable step size control (in-Integer)
   # initStepSize: initial step size (in-Double)
   # dcaFile: DCA file name (in-Character[512])
   # fluxFile: Flux file name (in-Character[512])
   # geoFile: Geo file name (in-Character[512])
   # jplFile: JPL file name (in-Character[512])
   # jplStart: JPL start time (in-Character[512])
   # jplStop: JPL stop time (in-Character[512])
   dllObj.SpSet4pAll.restype = None
   dllObj.SpSet4pAll.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]


   # Retrieves all numerical integration control parameters with a single function call
   # geoIdx: geopotential model (out-Integer)
   # bulgePert: earth gravity flag (out-Integer)
   # dragPert: drag pertubation flag (out-Integer)
   # radPresPert: radiation pressure pertubation flag (out-Integer)
   # lunSolPert: lunar/solar pertubation flag (out-Integer)
   # f10: f10 value (out-Integer)
   # f10Avg: f10 average value (out-Integer)
   # ap: ap (out-Integer)
   # trunc: geo truncation order/degree/zonals (out-Integer)
   # incr: corrector step convergenece criterion (out-Integer)
   # ogPert: outgassing pertubation flag (out-Integer)
   # tidePert: solid earth + ocean tide pertubation flag (out-Integer)
   # inCoord: input vector coordinate system (out-Integer)
   # nTerms: nutation terms (out-Integer)
   # reEval: recompute pertubations at each corrector step (out-Integer)
   # integStepMode: variable of integration control (out-Integer)
   # stepSizeMethod: variable step size control (out-Integer)
   # initStepSize: initial step size (out-Double)
   # dcaFile: DCA file name (out-Character[512])
   # fluxFile: Flux file name (out-Character[512])
   # geoFile: Geo file name (out-Character[512])
   # jplFile: JPL file name (out-Character[512])
   # jplStart: JPL start time (out-Character[512])
   # jplStop: JPL stop time (out-Character[512])
   dllObj.SpGet4pAll.restype = None
   dllObj.SpGet4pAll.argtypes = [c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_double_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p, c_char_p]


   # Read the integration control settings from a 4P-Card
   # card4P: The input 4P card (in-Character[512])
   dllObj.SpSet4PCard.restype = c_int
   dllObj.SpSet4PCard.argtypes = [c_char_p]


   # Builds and returns the integration control card (4P-Card) from the current settings
   # card4P: A string to hold the retrieved 4P card (out-Character[512])
   dllObj.SpGet4PCard.restype = None
   dllObj.SpGet4PCard.argtypes = [c_char_p]


   # Adds one solar flux record to memory. This API can be used to avoid SpLoadFile's file I/O      
   # refDs50UTC: Time tag of this record (DS50; UTC) (in-Double)
   # f10: f10 value (in-Double)
   # f10Avg: f10avg value (in-Double)
   # ap: Array of 3-hourly values of Ap (in-Double[8])
   dllObj.SpAddFluxRec.restype = c_int
   dllObj.SpAddFluxRec.argtypes = [c_double, c_double, c_double, c_double * 8]


   # Returns the times, in days since 1950 UTC, of ephemeris points stored in SP buffer that meet the requirement as specified in the minStepSize
   # This function is used to retrieve times in which SP propagator stored satellite's state vectors in memory (natural integration step size).
   # An error will occur if the actualEphPts reaches the maxEphPts. In this case, the function will return all ephemereris times up to the time when that maxEphPts is reached.
   # satKey: The satellite's unique key (in-Long)
   # maxEphPts: Maximum number of possible ephemeris points that the function won't go over. That means actualEphPts can't be greater than maxEphPts even though the time span may have more points than that (in-Integer)
   # startDs50UTC: Start time in days since 1950 UTC (in-Double)
   # stopDs50UTC: Stop time in days since 1950 UTC (in-Double)
   # minStepSize: Option to thin ephem points. Only pick ephem point when its next ephem point is older than the specified minStepSize (minutes). Set to 0 to get all ephem points (SP natural integration step size) (in-Double)
   # actualEphPts: Actual number of ephem points that meet the requirements (out-Integer)
   # ds50UTCArr: The resulting time array, in days since 1950 UTC, of all ephem points that meet the requirements (out-Double[*])
   dllObj.SpGetEphemTimes.restype = c_int
   dllObj.SpGetEphemTimes.argtypes = [c_longlong, c_int, c_double, c_double, c_double, c_int_p, c_void_p]


   # Generates ephemerides for the input satellite, represented by its satKey, for the specified time span and step size
   # Notes: if arrSize isn't big enough to store all the ephemeris points, the function will exit when the ephemArr reaches
   # that many points (arrSize) and the errCode is set to IDX_ERR_WARN
   # satKey: The unique key of the satellite to generate ephemerides. (in-Long)
   # startDs50UTC: Start time expressed in days since 1950, UTC. (in-Double)
   # stopDs50UTC: End time expressed in days since 1950, UTC. (in-Double)
   # stepSize: Step size in minutes, set to 0 if want to use SP natural integration step size (in-Double)
   # sp_ephem: Output ephemeris type: 1=ECI, 2=J2K. (in-Integer)
   # arrSize: Size of input ephemArr (in-Integer)
   # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec) (out-Double[*, 7])
   # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
   dllObj.SpGenEphems.restype = c_int
   dllObj.SpGenEphems.argtypes = [c_longlong, c_double, c_double, c_double, c_int, c_int, c_void_p, c_int_p]


   # This function is similar to SpGenEphems but also returns covariance matrix data
   # Notes: Make sure to turn on the "save partials" flag so that covariance matrix data can be generated
   # satKey: The unique key of the satellite to generate ephemerides. (in-Long)
   # startDs50UTC: Start time expressed in days since 1950, UTC. (in-Double)
   # stopDs50UTC: End time expressed in days since 1950, UTC. (in-Double)
   # stepSize: Step size in minutes, set to 0 if want to use SP natural integration step size (in-Double)
   # sp_ephem: Output ephemeris type: 1=ECI, 2=J2K. (in-Integer)
   # covType: Covariance matrix type, if available: 0=don't propagate,  1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K (in-Integer)
   # arrSize: Size of input ephemArr (in-Integer)
   # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec), 7-27: 21-elements lower triagular covariance matrix (out-Double[*, 28])
   # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
   dllObj.SpGenEphemsCov.restype = c_int
   dllObj.SpGenEphemsCov.argtypes = [c_longlong, c_double, c_double, c_double, c_int, c_int, c_int, c_void_p, c_int_p]


   # Generates ephemerides for the input vcm (in string format) for the specified time span and step size
   # Notes: if arrSize isn't big enough to store all the ephemeris points, the function will exit when the ephemArr reaches
   # that many points (arrSize) and the errCode is set to IDX_ERR_WARN
   # vcmString: 1-line or concatenated string representation of the VCM (in-Character[4000])
   # startDs50UTC: Start time expressed in days since 1950, UTC. (in-Double)
   # stopDs50UTC: End time expressed in days since 1950, UTC. (in-Double)
   # stepSize: Step size in minutes, set to 0 if want to use SP natural integration step size (in-Double)
   # sp_ephem: Output ephemeris type: 1=ECI, 2=J2K. (in-Integer)
   # arrSize: Size of input ephemArr (in-Integer)
   # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec) (out-Double[*, 7])
   # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
   dllObj.SpGenEphemsVcm_OS.restype = c_int
   dllObj.SpGenEphemsVcm_OS.argtypes = [c_char_p, c_double, c_double, c_double, c_int, c_int, c_void_p, c_int_p]


   # This function is similar to SpGenEphemsVcm_OS but also returns covariance matrix data
   # vcmString: 1-line or concatenated string representation of the VCM (in-Character[4000])
   # startDs50UTC: Start time expressed in days since 1950, UTC. (in-Double)
   # stopDs50UTC: End time expressed in days since 1950, UTC. (in-Double)
   # stepSize: Step size in minutes, set to 0 if want to use SP natural integration step size (in-Double)
   # sp_ephem: Output ephemeris type: 1=ECI, 2=J2K. (in-Integer)
   # covType: Covariance matrix type, if available:  1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K (in-Integer)
   # arrSize: Size of input ephemArr (in-Integer)
   # ephemArr: Output ephemerides - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec), 7-27: 21-elements lower triagular covariance matrix (out-Double[*, 28])
   # genEphemPts: Actual number of ephemeris points generated (always &le; arrSize) (out-Integer)
   dllObj.SpGenEphemsVcmCov_OS.restype = c_int
   dllObj.SpGenEphemsVcmCov_OS.argtypes = [c_char_p, c_double, c_double, c_double, c_int, c_int, c_int, c_void_p, c_int_p]


   # Propagates all input satellites, represented by their satKeys, to the time expressed in days since 1950, UTC. 
   # satKeys: The satellite keys of all input satellites (in-Long[*])
   # numOfSats: The total number of satellites (in-Integer)
   # ds50UTC: The time to propagate all satelllites to, expressed in days since 1950, UTC. (in-Double)
   # ephemArr: 0-2: pos (km), 3-5: vel (km/sec) - ECI TEME of Date (out-Double[*, 6])
   dllObj.SpPropAllSats.restype = c_int
   dllObj.SpPropAllSats.argtypes = [c_void_p, c_int, c_double, c_void_p]


   # Propagates a satellite, represented by the satKey, to the time expressed in either minutes since epoch or days since 1950, UTC. 
   # 
   # All propagation data is returned by this function.
   # satKey: The unique key of the satellite to propagate. (in-Long)
   # timeType: The propagation time type: 0 = minutes since epoch, 1 = days since 1950, UTC (in-Integer)
   # timeIn: The time to propagate to, expressed in either minutes since epoch or days since 1950, UTC. (in-Double)
   # spCoord: Output coordinate systems for pos/vel/acc, see SPCOORD_? for options (in-Integer)
   # xf_CovMtx: Covariance matrix type, see XF_COVMTX_? for options (in-Integer)
   # stmType: State transition matrix type, see STMTYPE_? for options (in-Integer)
   # xa_spExt: The array that stores all Sp propagation data, see XA_SPEXT_? for array arrangement (out-Double[128])
   dllObj.SpPropAllExt.restype = c_int
   dllObj.SpPropAllExt.argtypes = [c_longlong, c_int, c_double, c_int, c_int, c_int, c_double * 128]


   # Loads solar flux file (J70MOD or JBH09) for use in AtmspDensity() 
   # fluxFile: The name of the file containing SP-related parameters (in-Character[512])
   dllObj.SpLoadFluxFile.restype = c_int
   dllObj.SpLoadFluxFile.argtypes = [c_char_p]


   # Loads DCA temperature coefficient file (DCA1/HASDM1 or DCA2/HASDM2) for use in AtmspDensity()
   # dcaFile: The name of the file containing SP-related parameters (in-Character[512])
   dllObj.SpLoadDCAFile.restype = c_int
   dllObj.SpLoadDCAFile.argtypes = [c_char_p]


   # Computes atmospheric density using the input time/location/drag model
   # ds50UTC: Input time, expressed in days since 1950, UTC. (in-Double)
   # llh: Input array: latitude (deg)/longitude (deg)/height (km-above geoid) (in-Double[3])
   # drgMdl: Drag perturbations model, see DRGMDL_x for available options (in-Integer)
   # rho: Atmospheric density (kg / m**3) (out-Double)
   # errCode: Error code - 0 if successful, non-0 if there is an error (out-Integer)
   dllObj.AtmspDensity.restype = None
   dllObj.AtmspDensity.argtypes = [c_double, c_double * 3, c_int, c_double_p, c_int_p]


   # Gets DCA Record at specified time
   # ds50UTC: Request Time (in-Double)
   # ds50UTCRec: Time of the DCA record (out-Double)
   # flux: S10,S54,M10,M54,Y10,Y54,F10,F54 for IVER=3 JBH09 DCA (out-Double[8])
   # storm: ap,Dst,DTC geomagnetic storm values IVER=3 JBH09 DCA (out-Double[3])
   # ctxi: Even spherical harmonic coefficients for DTX (out-Double[7, 7])
   # stxi: Odd spherical harmonic coefficients for DTX (out-Double[7, 7])
   # ctci: Even spherical harmonic coefficients for DTC (out-Double[7, 7])
   # stci: Odd spherical harmonic coefficients for DTC (out-Double[7, 7])
   # errCode: Error code - 0 if successful, non-0 if there is an error (out-Integer)
   dllObj.GetDcaRec.restype = None
   dllObj.GetDcaRec.argtypes = [c_double, c_double_p, c_double * 8, c_double * 3, c_void_p, c_void_p, c_void_p, c_void_p, c_int_p]


   # Unloads the flux/JBHSGI flux
   dllObj.SpRemoveFlux.restype = None
   dllObj.SpRemoveFlux.argtypes = []


   # Unloads the DCA records
   dllObj.SpRemoveDCAFile.restype = None
   dllObj.SpRemoveDCAFile.argtypes = []

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj

# VCM additional options
# use VCM's own data
VCMOPT_USEOWN    = 0
# force VCM to use global solar flux and timing constants data
VCMOPT_USEGLOBAL = 1

# Run Modes
# Perfromance priority. This mode allows the buffer of integration points to extend freely
IDX_RUNMODE_PERF = 0
# Memory priority. This mode only allows a number of integration points to be saved in the buffer at any one time
IDX_RUNMODE_MEM  = 1

#*******************************************************************************

# Partials Saving Modes
# Save partials in the buffer
IDX_PARTIALS_SAVE = 1
# Don't save partials in the buffer
IDX_PARTIALS_DONT = 0

# Indexes of different covariance matrices
# UVW convariance matrix - TEME of DATE
XF_COVMTX_UVW_DATE  =  1
# Cartesian covariance matrix - TEME of DATE
XF_COVMTX_XYZ_DATE  =  2
# Equinoctial covariance matrix - TEME of DATE (not available for "PARTIALS: ANALYTIC")
XF_COVMTX_EQNX_DATE =  3
# UVW convariance matrix - MEME of J2K (same result as UVW TEME of DATE)
XF_COVMTX_UVW_J2K   = 11
# Cartesian covariance matrix - MEME of J2K
XF_COVMTX_XYZ_J2K   = 12
# Equinoctial covariance matrix - MEME of J2K  (not available for "PARTIALS: ANALYTIC")
XF_COVMTX_EQNX_J2K  = 13
#*******************************************************************************

# Indexes of Lunar/Solar and Planets perturbation modes
# Lunar/Solar perturbation off
LSPERT_NONE      = 0
# Lunar/Solar perturbation on (using Analytic mode)
LSPERT_ANALYTIC  = 1
# Lunar/Solar perturbation using JPL ephemeris file
LSPERT_JPL       = 2
# Lunar/Solar + All planets perturbation using JPL ephemeris file
LSPERT_ALL       = 3
# Lunar/Solar + Jupiter and Venus using JPL ephemeris file (Big Force Planets)
LSPERT_BIG       = 4
# Lunar/Solar + Jupiter, Venus, Saturn, Mars, and Mercury using JPL ephemeris file (Big and Medium Force Planets)
LSPERT_MED       = 5
# Lunar/Solar + All planets perturbation except Pluto using JPL ephemeris file (Big, Medium, and Small Force Planets)
LSPERT_SMA       = 6

#*******************************************************************************

# State Transition Matrix Types
# UVW state transition matrix
STMTYPE_UVW       = 1
# Cartesian state transition matrix
STMTYPE_XYZ       = 2
# Equinoctial state transition matrix
STMTYPE_EQNX      = 3

# Different output coordinate systems options for pos/vel/acc
# Output coordinate systems in TEME of Date
SPCOORD_ECI      = 1
# Output coordinate systems in MEME of J2K
SPCOORD_J2K      = 2

# Different drag perturbation models
# Jacchia 64 model
DRGMDL_JAC64   =  1
# Jacchia 70 model
DRGMDL_JAC70   =  2
# Dynamic Calibration Atmosphere 1 (DCA1/HASDM1) model
DRGMDL_DCA1    =  3
# JBH09 model
DRGMDL_JBH09   = 40
# JBH09 and Dynamic Calibration Atmosphere 2 (DCA2/HASDM2)
DRGMDL_JBHDCA2 = 41

# Indexes of SP 4P card fields
# Geopotential model to use
XF_4P_GEOIDX   = 1
# Earth gravity pertubations flag
XF_4P_BULGEFLG = 2
# Drag pertubations flag
XF_4P_DRAGFLG  = 3
# Radiation pressure pertubations flag
XF_4P_RADFLG   = 4
# Lunar/Solar pertubations flag
XF_4P_LUNSOL   = 5
# F10 value
XF_4P_F10      = 6
# F10 average value
XF_4P_F10AVG   = 7
# Ap value
XF_4P_AP       = 8
# Geopotential truncation order/degree/zonals
XF_4P_TRUNC    = 9
# Corrector step convergence criterion; exponent of 1/10; default = 10
XF_4P_CONVERG  = 10
# Outgassing pertubations flag
XF_4P_OGFLG    = 11
# Solid earth and ocean tide pertubations flag
XF_4P_TIDESFLG = 12
# Input vector coordinate system
XF_4P_INCOORD  = 13
# Nutation terms
XF_4P_NTERMS   = 14
# Recompute pertubations at each corrector step
XF_4P_REEVAL   = 15
# Variable of intergration control
XF_4P_INTEGCTRL= 16
# Variable step size control
XF_4P_VARSTEP  = 17
# Initial step size
XF_4P_INITSTEP = 18

# DCA file name
XF_4P_DCAFILE  = 21
# Solar flux file name
XF_4P_FLUXFILE = 22
# Geopotential file name
XF_4P_GEOFILE  = 23
# JPL file name
XF_4P_JPLFILE  = 24
# JPL start time
XF_4P_JPLSTART = 25
# JPL stop time
XF_4P_JPLSTOP  = 26

#XF_4P_PLANETS  = 27, &    # Sets perturbations from all planets to on
#XF_4P_MERCURY  = 28, &    # Sets perturbation from Mercury to on
#XF_4P_VENUS    = 29, &    # Sets perturbation from Venus to on
#XF_4P_MARS     = 30, &    # Sets perturbation from Mars to on
#XF_4P_JUPITER  = 31, &    # Sets perturbation from Jupiter to on
#XF_4P_SATURN   = 32, &    # Sets perturbation from Saturn to on
#XF_4P_URANUS   = 33, &    # Sets perturbation from Uranus to on
#XF_4P_NEPTUNE  = 34, &    # Sets perturbation from Neptune to on
#XF_4P_PLUTO    = 35;      # Sets perturbation from Pluto to on

#*******************************************************************************

# Indexes of SP application control (preference) parameters
# Geopotential directory path
XF_SPAPP_GEODIR   = 1
# Buffer size
XF_SPAPP_BUFSIZE  = 2
# Run mode, see IDX_RUNMODE_ for available options
XF_SPAPP_RUNMODE  = 3
# Save partials data
XF_SPAPP_SAVEPART = 4
# Specter compatibility mode
XF_SPAPP_SPECTR   = 5
# Consider parameter
XF_SPAPP_CONSIDER = 6
# Decay altitude
XF_SPAPP_DECAYALT = 7
# Output coordinate system
XF_SPAPP_OUTCOORD = 8
# VCM additional options
XF_SPAPP_VCMOPT   = 9

#*******************************************************************************

# Indexes of data fields of an initialized SP satellite
# Satellite number I5
XF_SPSAT_SATNUM  = 1
# Satellite's epoch time in days since 1950, UTC
XF_SPSAT_DS50UTC = 2
# Satellite's epoch time in days since 1950, TAI
XF_SPSAT_DS50TAI = 3
# Mu value
XF_SPSAT_MU      = 4
# Covariance Matrix flag
XF_SPSAT_HASCOV  = 5
# Integration mode
XF_SPSAT_INTMODE = 6
# Nutation terms
XF_SPSAT_NTERMS  = 7
# Specter compatibility mode
XF_SPSAT_SPECTR  = 8

#*******************************************************************************

## Indexes of Planetary Control
#   XAI_PLANET_MERCURY = 1, & # 0 = off, 1 = on
#   XAI_PLANET_VENUS   = 2, & # 0 = off, 1 = on
#   XAI_PLANET_EARTH   = 3, & # Not used
#   XAI_PLANET_MARS    = 4, & # 0 = off, 1 = on
#   XAI_PLANET_JUPITER = 5, & # 0 = off, 1 = on
#   XAI_PLANET_SATRUN  = 6, & # 0 = off, 1 = on
#   XAI_PLANET_URANUS  = 7, & # 0 = off, 1 = on
#   XAI_PLANET_NEPTUNE = 8, & # 0 = off, 1 = on
#   XAI_PLANET_PLUTO   = 9, & # 0 = off, 1 = on
#   XAI_PLANET_SIZE    = 9;   # Size of array
#
##*******************************************************************************

# Different time types for passing to SpPropAll
# propagation time is in minutes since epoch
SP_TIMETYPE_MSE      = 0
# propagation time is in days since 1950, UTC
SP_TIMETYPE_DS50UTC  = 1


# Sp propagated data
# Propagation time in days since 1950, UTC
XA_SPOUT_UTC       =  0
# Propagation time in minutes since the satellite's epoch time
XA_SPOUT_MSE       =  1
# Propagation time in days since 1950, UT1
XA_SPOUT_UT1       =  2
# Propagation time in days since 1950, TAI
XA_SPOUT_TAI       =  3
# Propagation time in days since 1950, ET
XA_SPOUT_ET        =  4
# Revolution number
XA_SPOUT_REVNUM    =  5
# Number of nutation terms
XA_SPOUT_NTERMS    =  6
# Spectr compatible mode (0=not compatible, 1=compatible)
XA_SPOUT_ISSPECTR  =  7
# Has input covariance matrix (0=no, 1=yes)
XA_SPOUT_HASCOVMTX =  8

# J2K position X (km)
XA_SPOUT_J2KPOSX   = 10
# J2K position Y (km)
XA_SPOUT_J2KPOSY   = 11
# J2K position Z (km)
XA_SPOUT_J2KPOSZ   = 12
# J2K velocity X (km/s)
XA_SPOUT_J2KVELX   = 13
# J2K velocity Y (km/s)
XA_SPOUT_J2KVELY   = 14
# J2K velocity Z (km/s)
XA_SPOUT_J2KVELZ   = 15
# ECI position X (km)
XA_SPOUT_ECIPOSX   = 16
# ECI position Y (km)
XA_SPOUT_ECIPOSY   = 17
# ECI position Z (km)
XA_SPOUT_ECIPOSZ   = 18
# ECI velocity X (km/s)
XA_SPOUT_ECIVELX   = 19
# ECI velocity Y (km/s)
XA_SPOUT_ECIVELY   = 20
# ECI velocity Z (km/s)
XA_SPOUT_ECIVELZ   = 21
# Geodetic latitude (deg)
XA_SPOUT_LAT       = 22
# Geodetic longitude (deg)
XA_SPOUT_LON       = 23
# Height above geoid (km)
XA_SPOUT_HEIGHT    = 24

# Covariance matrix type, if available:  1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K
XA_SPOUT_COVTYPE   = 30
# 6 by 6 covariance matrix (31-66)
XA_SPOUT_COVMTX    = 31

# J2K acceleration X (km/s^2)
XA_SPOUT_J2KACCX   = 70
# J2K acceleration Y (km/s^2)
XA_SPOUT_J2KACCY   = 71
# J2K acceleration Z (km/s^2)
XA_SPOUT_J2KACCZ   = 72
# ECI acceleration X (km/s^2)
XA_SPOUT_ECIACCX   = 73
# ECI acceleration Y (km/s^2)
XA_SPOUT_ECIACCY   = 74
# ECI acceleration Z (km/s^2)
XA_SPOUT_ECIACCZ   = 75

XA_SPOUT_SIZE      = 128

# Sp extended propagation data
# Propagation time in days since 1950, UTC
XA_SPEXT_UTC       =  0
# Propagation time in minutes since the satellite's epoch time
XA_SPEXT_MSE       =  1
# Propagation time in days since 1950, UT1
XA_SPEXT_UT1       =  2
# Propagation time in days since 1950, TAI
XA_SPEXT_TAI       =  3
# Propagation time in days since 1950, ET
XA_SPEXT_ET        =  4
# Revolution number
XA_SPEXT_REVNUM    =  5
# Number of nutation terms
XA_SPEXT_NTERMS    =  6
# Spectr compatible mode (0=not compatible, 1=compatible)
XA_SPEXT_ISSPECTR  =  7
# Has input covariance matrix (0=no, 1=yes)
XA_SPEXT_HASCOVMTX =  8

# Output coordSysinate of pos/vel/accel: 1=TEME of Date, 2= MEME of J2K
XA_SPEXT_COORD     = 10
# position X (km)
XA_SPEXT_POSX      = 11
# position Y (km)
XA_SPEXT_POSY      = 12
# position Z (km)
XA_SPEXT_POSZ      = 13
# velocity X (km/s)
XA_SPEXT_VELX      = 14
# velocity Y (km/s)
XA_SPEXT_VELY      = 15
# velocity Z (km/s)
XA_SPEXT_VELZ      = 16
# acceleration X (km/s^2)
XA_SPEXT_ACCX      = 17
# acceleration Y (km/s^2)
XA_SPEXT_ACCY      = 18
# acceleration Z (km/s^2)
XA_SPEXT_ACCZ      = 19

# Covariance matrix type, if available:  1=UVW, 2=ECI_DATE, 3=EQNX_DATE, 12=ECI_J2K, 13=EQNX_J2K
XA_SPEXT_COVTYPE   = 30
# 6 by 6 covariance matrix (31-66/1D format - 36 elements)
XA_SPEXT_COVMTX    = 31

# State transition matrix type, if available: 2=ECI_Date, 3=Eqnx_DATE
XA_SPEXT_STMTYPE   = 70
# 6x9 state transition matrix  (71-124/1D format - 54 elements - row major)
XA_SPEXT_STM       = 71

XA_SPEXT_SIZE      = 128


# Different options for generating ephemerides from SP
# ECI TEME of DATE     - 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec)
SP_EPHEM_ECI   = 1
# MEME of J2K (4 terms)- 0: time in days since 1950 UTC, 1-3: pos (km), 4-6: vel (km/sec)
SP_EPHEM_J2K   = 2


# Different time types returned by the SP propagator
# Time in minutes since the satellite's epoch time
XA_TIMETYPES_MSE  = 0
# Time in days since 1950, UTC
XA_TIMETYPES_UTC  = 1
# Time in days since 1950, UT1
XA_TIMETYPES_UT1  = 2
# Time in days since 1950, TAI
XA_TIMETYPES_TAI  = 3
# Time in days since 1950, ET
XA_TIMETYPES_ET   = 4

XA_TIMETYPES_SIZE = 5

# Indexes of SP application control (preference) parameters for individual satellite (thread-safe)
# Buffer size, enter zero if default value is desired
XA_SPPARMS_BUFSIZE  = 2
# Run mode, see IDX_RUNMODE_? for available options
XA_SPPARMS_RUNMODE  = 3
# Save partials data, 0=don't save partials, 1=save partials (needed for covariance)
XA_SPPARMS_SAVEPART = 4
# Specter compatibility mode
XA_SPPARMS_SPECTR   = 5
# Consider parameter
XA_SPPARMS_CONSIDER = 6
# Decay altitude
XA_SPPARMS_DECAYALT = 7
# VCM additional options, see VCMOPT_? for available options
XA_SPPARMS_VCMOPT   = 9
XA_SPPARMS_SIZE     = 32

# ========================= End of auto generated code ==========================
