r"""Wrapper for new_ObsDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . --compile-libdir=. -l libobs.so ./new_ObsDll.h -o ./ObsDll.py

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
_libs["libobs.so"] = load_library("libobs.so")

# 1 libraries
# End libraries

# No modules

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 22
if _libs["libobs.so"].has("ObsInit", "cdecl"):
    ObsInit = _libs["libobs.so"].get("ObsInit", "cdecl")
    ObsInit.argtypes = [c_int64]
    ObsInit.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 28
if _libs["libobs.so"].has("ObsGetInfo", "cdecl"):
    ObsGetInfo = _libs["libobs.so"].get("ObsGetInfo", "cdecl")
    ObsGetInfo.argtypes = [c_char * int(128)]
    ObsGetInfo.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 33
if _libs["libobs.so"].has("ObsSetTTYYear", "cdecl"):
    ObsSetTTYYear = _libs["libobs.so"].get("ObsSetTTYYear", "cdecl")
    ObsSetTTYYear.argtypes = [c_int]
    ObsSetTTYYear.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 39
if _libs["libobs.so"].has("ObsLoadFile", "cdecl"):
    ObsLoadFile = _libs["libobs.so"].get("ObsLoadFile", "cdecl")
    ObsLoadFile.argtypes = [c_char * int(512)]
    ObsLoadFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 47
if _libs["libobs.so"].has("ObsSaveFile", "cdecl"):
    ObsSaveFile = _libs["libobs.so"].get("ObsSaveFile", "cdecl")
    ObsSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    ObsSaveFile.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 53
if _libs["libobs.so"].has("ObsRemove", "cdecl"):
    ObsRemove = _libs["libobs.so"].get("ObsRemove", "cdecl")
    ObsRemove.argtypes = [c_int64]
    ObsRemove.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 58
if _libs["libobs.so"].has("ObsRemoveAll", "cdecl"):
    ObsRemoveAll = _libs["libobs.so"].get("ObsRemoveAll", "cdecl")
    ObsRemoveAll.argtypes = []
    ObsRemoveAll.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 63
if _libs["libobs.so"].has("ObsGetCount", "cdecl"):
    ObsGetCount = _libs["libobs.so"].get("ObsGetCount", "cdecl")
    ObsGetCount.argtypes = []
    ObsGetCount.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 79
if _libs["libobs.so"].has("ObsGetLoaded", "cdecl"):
    ObsGetLoaded = _libs["libobs.so"].get("ObsGetLoaded", "cdecl")
    ObsGetLoaded.argtypes = [c_int, POINTER(c_int64)]
    ObsGetLoaded.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 85
if _libs["libobs.so"].has("ObsLoadCard", "cdecl"):
    ObsLoadCard = _libs["libobs.so"].get("ObsLoadCard", "cdecl")
    ObsLoadCard.argtypes = [c_char * int(512)]
    ObsLoadCard.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 92
if _libs["libobs.so"].has("ObsLoadTwoCards", "cdecl"):
    ObsLoadTwoCards = _libs["libobs.so"].get("ObsLoadTwoCards", "cdecl")
    ObsLoadTwoCards.argtypes = [c_char * int(512), c_char * int(512)]
    ObsLoadTwoCards.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 98
if _libs["libobs.so"].has("ObsAddFrB3Card", "cdecl"):
    ObsAddFrB3Card = _libs["libobs.so"].get("ObsAddFrB3Card", "cdecl")
    ObsAddFrB3Card.argtypes = [c_char * int(512)]
    ObsAddFrB3Card.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 104
if _libs["libobs.so"].has("ObsAddFrB3CardML", "cdecl"):
    ObsAddFrB3CardML = _libs["libobs.so"].get("ObsAddFrB3CardML", "cdecl")
    ObsAddFrB3CardML.argtypes = [c_char * int(512), POINTER(c_int64)]
    ObsAddFrB3CardML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 111
if _libs["libobs.so"].has("ObsB3ToCsv", "cdecl"):
    ObsB3ToCsv = _libs["libobs.so"].get("ObsB3ToCsv", "cdecl")
    ObsB3ToCsv.argtypes = [c_char * int(512), c_char * int(512)]
    ObsB3ToCsv.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 119
if _libs["libobs.so"].has("ObsCsvToB3", "cdecl"):
    ObsCsvToB3 = _libs["libobs.so"].get("ObsCsvToB3", "cdecl")
    ObsCsvToB3.argtypes = [c_char * int(512), c_int, c_char * int(512)]
    ObsCsvToB3.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 126
if _libs["libobs.so"].has("ObsAddFrTTYCards", "cdecl"):
    ObsAddFrTTYCards = _libs["libobs.so"].get("ObsAddFrTTYCards", "cdecl")
    ObsAddFrTTYCards.argtypes = [c_char * int(512), c_char * int(512)]
    ObsAddFrTTYCards.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 133
if _libs["libobs.so"].has("ObsAddFrTTYCardsML", "cdecl"):
    ObsAddFrTTYCardsML = _libs["libobs.so"].get("ObsAddFrTTYCardsML", "cdecl")
    ObsAddFrTTYCardsML.argtypes = [c_char * int(512), c_char * int(512), POINTER(c_int64)]
    ObsAddFrTTYCardsML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 141
if _libs["libobs.so"].has("ObsTTYToCsv", "cdecl"):
    ObsTTYToCsv = _libs["libobs.so"].get("ObsTTYToCsv", "cdecl")
    ObsTTYToCsv.argtypes = [c_char * int(512), c_char * int(512), c_char * int(512)]
    ObsTTYToCsv.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 150
if _libs["libobs.so"].has("ObsCsvToTTY", "cdecl"):
    ObsCsvToTTY = _libs["libobs.so"].get("ObsCsvToTTY", "cdecl")
    ObsCsvToTTY.argtypes = [c_char * int(512), c_int, c_char * int(512), c_char * int(512)]
    ObsCsvToTTY.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 156
if _libs["libobs.so"].has("ObsAddFrCsv", "cdecl"):
    ObsAddFrCsv = _libs["libobs.so"].get("ObsAddFrCsv", "cdecl")
    ObsAddFrCsv.argtypes = [c_char * int(512)]
    ObsAddFrCsv.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 162
if _libs["libobs.so"].has("ObsAddFrCsvML", "cdecl"):
    ObsAddFrCsvML = _libs["libobs.so"].get("ObsAddFrCsvML", "cdecl")
    ObsAddFrCsvML.argtypes = [c_char * int(512), POINTER(c_int64)]
    ObsAddFrCsvML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 186
if _libs["libobs.so"].has("ObsAddFrFields", "cdecl"):
    ObsAddFrFields = _libs["libobs.so"].get("ObsAddFrFields", "cdecl")
    ObsAddFrFields.argtypes = [c_char, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_int, c_int, c_int, c_int, c_double * int(3), c_double * int(3), c_double * int(128)]
    ObsAddFrFields.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 210
if _libs["libobs.so"].has("ObsAddFrFieldsML", "cdecl"):
    ObsAddFrFieldsML = _libs["libobs.so"].get("ObsAddFrFieldsML", "cdecl")
    ObsAddFrFieldsML.argtypes = [c_char, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_int, c_int, c_int, c_int, c_double * int(3), c_double * int(3), c_double * int(128), POINTER(c_int64)]
    ObsAddFrFieldsML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 216
if _libs["libobs.so"].has("ObsAddFrArray", "cdecl"):
    ObsAddFrArray = _libs["libobs.so"].get("ObsAddFrArray", "cdecl")
    ObsAddFrArray.argtypes = [c_double * int(64)]
    ObsAddFrArray.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 222
if _libs["libobs.so"].has("ObsAddFrArrayML", "cdecl"):
    ObsAddFrArrayML = _libs["libobs.so"].get("ObsAddFrArrayML", "cdecl")
    ObsAddFrArrayML.argtypes = [c_double * int(64), POINTER(c_int64)]
    ObsAddFrArrayML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 247
if _libs["libobs.so"].has("ObsGetAllFields", "cdecl"):
    ObsGetAllFields = _libs["libobs.so"].get("ObsGetAllFields", "cdecl")
    ObsGetAllFields.argtypes = [c_int64, String, POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), String, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), c_double * int(3), c_double * int(3), c_double * int(128)]
    ObsGetAllFields.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 255
if _libs["libobs.so"].has("ObsDataToArray", "cdecl"):
    ObsDataToArray = _libs["libobs.so"].get("ObsDataToArray", "cdecl")
    ObsDataToArray.argtypes = [c_int64, c_double * int(64)]
    ObsDataToArray.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 277
if _libs["libobs.so"].has("ObsUpdateFrFields", "cdecl"):
    ObsUpdateFrFields = _libs["libobs.so"].get("ObsUpdateFrFields", "cdecl")
    ObsUpdateFrFields.argtypes = [c_int64, c_char, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_int, c_int, c_int, c_int, c_double * int(3), c_double * int(3), c_double * int(128)]
    ObsUpdateFrFields.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 285
if _libs["libobs.so"].has("ObsGetField", "cdecl"):
    ObsGetField = _libs["libobs.so"].get("ObsGetField", "cdecl")
    ObsGetField.argtypes = [c_int64, c_int, c_char * int(512)]
    ObsGetField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 295
if _libs["libobs.so"].has("ObsSetField", "cdecl"):
    ObsSetField = _libs["libobs.so"].get("ObsSetField", "cdecl")
    ObsSetField.argtypes = [c_int64, c_int, c_char * int(512)]
    ObsSetField.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 302
if _libs["libobs.so"].has("ObsGetB3Card", "cdecl"):
    ObsGetB3Card = _libs["libobs.so"].get("ObsGetB3Card", "cdecl")
    ObsGetB3Card.argtypes = [c_int64, c_char * int(512)]
    ObsGetB3Card.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 310
if _libs["libobs.so"].has("ObsGetTTYCard", "cdecl"):
    ObsGetTTYCard = _libs["libobs.so"].get("ObsGetTTYCard", "cdecl")
    ObsGetTTYCard.argtypes = [c_int64, c_char * int(512), c_char * int(512)]
    ObsGetTTYCard.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 317
if _libs["libobs.so"].has("ObsGetCsv", "cdecl"):
    ObsGetCsv = _libs["libobs.so"].get("ObsGetCsv", "cdecl")
    ObsGetCsv.argtypes = [c_int64, c_char * int(512)]
    ObsGetCsv.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 339
if _libs["libobs.so"].has("ObsFieldsToB3Card", "cdecl"):
    ObsFieldsToB3Card = _libs["libobs.so"].get("ObsFieldsToB3Card", "cdecl")
    ObsFieldsToB3Card.argtypes = [c_char, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_int, c_int, c_int, c_int, c_double * int(3), c_char * int(512)]
    ObsFieldsToB3Card.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 361
if _libs["libobs.so"].has("ObsFieldsToCsv", "cdecl"):
    ObsFieldsToCsv = _libs["libobs.so"].get("ObsFieldsToCsv", "cdecl")
    ObsFieldsToCsv.argtypes = [c_char, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_int, c_int, c_int, c_int, c_double * int(3), c_char * int(512)]
    ObsFieldsToCsv.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 380
if _libs["libobs.so"].has("ObsFieldsToTTYCard", "cdecl"):
    ObsFieldsToTTYCard = _libs["libobs.so"].get("ObsFieldsToTTYCard", "cdecl")
    ObsFieldsToTTYCard.argtypes = [c_char, c_int, c_int, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_double, c_char, c_double * int(3), c_char * int(512), c_char * int(512)]
    ObsFieldsToTTYCard.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 388
if _libs["libobs.so"].has("ObsFieldsToObsKey", "cdecl"):
    ObsFieldsToObsKey = _libs["libobs.so"].get("ObsFieldsToObsKey", "cdecl")
    ObsFieldsToObsKey.argtypes = [c_int, c_int, c_double]
    ObsFieldsToObsKey.restype = c_int64

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 396
if _libs["libobs.so"].has("ObsFieldsToObsKeyML", "cdecl"):
    ObsFieldsToObsKeyML = _libs["libobs.so"].get("ObsFieldsToObsKeyML", "cdecl")
    ObsFieldsToObsKeyML.argtypes = [c_int, c_int, c_double, POINTER(c_int64)]
    ObsFieldsToObsKeyML.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 419
if _libs["libobs.so"].has("ObsB3Parse", "cdecl"):
    ObsB3Parse = _libs["libobs.so"].get("ObsB3Parse", "cdecl")
    ObsB3Parse.argtypes = [c_char * int(512), String, POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_double), String, POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), c_double * int(3)]
    ObsB3Parse.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 427
if _libs["libobs.so"].has("ObsParse", "cdecl"):
    ObsParse = _libs["libobs.so"].get("ObsParse", "cdecl")
    ObsParse.argtypes = [c_char * int(512), c_char * int(512), c_double * int(64)]
    ObsParse.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 435
if _libs["libobs.so"].has("ObsLoadFileGID", "cdecl"):
    ObsLoadFileGID = _libs["libobs.so"].get("ObsLoadFileGID", "cdecl")
    ObsLoadFileGID.argtypes = [c_char * int(512), c_int]
    ObsLoadFileGID.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 444
if _libs["libobs.so"].has("ObsSaveFileGID", "cdecl"):
    ObsSaveFileGID = _libs["libobs.so"].get("ObsSaveFileGID", "cdecl")
    ObsSaveFileGID.argtypes = [c_char * int(512), c_int, c_int, c_int]
    ObsSaveFileGID.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 450
if _libs["libobs.so"].has("ObsRemoveGID", "cdecl"):
    ObsRemoveGID = _libs["libobs.so"].get("ObsRemoveGID", "cdecl")
    ObsRemoveGID.argtypes = [c_int]
    ObsRemoveGID.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 456
if _libs["libobs.so"].has("ObsGetCountGID", "cdecl"):
    ObsGetCountGID = _libs["libobs.so"].get("ObsGetCountGID", "cdecl")
    ObsGetCountGID.argtypes = [c_int]
    ObsGetCountGID.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 473
if _libs["libobs.so"].has("ObsGetLoadedGID", "cdecl"):
    ObsGetLoadedGID = _libs["libobs.so"].get("ObsGetLoadedGID", "cdecl")
    ObsGetLoadedGID.argtypes = [c_int, c_int, POINTER(c_int64)]
    ObsGetLoadedGID.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 479
if _libs["libobs.so"].has("ObsTypeCToI", "cdecl"):
    ObsTypeCToI = _libs["libobs.so"].get("ObsTypeCToI", "cdecl")
    ObsTypeCToI.argtypes = [c_char]
    ObsTypeCToI.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 485
if _libs["libobs.so"].has("ObsTypeIToC", "cdecl"):
    ObsTypeIToC = _libs["libobs.so"].get("ObsTypeIToC", "cdecl")
    ObsTypeIToC.argtypes = [c_int]
    ObsTypeIToC.restype = c_char

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 489
if _libs["libobs.so"].has("ObsResetSelObs", "cdecl"):
    ObsResetSelObs = _libs["libobs.so"].get("ObsResetSelObs", "cdecl")
    ObsResetSelObs.argtypes = []
    ObsResetSelObs.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 521
if _libs["libobs.so"].has("ObsGetStates", "cdecl"):
    ObsGetStates = _libs["libobs.so"].get("ObsGetStates", "cdecl")
    ObsGetStates.argtypes = [c_int64, c_double, c_double * int(64)]
    ObsGetStates.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 529
if _libs["libobs.so"].has("ObsDataToStates", "cdecl"):
    ObsDataToStates = _libs["libobs.so"].get("ObsDataToStates", "cdecl")
    ObsDataToStates.argtypes = [c_double * int(64), c_double * int(64)]
    ObsDataToStates.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 538
if _libs["libobs.so"].has("ObsArrToLines", "cdecl"):
    ObsArrToLines = _libs["libobs.so"].get("ObsArrToLines", "cdecl")
    ObsArrToLines.argtypes = [c_double * int(64), c_int, c_char * int(512), c_char * int(512)]
    ObsArrToLines.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 546
if _libs["libobs.so"].has("SetObsKeyMode", "cdecl"):
    SetObsKeyMode = _libs["libobs.so"].get("SetObsKeyMode", "cdecl")
    SetObsKeyMode.argtypes = [c_int]
    SetObsKeyMode.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 551
if _libs["libobs.so"].has("GetObsKeyMode", "cdecl"):
    GetObsKeyMode = _libs["libobs.so"].get("GetObsKeyMode", "cdecl")
    GetObsKeyMode.argtypes = []
    GetObsKeyMode.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 557
if _libs["libobs.so"].has("SatNumFrObsKey", "cdecl"):
    SatNumFrObsKey = _libs["libobs.so"].get("SatNumFrObsKey", "cdecl")
    SatNumFrObsKey.argtypes = [c_int64]
    SatNumFrObsKey.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 563
if _libs["libobs.so"].has("SenNumFrObsKey", "cdecl"):
    SenNumFrObsKey = _libs["libobs.so"].get("SenNumFrObsKey", "cdecl")
    SenNumFrObsKey.argtypes = [c_int64]
    SenNumFrObsKey.restype = c_int

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 571
if _libs["libobs.so"].has("ObsGetSelected", "cdecl"):
    ObsGetSelected = _libs["libobs.so"].get("ObsGetSelected", "cdecl")
    ObsGetSelected.argtypes = [c_double * int(128), c_int, POINTER(c_int), POINTER(c_int64)]
    ObsGetSelected.restype = None

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 990
for _lib in _libs.values():
    if not _lib.has("LoadObsDll", "cdecl"):
        continue
    LoadObsDll = _lib.get("LoadObsDll", "cdecl")
    LoadObsDll.argtypes = []
    LoadObsDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 991
for _lib in _libs.values():
    if not _lib.has("FreeObsDll", "cdecl"):
        continue
    FreeObsDll = _lib.get("FreeObsDll", "cdecl")
    FreeObsDll.argtypes = []
    FreeObsDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 14
try:
    ObsDll = 'libobs.so'
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 575
try:
    EQUINOX_OBSTIME = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 576
try:
    EQUINOX_OBSYEAR = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 577
try:
    EQUINOX_J2K = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 578
try:
    EQUINOX_B1950 = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 592
try:
    SORT_TIMESENTYPEEL = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 593
try:
    SORT_TIMEEL = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 594
try:
    SORT_TIMESENTYPEELSAT = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 595
try:
    SORT_SENSATTIMEEL = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 596
try:
    SORT_SENTIMEEL = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 597
try:
    SORT_SENSATTYPETIMEEL = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 598
try:
    SORT_SATTIMESENTYPEEL = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 599
try:
    SORT_ORDERASREAD = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 600
try:
    SORT_SATSENTIME = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 605
try:
    OBSFORM_B3 = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 606
try:
    OBSFORM_TTY = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 607
try:
    OBSFORM_CSV = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 608
try:
    OBSFORM_RF = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 616
try:
    OBS_KEYMODE_NODUP = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 617
try:
    OBS_KEYMODE_DMA = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 624
try:
    XF_OBS_SECCLASS = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 625
try:
    XF_OBS_SATNUM = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 626
try:
    XF_OBS_SENNUM = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 627
try:
    XF_OBS_DS50UTC = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 628
try:
    XF_OBS_ELEVATION = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 629
try:
    XF_OBS_DECLINATION = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 630
try:
    XF_OBS_AZIMUTH = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 631
try:
    XF_OBS_RA = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 632
try:
    XF_OBS_RANGE = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 633
try:
    XF_OBS_RANGERATE = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 634
try:
    XF_OBS_ELRATE = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 635
try:
    XF_OBS_AZRATE = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 636
try:
    XF_OBS_RANGEACCEL = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 637
try:
    XF_OBS_OBSTYPE = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 638
try:
    XF_OBS_TRACKIND = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 639
try:
    XF_OBS_ASTAT = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 640
try:
    XF_OBS_SITETAG = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 641
try:
    XF_OBS_SPADOCTAG = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 642
try:
    XF_OBS_POSE = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 643
try:
    XF_OBS_POSF = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 644
try:
    XF_OBS_POSG = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 645
try:
    XF_OBS_POSX = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 646
try:
    XF_OBS_POSY = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 647
try:
    XF_OBS_POSZ = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 649
try:
    XF_OBS_RCS_PP = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 650
try:
    XF_OBS_RCS_OP = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 651
try:
    XF_OBS_RCS_PPS = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 652
try:
    XF_OBS_RCS_OPS = 28
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 653
try:
    XF_OBS_SNR = 29
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 654
try:
    XF_OBS_BORE_AZ = 30
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 655
try:
    XF_OBS_BORE_EL = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 656
try:
    XF_OBS_VISMAG = 32
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 657
try:
    XF_OBS_VISMAG_NORM = 33
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 658
try:
    XF_OBS_SOL_PHASE = 34
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 659
try:
    XF_OBS_FRAME = 35
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 660
try:
    XF_OBS_ABERRATION = 36
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 661
try:
    XF_OBS_ASTAT_METHOD = 37
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 665
try:
    XA_OBS_SECCLASS = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 666
try:
    XA_OBS_SATNUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 667
try:
    XA_OBS_SENNUM = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 668
try:
    XA_OBS_DS50UTC = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 669
try:
    XA_OBS_OBSTYPE = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 672
try:
    XA_OBS_ELORDEC = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 673
try:
    XA_OBS_AZORRA = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 674
try:
    XA_OBS_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 675
try:
    XA_OBS_RANGERATE = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 676
try:
    XA_OBS_ELRATE = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 677
try:
    XA_OBS_AZRATE = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 678
try:
    XA_OBS_RANGEACCEL = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 679
try:
    XA_OBS_TRACKIND = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 680
try:
    XA_OBS_ASTAT = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 681
try:
    XA_OBS_SITETAG = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 682
try:
    XA_OBS_SPADOCTAG = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 683
try:
    XA_OBS_POSX = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 684
try:
    XA_OBS_POSY = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 685
try:
    XA_OBS_POSZ = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 686
try:
    XA_OBS_VELX = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 687
try:
    XA_OBS_VELY = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 688
try:
    XA_OBS_VELZ = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 689
try:
    XA_OBS_YROFEQNX = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 690
try:
    XA_OBS_ABERRATION = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 692
try:
    XA_OBS_AZORRABIAS = 33
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 693
try:
    XA_OBS_ELORDECBIAS = 34
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 694
try:
    XA_OBS_RGBIAS = 35
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 695
try:
    XA_OBS_RRBIAS = 36
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 696
try:
    XA_OBS_TIMEBIAS = 37
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 697
try:
    XA_OBS_RAZORRABIAS = 38
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 698
try:
    XA_OBS_RELORDECBIAS = 39
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 700
try:
    XA_OBS_SIGMATYPE = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 701
try:
    XA_OBS_SIGMAEL1 = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 702
try:
    XA_OBS_SIGMAEL2 = 42
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 703
try:
    XA_OBS_SIGMAEL3 = 43
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 704
try:
    XA_OBS_SIGMAEL4 = 44
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 705
try:
    XA_OBS_SIGMAEL5 = 45
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 706
try:
    XA_OBS_SIGMAEL6 = 46
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 707
try:
    XA_OBS_SIGMAEL7 = 47
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 708
try:
    XA_OBS_SIGMAEL8 = 48
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 709
try:
    XA_OBS_SIGMAEL9 = 49
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 710
try:
    XA_OBS_SIGMAEL10 = 50
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 711
try:
    XA_OBS_SIGMAEL11 = 51
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 712
try:
    XA_OBS_SIGMAEL12 = 52
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 713
try:
    XA_OBS_SIGMAEL13 = 53
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 714
try:
    XA_OBS_SIGMAEL14 = 54
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 715
try:
    XA_OBS_SIGMAEL15 = 55
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 716
try:
    XA_OBS_SIGMAEL16 = 56
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 717
try:
    XA_OBS_SIGMAEL17 = 57
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 718
try:
    XA_OBS_SIGMAEL18 = 58
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 719
try:
    XA_OBS_SIGMAEL19 = 59
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 720
try:
    XA_OBS_SIGMAEL20 = 60
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 721
try:
    XA_OBS_SIGMAEL21 = 61
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 723
try:
    XA_OBS_SIZE = 64
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 727
try:
    XA_OTCSV_SECCLASS = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 728
try:
    XA_OTCSV_SATNUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 729
try:
    XA_OTCSV_SENNUM = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 730
try:
    XA_OTCSV_DS50UTC = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 731
try:
    XA_OTCSV_ELORDEC = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 732
try:
    XA_OTCSV_AZORRA = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 733
try:
    XA_OTCSV_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 734
try:
    XA_OTCSV_RANGERATE = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 735
try:
    XA_OTCSV_ELRATE = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 736
try:
    XA_OTCSV_AZRATE = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 737
try:
    XA_OTCSV_RANGEACCEL = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 738
try:
    XA_OTCSV_OBSTYPE = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 739
try:
    XA_OTCSV_TRACKIND = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 740
try:
    XA_OTCSV_ASTAT = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 741
try:
    XA_OTCSV_SITETAG = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 742
try:
    XA_OTCSV_SPADOCTAG = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 743
try:
    XA_OTCSV_POSX = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 744
try:
    XA_OTCSV_POSY = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 745
try:
    XA_OTCSV_POSZ = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 746
try:
    XA_OTCSV_VELX = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 747
try:
    XA_OTCSV_VELY = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 748
try:
    XA_OTCSV_VELZ = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 749
try:
    XA_OTCSV_YROFEQNX = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 751
try:
    XA_OTCSV_RCS_PP = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 752
try:
    XA_OTCSV_RCS_OP = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 753
try:
    XA_OTCSV_RCS_PPS = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 754
try:
    XA_OTCSV_RCS_OPS = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 755
try:
    XA_OTCSV_SNR = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 756
try:
    XA_OTCSV_BORE_AZ = 28
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 757
try:
    XA_OTCSV_BORE_EL = 29
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 758
try:
    XA_OTCSV_VISMAG = 30
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 759
try:
    XA_OTCSV_VISMAG_NORM = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 760
try:
    XA_OTCSV_SOL_PHASE = 32
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 761
try:
    XA_OTCSV_FRAME = 33
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 762
try:
    XA_OTCSV_ABERRATION = 34
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 763
try:
    XA_OTCSV_ASTAT_METHOD = 35
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 765
try:
    XA_OTCSV_SIGMATYPE = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 766
try:
    XA_OTCSV_SIGMAEL1 = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 767
try:
    XA_OTCSV_SIGMAEL2 = 42
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 768
try:
    XA_OTCSV_SIGMAEL3 = 43
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 769
try:
    XA_OTCSV_SIGMAEL4 = 44
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 770
try:
    XA_OTCSV_SIGMAEL5 = 45
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 771
try:
    XA_OTCSV_SIGMAEL6 = 46
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 772
try:
    XA_OTCSV_SIGMAEL7 = 47
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 773
try:
    XA_OTCSV_BIAS1 = 48
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 774
try:
    XA_OTCSV_BIAS2 = 49
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 775
try:
    XA_OTCSV_BIAS3 = 50
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 776
try:
    XA_OTCSV_BIAS4 = 51
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 777
try:
    XA_OTCSV_BIAS5 = 52
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 780
try:
    XA_OTCSV_SIZE = 64
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 784
try:
    XA_OBSTATE_SATNUM = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 785
try:
    XA_OBSTATE_SENNUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 786
try:
    XA_OBSTATE_DS50UTC = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 788
try:
    XA_OBSTATE_POSX = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 789
try:
    XA_OBSTATE_POSY = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 790
try:
    XA_OBSTATE_POSZ = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 791
try:
    XA_OBSTATE_VELX = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 792
try:
    XA_OBSTATE_VELY = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 793
try:
    XA_OBSTATE_VELZ = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 794
try:
    XA_OBSTATE_LAT = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 795
try:
    XA_OBSTATE_LON = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 796
try:
    XA_OBSTATE_HGHT = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 797
try:
    XA_OBSTATE_POSE = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 798
try:
    XA_OBSTATE_POSF = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 799
try:
    XA_OBSTATE_POSG = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 802
try:
    XA_OBSTATE_SIZE = 64
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 807
try:
    XA_OT0_RANGERATE = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 809
try:
    XA_OT1_ELEVATION = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 810
try:
    XA_OT1_AZIMUTH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 812
try:
    XA_OT2_ELEVATION = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 813
try:
    XA_OT2_AZIMUTH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 814
try:
    XA_OT2_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 816
try:
    XA_OT3_ELEVATION = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 817
try:
    XA_OT3_AZIMUTH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 818
try:
    XA_OT3_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 819
try:
    XA_OT3_RANGERATE = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 821
try:
    XA_OT4_ELEVATION = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 822
try:
    XA_OT4_AZIMUTH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 823
try:
    XA_OT4_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 824
try:
    XA_OT4_RANGERATE = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 825
try:
    XA_OT4_ELRATE = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 826
try:
    XA_OT4_AZRATE = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 827
try:
    XA_OT4_RANGEACCEL = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 829
try:
    XA_OT5_DECL = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 830
try:
    XA_OT5_RIGHTASC = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 831
try:
    XA_OT5_YROFEQNX = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 832
try:
    XA_OT5_ABERRATION = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 834
try:
    XA_OT6_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 836
try:
    XA_OT8_ELEVATION = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 837
try:
    XA_OT8_AZIMUTH = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 838
try:
    XA_OT8_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 839
try:
    XA_OT8_POSE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 840
try:
    XA_OT8_POSF = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 841
try:
    XA_OT8_POSG = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 843
try:
    XA_OT9_DECL = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 844
try:
    XA_OT9_RIGHTASC = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 845
try:
    XA_OT9_RANGE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 846
try:
    XA_OT9_POSE = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 847
try:
    XA_OT9_POSF = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 848
try:
    XA_OT9_POSG = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 849
try:
    XA_OT9_YROFEQNX = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 850
try:
    XA_OT9_ABERRATION = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 852
try:
    XA_OTP_POSX = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 853
try:
    XA_OTP_POSY = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 854
try:
    XA_OTP_POSZ = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 856
try:
    XA_OTV_POSX = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 857
try:
    XA_OTV_POSY = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 858
try:
    XA_OTV_POSZ = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 859
try:
    XA_OTV_VELX = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 860
try:
    XA_OTV_VELY = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 861
try:
    XA_OTV_VELZ = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 863
try:
    XA_OT_SIZE = 64
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 867
try:
    XA_SELOB_MODE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 869
try:
    XA_SELOB_FRTIME = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 870
try:
    XA_SELOB_TOTIME = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 872
try:
    XA_SELOB_FRIDX = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 873
try:
    XA_SELOB_TOIDX = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 875
try:
    XA_SELOB_SAT1 = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 876
try:
    XA_SELOB_SAT2 = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 877
try:
    XA_SELOB_SAT3 = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 878
try:
    XA_SELOB_SAT4 = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 879
try:
    XA_SELOB_SAT5 = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 880
try:
    XA_SELOB_SAT6 = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 881
try:
    XA_SELOB_SAT7 = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 882
try:
    XA_SELOB_SAT8 = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 883
try:
    XA_SELOB_SAT9 = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 884
try:
    XA_SELOB_SAT10 = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 886
try:
    XA_SELOB_SEN1 = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 887
try:
    XA_SELOB_SEN2 = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 888
try:
    XA_SELOB_SEN3 = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 889
try:
    XA_SELOB_SEN4 = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 890
try:
    XA_SELOB_SEN5 = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 891
try:
    XA_SELOB_SEN6 = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 892
try:
    XA_SELOB_SEN7 = 27
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 893
try:
    XA_SELOB_SEN8 = 28
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 894
try:
    XA_SELOB_SEN9 = 29
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 895
try:
    XA_SELOB_SEN10 = 30
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 897
try:
    XA_SELOB_OT1 = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 898
try:
    XA_SELOB_OT2 = 32
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 899
try:
    XA_SELOB_OT3 = 33
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 900
try:
    XA_SELOB_OT4 = 34
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 901
try:
    XA_SELOB_OT5 = 35
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 902
try:
    XA_SELOB_OT6 = 36
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 903
try:
    XA_SELOB_OT7 = 37
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 904
try:
    XA_SELOB_OT8 = 38
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 905
try:
    XA_SELOB_OT9 = 39
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 906
try:
    XA_SELOB_OT10 = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 908
try:
    XA_SELOB_FRAZ = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 909
try:
    XA_SELOB_TOAZ = 42
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 910
try:
    XA_SELOB_FREL = 43
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 911
try:
    XA_SELOB_TOEL = 44
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 912
try:
    XA_SELOB_FRRA = 45
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 913
try:
    XA_SELOB_TORA = 46
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 914
try:
    XA_SELOB_FRDEC = 47
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 915
try:
    XA_SELOB_TODEC = 48
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 916
try:
    XA_SELOB_FRRNG = 49
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 917
try:
    XA_SELOB_TORNG = 50
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 918
try:
    XA_SELOB_FRRNGRT = 51
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 919
try:
    XA_SELOB_TORNGRT = 52
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 920
try:
    XA_SELOB_FRAZRT = 53
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 921
try:
    XA_SELOB_TOAZRT = 54
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 922
try:
    XA_SELOB_FRELRT = 55
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 923
try:
    XA_SELOB_TOELRT = 56
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 924
try:
    XA_SELOB_FRASTAT = 57
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 925
try:
    XA_SELOB_TOASTAT = 58
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_ObsDll.h: 927
try:
    XA_SELOB_SIZE = 128
except:
    pass

# No inserted files

# No prefix-stripping

