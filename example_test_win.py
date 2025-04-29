from astrostandards.utils.load_utils import *

init_all()

S = Cstr('',128)
DllMainDll.DllMainGetInfo(S)
print(S.value)
