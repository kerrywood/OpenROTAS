# KNW : the order here doesn't matter, init'ing them does
import ctypes
import sys
import DllMainDll
import TimeFuncDll
import EnvConstDll
import AstroFuncDll
import TleDll
import SpVecDll
import VcmDll
import ExtEphemDll
import Sgp4PropDll
import SatStateDll
import SensorDll
import ObsDll

# -----------------------------------------------------------------------------------------------------
def get_last_errmsg( ):
    stbuf = ctypes.create_string_buffer( 128 )
    DllMainDll.GetLastErrMsg( stbuf )
    return stbuf.value.decode('utf-8')

# -----------------------------------------------------------------------------------------------------
def load_val( rv, good_value=0 ):
    stbuf = ctypes.create_string_buffer( 128 )
    print(rv)
    if rv !=  good_value :
        DllMainDll.GetLastErrMsg( stbuf )
        return "ERROR:\n\t" + stbuf.value.rstrip()

# -----------------------------------------------------------------------------------------------------
def Cstr( S, slen=128 ):
    stbuf = ctypes.create_string_buffer( slen )
    stbuf.value = S.encode()
    return stbuf

# -----------------------------------------------------------------------------------------------------
def init_main( logfile='aslog.txt', verbose=True ):
    ptr = DllMainDll.DllMainInit()
    if logfile: DllMainDll.OpenLogFile( Cstr( logfile, 512) )
    return ptr

FUNC_ORDER = (
    EnvConstDll.EnvInit,
    TimeFuncDll.TimeFuncInit,
    AstroFuncDll.AstroFuncInit,
    TleDll.TleInit,
    SpVecDll.SpVecInit,
    VcmDll.VcmInit,
    ExtEphemDll.ExtEphInit,
    Sgp4PropDll.Sgp4Init,
    SpPropDll.SpInit,
    ElOpsDll.ElOpsInit,
    SatStateDll.SatStateInit,
    SensorDll.SensorInit,
    ObsDll.ObsInit,
    ObsOpsDll.ObsOpsInit,
    LamodDll.LamodInit,
    RotasDll.RotasInit,
    BatchDCDll.BatchDCInit,
#    BamDll.BamInit,
#    CocoDll.CocoInit,
    ComboDll.ComboInit,
    ElCompDll.ElCompInit,
#    ElOpsDll.ElOpsInit,
#    FovDll.FovInit,
    LamodDll.LamodInit,
#    SaasDll.SaasInit,
)
# -----------------------------------------------------------------------------------------------------
def init_all( logfile='aslog.txt', verbose=True ):
    ptr = DllMainDll.DllMainInit()
    if verbose: 
        print('--- INITIALIZING DLLs ---')
        print('{:20}   : {}'.format( 'DllMainInit', ptr ) )
    if logfile: DllMainDll.OpenLogFile( Cstr( logfile, 512) )
    for F in FUNC_ORDER:
        rv = F( ptr )
        if verbose: print('{:20}   : {}'.format( F.__name__, rv ) )
        assert rv == 0
    return ptr

# -----------------------------------------------------------------------------------------------------
def get_versions( ):
    glob = globals()
    dll  = list( filter( lambda X: X.endswith('Dll'), glob ) )
    vstr = Cstr('',128)
    for D in dll:
        lib  = glob[D]
        info = list(filter( lambda X : 'GetInfo' in X, dir(lib) ) )
        if len(info) == 0: 
            print('{:30} no version function found'.format(D))
            continue
        vfc = getattr( lib, info[0] )
        vfc( vstr )
        print('{:30}  {}'.format( D, vstr.value.decode('utf-8')))

# -----------------------------------------------------------------------------------------------------
# WARNING
def time_warning():
    sys.stderr.write('*'*100 +'\n')
    sys.stderr.write('Remember when converting dates/times that you should use Julian dates to avoid leap second issues\n')
    sys.stderr.write('   helpers.DS50EPOCH + <days_since_50_float> * u.day ---> WRONG\n')
    sys.stderr.write("   astropy.time.Time( helpers.DS50EPOCH.jd + <days_since_50_float> , format='jd') ---> CORRECT\n")
    sys.stderr.write('*'*100 + '\n')

# -----------------------------------------------------------------------------------------------------
def test_dates():
    from datetime import datetime, timedelta
    print('---------------------------------------------------------------------------------')
    print('--- Running datetime tests... ---')
    print('---------------------------------------------------------------------------------')
    print('AstroStandards uses days from an an epoch of 1950-01-01 where that day is day *1*')
    print('...to use Python datetime, set your zero epoch at 1949-12-31T00:00:00')
    
    now = datetime.utcnow()
    ds = now.strftime('%y%j%H%M%S.%f')[:-3]
    print('ISO now                : {}'.format( now.isoformat()))
    print('DTG now (test string)  : {}'.format( ds ) )
    epoch = datetime.strptime( '1949-12-31T00:00:00', "%Y-%m-%dT%H:%M:%S")
    print('Datetime epoch ISO     : {}'.format( epoch.isoformat() ) )

    def get_days_between(datePast, dateFuture):
        difference = dateFuture - datePast
        return difference.total_seconds() / 86400.

    ds50 = TimeFuncDll.DTGToUTC(  Cstr( ds,20 ) )
    print('AstroStd DS50 answer   : {}'.format( ds50 ) )
    python_ans = get_days_between( epoch, now ) 
    print('Python datetime answer : {}'.format( python_ans ) )
    print('Delta (seconds)        : {}'.format( 86400 * (ds50 - python_ans ) ) )
    

# =====================================================================================================
if __name__ == "__main__":
    # /////////////////////////////////////////////////////////////////////////////////////////////////////
    # some dates checks
    # ////////////////////////////////////////////////////////////////////////////////////////////////////
    ptr = init_all()
    test_dates() 
    get_versions()
