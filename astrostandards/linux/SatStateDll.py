r"""Wrapper for new_SatStateDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . --compile-libdir=. -l libsatstate.so ./new_SatStateDll.h -o ./SatStateDll.py

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
_libs["libsatstate.so"] = load_library("libsatstate.so")

# 1 libraries
# End libraries

# No modules

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 25
if _libs["libsatstate.so"].has("SatStateInit", "cdecl"):
    SatStateInit = _libs["libsatstate.so"].get("SatStateInit", "cdecl")
    SatStateInit.argtypes = [c_int64]
    SatStateInit.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 32
if _libs["libsatstate.so"].has("SatStateGetInfo", "cdecl"):
    SatStateGetInfo = _libs["libsatstate.so"].get("SatStateGetInfo", "cdecl")
    SatStateGetInfo.argtypes = [c_char * int(128)]
    SatStateGetInfo.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 42
if _libs["libsatstate.so"].has("SatStateLoadFile", "cdecl"):
    SatStateLoadFile = _libs["libsatstate.so"].get("SatStateLoadFile", "cdecl")
    SatStateLoadFile.argtypes = [c_char * int(512), c_int]
    SatStateLoadFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 56
if _libs["libsatstate.so"].has("SatStateSaveFile", "cdecl"):
    SatStateSaveFile = _libs["libsatstate.so"].get("SatStateSaveFile", "cdecl")
    SatStateSaveFile.argtypes = [c_char * int(512), c_int, c_int, c_int]
    SatStateSaveFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 65
if _libs["libsatstate.so"].has("SatStateRemoveSat", "cdecl"):
    SatStateRemoveSat = _libs["libsatstate.so"].get("SatStateRemoveSat", "cdecl")
    SatStateRemoveSat.argtypes = [c_int64]
    SatStateRemoveSat.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 73
if _libs["libsatstate.so"].has("SatStateRemoveSatAll", "cdecl"):
    SatStateRemoveSatAll = _libs["libsatstate.so"].get("SatStateRemoveSatAll", "cdecl")
    SatStateRemoveSatAll.argtypes = [c_int64]
    SatStateRemoveSatAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 79
if _libs["libsatstate.so"].has("SatStateRemoveAllSats", "cdecl"):
    SatStateRemoveAllSats = _libs["libsatstate.so"].get("SatStateRemoveAllSats", "cdecl")
    SatStateRemoveAllSats.argtypes = []
    SatStateRemoveAllSats.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 83
if _libs["libsatstate.so"].has("SatStateReset", "cdecl"):
    SatStateReset = _libs["libsatstate.so"].get("SatStateReset", "cdecl")
    SatStateReset.argtypes = []
    SatStateReset.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 90
if _libs["libsatstate.so"].has("SatStateGetCount", "cdecl"):
    SatStateGetCount = _libs["libsatstate.so"].get("SatStateGetCount", "cdecl")
    SatStateGetCount.argtypes = []
    SatStateGetCount.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 101
if _libs["libsatstate.so"].has("SatStateGetLoaded", "cdecl"):
    SatStateGetLoaded = _libs["libsatstate.so"].get("SatStateGetLoaded", "cdecl")
    SatStateGetLoaded.argtypes = [c_int, POINTER(c_int64)]
    SatStateGetLoaded.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 111
if _libs["libsatstate.so"].has("SatStateNumToKey", "cdecl"):
    SatStateNumToKey = _libs["libsatstate.so"].get("SatStateNumToKey", "cdecl")
    SatStateNumToKey.argtypes = [c_int]
    SatStateNumToKey.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 142
if _libs["libsatstate.so"].has("SatStateGetSatDataAll", "cdecl"):
    SatStateGetSatDataAll = _libs["libsatstate.so"].get("SatStateGetSatDataAll", "cdecl")
    SatStateGetSatDataAll.argtypes = [c_int64, POINTER(c_int), c_char * int(8), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    SatStateGetSatDataAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 150
if _libs["libsatstate.so"].has("SatStateGetSatDataField", "cdecl"):
    SatStateGetSatDataField = _libs["libsatstate.so"].get("SatStateGetSatDataField", "cdecl")
    SatStateGetSatDataField.argtypes = [c_int64, c_int, c_char * int(512)]
    SatStateGetSatDataField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 156
if _libs["libsatstate.so"].has("SatStateInitSat", "cdecl"):
    SatStateInitSat = _libs["libsatstate.so"].get("SatStateInitSat", "cdecl")
    SatStateInitSat.argtypes = [c_int64]
    SatStateInitSat.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 169
if _libs["libsatstate.so"].has("SatStateMse", "cdecl"):
    SatStateMse = _libs["libsatstate.so"].get("SatStateMse", "cdecl")
    SatStateMse.argtypes = [c_int64, c_double, POINTER(c_double), POINTER(c_int), c_double * int(3), c_double * int(3), c_double * int(3)]
    SatStateMse.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 182
if _libs["libsatstate.so"].has("SatStateDs50UTC", "cdecl"):
    SatStateDs50UTC = _libs["libsatstate.so"].get("SatStateDs50UTC", "cdecl")
    SatStateDs50UTC.argtypes = [c_int64, c_double, POINTER(c_double), POINTER(c_int), c_double * int(3), c_double * int(3), c_double * int(3)]
    SatStateDs50UTC.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 192
if _libs["libsatstate.so"].has("SatStateGetPropOut", "cdecl"):
    SatStateGetPropOut = _libs["libsatstate.so"].get("SatStateGetPropOut", "cdecl")
    SatStateGetPropOut.argtypes = [c_int64, c_int, c_double * int(128)]
    SatStateGetPropOut.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 205
if _libs["libsatstate.so"].has("SatStateEphCom", "cdecl"):
    SatStateEphCom = _libs["libsatstate.so"].get("SatStateEphCom", "cdecl")
    SatStateEphCom.argtypes = [c_int64, c_int64, c_double, c_int, c_double * int(100)]
    SatStateEphCom.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 217
if _libs["libsatstate.so"].has("SatStateEphCom_OS", "cdecl"):
    SatStateEphCom_OS = _libs["libsatstate.so"].get("SatStateEphCom_OS", "cdecl")
    SatStateEphCom_OS.argtypes = [c_double * int(6), c_double * int(6), c_double, c_int, c_double * int(100)]
    SatStateEphCom_OS.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 224
if _libs["libsatstate.so"].has("SatStateHasCovMtx", "cdecl"):
    SatStateHasCovMtx = _libs["libsatstate.so"].get("SatStateHasCovMtx", "cdecl")
    SatStateHasCovMtx.argtypes = [c_int64]
    SatStateHasCovMtx.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 232
if _libs["libsatstate.so"].has("SatStateGetCovUVW", "cdecl"):
    SatStateGetCovUVW = _libs["libsatstate.so"].get("SatStateGetCovUVW", "cdecl")
    SatStateGetCovUVW.argtypes = [c_int64, c_double, (c_double * int(6)) * int(6)]
    SatStateGetCovUVW.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 244
if _libs["libsatstate.so"].has("SatStateGenEphFile", "cdecl"):
    SatStateGenEphFile = _libs["libsatstate.so"].get("SatStateGenEphFile", "cdecl")
    SatStateGenEphFile.argtypes = [c_int64, c_double, c_double, c_double, c_char * int(512), c_int]
    SatStateGenEphFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 251
if _libs["libsatstate.so"].has("GetNodalCrossingPriorToTime", "cdecl"):
    GetNodalCrossingPriorToTime = _libs["libsatstate.so"].get("GetNodalCrossingPriorToTime", "cdecl")
    GetNodalCrossingPriorToTime.argtypes = [c_int64, c_double]
    GetNodalCrossingPriorToTime.restype = c_double

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 259
if _libs["libsatstate.so"].has("GetGobsParams", "cdecl"):
    GetGobsParams = _libs["libsatstate.so"].get("GetGobsParams", "cdecl")
    GetGobsParams.argtypes = [c_int64, c_double, c_double * int(32), POINTER(c_int)]
    GetGobsParams.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 269
if _libs["libsatstate.so"].has("GobsCom", "cdecl"):
    GobsCom = _libs["libsatstate.so"].get("GobsCom", "cdecl")
    GobsCom.argtypes = [c_int64, c_int64, c_double, c_double * int(16), c_double * int(32)]
    GobsCom.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 277
if _libs["libsatstate.so"].has("GobsComArr", "cdecl"):
    GobsComArr = _libs["libsatstate.so"].get("GobsComArr", "cdecl")
    GobsComArr.argtypes = [c_double * int(32), c_double * int(32), c_double * int(16), c_double * int(16)]
    GobsComArr.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 449
for _lib in _libs.values():
    if not _lib.has("LoadSatStateDll", "cdecl"):
        continue
    LoadSatStateDll = _lib.get("LoadSatStateDll", "cdecl")
    LoadSatStateDll.argtypes = []
    LoadSatStateDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 450
for _lib in _libs.values():
    if not _lib.has("FreeSatStateDll", "cdecl"):
        continue
    FreeSatStateDll = _lib.get("FreeSatStateDll", "cdecl")
    FreeSatStateDll.argtypes = []
    FreeSatStateDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 14
try:
    SatStateDll = 'libsatstate.so'
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 281
try:
    XF_SATFIELD_EPOCHUTC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 282
try:
    XF_SATFIELD_MNANOM = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 283
try:
    XF_SATFIELD_NODE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 284
try:
    XF_SATFIELD_OMEGA = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 285
try:
    XF_SATFIELD_PERIOD = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 286
try:
    XF_SATFIELD_ECCEN = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 287
try:
    XF_SATFIELD_INCLI = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 288
try:
    XF_SATFIELD_MNMOTION = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 289
try:
    XF_SATFIELD_BFIELD = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 290
try:
    XF_SATFIELD_PERIGEEHT = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 291
try:
    XF_SATFIELD_APOGEEHT = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 292
try:
    XF_SATFIELD_PERIGEE = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 293
try:
    XF_SATFIELD_APOGEE = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 294
try:
    XF_SATFIELD_A = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 295
try:
    XF_SATFIELD_NDOT = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 296
try:
    XF_SATFIELD_SATCAT = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 297
try:
    XF_SATFIELD_HTM3 = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 298
try:
    XF_SATFIELD_CMOFFSET = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 299
try:
    XF_SATFIELD_N2DOT = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 300
try:
    XF_SATFIELD_NODEDOT = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 301
try:
    XF_SATFIELD_ERRORTIME = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 302
try:
    XF_SATFIELD_MU = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 309
try:
    XA_DELTA_POS = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 310
try:
    XA_DELTA_TIME = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 311
try:
    XA_DELTA_PRADIAL = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 312
try:
    XA_DELTA_PINTRCK = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 313
try:
    XA_DELTA_PCRSSTRCK = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 314
try:
    XA_DELTA_VEL = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 315
try:
    XA_DELTA_VRADIAL = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 316
try:
    XA_DELTA_VINTRCK = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 317
try:
    XA_DELTA_VCRSSTRCK = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 318
try:
    XA_DELTA_BETA = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 319
try:
    XA_DELTA_HEIGHT = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 320
try:
    XA_DELTA_ANGMOM = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 321
try:
    XA_DELTA_MHLNBS_UVW = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 322
try:
    XA_DELTA_MHLNBS_HTB = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 324
try:
    XA_DELTA_SIZE = 100
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 328
try:
    XF_SAT_NUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 329
try:
    XF_SAT_NAME = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 330
try:
    XF_SAT_ELTTYPE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 331
try:
    XF_SAT_EPHTYPE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 332
try:
    XF_SAT_REVNUM = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 333
try:
    XF_SAT_EPOCH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 334
try:
    XF_SAT_BFIELD = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 335
try:
    XF_SAT_ELSETNUM = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 336
try:
    XF_SAT_INCLI = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 337
try:
    XF_SAT_NODE = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 338
try:
    XF_SAT_ECCEN = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 339
try:
    XF_SAT_OMEGA = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 340
try:
    XF_SAT_MNANOM = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 341
try:
    XF_SAT_MNMOTN = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 342
try:
    XF_SAT_PERIOD = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 343
try:
    XF_SAT_PERIGEEHT = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 344
try:
    XF_SAT_APOGEEHT = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 345
try:
    XF_SAT_PERIGEE = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 346
try:
    XF_SAT_APOGEE = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 347
try:
    XF_SAT_A = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 352
try:
    XF_TASK_CTRLONLY = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 353
try:
    XF_TASK_SATONLY = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 354
try:
    XF_TASK_BOTH = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 359
try:
    EPHFILETYPE_ITC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 360
try:
    EPHFILETYPE_ITC_WOCOV = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 365
try:
    XA_GOBS_SATNUM = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 366
try:
    XA_GOBS_LONE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 367
try:
    XA_GOBS_DRIFT = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 368
try:
    XA_GOBS_RELENERGY = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 369
try:
    XA_GOBS_WX = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 370
try:
    XA_GOBS_WY = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 371
try:
    XA_GOBS_WZ = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 372
try:
    XA_GOBS_ABARX = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 373
try:
    XA_GOBS_ABARY = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 374
try:
    XA_GOBS_ABARZ = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 375
try:
    XA_GOBS_AGOM = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 376
try:
    XA_GOBS_TROUGH = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 378
try:
    XA_GOBS_SIZE = 32
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 383
try:
    XA_GOBS_LIM_TROUGH = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 384
try:
    XA_GOBS_LIM_PCP = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 385
try:
    XA_GOBS_LIM_PCS = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 386
try:
    XA_GOBS_LIM_ACTIVEP = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 387
try:
    XA_GOBS_LIM_ACTIVES = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 388
try:
    XA_GOBS_LIM_LONGMIN = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 389
try:
    XA_GOBS_LIM_LONGMAX = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 390
try:
    XA_GOBS_LIM_AGOMMIN = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 391
try:
    XA_GOBS_LIM_AGOMMAX = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 393
try:
    XA_GOBS_LIM_SIZE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 398
try:
    XA_GOBS_DELTA_PRIMESAT = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 399
try:
    XA_GOBS_DELTA_SECONDARYSAT = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 400
try:
    XA_GOBS_DELTA_ASTAT = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 401
try:
    XA_GOBS_DELTA_DOP = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 402
try:
    XA_GOBS_DELTA_DABAR = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 403
try:
    XA_GOBS_DELTA_DRELENERGY = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 404
try:
    XA_GOBS_DELTA_LONGP = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 405
try:
    XA_GOBS_DELTA_LONGMIN = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 406
try:
    XA_GOBS_DELTA_LONGMAX = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 407
try:
    XA_GOBS_DELTA_TROUGH = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 408
try:
    XA_GOBS_DELTA_PLANE = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 409
try:
    XA_GOBS_DELTA_SHAPE = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 410
try:
    XA_GOBS_DELTA_ENERGY = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 411
try:
    XA_GOBS_DELTA_LONG = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 412
try:
    XA_GOBS_DELTA_AGOM = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SatStateDll.h: 414
try:
    XA_GOBS_DELTA_SIZE = 16
except:
    pass

# No inserted files

# No prefix-stripping

