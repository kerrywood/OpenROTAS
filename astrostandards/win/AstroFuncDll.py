r"""Wrapper for new_AstroFuncDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . --compile-libdir=. -l AstroFunc.dll ./new_AstroFuncDll.h -o ./AstroFuncDll.py

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
_libs["AstroFunc.dll"] = load_library("AstroFunc.dll")

# 1 libraries
# End libraries

# No modules

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 25
if _libs["AstroFunc.dll"].has("AstroFuncInit", "cdecl"):
    AstroFuncInit = _libs["AstroFunc.dll"].get("AstroFuncInit", "cdecl")
    AstroFuncInit.argtypes = [c_int64]
    AstroFuncInit.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 31
if _libs["AstroFunc.dll"].has("AstroFuncGetInfo", "cdecl"):
    AstroFuncGetInfo = _libs["AstroFunc.dll"].get("AstroFuncGetInfo", "cdecl")
    AstroFuncGetInfo.argtypes = [c_char * int(128)]
    AstroFuncGetInfo.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 37
if _libs["AstroFunc.dll"].has("KepToEqnx", "cdecl"):
    KepToEqnx = _libs["AstroFunc.dll"].get("KepToEqnx", "cdecl")
    KepToEqnx.argtypes = [c_double * int(6), c_double * int(6)]
    KepToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 44
if _libs["AstroFunc.dll"].has("KepToPosVel", "cdecl"):
    KepToPosVel = _libs["AstroFunc.dll"].get("KepToPosVel", "cdecl")
    KepToPosVel.argtypes = [c_double * int(6), c_double * int(3), c_double * int(3)]
    KepToPosVel.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 52
if _libs["AstroFunc.dll"].has("KepToUVW", "cdecl"):
    KepToUVW = _libs["AstroFunc.dll"].get("KepToUVW", "cdecl")
    KepToUVW.argtypes = [c_double * int(6), c_double * int(3), c_double * int(3), c_double * int(3)]
    KepToUVW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 58
if _libs["AstroFunc.dll"].has("ClassToEqnx", "cdecl"):
    ClassToEqnx = _libs["AstroFunc.dll"].get("ClassToEqnx", "cdecl")
    ClassToEqnx.argtypes = [c_double * int(6), c_double * int(6)]
    ClassToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 64
if _libs["AstroFunc.dll"].has("EqnxToClass", "cdecl"):
    EqnxToClass = _libs["AstroFunc.dll"].get("EqnxToClass", "cdecl")
    EqnxToClass.argtypes = [c_double * int(6), c_double * int(6)]
    EqnxToClass.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 70
if _libs["AstroFunc.dll"].has("EqnxToKep", "cdecl"):
    EqnxToKep = _libs["AstroFunc.dll"].get("EqnxToKep", "cdecl")
    EqnxToKep.argtypes = [c_double * int(6), c_double * int(6)]
    EqnxToKep.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 77
if _libs["AstroFunc.dll"].has("EqnxToPosVel", "cdecl"):
    EqnxToPosVel = _libs["AstroFunc.dll"].get("EqnxToPosVel", "cdecl")
    EqnxToPosVel.argtypes = [c_double * int(6), c_double * int(3), c_double * int(3)]
    EqnxToPosVel.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 84
if _libs["AstroFunc.dll"].has("PosVelToEqnx", "cdecl"):
    PosVelToEqnx = _libs["AstroFunc.dll"].get("PosVelToEqnx", "cdecl")
    PosVelToEqnx.argtypes = [c_double * int(3), c_double * int(3), c_double * int(6)]
    PosVelToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 93
if _libs["AstroFunc.dll"].has("PosVelMuToEqnx", "cdecl"):
    PosVelMuToEqnx = _libs["AstroFunc.dll"].get("PosVelMuToEqnx", "cdecl")
    PosVelMuToEqnx.argtypes = [c_double * int(3), c_double * int(3), c_double, c_double * int(6)]
    PosVelMuToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 100
if _libs["AstroFunc.dll"].has("PosVelToKep", "cdecl"):
    PosVelToKep = _libs["AstroFunc.dll"].get("PosVelToKep", "cdecl")
    PosVelToKep.argtypes = [c_double * int(3), c_double * int(3), c_double * int(6)]
    PosVelToKep.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 109
if _libs["AstroFunc.dll"].has("PosVelMuToKep", "cdecl"):
    PosVelMuToKep = _libs["AstroFunc.dll"].get("PosVelMuToKep", "cdecl")
    PosVelMuToKep.argtypes = [c_double * int(3), c_double * int(3), c_double, c_double * int(6)]
    PosVelMuToKep.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 122
if _libs["AstroFunc.dll"].has("PosVelToUUVW", "cdecl"):
    PosVelToUUVW = _libs["AstroFunc.dll"].get("PosVelToUUVW", "cdecl")
    PosVelToUUVW.argtypes = [c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    PosVelToUUVW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 135
if _libs["AstroFunc.dll"].has("PosVelToPTW", "cdecl"):
    PosVelToPTW = _libs["AstroFunc.dll"].get("PosVelToPTW", "cdecl")
    PosVelToPTW.argtypes = [c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    PosVelToPTW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 141
if _libs["AstroFunc.dll"].has("SolveKepEqtn", "cdecl"):
    SolveKepEqtn = _libs["AstroFunc.dll"].get("SolveKepEqtn", "cdecl")
    SolveKepEqtn.argtypes = [c_double * int(6)]
    SolveKepEqtn.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 147
if _libs["AstroFunc.dll"].has("CompTrueAnomaly", "cdecl"):
    CompTrueAnomaly = _libs["AstroFunc.dll"].get("CompTrueAnomaly", "cdecl")
    CompTrueAnomaly.argtypes = [c_double * int(6)]
    CompTrueAnomaly.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 153
if _libs["AstroFunc.dll"].has("NToA", "cdecl"):
    NToA = _libs["AstroFunc.dll"].get("NToA", "cdecl")
    NToA.argtypes = [c_double]
    NToA.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 159
if _libs["AstroFunc.dll"].has("AToN", "cdecl"):
    AToN = _libs["AstroFunc.dll"].get("AToN", "cdecl")
    AToN.argtypes = [c_double]
    AToN.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 168
if _libs["AstroFunc.dll"].has("KozaiToBrouwer", "cdecl"):
    KozaiToBrouwer = _libs["AstroFunc.dll"].get("KozaiToBrouwer", "cdecl")
    KozaiToBrouwer.argtypes = [c_double, c_double, c_double]
    KozaiToBrouwer.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 177
if _libs["AstroFunc.dll"].has("BrouwerToKozai", "cdecl"):
    BrouwerToKozai = _libs["AstroFunc.dll"].get("BrouwerToKozai", "cdecl")
    BrouwerToKozai.argtypes = [c_double, c_double, c_double]
    BrouwerToKozai.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 183
if _libs["AstroFunc.dll"].has("KepOscToMean", "cdecl"):
    KepOscToMean = _libs["AstroFunc.dll"].get("KepOscToMean", "cdecl")
    KepOscToMean.argtypes = [c_double * int(6), c_double * int(6)]
    KepOscToMean.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 190
if _libs["AstroFunc.dll"].has("XYZToLLH", "cdecl"):
    XYZToLLH = _libs["AstroFunc.dll"].get("XYZToLLH", "cdecl")
    XYZToLLH.argtypes = [c_double, c_double * int(3), c_double * int(3)]
    XYZToLLH.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 197
if _libs["AstroFunc.dll"].has("XYZToLLHTime", "cdecl"):
    XYZToLLHTime = _libs["AstroFunc.dll"].get("XYZToLLHTime", "cdecl")
    XYZToLLHTime.argtypes = [c_double, c_double * int(3), c_double * int(3)]
    XYZToLLHTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 204
if _libs["AstroFunc.dll"].has("LLHToXYZ", "cdecl"):
    LLHToXYZ = _libs["AstroFunc.dll"].get("LLHToXYZ", "cdecl")
    LLHToXYZ.argtypes = [c_double, c_double * int(3), c_double * int(3)]
    LLHToXYZ.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 211
if _libs["AstroFunc.dll"].has("LLHToXYZTime", "cdecl"):
    LLHToXYZTime = _libs["AstroFunc.dll"].get("LLHToXYZTime", "cdecl")
    LLHToXYZTime.argtypes = [c_double, c_double * int(3), c_double * int(3)]
    LLHToXYZTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 220
if _libs["AstroFunc.dll"].has("EFGToECI", "cdecl"):
    EFGToECI = _libs["AstroFunc.dll"].get("EFGToECI", "cdecl")
    EFGToECI.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    EFGToECI.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 229
if _libs["AstroFunc.dll"].has("EFGToECITime", "cdecl"):
    EFGToECITime = _libs["AstroFunc.dll"].get("EFGToECITime", "cdecl")
    EFGToECITime.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    EFGToECITime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 238
if _libs["AstroFunc.dll"].has("ECIToEFG", "cdecl"):
    ECIToEFG = _libs["AstroFunc.dll"].get("ECIToEFG", "cdecl")
    ECIToEFG.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    ECIToEFG.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 247
if _libs["AstroFunc.dll"].has("ECIToEFGTime", "cdecl"):
    ECIToEFGTime = _libs["AstroFunc.dll"].get("ECIToEFGTime", "cdecl")
    ECIToEFGTime.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    ECIToEFGTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 257
if _libs["AstroFunc.dll"].has("ECRToEFG", "cdecl"):
    ECRToEFG = _libs["AstroFunc.dll"].get("ECRToEFG", "cdecl")
    ECRToEFG.argtypes = [c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    ECRToEFG.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 266
if _libs["AstroFunc.dll"].has("ECRToEFGTime", "cdecl"):
    ECRToEFGTime = _libs["AstroFunc.dll"].get("ECRToEFGTime", "cdecl")
    ECRToEFGTime.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    ECRToEFGTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 276
if _libs["AstroFunc.dll"].has("EFGToECR", "cdecl"):
    EFGToECR = _libs["AstroFunc.dll"].get("EFGToECR", "cdecl")
    EFGToECR.argtypes = [c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    EFGToECR.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 285
if _libs["AstroFunc.dll"].has("EFGToECRTime", "cdecl"):
    EFGToECRTime = _libs["AstroFunc.dll"].get("EFGToECRTime", "cdecl")
    EFGToECRTime.argtypes = [c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    EFGToECRTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 291
if _libs["AstroFunc.dll"].has("EFGPosToLLH", "cdecl"):
    EFGPosToLLH = _libs["AstroFunc.dll"].get("EFGPosToLLH", "cdecl")
    EFGPosToLLH.argtypes = [c_double * int(3), c_double * int(3)]
    EFGPosToLLH.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 297
if _libs["AstroFunc.dll"].has("LLHToEFGPos", "cdecl"):
    LLHToEFGPos = _libs["AstroFunc.dll"].get("LLHToEFGPos", "cdecl")
    LLHToEFGPos.argtypes = [c_double * int(3), c_double * int(3)]
    LLHToEFGPos.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 308
if _libs["AstroFunc.dll"].has("RotJ2KToDate", "cdecl"):
    RotJ2KToDate = _libs["AstroFunc.dll"].get("RotJ2KToDate", "cdecl")
    RotJ2KToDate.argtypes = [c_int, c_int, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    RotJ2KToDate.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 319
if _libs["AstroFunc.dll"].has("RotDateToJ2K", "cdecl"):
    RotDateToJ2K = _libs["AstroFunc.dll"].get("RotDateToJ2K", "cdecl")
    RotDateToJ2K.argtypes = [c_int, c_int, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    RotDateToJ2K.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 328
if _libs["AstroFunc.dll"].has("CompSunMoonPos", "cdecl"):
    CompSunMoonPos = _libs["AstroFunc.dll"].get("CompSunMoonPos", "cdecl")
    CompSunMoonPos.argtypes = [c_double, c_double * int(3), POINTER(c_double), c_double * int(3), POINTER(c_double)]
    CompSunMoonPos.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 335
if _libs["AstroFunc.dll"].has("CompSunPos", "cdecl"):
    CompSunPos = _libs["AstroFunc.dll"].get("CompSunPos", "cdecl")
    CompSunPos.argtypes = [c_double, c_double * int(3), POINTER(c_double)]
    CompSunPos.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 342
if _libs["AstroFunc.dll"].has("CompMoonPos", "cdecl"):
    CompMoonPos = _libs["AstroFunc.dll"].get("CompMoonPos", "cdecl")
    CompMoonPos.argtypes = [c_double, c_double * int(3), POINTER(c_double)]
    CompMoonPos.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 350
if _libs["AstroFunc.dll"].has("AstroConvFrTo", "cdecl"):
    AstroConvFrTo = _libs["AstroFunc.dll"].get("AstroConvFrTo", "cdecl")
    AstroConvFrTo.argtypes = [c_int, c_double * int(128), c_double * int(128)]
    AstroConvFrTo.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 359
if _libs["AstroFunc.dll"].has("RADecToLAD", "cdecl"):
    RADecToLAD = _libs["AstroFunc.dll"].get("RADecToLAD", "cdecl")
    RADecToLAD.argtypes = [c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3)]
    RADecToLAD.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 368
if _libs["AstroFunc.dll"].has("AzElToLAD", "cdecl"):
    AzElToLAD = _libs["AstroFunc.dll"].get("AzElToLAD", "cdecl")
    AzElToLAD.argtypes = [c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3)]
    AzElToLAD.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 389
if _libs["AstroFunc.dll"].has("ECIToTopoComps", "cdecl"):
    ECIToTopoComps = _libs["AstroFunc.dll"].get("ECIToTopoComps", "cdecl")
    ECIToTopoComps.argtypes = [c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(10)]
    ECIToTopoComps.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 400
if _libs["AstroFunc.dll"].has("RaDecToAzEl", "cdecl"):
    RaDecToAzEl = _libs["AstroFunc.dll"].get("RaDecToAzEl", "cdecl")
    RaDecToAzEl.argtypes = [c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    RaDecToAzEl.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 411
if _libs["AstroFunc.dll"].has("RaDecToAzElTime", "cdecl"):
    RaDecToAzElTime = _libs["AstroFunc.dll"].get("RaDecToAzElTime", "cdecl")
    RaDecToAzElTime.argtypes = [c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    RaDecToAzElTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 422
if _libs["AstroFunc.dll"].has("AzElToRaDec", "cdecl"):
    AzElToRaDec = _libs["AstroFunc.dll"].get("AzElToRaDec", "cdecl")
    AzElToRaDec.argtypes = [c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    AzElToRaDec.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 433
if _libs["AstroFunc.dll"].has("AzElToRaDecTime", "cdecl"):
    AzElToRaDecTime = _libs["AstroFunc.dll"].get("AzElToRaDecTime", "cdecl")
    AzElToRaDecTime.argtypes = [c_double, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    AzElToRaDecTime.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 450
if _libs["AstroFunc.dll"].has("RAEToECI", "cdecl"):
    RAEToECI = _libs["AstroFunc.dll"].get("RAEToECI", "cdecl")
    RAEToECI.argtypes = [c_double, c_double, c_double * int(6), c_double * int(3), c_double * int(3), c_double * int(3)]
    RAEToECI.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 458
if _libs["AstroFunc.dll"].has("GetInitialDrag", "cdecl"):
    GetInitialDrag = _libs["AstroFunc.dll"].get("GetInitialDrag", "cdecl")
    GetInitialDrag.argtypes = [c_double, c_double, POINTER(c_double), POINTER(c_double)]
    GetInitialDrag.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 468
if _libs["AstroFunc.dll"].has("CovMtxPTWToUVW", "cdecl"):
    CovMtxPTWToUVW = _libs["AstroFunc.dll"].get("CovMtxPTWToUVW", "cdecl")
    CovMtxPTWToUVW.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxPTWToUVW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 478
if _libs["AstroFunc.dll"].has("CovMtxUVWToPTW", "cdecl"):
    CovMtxUVWToPTW = _libs["AstroFunc.dll"].get("CovMtxUVWToPTW", "cdecl")
    CovMtxUVWToPTW.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxUVWToPTW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 488
if _libs["AstroFunc.dll"].has("EarthObstructionAngles", "cdecl"):
    EarthObstructionAngles = _libs["AstroFunc.dll"].get("EarthObstructionAngles", "cdecl")
    EarthObstructionAngles.argtypes = [c_double, c_double * int(3), c_double * int(3), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    EarthObstructionAngles.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 495
if _libs["AstroFunc.dll"].has("IsPointSunlit", "cdecl"):
    IsPointSunlit = _libs["AstroFunc.dll"].get("IsPointSunlit", "cdecl")
    IsPointSunlit.argtypes = [c_double, c_double * int(3)]
    IsPointSunlit.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 507
if _libs["AstroFunc.dll"].has("RotRADecl", "cdecl"):
    RotRADecl = _libs["AstroFunc.dll"].get("RotRADecl", "cdecl")
    RotRADecl.argtypes = [c_int, c_int, c_double, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    RotRADecl.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 519
if _libs["AstroFunc.dll"].has("RotRADec_DateToEqnx", "cdecl"):
    RotRADec_DateToEqnx = _libs["AstroFunc.dll"].get("RotRADec_DateToEqnx", "cdecl")
    RotRADec_DateToEqnx.argtypes = [c_int, c_int, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    RotRADec_DateToEqnx.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 531
if _libs["AstroFunc.dll"].has("RotRADec_EqnxToDate", "cdecl"):
    RotRADec_EqnxToDate = _libs["AstroFunc.dll"].get("RotRADec_EqnxToDate", "cdecl")
    RotRADec_EqnxToDate.argtypes = [c_int, c_int, c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    RotRADec_EqnxToDate.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 542
if _libs["AstroFunc.dll"].has("CovMtxEqnxToUVW", "cdecl"):
    CovMtxEqnxToUVW = _libs["AstroFunc.dll"].get("CovMtxEqnxToUVW", "cdecl")
    CovMtxEqnxToUVW.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxEqnxToUVW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 553
if _libs["AstroFunc.dll"].has("CovMtxUVWToEqnx", "cdecl"):
    CovMtxUVWToEqnx = _libs["AstroFunc.dll"].get("CovMtxUVWToEqnx", "cdecl")
    CovMtxUVWToEqnx.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxUVWToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 562
if _libs["AstroFunc.dll"].has("CovMtxECIToUVW", "cdecl"):
    CovMtxECIToUVW = _libs["AstroFunc.dll"].get("CovMtxECIToUVW", "cdecl")
    CovMtxECIToUVW.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxECIToUVW.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 571
if _libs["AstroFunc.dll"].has("CovMtxUVWToECI", "cdecl"):
    CovMtxUVWToECI = _libs["AstroFunc.dll"].get("CovMtxUVWToECI", "cdecl")
    CovMtxUVWToECI.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxUVWToECI.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 580
if _libs["AstroFunc.dll"].has("CovMtxECIToEFG", "cdecl"):
    CovMtxECIToEFG = _libs["AstroFunc.dll"].get("CovMtxECIToEFG", "cdecl")
    CovMtxECIToEFG.argtypes = [c_double, (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxECIToEFG.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 589
if _libs["AstroFunc.dll"].has("CovMtxEFGToECI", "cdecl"):
    CovMtxEFGToECI = _libs["AstroFunc.dll"].get("CovMtxEFGToECI", "cdecl")
    CovMtxEFGToECI.argtypes = [c_double, (c_double * int(6)) * int(6), (c_double * int(6)) * int(6)]
    CovMtxEFGToECI.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 595
if _libs["AstroFunc.dll"].has("Mtx6x6ToLTA21", "cdecl"):
    Mtx6x6ToLTA21 = _libs["AstroFunc.dll"].get("Mtx6x6ToLTA21", "cdecl")
    Mtx6x6ToLTA21.argtypes = [(c_double * int(6)) * int(6), c_double * int(21)]
    Mtx6x6ToLTA21.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 601
if _libs["AstroFunc.dll"].has("LTA21ToMtx6x6", "cdecl"):
    LTA21ToMtx6x6 = _libs["AstroFunc.dll"].get("LTA21ToMtx6x6", "cdecl")
    LTA21ToMtx6x6.argtypes = [c_double * int(21), (c_double * int(6)) * int(6)]
    LTA21ToMtx6x6.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 607
if _libs["AstroFunc.dll"].has("Mtx9x9ToLTA45", "cdecl"):
    Mtx9x9ToLTA45 = _libs["AstroFunc.dll"].get("Mtx9x9ToLTA45", "cdecl")
    Mtx9x9ToLTA45.argtypes = [(c_double * int(9)) * int(9), c_double * int(45)]
    Mtx9x9ToLTA45.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 613
if _libs["AstroFunc.dll"].has("LTA45ToMtx9x9", "cdecl"):
    LTA45ToMtx9x9 = _libs["AstroFunc.dll"].get("LTA45ToMtx9x9", "cdecl")
    LTA45ToMtx9x9.argtypes = [c_double * int(45), (c_double * int(9)) * int(9)]
    LTA45ToMtx9x9.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 622
if _libs["AstroFunc.dll"].has("PropCovFrState", "cdecl"):
    PropCovFrState = _libs["AstroFunc.dll"].get("PropCovFrState", "cdecl")
    PropCovFrState.argtypes = [c_double, c_double, c_double * int(54), (c_double * int(9)) * int(9), (c_double * int(6)) * int(6)]
    PropCovFrState.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 631
if _libs["AstroFunc.dll"].has("CovMtxECIToEqnx", "cdecl"):
    CovMtxECIToEqnx = _libs["AstroFunc.dll"].get("CovMtxECIToEqnx", "cdecl")
    CovMtxECIToEqnx.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(9)) * int(9), (c_double * int(9)) * int(9)]
    CovMtxECIToEqnx.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 640
if _libs["AstroFunc.dll"].has("CovMtxEqnxToECI9x9", "cdecl"):
    CovMtxEqnxToECI9x9 = _libs["AstroFunc.dll"].get("CovMtxEqnxToECI9x9", "cdecl")
    CovMtxEqnxToECI9x9.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(9)) * int(9), (c_double * int(9)) * int(9)]
    CovMtxEqnxToECI9x9.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 649
if _libs["AstroFunc.dll"].has("CovMtxEqnxToUVW9x9", "cdecl"):
    CovMtxEqnxToUVW9x9 = _libs["AstroFunc.dll"].get("CovMtxEqnxToUVW9x9", "cdecl")
    CovMtxEqnxToUVW9x9.argtypes = [c_double * int(3), c_double * int(3), (c_double * int(9)) * int(9), (c_double * int(9)) * int(9)]
    CovMtxEqnxToUVW9x9.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 662
if _libs["AstroFunc.dll"].has("CovMtxUpdate", "cdecl"):
    CovMtxUpdate = _libs["AstroFunc.dll"].get("CovMtxUpdate", "cdecl")
    CovMtxUpdate.argtypes = [c_double, c_double, (c_double * int(9)) * int(9), c_double * int(54), (c_double * int(6)) * int(6)]
    CovMtxUpdate.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 671
if _libs["AstroFunc.dll"].has("AberrationAnnual", "cdecl"):
    AberrationAnnual = _libs["AstroFunc.dll"].get("AberrationAnnual", "cdecl")
    AberrationAnnual.argtypes = [c_double, c_double, c_double, POINTER(c_double), POINTER(c_double)]
    AberrationAnnual.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 682
if _libs["AstroFunc.dll"].has("AberrationDiurnal", "cdecl"):
    AberrationDiurnal = _libs["AstroFunc.dll"].get("AberrationDiurnal", "cdecl")
    AberrationDiurnal.argtypes = [c_double, c_double, c_double, c_double * int(3), POINTER(c_double), POINTER(c_double)]
    AberrationDiurnal.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 690
if _libs["AstroFunc.dll"].has("JplSetParameters", "cdecl"):
    JplSetParameters = _libs["AstroFunc.dll"].get("JplSetParameters", "cdecl")
    JplSetParameters.argtypes = [c_char * int(512), c_double, c_double]
    JplSetParameters.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 697
if _libs["AstroFunc.dll"].has("JplGetParameters", "cdecl"):
    JplGetParameters = _libs["AstroFunc.dll"].get("JplGetParameters", "cdecl")
    JplGetParameters.argtypes = [c_char * int(512), POINTER(c_double), POINTER(c_double)]
    JplGetParameters.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 701
if _libs["AstroFunc.dll"].has("JplReset", "cdecl"):
    JplReset = _libs["AstroFunc.dll"].get("JplReset", "cdecl")
    JplReset.argtypes = []
    JplReset.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 711
if _libs["AstroFunc.dll"].has("JplCompSunMoonVec", "cdecl"):
    JplCompSunMoonVec = _libs["AstroFunc.dll"].get("JplCompSunMoonVec", "cdecl")
    JplCompSunMoonVec.argtypes = [c_double, c_double * int(3), POINTER(c_double), c_double * int(3), POINTER(c_double)]
    JplCompSunMoonVec.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 719
if _libs["AstroFunc.dll"].has("JplCompSunMoonPos", "cdecl"):
    JplCompSunMoonPos = _libs["AstroFunc.dll"].get("JplCompSunMoonPos", "cdecl")
    JplCompSunMoonPos.argtypes = [c_double, c_double * int(3), c_double * int(3)]
    JplCompSunMoonPos.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 723
if _libs["AstroFunc.dll"].has("RemoveJpl", "cdecl"):
    RemoveJpl = _libs["AstroFunc.dll"].get("RemoveJpl", "cdecl")
    RemoveJpl.argtypes = []
    RemoveJpl.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 734
if _libs["AstroFunc.dll"].has("TemeEpochToDate", "cdecl"):
    TemeEpochToDate = _libs["AstroFunc.dll"].get("TemeEpochToDate", "cdecl")
    TemeEpochToDate.argtypes = [c_int, c_double, c_double, c_double * int(3), c_double * int(3), c_double * int(3), c_double * int(3)]
    TemeEpochToDate.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 890
for _lib in _libs.values():
    if not _lib.has("LoadAstroFuncDll", "cdecl"):
        continue
    LoadAstroFuncDll = _lib.get("LoadAstroFuncDll", "cdecl")
    LoadAstroFuncDll.argtypes = []
    LoadAstroFuncDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 891
for _lib in _libs.values():
    if not _lib.has("FreeAstroFuncDll", "cdecl"):
        continue
    FreeAstroFuncDll = _lib.get("FreeAstroFuncDll", "cdecl")
    FreeAstroFuncDll.argtypes = []
    FreeAstroFuncDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 14
try:
    AstroFuncDll = 'AstroFunc.dll'
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 738
try:
    XA_KEP_A = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 739
try:
    XA_KEP_E = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 740
try:
    XA_KEP_INCLI = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 741
try:
    XA_KEP_MA = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 742
try:
    XA_KEP_NODE = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 743
try:
    XA_KEP_OMEGA = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 744
try:
    XA_KEP_SIZE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 748
try:
    XA_CLS_N = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 749
try:
    XA_CLS_E = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 750
try:
    XA_CLS_INCLI = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 751
try:
    XA_CLS_MA = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 752
try:
    XA_CLS_NODE = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 753
try:
    XA_CLS_OMEGA = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 754
try:
    XA_CLS_SIZE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 758
try:
    XA_EQNX_AF = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 759
try:
    XA_EQNX_AG = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 760
try:
    XA_EQNX_CHI = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 761
try:
    XA_EQNX_PSI = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 762
try:
    XA_EQNX_L = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 763
try:
    XA_EQNX_N = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 764
try:
    XA_EQNX_SIZE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 768
try:
    XF_CONV_SGP42SGP = 101
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 773
try:
    XA_TOPO_RA = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 774
try:
    XA_TOPO_DEC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 775
try:
    XA_TOPO_AZ = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 776
try:
    XA_TOPO_EL = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 777
try:
    XA_TOPO_RANGE = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 778
try:
    XA_TOPO_RADOT = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 779
try:
    XA_TOPO_DECDOT = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 780
try:
    XA_TOPO_AZDOT = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 781
try:
    XA_TOPO_ELDOT = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 782
try:
    XA_TOPO_RANGEDOT = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 783
try:
    XA_TOPO_SIZE = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 788
try:
    XA_RAE_RANGE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 789
try:
    XA_RAE_AZ = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 790
try:
    XA_RAE_EL = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 791
try:
    XA_RAE_RANGEDOT = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 792
try:
    XA_RAE_AZDOT = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 793
try:
    XA_RAE_ELDOT = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 794
try:
    XA_RAE_SIZE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 799
try:
    YROFEQNX_OBTIME = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 800
try:
    YROFEQNX_CURR = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 801
try:
    YROFEQNX_2000 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_AstroFuncDll.h: 802
try:
    YROFEQNX_1950 = 3
except:
    pass

# No inserted files

# No prefix-stripping

