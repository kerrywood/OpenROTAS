import ctypes
from utils.astrostds import AstroStds
from utils.wrappers.AstroUtils import *

astrostds = AstroStds()


TLE = ['1 99999U F0078521 23129.36741898 0.00000000 +71470-1 +36483-1 0 00003',
       '2 99999  11.1157 135.4398 4764778 123.8103 223.8499  1.83169650000003']

satKey = astrostds.Tle.TleAddSatFrLines(TLE[0].encode('utf-8'), TLE[1].encode('utf-8'))

# Print the satellite key
print('satKey:', satKey)

# Get the TLE epoch
epoch = ctypes.create_string_buffer(513)
astrostds.Tle.TleGetField(satKey, 4, epoch)

astrostds.Sgp4Prop.Sgp4InitSat(satKey)

ds50UTC = ctypes.c_double()
pos = CreateCArray(c_double, [3])
vel = CreateCArray(c_double, [3])
llh = CreateCArray(c_double, [3])

# propagate the initialized TLE to the specified time in minutes since epoch
astrostds.Sgp4Prop.Sgp4PropMse(c_longlong(satKey), 0, byref(ds50UTC), pos, vel, llh)
print(pos[0], pos[1], pos[2], vel[0], vel[1], vel[2])

S = create_string_buffer(128)
astrostds.DllMain.DllMainGetInfo(S)
print(S.value)
