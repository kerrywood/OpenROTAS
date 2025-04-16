# ########################################################################################### 
# MIT License
# 
# Copyright (c) 2023 Kerry N. Wood (kerry.wood@jhuapl.edu)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
#     The above copyright notice and this permission notice shall be included in all
#     copies or substantial portions of the Software.
# 
#     THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#     IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#     FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#     AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#     LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#     OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#     SOFTWARE.
# ########################################################################################### 
# developed in support of SSDP, JHU/APL contract FA8819-18-D-0009/FA8819-20-F-1005
# ########################################################################################### 
import os
from datetime import datetime, timezone
import numpy as np
import json
import ctypes

# -----------------------------------------------------------------------------------------------------
def Cstr( S, slen=128 ):
    stbuf = ctypes.create_string_buffer( slen )
    stbuf.value = S.encode()
    return stbuf

# -----------------------------------------------------------------------------------------------------
def toAstroStdTime( dtime : datetime, TimeFuncDll ):
    '''
    helper function to turn a datetime into the DS50 value in astrostandards
    this needs Cstr, so we re-define it in here
    '''
    if dtime.tzinfo is not None and dtime.tzinfo.utcoffset(d) is not None:
        dtime = dtime.astimezone( timezone.utc )

    obtime_as = dtime.strftime('%Y/%j %H%M %S.%f')[:-3]
    ds50 = TimeFuncDll.DTGToUTC( Cstr(obtime_as,20) )
    return ds50

# -------------------------------------------------------------
def datetime_to_ds50( dt , TimeFuncDll ):
    return TimeFuncDll.TimeComps2ToUTC( dt.year, dt.month, dt.day, dt.hour, dt.minute, 
            ctypes.c_double( dt.second + dt.microsecond/1e6) )


# -------------------------------------------------------------
def ds50_to_datetime( ds50, TimeFuncDll ):
    tstr = Cstr('',20)
    # yields YYYY/DDD HHMM SS.SSS
    TimeFuncDll.UTCToDTG20( ds50, tstr )
    return datetime.strptime( tstr.value.decode('utf-8'), '%Y/%j %H%M %S.%f')


# -----------------------------------------------------------------------------------------------------
class astrostd_named_fields(dict):
    def __init__( self, DLL, data=None, prefix='XAI_CTRL', datatype=ctypes.c_double):
        self.param_max = 0  
        self.data      = None
        self.name2num  = {}
        self.num2name  = {}
        self.datatype  = datatype

        # get the names
        self.param_names = list( filter( lambda X: X.startswith(prefix) , dir(DLL) ) )

        for name in self.param_names:
            if name.endswith("_SIZE"):
                self.param_max = int(getattr( DLL, name ))
                continue
            num = int(getattr( DLL, name ))  # these are locations, so they must be integers
            self.name2num[ name ] = num
            self.num2name[ num ] = name

        # keep a list of sorted names for easy output
        self.sorted_by_place = sorted( self.name2num.items(), key=lambda X: X[1] )
        self.clear_data = [0 for _ in range(self.param_max) ]
        if data: 
            self.data = (datatype * self.param_max)( *data )
        else:
            self.data = (datatype * self.param_max)( *self.clear_data)   # init the buffer

        if self.param_max == 0:
            raise Exception('{} : showing zero for parameter size; this is usually caused by a DLL / field name mis-spelling or mismatch'.format(
                self.__class__.__name__) )

    def __call__(self, data):
        self.setData( data )
        return self

    def setData( self, data ):
        self.data = (self.datatype * self.param_max)(  * list(data) )
        return self

    def getData( self ):
        return self.data

    def clear( self ):
        for i,v in enumerate(self.clear_data): self.data[i] = v

    def __setitem__(self, key, val):
        if isinstance(key, int) :
            self.data[ key ] = val
            return
        if isinstance(key, str) :
            self.data[ self.name2num[key] ] = val
            return
        raise Exception('invalid key value entered, must be str or int, you entered {} , {}'.format( key, type(key)))

    def __getitem__(self, key ):
        if isinstance(key, int) :
            return self.data[ key ] 
        if isinstance(key, str) :
            return self.data[ self.name2num[key] ] 
        raise Exception('invalid key value entered, must be str or int, you entered {} , {}'.format( key, type(key)))

    def toDict( self ):
        return dict( [ (X[0], self.data[X[1]]) for X in self.sorted_by_place ] )

    def toJSON( self ):
        return json.dumps( self.toDict( ) )

    def __dict__(self):
        return self.toDict()

    def __repr__(self):
        return self.toJSON()
           

# -----------------------------------------------------------------------------------------------------
def get_log( ):
    with open('./aslog.txt','r') as F: lines = F.readlines()
    return ''.join( lines )


#
#class TwoWayDict(dict):
#    def __setitem__(self, key, value):
#        # Remove any previous connections with these values
#        if key in self:
#            del self[key]
#        if value in self:
#            del self[value]
#        dict.__setitem__(self, key, value)
#        dict.__setitem__(self, value, key)
#
#    def __delitem__(self, key):
#        dict.__delitem__(self, self[key])
#        dict.__delitem__(self, key)
#
#    def __len__(self):
#        """Returns the number of connections"""
#        return dict.__len__(self) // 2
#
#
