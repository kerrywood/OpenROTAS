# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'Rotas.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'librotas.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'librotas.dylib'

def LoadRotasDll():
   """ LoadRotasDll() -- Loads Rotas.dll from the PATH or LD_LIBRARY_PATH
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
   # Initializes Rotas DLL for use in the program
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.RotasInit.restype = c_int
   dllObj.RotasInit.argtypes = [c_longlong]


   # Returns information about the current version of Rotas DLL. 
   # The information is placed in the string parameter passed in.
   # infoStr: A string to hold the information about Rotas.dll (out-Character[128])
   dllObj.RotasGetInfo.restype = None
   dllObj.RotasGetInfo.argtypes = [c_char_p]


   # Loads Rotas-related parameters from an input text file
   # rotasInputFile: The name of the file containing Rotas-related parameters (in-Character[512])
   dllObj.RotasLoadFile.restype = c_int
   dllObj.RotasLoadFile.argtypes = [c_char_p]


   # Loads Rotas control parameters and all Rotas related data (environment, time, elsets, sensors, obs) from an input text file
   # rotasInputFile: The name of the file containing Rotas control parameters and all Rotas related data (in-Character[512])
   dllObj.RotasLoadFileAll.restype = c_int
   dllObj.RotasLoadFileAll.argtypes = [c_char_p]


   # Loads a single Rotas-typed card
   # card: Rotas-type input card (in-Character[512])
   dllObj.RotasLoadCard.restype = c_int
   dllObj.RotasLoadCard.argtypes = [c_char_p]


   # Saves current Rotas settings to a file
   # rotasFile: The name of the file in which to save the settings (in-Character[512])
   # saveMode: Specifies whether to create a new file or append to an existing one (0 = create, 1= append) (in-Integer)
   # saveForm: Specifies the mode in which to save the file (0 = text format, 1 = not yet implemented, reserved for future) (in-Integer)
   dllObj.RotasSaveFile.restype = c_int
   dllObj.RotasSaveFile.argtypes = [c_char_p, c_int, c_int]


   # Builds and returns the Rotas P-Card from the current Rotas settings
   # rotasPCard: The resulting Rotas P-Card string (out-Character[512])
   dllObj.RotasGetPCard.restype = None
   dllObj.RotasGetPCard.argtypes = [c_char_p]


   # Retrieves all Rotas control parameters with a single function call
   # rotasMode: Rotas processing mode: TAG=verify ob tab (default), FTAG=force assoc vs all input elsets, ALLEL=find the best # assoc elsets (out-Character[5])
   # grossBeta: gross beta threshold (deg) (default=2.0) (out-Double)
   # betaLimit: ASTAT 0 beta limit (deg) (default=0.05) (out-Double)
   # deltaTLimit: ASTAT 0 delta-t limit (min) (default=0.05) (out-Double)
   # deltaHLimit: ASTAT 0 delta-height limit (km) (default=10) (out-Double)
   # astat2Mult: ASTAT 2 multiplier (default=4) (out-Integer)
   # prtFlag: Residual print flag: 1=print all, 2=print ASTAT 0/1, 3=print no residuals, 4=print ASTAT 0/1/2 (out-Integer)
   # retagFlag: Retag flag: 0=don't retag (default), 1=retag ASTAT 0/1 to B3, 2=retag ASTAT 0/1 to TTY, 3=retag ASTAT 0/1/2 to B3 (out-Integer)
   # ltcFlag: Type 5 observation light-time correct flag: 0=don't apply LTC, 1=apply LTC analytically, 2=apply LTC exactly (out-Integer)
   # maxNumAssoc: Max number of associations per ob (ALLEL mode only) (out-Integer)
   # debiasFlag: Debias observation flag: 0=don't apply debias, 1=debias ob by applying sensor's bias data (out-Integer)
   # diagMode: Diagnostic print flag (out-Integer)
   # covPrtFlag: Covariance flag: 1=Propagate covariance and compute covariance matrix (covariance matrix must be available) (out-Integer)
   # isTrackMode: Track mode: 1=use track processing (each track is treated as a single entity) (out-Integer)
   # remRetagObs: Retagged obs are removed from further association (out-Integer)
   # extArr: For future use (out-Double[128])
   dllObj.RotasGetPAll.restype = None
   dllObj.RotasGetPAll.argtypes = [c_char_p, c_double_p, c_double_p, c_double_p, c_double_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_int_p, c_double * 128]


   # Sets all Rotas control parameters with a single function call
   # rotasMode: Rotas processing mode: TAG=verify ob tab (default), FTAG=force assoc vs all input elsets, ALLEL=find the best # assoc (in-Character[5])
   # grossBeta: gross beta threshold (deg) (default=2.0) (in-Double)
   # betaLimit: ASTAT 0 beta limit (deg) (default=0.05) (in-Double)
   # deltaTLimit: ASTAT 0 delta-t limit (min) (default=0.05) (in-Double)
   # deltaHLimit: ASTAT 0 delta-height limit (km) (default=10) (in-Double)
   # astat2Mult: ASTAT 2 multiplier (default=4) (in-Integer)
   # prtFlag: Residual print flag: 1=print all, 2=print ASTAT 0/1, 3=print no residuals, 4=print ASTAT 0/1/2 (in-Integer)
   # retagFlag: Retag flag: 0=don't retag (default), 1=retag ASTAT 0/1 to B3, 2=retag ASTAT 0/1 to TTY, 3=retag ASTAT 0/1/2 to B3 (in-Integer)
   # ltcFlag: Type 5 observation light-time correct flag: 0=don't apply LTC, 1=apply LTC analytically, 2=apply LTC exactly (in-Integer)
   # maxNumAssoc: Max number of associations per ob (ALLEL mode only) (in-Integer)
   # debiasFlag: Debias observation flag: 0=don't apply debias, 1=debias ob by applying sensor's bias data (in-Integer)
   # diagMode: Diagnostic print flag (in-Integer)
   # covPrtFlag: Covariance flag: 1=Propagate covariance and compute covariance matrix (covariance matrix must be available) (in-Integer)
   # isTrackMode: Track mode: 1=use track processing (each track is treated as a single entity) (in-Integer)
   # remRetagObs: Retagged obs are removed from further association (in-Integer)
   # extArr: For future use (in-Double[128])
   dllObj.RotasSetPAll.restype = None
   dllObj.RotasSetPAll.argtypes = [c_char_p, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double * 128]


   # Retrieves the value of a specified Rotas control parameter (P-card field)
   # 
   # The table below shows the values for the xf_RP parameter:
   # 
   # table
   # 
   # Index
   # Index Interpretation
   # 
   #  1  Rotas processing mode
   #  2  Gross Beta limit (deg)
   #  3  ASTAT 0 Beta limit (deg)
   #  4  ASTAT 0 delta-t limit (min)
   #  5  ASTAT 0 delta-height limit (km)
   #  6  ASTAT 2 multiplier
   #  7  Residual print flag
   #  8  Retag ASTAT 1 ob flag
   #  9  Light-time correction flag
   # 10  Maximum number of ALLEL assoc's to compute
   # 11  Diagnostic print flag
   # 12  Covariance print flag
   # 13  Perform track processing
   # 14  Retagged ob are removed from further association
   # 15  Debias ob flag
   # 
   # xf_RP: Predefined number specifying which Rotas control parameter  to retrieve (in-Integer)
   # retVal: A string to hold the value of the requested Rotas parameter (out-Character[512])
   dllObj.RotasGetPField.restype = None
   dllObj.RotasGetPField.argtypes = [c_int, c_char_p]


   #  Sets the value of a specified Rotas control parameter (P-card field)
   # See RotasGetPField for values for the xf_RP parameter.
   # xf_RP: Predefined number specifying which Rotas control parameter to set (in-Integer)
   # valueStr: The new value of the specified field, expressed as a string (in-Character[512])
   dllObj.RotasSetPField.restype = None
   dllObj.RotasSetPField.argtypes = [c_int, c_char_p]


   # Gets ASTAT 1 association multipliers
   # xa_assocMultp: ASTAT 1 association multiplier array, see XA_ASSOCMULTP_? for array arrangement (out-Integer[12])
   dllObj.RotasGetAssocMultipliers.restype = None
   dllObj.RotasGetAssocMultipliers.argtypes = [c_int * 12]


   # Sets ASTAT 1 association multipliers
   # xa_assocMultp: ASTAT 1 association multiplier array, see XA_ASSOCMULTP_? for array arrangement (in-Integer[12])
   dllObj.RotasSetAssocMultipliers.restype = None
   dllObj.RotasSetAssocMultipliers.argtypes = [c_int * 12]


   # Resets all Rotas control parameters back to their default values
   dllObj.RotasResetAll.restype = None
   dllObj.RotasResetAll.argtypes = []


   # Determines if the observation/satellite pair can possibly have an association
   # obsKey: The obervation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   dllObj.RotasHasASTAT.restype = c_int
   dllObj.RotasHasASTAT.argtypes = [c_longlong, c_longlong]


   # Determines if the observation/satellite pair can possibly have an association - suitable for multithread application (using global Multipliers)
   # xa_rt_parms: ROTAS control parameters - see XA_RT_PARMS_? for array arrangement (in-Double[16])
   # obsKey: The obervation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   dllObj.RotasHasASTAT_MT.restype = c_int
   dllObj.RotasHasASTAT_MT.argtypes = [c_double * 16, c_longlong, c_longlong]


   # Determines if the observation/satellite pair can possibly have an association - suitable for multithread application (using provided Multipliers)
   # xa_assocMultp: ASTAT 1 association multiplier array, see XA_ASSOCMULTP_? for array arrangement (in-Integer[12])
   # xa_rt_parms: ROTAS control parameters - see XA_RT_PARMS_? for array arrangement (in-Double[16])
   # obsKey: The obervation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   dllObj.RotasHasASTATMultp_MT.restype = c_int
   dllObj.RotasHasASTATMultp_MT.argtypes = [c_int * 12, c_double * 16, c_longlong, c_longlong]


   # Computes residuals for one observation against one satellite
   # Obs type 0 (range rate only) cannot be used to compute residuals.
   # obsKey: The observation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   # satElts: satellite state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); satellite LLH (7th-9th) (out-Double[9])
   # obElts: observation state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); observation LLH (7th-9th) (out-Double[9])
   dllObj.RotasComputeObsResiduals.restype = c_int
   dllObj.RotasComputeObsResiduals.argtypes = [c_longlong, c_longlong, c_double * 100, c_double * 9, c_double * 9]


   # Computes residuals for one observation against one satellite - suitable for multithread application (using global Multipliers)
   # Obs type 0 (range rate only) cannot be used to compute residuals.
   # xa_rt_parms: ROTAS control parameters - see XA_RT_PARMS_? for array arrangement (in-Double[16])
   # obsKey: The observation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   # satElts: satellite state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); satellite LLH (7th-9th) (out-Double[9])
   # obElts: observation state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); observation LLH (7th-9th) (out-Double[9])
   dllObj.RotasComputeObsResiduals_MT.restype = c_int
   dllObj.RotasComputeObsResiduals_MT.argtypes = [c_double * 16, c_longlong, c_longlong, c_double * 100, c_double * 9, c_double * 9]


   # Computes residuals for one observation against one satellite - suitable for multithread application (using provided Multipliers)
   # Obs type 0 (range rate only) cannot be used to compute residuals.
   # xa_assocMultp: ASTAT 1 association multiplier array, see XA_ASSOCMULTP_? for array arrangement (in-Integer[12])
   # xa_rt_parms: ROTAS control parameters - see XA_RT_PARMS_? for array arrangement (in-Double[16])
   # obsKey: The observation's unique key (in-Long)
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   # satElts: satellite state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); satellite LLH (7th-9th) (out-Double[9])
   # obElts: observation state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); observation LLH (7th-9th) (out-Double[9])
   dllObj.RotasComputeObsResidualsMultp_MT.restype = c_int
   dllObj.RotasComputeObsResidualsMultp_MT.argtypes = [c_int * 12, c_double * 16, c_longlong, c_longlong, c_double * 100, c_double * 9, c_double * 9]


   # Computes residuals for a track of observations against one satellite. Each track is treated as a single entity (using global parameters)
   # obsKeys: The input array of obsKeys sorted in ascending order of sensor, satno, obsType, time, elev (in-Long[*])
   # trackStartIdx: The start index of the first obs of the track (in-Integer)
   # trackLength: The input track length (in-Integer)
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   # trackObsKeys: The 3 obsKeys of the 3 obs that were chosen to represent the track (out-Long[3])
   # b3ObsCard: The resulting B3-card created by IOMOD to represent the whole track (out-Character[512])
   # satElts: satellite state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); satellite LLH (8th-9th) (out-Double[9])
   # obElts: observation state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); observation LLH (8th-9th) (out-Double[9])
   dllObj.RotasComputeTrackResiduals.restype = c_int
   dllObj.RotasComputeTrackResiduals.argtypes = [c_void_p, c_int, c_int, c_longlong, c_double * 100, c_longlong * 3, c_char_p, c_double * 9, c_double * 9]


   # Computes residuals for a track of observations against one satellite. Each track is treated as a single entity (using provided parameters)
   # xa_assocMultp: ASTAT 1 association multiplier array, see XA_ASSOCMULTP_? for array arrangement (in-Integer[12])
   # xa_rt_parms: ROTAS control parameters - see XA_RT_PARMS_? for array arrangement (in-Double[16])
   # obsKeys: The input array of obsKeys sorted in ascending order of sensor, satno, obsType, time, elev (in-Long[*])
   # trackStartIdx: The start index of the first obs of the track (in-Integer)
   # trackLength: The input track length (in-Integer)
   # satKey: The satellite's unique key (in-Long)
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   # trackObsKeys: The 3 obsKeys of the 3 obs that were chosen to represent the track (out-Long[3])
   # b3ObsCard: The resulting B3-card created by IOMOD to represent the whole track (out-Character[512])
   # satElts: satellite state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); satellite LLH (8th-9th) (out-Double[9])
   # obElts: observation state in ECI/TEME of Date: position (1st-3rd), velocity (4th-6th); observation LLH (8th-9th) (out-Double[9])
   dllObj.RotasComputeTrackResiduals_MT.restype = c_int
   dllObj.RotasComputeTrackResiduals_MT.argtypes = [c_int * 12, c_double * 16, c_void_p, c_int, c_int, c_longlong, c_double * 100, c_longlong * 3, c_char_p, c_double * 9, c_double * 9]


   # Computes residuals for one observation against one satellite directly (no need to load ob and propagate satellite)
   # obDataArr: The array storing observation data: position (1st-3rd), velocity (4th-6th), unused (7th-16th) (in-Double[16])
   # satDataArr: The array storing satellite data: position (1st-3rd), velocity (4th-6th), unused (7th-16th) (in-Double[16])
   # xa_ObsRes: The resulting array of obs residuals, see XA_OBSRES_? for array arrangement (out-Double[100])
   dllObj.RotasCompObResDirect.restype = c_int
   dllObj.RotasCompObResDirect.argtypes = [c_double * 16, c_double * 16, c_double * 100]


   # Returns the name of the retag obs file
   # retagObsFile: The resulting retag file name (out-Character[512])
   dllObj.RotasGetRetagObsFile.restype = None
   dllObj.RotasGetRetagObsFile.argtypes = [c_char_p]


   # Sets the file name of the retag obs file
   # retagObsFile: The retag file name (in-Character[512])
   dllObj.RotasSetRetagObsFile.restype = None
   dllObj.RotasSetRetagObsFile.argtypes = [c_char_p]

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj

# Different light-time correction (LTC) options
# Don't apply LTC
LTC_DONTAPPLY  = 0
# Apply LTC analytically
LTC_ANALYTIC   = 1
# Apply LTC exactly
LTC_EXACT      = 2

# Residual computation methods
# Delta/427M method
RESCOMPMETH_DELTA427M = 1
# Spadoc 4 method
RESCOMPMETH_SPADOC4   = 2

# PV Ob data
# ob ECI position X (km) in TEME of Date
XA_OBPV_POSX     =  0
# ob ECI position Y (km) in TEME of Date
XA_OBPV_POSY     =  1
# ob ECI position Z (km) in TEME of Date
XA_OBPV_POSZ     =  2
# ob ECI velocity X (km/sec) in TEME of Date
XA_OBPV_VELX     =  3
# ob ECI velocity Y (km/sec) in TEME of Date
XA_OBPV_VELY     =  4
# ob ECI velocity Z (km/sec) in TEME of Date
XA_OBPV_VELZ     =  5
# ob time in days since 1950, UTC
XA_OBPV_TIME     =  6

# the last available index
XA_OBPV_END      = 15
XA_OBPV_SIZE     = 16

# Satellite state data
# satellite ECI position X (km) in TEME of Date
XA_SATPV_POSX    =  0
# satellite ECI position Y (km) in TEME of Date
XA_SATPV_POSY    =  1
# satellite ECI position Z (km) in TEME of Date
XA_SATPV_POSZ    =  2
# satellite ECI velocity X (km/sec) in TEME of Date
XA_SATPV_VELX    =  3
# satellite ECI velocity Y (km/sec) in TEME of Date
XA_SATPV_VELY    =  4
# satellite ECI velocity Z (km/sec) in TEME of Date
XA_SATPV_VELZ    =  5

# the last available index
XA_SATPV_END     = 15
XA_SATPV_SIZE    = 16


# Obs residual data field indexes
# Azimuth residual (deg)
XA_OBSRES_AZ     =  0
# Elevation residual (deg)
XA_OBSRES_EL     =  1
# Range residual (km)
XA_OBSRES_RANGE  =  2
# Height residual (deg)
XA_OBSRES_HEIGHT =  3
# Beta residual (deg). asin(dot(priU, secW))
XA_OBSRES_BETA   =  4
# Delta T residual (min)
XA_OBSRES_DELTAT =  5
# Vector magnitude (km)
XA_OBSRES_VMAG   =  6
# Time since epoch (days)
XA_OBSRES_AGE    =  7
# True argument of latitude (deg)
XA_OBSRES_SU     =  8
# Revolution number
XA_OBSRES_REVNUM =  9
# Range rate residual (km/sec)
XA_OBSRES_RNGRATE= 10
# Observation ASTAT
XA_OBSRES_ASTAT  = 11
# Observation type
XA_OBSRES_OBSTYPE= 12
# Satellite true anomaly (deg)
XA_OBSRES_SATANOM= 13
# Satellite elevation (deg)
XA_OBSRES_SATELEV= 14
# Satellite maintenance category
XA_OBSRES_SATCAT = 15
# Obs time in ds50UTC
XA_OBSRES_OBSTIME= 16
# Obs azimuth (deg)
XA_OBSRES_OBSAZ  = 17
# Obs elevation (deg)
XA_OBSRES_OBSEL  = 18
# Velocity angle residual (deg)
XA_OBSRES_VELANG = 19
# Angular momentum residual (deg).  acos(dot(priW, secW))
XA_OBSRES_ANGMOM = 20
# Right ascension residual (deg) (for ob types 5, 9, 19)
XA_OBSRES_RA     = 21
# Declination residual (deg) (for ob types 5, 9, 19)
XA_OBSRES_DEC    = 22
# Delta X position (km)
XA_OBSRES_POSX   = 23
# Delta Y position (km)
XA_OBSRES_POSY   = 24
# Delta Z position (km)
XA_OBSRES_POSZ   = 25
# Delta X velocity (km/sec)
XA_OBSRES_VELX   = 26
# Delta Y velocity (km/sec)
XA_OBSRES_VELY   = 27
# Delta Z velocity (km/sec)
XA_OBSRES_VELZ   = 28
# Angle only - Obs computed range (km)
XA_OBSRES_OBSRNG = 29

# Obs right ascension (deg)
XA_OBSRES_OBSRA  = 30
# Obs declination (deg)
XA_OBSRES_OBSDEC = 31
# Delta east longitude (deg)
XA_OBSRES_LON    = 32

# Delta U position (km)
XA_OBSRES_POSU   = 33
# Delta V position (km)
XA_OBSRES_POSV   = 34
# Delta W position (km)
XA_OBSRES_POSW   = 35
# 3D position chi-squared residual (km) (Light Time Correction flag must be set to 0 or 2, will not work with 1)
XA_OBSRES_CHI    = 36

# Angular Separation between Obs and State (Deg)
XA_OBSRES_ANGSEP = 38
# TDOA Time Difference of Arrival residual (nano-second)
XA_OBSRES_TDOA   = 39
# FDOA Frequency Differecnce of Arrival (Hz)
XA_OBSRES_FDOA   = 40

XA_OBSRES_SIZE   =100

# Indexes of Rotas Control parameter fields (Rotas P-Card)
# Rotas processing mode
XF_RP_MODE       =  1
# Gross Beta limit (deg)
XF_RP_GROSSBETA  =  2
# ASTAT 0 Beta limit (deg)
XF_RP_BETALIM    =  3
# ASTAT 0 delta-t limit (min)
XF_RP_DELTATLIM  =  4
# ASTAT 0 delta-height limit (km)
XF_RP_DELTAHLIM  =  5
# ASTAT 2 multiplier
XF_RP_ASTAT2MULT =  6
# Residual print flag
XF_RP_PRTFLAG    =  7
# Retag ASTAT 1 ob flag
XF_RP_RETAGFLAG  =  8
# Light-time correction flag
XF_RP_LTC        =  9
# Maximum number of ALLEL assoc's to compute
XF_RP_NUMASSOC   = 10
# Diagnostic print flag
XF_RP_DIAGNOSTIC = 11
# Covariance print flag
XF_RP_PRTCOV     = 12
# Perform track processing
XF_RP_TRACKFLAG  = 13
# Retagged ob are removed from further association
XF_RP_REMRETAG   = 14
# Debias ob flag
XF_RP_DEBIAS     = 15
# Residual computation method: 1=DELTA/427M, 2=SPADOC-4(default)
XF_RP_RESCOMPMETH= 16

# ROTAS control parameters in input array xa_rt_parms that is used in RotasHasASTAT_MT() and
# Gross Beta limit (deg)
XA_RT_PARMS_GROSSBETA   =  1
# ASTAT 0 Beta limit (deg)
XA_RT_PARMS_BETALIM     =  2
# ASTAT 0 delta-t limit (min)
XA_RT_PARMS_DELTATLIM   =  3
# ASTAT 0 delta-height limit (km)
XA_RT_PARMS_DELTAHLIM   =  4
# ASTAT 2 multiplier
XA_RT_PARMS_ASTAT2MULT  =  5
# Light-time correction (LTC) flag: 0= don't apply LTC, 1= apply LTC analytically, 2= apply LTC exactly
XA_RT_PARMS_LTC         =  6
# debias ob flag: 0= do not debias, 1= debias ob
XA_RT_PARMS_DEBIAS      =  7
# Residual computation method: 1=DELTA/427M, 2=SPADOC-4(default)
XA_RT_PARMS_RESCOMPMETH =  8
# Flag for Annual Aberration 0 = do not apply, 1 = apply aberration correction
XA_RT_PARMS_ANNUALAB	   =  9
# Flag for Diurnal Aberration 0 = do not apply, 1 = apply aberration correction
XA_RT_PARMS_DIURNALAB   = 10
XA_RT_PARMS_SIZE        = 16

# ROTAS Association Multipliers
# ASTAT 1 Beta multiplier for Synchronous
XA_ASSOCMULTP_BETA_SYN   =  0
# ASTAT 1 Delta-t multiplier for Synchronous
XA_ASSOCMULTP_DELTAT_SYN =  1
# ASTAT 1 Delta-height multiplier for Synchronous
XA_ASSOCMULTP_DELTAH_SYN =  2
# ASTAT 1 Beta multiplier for Deep-space
XA_ASSOCMULTP_BETA_DS    =  3
# ASTAT 1 Delta-t multiplier for Deep-space
XA_ASSOCMULTP_DELTAT_DS  =  4
# ASTAT 1 Delta-height multiplier for Deep-space
XA_ASSOCMULTP_DELTAH_DS  =  5
# ASTAT 1 Beta multiplier for Decaying
XA_ASSOCMULTP_BETA_DCY   =  6
# ASTAT 1 Delta-t multiplier for Decaying
XA_ASSOCMULTP_DELTAT_DCY =  7
# ASTAT 1 Delta-height multiplier for Decaying
XA_ASSOCMULTP_DELTAH_DCY =  8
# ASTAT 1 Beta multiplier for Routine
XA_ASSOCMULTP_BETA_RTN   =  9
# ASTAT 1 Delta-t multiplier for Routine
XA_ASSOCMULTP_DELTAT_RTN = 10
# ASTAT 1 Delta-height multiplier for Routine
XA_ASSOCMULTP_DELTAH_RTN = 11

XA_ASSOCMULTP_SIZE       = 12

# ========================= End of auto generated code ==========================
