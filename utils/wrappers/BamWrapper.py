# This wrapper file was generated automatically by the GenDllWrappers program.
import sys
import os
import platform
from ctypes import *
from utils.wrappers.AstroUtils import *

# get the right filename of the dll/so
if platform.uname()[0] == "Windows":
   DLL_NAME = 'Bam.dll'

if platform.uname()[0] == "Linux":
   DLL_NAME = 'libbam.so'

if platform.uname()[0] == "Darwin":
   DLL_NAME = 'libbam.dylib'

def LoadBamDll():
   """ LoadBamDll() -- Loads Bam.dll from the PATH or LD_LIBRARY_PATH
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
   # Initializes Bam dll for use in the program
   # apAddr: The handle that was returned from DllMainInit() (in-Long)
   dllObj.BamInit.restype = c_int
   dllObj.BamInit.argtypes = [c_longlong]


   # Returns information about the current version of Bam.dll. The information is placed in the string parameter you pass in
   # infoStr: A string to hold the information about Bam.dll (out-Character[128])
   dllObj.BamGetInfo.restype = None
   dllObj.BamGetInfo.argtypes = [c_char_p]


   # Computes the number of time steps using the input start/end times and the step size
   # startDs50UTC: start time in days since 1950, UTC (in-Double)
   # stopDs50UTC: stop time in days since 1950, UTC (in-Double)
   # stepSizeMin: step size in minutes (in-Double)
   dllObj.BamCompNumTSs.restype = c_int
   dllObj.BamCompNumTSs.argtypes = [c_double, c_double, c_double]


   # Computes and returns separate/missed distance data
   # 
   # The table below shows the indexes for the Separation Distance values contained in the extBamArr array:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0time at mininum average separate distances (ds50UTC)
   #     1minimum average separate distance (km)
   #     2average position X at minimum average separate distance (km)
   #     3average position Y at minimum average separate distance (km)
   #     4average position Z at minimum average separate distance (km)
   #     5average velocity X at minimum average separate distance (km/s)
   #     6average velocity Y at minimum average separate distance (km/s)
   #     7average velocity Z at minimum average separate distance (km/s)
   #     8average latitude at minimum average separate distance (deg)
   #     9average longitude at minimum average separate distance (deg)
   #     10average height at minimum average separate distance (km)
   # 
   # 
   # The table below shows the indexes for the Miss Distance values contained in the extBamArr array:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     20time at mininum average missed distances (ds50UTC)
   #     21minimum average missed distance (km)
   #     22average position X of satellites when they cross the pinch point plan (km)
   #     23average position Y of satellites when they cross the pinch point plan (km)
   #     24average position Z of satellites when they cross the pinch point plan (km)
   #     25average velocity X of satellites when they cross the pinch point plan (km/s)
   #     26average velocity Y of satellites when they cross the pinch point plan (km/s)
   #     27average velocity Z of satellites when they cross the pinch point plan (km/s)
   #     28average latitude of satellites when they cross the pinch point plan (deg)
   #     29average longitude of satellites when they cross the pinch point plan (deg)
   #     30average height of satellites when they cross the pinch point plan (km)
   # 
   # satKeys: array of satellite keys that wil be used in BAM (in-Long[*])
   # numSats: the size of the satKeys array (in-Integer)
   # startDs50UTC: start time in days since 1950, UTC (in-Double)
   # stopDs50UTC: stop time in days since 1950, UTC (in-Double)
   # stepSizeMin: step size in minutes (in-Double)
   # avgSDs: average separate distances of all time steps (out-Double[*])
   # avgMDs: average missed distances of all time steps (out-Double[*])
   # extBamArr: other BAM resulting data (out-Double[64])
   # errCode: 0 if Bam is successful, non-0 if there is an error (out-Integer)
   dllObj.BamCompute.restype = None
   dllObj.BamCompute.argtypes = [c_void_p, c_int, c_double, c_double, c_double, c_void_p, c_void_p, c_double * 64, c_int_p]


   # Retrieves other BAM data
   # 
   # The table below shows the indexes for the values for the xf_bam parameter:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0times when satellites cross the pinch point plan (ds50UTC)
   #     1missed distances from satellites to the pinch point (km)
   #     2nadir angles of satellites when they cross the pinch point plan
   #     3position Xs of satellites when they cross the pinch point plan (km)
   #     4position Ys of satellites when they cross the pinch point plan (km)
   #     5position Zs of satellites when they cross the pinch point plan (km)
   #     6velocity Xs of satellites when they cross the pinch point plan (km/s)
   #     7velocity Ys of satellites when they cross the pinch point plan (km/s)
   #     8velocity Zs of satellites when they cross the pinch point plan (km/s)
   #     9latitude of satellites when they cross the pinch point plan (deg)
   #     10longitude of satellites when they cross the pinch point plan (deg)
   #     11height of satellites when they cross the pinch point plan (km)
   # 
   # xf_bam: Predefined number specifying which BAM array to retrieve (in-Integer)
   # bamArr: An array to store the retrieved result (out-Double[*])
   dllObj.BamGetResults.restype = None
   dllObj.BamGetResults.argtypes = [c_int, c_void_p]


   # Retrieves other BAM data. Same as BamGetResults, but returns everything in one call
   # 
   # The table below shows the indexes for the values for the xf_bam parameter:
   # 
   #     table
   #     
   #         Index
   #         Index Interpretation
   #     
   #     0times when satellites cross the pinch point plan (ds50UTC)
   #     1missed distances from satellites to the pinch point (km)
   #     2nadir angles of satellites when they cross the pinch point plan
   #     3position Xs of satellites when they cross the pinch point plan (km)
   #     4position Ys of satellites when they cross the pinch point plan (km)
   #     5position Zs of satellites when they cross the pinch point plan (km)
   #     6velocity Xs of satellites when they cross the pinch point plan (km/s)
   #     7velocity Ys of satellites when they cross the pinch point plan (km/s)
   #     8velocity Zs of satellites when they cross the pinch point plan (km/s)
   #     9latitude of satellites when they cross the pinch point plan (deg)
   #     10longitude of satellites when they cross the pinch point plan (deg)
   #     11height of satellites when they cross the pinch point plan (km)
   # 
   # bamArr: An array to store the retrieved result (out-Double[*, 12])
   dllObj.BamGetResultsFull.restype = None
   dllObj.BamGetResultsFull.argtypes = [c_void_p]


   # satKeys: array of satellite keys that wil be used in BAM (in-Long[*])
   # numSats: the size of the satKeys array (in-Integer)
   # startDs50UTC: start time in days since 1950, UTC (in-Double)
   # stopDs50UTC: stop time in days since 1950, UTC (in-Double)
   # stepSizeMin: step size in minutes (in-Double)
   # avgSDs: average separate distances of all time steps (out-Double[*])
   # avgMDs: average missed distances of all time steps (out-Double[*])
   # extBamArr: other BAM resulting data (out-Double[64])
   # bamArr: An array to store the retrieved result (out-Double[*, 12])
   # errCode: 0 if Bam is successful, non-0 if there is an error (out-Integer)
   dllObj.BamComputeAll.restype = None
   dllObj.BamComputeAll.argtypes = [c_void_p, c_int, c_double, c_double, c_double, c_void_p, c_void_p, c_double * 64, c_void_p, c_int_p]

   # Comment out the below line to disable load message
   print(DLL_NAME + ' loaded successfully.')
   return dllObj

# time at mininum average separate distances (ds50UTC)
BAM_SD_TIME    =  0
# minimum average separate distance (km)
BAM_SD_DIST    =  1
# average position X at minimum average separate distance (km)
BAM_SD_POSX    =  2
# average position Y at minimum average separate distance (km)
BAM_SD_POSY    =  3
# average position Z at minimum average separate distance (km)
BAM_SD_POSZ    =  4
# average velocity X at minimum average separate distance (km/s)
BAM_SD_VELX    =  5
# average velocity Y at minimum average separate distance (km/s)
BAM_SD_VELY    =  6
# average velocity Z at minimum average separate distance (km/s)
BAM_SD_VELZ    =  7
# average latitude at minimum average separate distance (deg)
BAM_SD_LAT     =  8
# average longitude at minimum average separate distance (deg)
BAM_SD_LON     =  9
# average height at minimum average separate distance (km)
BAM_SD_HEIGHT  = 10

# time at mininum average missed distances (ds50UTC)
BAM_MD_TIME    = 20
# minimum average missed distance (km)
BAM_MD_DIST    = 21
# average position X of satellites when they cross the pinch point plan (km)
BAM_MD_POSX    = 22
# average position Y of satellites when they cross the pinch point plan (km)
BAM_MD_POSY    = 23
# average position Z of satellites when they cross the pinch point plan (km)
BAM_MD_POSZ    = 24
# average velocity X of satellites when they cross the pinch point plan (km/s)
BAM_MD_VELX    = 25
# average velocity Y of satellites when they cross the pinch point plan (km/s)
BAM_MD_VELY    = 26
# average velocity Z of satellites when they cross the pinch point plan (km/s)
BAM_MD_VELZ    = 27
# average latitude of satellites when they cross the pinch point plan (deg)
BAM_MD_LAT     = 28
# average longitude of satellites when they cross the pinch point plan (deg)
BAM_MD_LON     = 29
# average height of satellites when they cross the pinch point plan (km)
BAM_MD_HEIGHT  = 30

BAM_MD_SIZE    = 64

# times when satellites cross the pinch point plan (ds50UTC)
XF_BAM_MDTIME  =  0
# missed distances from satellites to the pinch point (km)
XF_BAM_RANGE   =  1
# nadir angles of satellites when they cross the pinch point plan
XF_BAM_NADIR   =  2
# position Xs of satellites when they cross the pinch point plan (km)
XF_BAM_POSX    =  3
# position Ys of satellites when they cross the pinch point plan (km)
XF_BAM_POSY    =  4
# position Zs of satellites when they cross the pinch point plan (km)
XF_BAM_POSZ    =  5
# velocity Xs of satellites when they cross the pinch point plan (km/s)
XF_BAM_VELX    =  6
# velocity Ys of satellites when they cross the pinch point plan (km/s)
XF_BAM_VELY    =  7
# velocity Zs of satellites when they cross the pinch point plan (km/s)
XF_BAM_VELZ    =  8
# latitude of satellites when they cross the pinch point plan (deg)
XF_BAM_LAT     =  9
# longitude of satellites when they cross the pinch point plan (deg)
XF_BAM_LON     = 10
# height of satellites when they cross the pinch point plan (km)
XF_BAM_HEIGHT  = 11



# ========================= End of auto generated code ==========================
