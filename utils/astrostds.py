import ctypes
from utils.wrappers.DllMainWrapper import *
from utils.wrappers.EnvConstWrapper import *
from utils.wrappers.AstroFuncWrapper import *
from utils.wrappers.TimeFuncWrapper import *
from utils.wrappers.TleWrapper import *
from utils.wrappers.Sgp4PropWrapper import *
from utils.wrappers.SpVecWrapper import *
from utils.wrappers.VcmWrapper import *
from utils.wrappers.ExtEphemWrapper import *
from utils.wrappers.SatStateWrapper import *
from utils.wrappers.SensorWrapper import *
from utils.wrappers.ObsWrapper import *
from utils.wrappers.RotasWrapper import *


class AstroStds(object):
    DllMainDll = None
    EnvConstDll = None
    AstroFuncDll = None
    TimeFuncDll = None
    TleDll = None
    Sgp4PropDll = None
    RotasDll = None

    def __init__(self):
      # Load and initialize dll's
      self.DllMainDll = LoadDllMainDll()
      self.EnvConstDll = LoadEnvConstDll()
      self.TimeFuncDll = LoadTimeFuncDll()
      self.AstroFuncDll = LoadAstroFuncDll()
      self.TleDll = LoadTleDll()
      self.Sgp4PropDll = LoadSgp4PropDll()
      self.SpVecDll = LoadSpVecDll()
      self.VcmDll = LoadVcmDll()
      self.ExtEphemDll = LoadExtEphemDll()
      self.SatStateDll = LoadSatStateDll()
      self.SensorDll = LoadSensorDll()
      self.ObsDll = LoadObsDll()
      self.RotasDll = LoadRotasDll()
      
      apPtr = self.DllMainDll.DllMainInit()
      for initFunction in [self.EnvConstDll.EnvInit, self.AstroFuncDll.AstroFuncInit, self.TimeFuncDll.TimeFuncInit,
                           self.TleDll.TleInit, self.SpVecDll.SpVecInit, self.VcmDll.VcmInit,
                           self.ExtEphemDll.ExtEphInit, self.Sgp4PropDll.Sgp4Init, self.SatStateDll.SatStateInit,
                           self.SensorDll.SensorInit, self.ObsDll.ObsInit, self.RotasDll.RotasInit]:

         if initFunction(apPtr):
            ShowMsgAndTerminate(self.DllMainDll)

    def Cstr(self, S, slen=128):
        stbuf = ctypes.create_string_buffer(slen)
        stbuf.value = S.encode()
        return stbuf

if __name__ == "__main__":

    astrostds = AstroStds()
