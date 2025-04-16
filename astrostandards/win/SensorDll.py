r"""Wrapper for new_SensorDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . --compile-libdir=. -l Sensor.dll ./new_SensorDll.h -o ./SensorDll.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python

import ctypes
import sys
from ctypes import *  # noqa: F401, F403

_int_types = (ctypes.c_int16, ctypes.c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have ctypes.c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (ctypes.c_int64,)
for t in _int_types:
    if ctypes.sizeof(t) == ctypes.sizeof(ctypes.c_size_t):
        c_ptrdiff_t = t
del t
del _int_types



class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, ctypes.Union):

    _fields_ = [("raw", ctypes.POINTER(ctypes.c_char)), ("data", ctypes.c_char_p)]

    def __init__(self, obj=b""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(ctypes.POINTER(ctypes.c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, ctypes.c_char_p):
            return obj

        # Convert from POINTER(ctypes.c_char)
        elif isinstance(obj, ctypes.POINTER(ctypes.c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(ctypes.cast(obj, ctypes.POINTER(ctypes.c_char)))

        # Convert from ctypes.c_char array
        elif isinstance(obj, ctypes.c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to ctypes.c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return ctypes.c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = ['.']

# Begin loader

"""
Load libraries - appropriately for all our supported platforms
"""
# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import ctypes
import ctypes.util
import glob
import os.path
import platform
import re
import sys


def _environ_path(name):
    """Split an environment variable into a path-like list elements"""
    if name in os.environ:
        return os.environ[name].split(":")
    return []


class LibraryLoader:
    """
    A base class For loading of libraries ;-)
    Subclasses load libraries for specific platforms.
    """

    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup:
        """Looking up calling conventions for a platform"""

        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            """Return the given name according to the selected calling convention"""
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            """Return True if this given calling convention finds the given 'name'"""
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            # noinspection PyBroadException
            try:
                return self.Lookup(path)
            except Exception:  # pylint: disable=broad-except
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # check if this code is even stored in a physical file
            try:
                this_file = __file__
            except NameError:
                this_file = None

            # then we search the directory where the generated python interface is stored
            if this_file is not None:
                for fmt in self.name_formats:
                    yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, _libname):  # pylint: disable=no-self-use
        """Return all the library paths available in this platform"""
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    """Library loader for MacOS"""

    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        """
        Looking up library files for this platform (Darwin aka MacOS)
        """

        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [fmt % libname for fmt in self.name_formats]

        for directory in self.getdirs(libname):
            for name in names:
                yield os.path.join(directory, name)

    @staticmethod
    def getdirs(libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [
                os.path.expanduser("~/lib"),
                "/usr/local/lib",
                "/usr/lib",
            ]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
            dirs.extend(_environ_path("LD_RUN_PATH"))

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    """Library loader for POSIX-like systems (including Linux)"""

    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    name_formats = ["lib%s.so", "%s.so", "%s"]

    class _Directories(dict):
        """Deal with directories"""

        def __init__(self):
            dict.__init__(self)
            self.order = 0

        def add(self, directory):
            """Add a directory to our current set of directories"""
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            order = self.setdefault(directory, self.order)
            if order == self.order:
                self.order += 1

        def extend(self, directories):
            """Add a list of directories to our set"""
            for a_dir in directories:
                self.add(a_dir)

        def ordered(self):
            """Sort the list of directories"""
            return (i[0] for i in sorted(self.items(), key=lambda d: d[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive function to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as fileobj:
                for dirname in fileobj:
                    dirname = dirname.strip()
                    if not dirname:
                        continue

                    match = self._include.match(dirname)
                    if not match:
                        dirs.add(dirname)
                    else:
                        for dir2 in glob.glob(match.group("pattern")):
                            self._get_ld_so_conf_dirs(dir2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HP-UX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compatible
                unix_lib_dirs_list += [
                    "/lib/x86_64-linux-gnu",
                    "/usr/lib/x86_64-linux-gnu",
                ]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        # ext_re = re.compile(r"\.s[ol]$")
        for our_dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % our_dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    """Library loader for Microsoft Windows"""

    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        """Lookup class for Windows libraries..."""

        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for path in other_dirs:
        if not os.path.isabs(path):
            path = os.path.abspath(path)
        load_library.other_dirs.append(path)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["Sensor.dll"] = load_library("Sensor.dll")

# 1 libraries
# End libraries

# No modules

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 25
if _libs["Sensor.dll"].has("SensorInit", "cdecl"):
    SensorInit = _libs["Sensor.dll"].get("SensorInit", "cdecl")
    SensorInit.argtypes = [c_int64]
    SensorInit.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 32
if _libs["Sensor.dll"].has("SensorGetInfo", "cdecl"):
    SensorGetInfo = _libs["Sensor.dll"].get("SensorGetInfo", "cdecl")
    SensorGetInfo.argtypes = [c_char * int(128)]
    SensorGetInfo.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 46
if _libs["Sensor.dll"].has("SensorLoadFile", "cdecl"):
    SensorLoadFile = _libs["Sensor.dll"].get("SensorLoadFile", "cdecl")
    SensorLoadFile.argtypes = [c_char * int(512)]
    SensorLoadFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 52
if _libs["Sensor.dll"].has("SensorLoadCard", "cdecl"):
    SensorLoadCard = _libs["Sensor.dll"].get("SensorLoadCard", "cdecl")
    SensorLoadCard.argtypes = [c_char * int(512)]
    SensorLoadCard.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 64
if _libs["Sensor.dll"].has("SensorSaveFile", "cdecl"):
    SensorSaveFile = _libs["Sensor.dll"].get("SensorSaveFile", "cdecl")
    SensorSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    SensorSaveFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 71
if _libs["Sensor.dll"].has("SensorRemove", "cdecl"):
    SensorRemove = _libs["Sensor.dll"].get("SensorRemove", "cdecl")
    SensorRemove.argtypes = [c_int64]
    SensorRemove.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 77
if _libs["Sensor.dll"].has("SensorRemoveAll", "cdecl"):
    SensorRemoveAll = _libs["Sensor.dll"].get("SensorRemoveAll", "cdecl")
    SensorRemoveAll.argtypes = []
    SensorRemoveAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 84
if _libs["Sensor.dll"].has("SensorGetCount", "cdecl"):
    SensorGetCount = _libs["Sensor.dll"].get("SensorGetCount", "cdecl")
    SensorGetCount.argtypes = []
    SensorGetCount.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 95
if _libs["Sensor.dll"].has("SensorGetLoaded", "cdecl"):
    SensorGetLoaded = _libs["Sensor.dll"].get("SensorGetLoaded", "cdecl")
    SensorGetLoaded.argtypes = [c_int, POINTER(c_int64)]
    SensorGetLoaded.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 107
if _libs["Sensor.dll"].has("SensorGetLocAll", "cdecl"):
    SensorGetLocAll = _libs["Sensor.dll"].get("SensorGetLocAll", "cdecl")
    SensorGetLocAll.argtypes = [c_int64, POINTER(c_double), POINTER(c_double), c_double * int(3), c_char * int(24), POINTER(c_int), String]
    SensorGetLocAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 124
if _libs["Sensor.dll"].has("SensorSetLocAll", "cdecl"):
    SensorSetLocAll = _libs["Sensor.dll"].get("SensorSetLocAll", "cdecl")
    SensorSetLocAll.argtypes = [c_int64, c_double, c_double, c_double * int(3), c_char * int(24), c_int, c_char]
    SensorSetLocAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 152
if _libs["Sensor.dll"].has("SensorGetLocField", "cdecl"):
    SensorGetLocField = _libs["Sensor.dll"].get("SensorGetLocField", "cdecl")
    SensorGetLocField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorGetLocField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 164
if _libs["Sensor.dll"].has("SensorSetLocField", "cdecl"):
    SensorSetLocField = _libs["Sensor.dll"].get("SensorSetLocField", "cdecl")
    SensorSetLocField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorSetLocField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 187
if _libs["Sensor.dll"].has("SensorGet1L", "cdecl"):
    SensorGet1L = _libs["Sensor.dll"].get("SensorGet1L", "cdecl")
    SensorGet1L.argtypes = [c_int64, String, String, POINTER(c_int), POINTER(c_double), String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_int), POINTER(c_double)]
    SensorGet1L.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 214
if _libs["Sensor.dll"].has("SensorSet1L", "cdecl"):
    SensorSet1L = _libs["Sensor.dll"].get("SensorSet1L", "cdecl")
    SensorSet1L.argtypes = [c_int64, c_char, c_char, c_int, c_double, c_char, c_double, c_double, c_double, c_double, c_double, c_int, c_int, c_int, c_double, c_int, c_double]
    SensorSet1L.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 232
if _libs["Sensor.dll"].has("SensorGet2L", "cdecl"):
    SensorGet2L = _libs["Sensor.dll"].get("SensorGet2L", "cdecl")
    SensorGet2L.argtypes = [c_int64, String, POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    SensorGet2L.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 252
if _libs["Sensor.dll"].has("SensorSet2L", "cdecl"):
    SensorSet2L = _libs["Sensor.dll"].get("SensorSet2L", "cdecl")
    SensorSet2L.argtypes = [c_int64, c_char, c_double, c_double, c_double, c_double, c_int, c_double, c_double, c_double, c_double, c_double]
    SensorSet2L.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 298
if _libs["Sensor.dll"].has("SensorGetLimField", "cdecl"):
    SensorGetLimField = _libs["Sensor.dll"].get("SensorGetLimField", "cdecl")
    SensorGetLimField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorGetLimField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 310
if _libs["Sensor.dll"].has("SensorSetLimField", "cdecl"):
    SensorSetLimField = _libs["Sensor.dll"].get("SensorSetLimField", "cdecl")
    SensorSetLimField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorSetLimField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 317
if _libs["Sensor.dll"].has("SensorGetBS", "cdecl"):
    SensorGetBS = _libs["Sensor.dll"].get("SensorGetBS", "cdecl")
    SensorGetBS.argtypes = [c_int64, c_double * int(16)]
    SensorGetBS.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 324
if _libs["Sensor.dll"].has("SensorSetBS", "cdecl"):
    SensorSetBS = _libs["Sensor.dll"].get("SensorSetBS", "cdecl")
    SensorSetBS.argtypes = [c_int64, c_double * int(16)]
    SensorSetBS.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 332
if _libs["Sensor.dll"].has("SensorGetBSField", "cdecl"):
    SensorGetBSField = _libs["Sensor.dll"].get("SensorGetBSField", "cdecl")
    SensorGetBSField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorGetBSField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 340
if _libs["Sensor.dll"].has("SensorSetBSField", "cdecl"):
    SensorSetBSField = _libs["Sensor.dll"].get("SensorSetBSField", "cdecl")
    SensorSetBSField.argtypes = [c_int64, c_int, c_char * int(512)]
    SensorSetBSField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 349
if _libs["Sensor.dll"].has("SensorGetLines", "cdecl"):
    SensorGetLines = _libs["Sensor.dll"].get("SensorGetLines", "cdecl")
    SensorGetLines.argtypes = [c_int64, c_char * int(512), c_char * int(512), c_char * int(512)]
    SensorGetLines.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 356
if _libs["Sensor.dll"].has("SensorGetOrbSatKey", "cdecl"):
    SensorGetOrbSatKey = _libs["Sensor.dll"].get("SensorGetOrbSatKey", "cdecl")
    SensorGetOrbSatKey.argtypes = [c_int64, POINTER(c_int64)]
    SensorGetOrbSatKey.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 363
if _libs["Sensor.dll"].has("SensorSetOrbSatKey", "cdecl"):
    SensorSetOrbSatKey = _libs["Sensor.dll"].get("SensorSetOrbSatKey", "cdecl")
    SensorSetOrbSatKey.argtypes = [c_int64, c_int64]
    SensorSetOrbSatKey.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 370
if _libs["Sensor.dll"].has("SensorLoadAzElTable", "cdecl"):
    SensorLoadAzElTable = _libs["Sensor.dll"].get("SensorLoadAzElTable", "cdecl")
    SensorLoadAzElTable.argtypes = [c_int64, c_char * int(512)]
    SensorLoadAzElTable.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 378
if _libs["Sensor.dll"].has("SensorAddSegment", "cdecl"):
    SensorAddSegment = _libs["Sensor.dll"].get("SensorAddSegment", "cdecl")
    SensorAddSegment.argtypes = [c_int64, c_int, c_double * int(16)]
    SensorAddSegment.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 387
if _libs["Sensor.dll"].has("SensorGetSegment", "cdecl"):
    SensorGetSegment = _libs["Sensor.dll"].get("SensorGetSegment", "cdecl")
    SensorGetSegment.argtypes = [c_int64, c_int, POINTER(c_int), c_double * int(16)]
    SensorGetSegment.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 395
if _libs["Sensor.dll"].has("SetSenKeyMode", "cdecl"):
    SetSenKeyMode = _libs["Sensor.dll"].get("SetSenKeyMode", "cdecl")
    SetSenKeyMode.argtypes = [c_int]
    SetSenKeyMode.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 400
if _libs["Sensor.dll"].has("GetSenKeyMode", "cdecl"):
    GetSenKeyMode = _libs["Sensor.dll"].get("GetSenKeyMode", "cdecl")
    GetSenKeyMode.argtypes = []
    GetSenKeyMode.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 406
if _libs["Sensor.dll"].has("SenNumOf", "cdecl"):
    SenNumOf = _libs["Sensor.dll"].get("SenNumOf", "cdecl")
    SenNumOf.argtypes = [c_int64]
    SenNumOf.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 413
if _libs["Sensor.dll"].has("SensorGetSenKey", "cdecl"):
    SensorGetSenKey = _libs["Sensor.dll"].get("SensorGetSenKey", "cdecl")
    SensorGetSenKey.argtypes = [c_int]
    SensorGetSenKey.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 421
if _libs["Sensor.dll"].has("SensorGetSenKeyML", "cdecl"):
    SensorGetSenKeyML = _libs["Sensor.dll"].get("SensorGetSenKeyML", "cdecl")
    SensorGetSenKeyML.argtypes = [c_int, POINTER(c_int64)]
    SensorGetSenKeyML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 428
if _libs["Sensor.dll"].has("SensorAddFrArray", "cdecl"):
    SensorAddFrArray = _libs["Sensor.dll"].get("SensorAddFrArray", "cdecl")
    SensorAddFrArray.argtypes = [c_double * int(128), c_char * int(512)]
    SensorAddFrArray.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 436
if _libs["Sensor.dll"].has("SensorDataToArray", "cdecl"):
    SensorDataToArray = _libs["Sensor.dll"].get("SensorDataToArray", "cdecl")
    SensorDataToArray.argtypes = [c_int64, c_double * int(128), c_char * int(512)]
    SensorDataToArray.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 775
for _lib in _libs.values():
    if not _lib.has("LoadSensorDll", "cdecl"):
        continue
    LoadSensorDll = _lib.get("LoadSensorDll", "cdecl")
    LoadSensorDll.argtypes = []
    LoadSensorDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 776
for _lib in _libs.values():
    if not _lib.has("FreeSensorDll", "cdecl"):
        continue
    FreeSensorDll = _lib.get("FreeSensorDll", "cdecl")
    FreeSensorDll.argtypes = []
    FreeSensorDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 14
try:
    SensorDll = 'Sensor.dll'
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 440
try:
    SEG_BCONE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 441
try:
    SEG_DOME = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 447
try:
    XA_SEG_DOME_AZFR = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 448
try:
    XA_SEG_DOME_AZTO = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 449
try:
    XA_SEG_DOME_ELFR = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 450
try:
    XA_SEG_DOME_ELTO = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 451
try:
    XA_SEG_DOME_MINRNG = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 452
try:
    XA_SEG_DOME_MAXRNG = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 454
try:
    XA_SEG_DOME_SIZE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 459
try:
    XA_SEG_BCONE_BSAZ = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 460
try:
    XA_SEG_BCONE_BSEL = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 461
try:
    XA_SEG_BCONE_ANGFR = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 462
try:
    XA_SEG_BCONE_ANGTO = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 463
try:
    XA_SEG_BCONE_MINRNG = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 464
try:
    XA_SEG_BCONE_MAXRNG = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 465
try:
    XA_SEG_BCONE_MINEL = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 467
try:
    XA_SEG_BCONE_SIZE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 472
try:
    SEN_KEYMODE_NODUP = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 473
try:
    SEN_KEYMODE_DMA = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 477
try:
    BADSENKEY = (-1)
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 478
try:
    DUPSENKEY = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 482
try:
    VT_BCT = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 483
try:
    VT_CON = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 484
try:
    VT_OPT = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 485
try:
    VT_FAN = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 486
try:
    VT_ORB = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 487
try:
    VT_FOR = 82
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 488
try:
    VT_FOV = 86
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 492
try:
    SENLOC_TYPE_ECR = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 493
try:
    SENLOC_TYPE_EFG = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 494
try:
    SENLOC_TYPE_LLH = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 502
try:
    XA_SEN_GEN_SENNUM = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 503
try:
    XA_SEN_GEN_MINRNG = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 504
try:
    XA_SEN_GEN_MAXRNG = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 505
try:
    XA_SEN_GEN_RRLIM = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 506
try:
    XA_SEN_GEN_RNGLIMFLG = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 507
try:
    XA_SEN_GEN_SMSEN = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 513
try:
    XA_SEN_GRN_LOCTYPE = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 514
try:
    XA_SEN_GRN_POS1 = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 515
try:
    XA_SEN_GRN_POS2 = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 516
try:
    XA_SEN_GRN_POS3 = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 517
try:
    XA_SEN_GRN_ASTROLAT = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 518
try:
    XA_SEN_GRN_ASTROLON = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 525
try:
    XA_SEN_BCT_BRSGHTAZ = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 526
try:
    XA_SEN_BCT_BRSGHTEL = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 527
try:
    XA_SEN_BCT_HALFANG = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 528
try:
    XA_SEN_BCT_MINEL = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 532
try:
    XA_SEN_CON_ELFR1 = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 533
try:
    XA_SEN_CON_ELTO1 = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 534
try:
    XA_SEN_CON_AZFR1 = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 535
try:
    XA_SEN_CON_AZTO1 = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 536
try:
    XA_SEN_CON_ELFR2 = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 537
try:
    XA_SEN_CON_ELTO2 = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 538
try:
    XA_SEN_CON_AZFR2 = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 539
try:
    XA_SEN_CON_AZTO2 = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 543
try:
    XA_SEN_OPT_ELFR1 = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 544
try:
    XA_SEN_OPT_ELTO1 = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 545
try:
    XA_SEN_OPT_AZFR1 = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 546
try:
    XA_SEN_OPT_AZTO1 = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 547
try:
    XA_SEN_OPT_ELFR2 = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 548
try:
    XA_SEN_OPT_ELTO2 = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 549
try:
    XA_SEN_OPT_AZFR2 = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 550
try:
    XA_SEN_OPT_AZTO2 = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 552
try:
    XA_SEN_OPT_SEA = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 553
try:
    XA_SEN_OPT_TWILGHT = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 554
try:
    XA_SEN_OPT_VISCHK = 42
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 558
try:
    XA_SEN_FAN_AZ = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 559
try:
    XA_SEN_FAN_TILTANGLE = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 560
try:
    XA_SEN_FAN_OBSANGLE = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 565
try:
    XA_SEN_ORB_SATNUM = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 567
try:
    XA_SEN_ORB_ELMIN1 = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 568
try:
    XA_SEN_ORB_ELMAX1 = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 569
try:
    XA_SEN_ORB_AZMIN1 = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 570
try:
    XA_SEN_ORB_AZMAX1 = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 571
try:
    XA_SEN_ORB_ELMIN2 = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 572
try:
    XA_SEN_ORB_ELMAX2 = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 573
try:
    XA_SEN_ORB_AZMIN2 = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 574
try:
    XA_SEN_ORB_AZMAX2 = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 576
try:
    XA_SEN_ORB_EARTHLIMB = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 577
try:
    XA_SEN_ORB_SEA = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 578
try:
    XA_SEN_ORB_LEA = 42
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 579
try:
    XA_SEN_ORB_MINILLUM = 43
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 580
try:
    XA_SEN_ORB_EARTHBRND = 44
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 581
try:
    XA_SEN_ORB_PLNTRYRES = 45
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 592
try:
    XA_SEN_FOV_BEAMWIDTH = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 593
try:
    XA_SEN_FOV_TILTANGLE = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 599
try:
    XA_SEN_GEN_UNIT = 90
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 600
try:
    XA_SEN_GEN_INTERVAL = 91
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 601
try:
    XA_SEN_GEN_PTSPERPAS = 92
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 605
try:
    XA_SEN_GEN_AZSIGMA = 110
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 606
try:
    XA_SEN_GEN_ELSIGMA = 111
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 607
try:
    XA_SEN_GEN_RGSIGMA = 112
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 608
try:
    XA_SEN_GEN_RRSIGMA = 113
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 609
try:
    XA_SEN_GEN_ARSIGMA = 114
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 610
try:
    XA_SEN_GEN_ERSIGMA = 115
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 611
try:
    XA_SEN_GEN_AZBIAS = 116
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 612
try:
    XA_SEN_GEN_ELBIAS = 117
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 613
try:
    XA_SEN_GEN_RGBIAS = 118
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 614
try:
    XA_SEN_GEN_RRBIAS = 119
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 615
try:
    XA_SEN_GEN_TIMEBIAS = 120
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 618
try:
    XA_SEN_SIZE = 128
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 623
try:
    XS_SEN_SECCLASS_0_1 = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 624
try:
    XS_SEN_VIEWTYPE_1_1 = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 625
try:
    XS_SEN_OBSTYPE_2_1 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 626
try:
    XS_SEN_DSCRPTN_3_24 = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 627
try:
    XS_SEN_ORB_BSVEC1_27_1 = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 628
try:
    XS_SEN_ORB_BSVEC2_28_1 = 28
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 629
try:
    XS_SEN_FOR_AZFILE_255_256 = 255
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 631
try:
    XS_SEN_LENGTH = 512
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 635
try:
    XF_SENLOC_NUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 636
try:
    XF_SENLOC_LAT = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 637
try:
    XF_SENLOC_LON = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 638
try:
    XF_SENLOC_POSX = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 639
try:
    XF_SENLOC_POSY = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 640
try:
    XF_SENLOC_POSZ = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 641
try:
    XF_SENLOC_DESC = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 642
try:
    XF_SENLOC_ORBSATNUM = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 643
try:
    XF_SENLOC_SECCLASS = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 645
try:
    XF_SENLIM_VIEWTYPE = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 646
try:
    XF_SENLIM_OBSTYPE = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 647
try:
    XF_SENLIM_UNIT = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 648
try:
    XF_SENLIM_MAXRNG = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 649
try:
    XF_SENLIM_MINRNG = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 650
try:
    XF_SENLIM_INTERVAL = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 651
try:
    XF_SENLIM_OPTVISFLG = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 652
try:
    XF_SENLIM_RNGLIMFLG = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 653
try:
    XF_SENLIM_PTSPERPAS = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 654
try:
    XF_SENLIM_RRLIM = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 656
try:
    XF_SENLIM_ELLIM1 = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 657
try:
    XF_SENLIM_ELLIM2 = 32
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 658
try:
    XF_SENLIM_ELLIM3 = 33
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 659
try:
    XF_SENLIM_ELLIM4 = 34
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 660
try:
    XF_SENLIM_AZLIM1 = 35
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 661
try:
    XF_SENLIM_AZLIM2 = 36
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 662
try:
    XF_SENLIM_AZLIM3 = 37
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 663
try:
    XF_SENLIM_AZLIM4 = 38
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 666
try:
    XF_SENLIM_PLNTRYRES = 52
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 667
try:
    XF_SENLIM_BOREVEC1 = 53
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 668
try:
    XF_SENLIM_BOREVEC2 = 54
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 669
try:
    XF_SENLIM_KEARTH = 55
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 670
try:
    XF_SENLIM_ELIMB = 56
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 671
try:
    XF_SENLIM_SOLEXCANG = 57
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 672
try:
    XF_SENLIM_LUNEXCANG = 58
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 675
try:
    XF_SENLIM_MINIL = 59
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 676
try:
    XF_SENLIM_TWILIT = 60
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 677
try:
    XF_SENLIM_SMSEN = 61
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 678
try:
    XF_SENLIM_NUMSEGS = 62
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 679
try:
    XF_SENLIM_FILE = 63
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 680
try:
    XF_SENLIM_AZELROWS = 64
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 686
try:
    XA_SENLOC_NUM = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 687
try:
    XA_SENLOC_LAT = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 688
try:
    XA_SENLOC_LON = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 689
try:
    XA_SENLOC_POSX = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 690
try:
    XA_SENLOC_POSY = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 691
try:
    XA_SENLOC_POSZ = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 693
try:
    XA_SENLOC_SIZE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 699
try:
    XAF_SENBS_AZSIGMA = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 700
try:
    XAF_SENBS_ELSIGMA = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 701
try:
    XAF_SENBS_RGSIGMA = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 702
try:
    XAF_SENBS_RRSIGMA = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 703
try:
    XAF_SENBS_ARSIGMA = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 704
try:
    XAF_SENBS_ERSIGMA = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 706
try:
    XAF_SENBS_AZBIAS = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 707
try:
    XAF_SENBS_ELBIAS = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 708
try:
    XAF_SENBS_RGBIAS = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 709
try:
    XAF_SENBS_RRBIAS = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 710
try:
    XAF_SENBS_TIMEBIAS = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 712
try:
    XAF_SENBS_SIZE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 716
try:
    OT_RRATE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 717
try:
    OT_AZEL = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 718
try:
    OT_AZEL_RNG = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 719
try:
    OT_AZEL_RNGRRATE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 720
try:
    OT_AZEL_ALL = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 721
try:
    OT_RADEC = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 722
try:
    OT_RNGONLY = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 723
try:
    OT_AZEL_SENPOS = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 724
try:
    OT_RADEC_SENPOS = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 725
try:
    OT_VEL = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 726
try:
    OT_POS = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 727
try:
    OT_STAR = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 728
try:
    OT_RF = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 729
try:
    OT_SLR = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 730
try:
    OT_M = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 731
try:
    OT_O = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SensorDll.h: 732
try:
    OT_RRATE_SELOB = 999
except:
    pass

# No inserted files

# No prefix-stripping

