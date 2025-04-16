r"""Wrapper for new_SpPropDll.h

Generated with:
/home/woodkn1/DND/bin/ctypesgen -I . ./new_SpPropDll.h -o ./SpPropDll.py

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
_libdirs = []

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

# No libraries

# No modules

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 23
for _lib in _libs.values():
    if not _lib.has("SpInit", "cdecl"):
        continue
    SpInit = _lib.get("SpInit", "cdecl")
    SpInit.argtypes = [c_int64]
    SpInit.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 29
for _lib in _libs.values():
    if not _lib.has("SpGetInfo", "cdecl"):
        continue
    SpGetInfo = _lib.get("SpGetInfo", "cdecl")
    SpGetInfo.argtypes = [c_char * int(128)]
    SpGetInfo.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 35
for _lib in _libs.values():
    if not _lib.has("SpLoadFile", "cdecl"):
        continue
    SpLoadFile = _lib.get("SpLoadFile", "cdecl")
    SpLoadFile.argtypes = [c_char * int(512)]
    SpLoadFile.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 41
for _lib in _libs.values():
    if not _lib.has("SpLoadFileAll", "cdecl"):
        continue
    SpLoadFileAll = _lib.get("SpLoadFileAll", "cdecl")
    SpLoadFileAll.argtypes = [c_char * int(512)]
    SpLoadFileAll.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 50
for _lib in _libs.values():
    if not _lib.has("SpSaveFile", "cdecl"):
        continue
    SpSaveFile = _lib.get("SpSaveFile", "cdecl")
    SpSaveFile.argtypes = [c_char * int(512), c_int, c_int]
    SpSaveFile.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 59
for _lib in _libs.values():
    if not _lib.has("SpInitSat", "cdecl"):
        continue
    SpInitSat = _lib.get("SpInitSat", "cdecl")
    SpInitSat.argtypes = [c_int64]
    SpInitSat.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 69
for _lib in _libs.values():
    if not _lib.has("SpInitSat_MT", "cdecl"):
        continue
    SpInitSat_MT = _lib.get("SpInitSat_MT", "cdecl")
    SpInitSat_MT.argtypes = [c_int64, c_double * int(32)]
    SpInitSat_MT.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 77
for _lib in _libs.values():
    if not _lib.has("SpRemoveSat", "cdecl"):
        continue
    SpRemoveSat = _lib.get("SpRemoveSat", "cdecl")
    SpRemoveSat.argtypes = [c_int64]
    SpRemoveSat.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 84
for _lib in _libs.values():
    if not _lib.has("SpRemoveAllSats", "cdecl"):
        continue
    SpRemoveAllSats = _lib.get("SpRemoveAllSats", "cdecl")
    SpRemoveAllSats.argtypes = []
    SpRemoveAllSats.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 89
for _lib in _libs.values():
    if not _lib.has("SpGetCount", "cdecl"):
        continue
    SpGetCount = _lib.get("SpGetCount", "cdecl")
    SpGetCount.argtypes = []
    SpGetCount.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 93
for _lib in _libs.values():
    if not _lib.has("SpReset", "cdecl"):
        continue
    SpReset = _lib.get("SpReset", "cdecl")
    SpReset.argtypes = []
    SpReset.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 117
for _lib in _libs.values():
    if not _lib.has("SpGetApCtrl", "cdecl"):
        continue
    SpGetApCtrl = _lib.get("SpGetApCtrl", "cdecl")
    SpGetApCtrl.argtypes = [c_int, c_char * int(512)]
    SpGetApCtrl.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 129
for _lib in _libs.values():
    if not _lib.has("SpGetApCtrlAll", "cdecl"):
        continue
    SpGetApCtrlAll = _lib.get("SpGetApCtrlAll", "cdecl")
    SpGetApCtrlAll.argtypes = [c_char * int(512), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_int), POINTER(c_int)]
    SpGetApCtrlAll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 136
for _lib in _libs.values():
    if not _lib.has("SpSetApCtrl", "cdecl"):
        continue
    SpSetApCtrl = _lib.get("SpSetApCtrl", "cdecl")
    SpSetApCtrl.argtypes = [c_int, c_char * int(512)]
    SpSetApCtrl.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 148
for _lib in _libs.values():
    if not _lib.has("SpSetApCtrlAll", "cdecl"):
        continue
    SpSetApCtrlAll = _lib.get("SpSetApCtrlAll", "cdecl")
    SpSetApCtrlAll.argtypes = [c_char * int(512), c_int, c_int, c_int, c_int, c_double, c_int, c_int]
    SpSetApCtrlAll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 187
for _lib in _libs.values():
    if not _lib.has("SpGet4P", "cdecl"):
        continue
    SpGet4P = _lib.get("SpGet4P", "cdecl")
    SpGet4P.argtypes = [c_int, c_char * int(512)]
    SpGet4P.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 196
for _lib in _libs.values():
    if not _lib.has("SpSet4P", "cdecl"):
        continue
    SpSet4P = _lib.get("SpSet4P", "cdecl")
    SpSet4P.argtypes = [c_int, c_char * int(512)]
    SpSet4P.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 205
for _lib in _libs.values():
    if not _lib.has("SpGetPredCtrl", "cdecl"):
        continue
    SpGetPredCtrl = _lib.get("SpGetPredCtrl", "cdecl")
    SpGetPredCtrl.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double)]
    SpGetPredCtrl.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 214
for _lib in _libs.values():
    if not _lib.has("SpSetPredCtrl", "cdecl"):
        continue
    SpSetPredCtrl = _lib.get("SpSetPredCtrl", "cdecl")
    SpSetPredCtrl.argtypes = [c_int, c_int, c_double, c_double, c_double]
    SpSetPredCtrl.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 239
for _lib in _libs.values():
    if not _lib.has("SpGetSatData", "cdecl"):
        continue
    SpGetSatData = _lib.get("SpGetSatData", "cdecl")
    SpGetSatData.argtypes = [c_int64, c_int, c_char * int(512)]
    SpGetSatData.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 253
for _lib in _libs.values():
    if not _lib.has("SpGetSatDataAll", "cdecl"):
        continue
    SpGetSatDataAll = _lib.get("SpGetSatDataAll", "cdecl")
    SpGetSatDataAll.argtypes = [c_int64, POINTER(c_int), POINTER(c_double), POINTER(c_double), POINTER(c_double), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    SpGetSatDataAll.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 265
for _lib in _libs.values():
    if not _lib.has("SpPropMse", "cdecl"):
        continue
    SpPropMse = _lib.get("SpPropMse", "cdecl")
    SpPropMse.argtypes = [c_int64, c_double, c_double * int(5), POINTER(c_int), c_double * int(3), c_double * int(3)]
    SpPropMse.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 276
for _lib in _libs.values():
    if not _lib.has("SpPropDs50UTC", "cdecl"):
        continue
    SpPropDs50UTC = _lib.get("SpPropDs50UTC", "cdecl")
    SpPropDs50UTC.argtypes = [c_int64, c_double, c_double * int(5), POINTER(c_int), c_double * int(3), c_double * int(3)]
    SpPropDs50UTC.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 288
for _lib in _libs.values():
    if not _lib.has("SpPropDs50UtcLLH", "cdecl"):
        continue
    SpPropDs50UtcLLH = _lib.get("SpPropDs50UtcLLH", "cdecl")
    SpPropDs50UtcLLH.argtypes = [c_int64, c_double, c_double * int(3)]
    SpPropDs50UtcLLH.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 300
for _lib in _libs.values():
    if not _lib.has("SpPropDs50UtcPos", "cdecl"):
        continue
    SpPropDs50UtcPos = _lib.get("SpPropDs50UtcPos", "cdecl")
    SpPropDs50UtcPos.argtypes = [c_int64, c_double, c_double * int(3)]
    SpPropDs50UtcPos.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 312
for _lib in _libs.values():
    if not _lib.has("SpPropAll", "cdecl"):
        continue
    SpPropAll = _lib.get("SpPropAll", "cdecl")
    SpPropAll.argtypes = [c_int64, c_int, c_double, c_int, c_double * int(128)]
    SpPropAll.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 322
for _lib in _libs.values():
    if not _lib.has("SpGetStateDs50UTC", "cdecl"):
        continue
    SpGetStateDs50UTC = _lib.get("SpGetStateDs50UTC", "cdecl")
    SpGetStateDs50UTC.argtypes = [c_int64, c_double, c_double * int(3), c_double * int(3)]
    SpGetStateDs50UTC.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 332
for _lib in _libs.values():
    if not _lib.has("SpSetStateDs50UTC", "cdecl"):
        continue
    SpSetStateDs50UTC = _lib.get("SpSetStateDs50UTC", "cdecl")
    SpSetStateDs50UTC.argtypes = [c_int64, c_double, c_double * int(3), c_double * int(3)]
    SpSetStateDs50UTC.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 343
for _lib in _libs.values():
    if not _lib.has("SpSetAndProp", "cdecl"):
        continue
    SpSetAndProp = _lib.get("SpSetAndProp", "cdecl")
    SpSetAndProp.argtypes = [c_int64, c_double * int(128), c_double, c_double * int(128)]
    SpSetAndProp.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 352
for _lib in _libs.values():
    if not _lib.has("SpGetPropOut", "cdecl"):
        continue
    SpGetPropOut = _lib.get("SpGetPropOut", "cdecl")
    SpGetPropOut.argtypes = [c_int64, c_int, POINTER(c_double)]
    SpGetPropOut.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 361
for _lib in _libs.values():
    if not _lib.has("SpGetCovMtx", "cdecl"):
        continue
    SpGetCovMtx = _lib.get("SpGetCovMtx", "cdecl")
    SpGetCovMtx.argtypes = [c_int64, c_int, (c_double * int(6)) * int(6)]
    SpGetCovMtx.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 367
for _lib in _libs.values():
    if not _lib.has("SpCompCovSigma", "cdecl"):
        continue
    SpCompCovSigma = _lib.get("SpCompCovSigma", "cdecl")
    SpCompCovSigma.argtypes = [(c_double * int(6)) * int(6), c_double * int(6)]
    SpCompCovSigma.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 395
for _lib in _libs.values():
    if not _lib.has("SpSet4pAll", "cdecl"):
        continue
    SpSet4pAll = _lib.get("SpSet4pAll", "cdecl")
    SpSet4pAll.argtypes = [c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_int, c_double, c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512)]
    SpSet4pAll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 423
for _lib in _libs.values():
    if not _lib.has("SpGet4pAll", "cdecl"):
        continue
    SpGet4pAll = _lib.get("SpGet4pAll", "cdecl")
    SpGet4pAll.argtypes = [POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_int), POINTER(c_double), c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512), c_char * int(512)]
    SpGet4pAll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 429
for _lib in _libs.values():
    if not _lib.has("SpSet4PCard", "cdecl"):
        continue
    SpSet4PCard = _lib.get("SpSet4PCard", "cdecl")
    SpSet4PCard.argtypes = [c_char * int(512)]
    SpSet4PCard.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 434
for _lib in _libs.values():
    if not _lib.has("SpGet4PCard", "cdecl"):
        continue
    SpGet4PCard = _lib.get("SpGet4PCard", "cdecl")
    SpGet4PCard.argtypes = [c_char * int(512)]
    SpGet4PCard.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 443
for _lib in _libs.values():
    if not _lib.has("SpAddFluxRec", "cdecl"):
        continue
    SpAddFluxRec = _lib.get("SpAddFluxRec", "cdecl")
    SpAddFluxRec.argtypes = [c_double, c_double, c_double, c_double * int(8)]
    SpAddFluxRec.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 457
for _lib in _libs.values():
    if not _lib.has("SpGetEphemTimes", "cdecl"):
        continue
    SpGetEphemTimes = _lib.get("SpGetEphemTimes", "cdecl")
    SpGetEphemTimes.argtypes = [c_int64, c_int, c_double, c_double, c_double, POINTER(c_int), POINTER(c_double)]
    SpGetEphemTimes.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 472
for _lib in _libs.values():
    if not _lib.has("SpGenEphems", "cdecl"):
        continue
    SpGenEphems = _lib.get("SpGenEphems", "cdecl")
    SpGenEphems.argtypes = [c_int64, c_double, c_double, c_double, c_int, c_int, POINTER(c_double * int(7)), POINTER(c_int)]
    SpGenEphems.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 487
for _lib in _libs.values():
    if not _lib.has("SpGenEphemsCov", "cdecl"):
        continue
    SpGenEphemsCov = _lib.get("SpGenEphemsCov", "cdecl")
    SpGenEphemsCov.argtypes = [c_int64, c_double, c_double, c_double, c_int, c_int, c_int, POINTER(c_double * int(28)), POINTER(c_int)]
    SpGenEphemsCov.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 502
for _lib in _libs.values():
    if not _lib.has("SpGenEphemsVcm_OS", "cdecl"):
        continue
    SpGenEphemsVcm_OS = _lib.get("SpGenEphemsVcm_OS", "cdecl")
    SpGenEphemsVcm_OS.argtypes = [c_char * int(4000), c_double, c_double, c_double, c_int, c_int, POINTER(c_double * int(7)), POINTER(c_int)]
    SpGenEphemsVcm_OS.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 516
for _lib in _libs.values():
    if not _lib.has("SpGenEphemsVcmCov_OS", "cdecl"):
        continue
    SpGenEphemsVcmCov_OS = _lib.get("SpGenEphemsVcmCov_OS", "cdecl")
    SpGenEphemsVcmCov_OS.argtypes = [c_char * int(4000), c_double, c_double, c_double, c_int, c_int, c_int, POINTER(c_double * int(28)), POINTER(c_int)]
    SpGenEphemsVcmCov_OS.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 525
for _lib in _libs.values():
    if not _lib.has("SpPropAllSats", "cdecl"):
        continue
    SpPropAllSats = _lib.get("SpPropAllSats", "cdecl")
    SpPropAllSats.argtypes = [POINTER(c_int64), c_int, c_double, POINTER(c_double * int(6))]
    SpPropAllSats.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 539
for _lib in _libs.values():
    if not _lib.has("SpPropAllExt", "cdecl"):
        continue
    SpPropAllExt = _lib.get("SpPropAllExt", "cdecl")
    SpPropAllExt.argtypes = [c_int64, c_int, c_double, c_int, c_int, c_int, c_double * int(128)]
    SpPropAllExt.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 545
for _lib in _libs.values():
    if not _lib.has("SpLoadFluxFile", "cdecl"):
        continue
    SpLoadFluxFile = _lib.get("SpLoadFluxFile", "cdecl")
    SpLoadFluxFile.argtypes = [c_char * int(512)]
    SpLoadFluxFile.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 551
for _lib in _libs.values():
    if not _lib.has("SpLoadDCAFile", "cdecl"):
        continue
    SpLoadDCAFile = _lib.get("SpLoadDCAFile", "cdecl")
    SpLoadDCAFile.argtypes = [c_char * int(512)]
    SpLoadDCAFile.restype = c_int
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 560
for _lib in _libs.values():
    if not _lib.has("AtmspDensity", "cdecl"):
        continue
    AtmspDensity = _lib.get("AtmspDensity", "cdecl")
    AtmspDensity.argtypes = [c_double, c_double * int(3), c_int, POINTER(c_double), POINTER(c_int)]
    AtmspDensity.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 573
for _lib in _libs.values():
    if not _lib.has("GetDcaRec", "cdecl"):
        continue
    GetDcaRec = _lib.get("GetDcaRec", "cdecl")
    GetDcaRec.argtypes = [c_double, POINTER(c_double), c_double * int(8), c_double * int(3), (c_double * int(7)) * int(7), (c_double * int(7)) * int(7), (c_double * int(7)) * int(7), (c_double * int(7)) * int(7), POINTER(c_int)]
    GetDcaRec.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 577
for _lib in _libs.values():
    if not _lib.has("SpRemoveFlux", "cdecl"):
        continue
    SpRemoveFlux = _lib.get("SpRemoveFlux", "cdecl")
    SpRemoveFlux.argtypes = []
    SpRemoveFlux.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 581
for _lib in _libs.values():
    if not _lib.has("SpRemoveDCAFile", "cdecl"):
        continue
    SpRemoveDCAFile = _lib.get("SpRemoveDCAFile", "cdecl")
    SpRemoveDCAFile.argtypes = []
    SpRemoveDCAFile.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 882
for _lib in _libs.values():
    if not _lib.has("LoadSpPropDll", "cdecl"):
        continue
    LoadSpPropDll = _lib.get("LoadSpPropDll", "cdecl")
    LoadSpPropDll.argtypes = []
    LoadSpPropDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 883
for _lib in _libs.values():
    if not _lib.has("FreeSpPropDll", "cdecl"):
        continue
    FreeSpPropDll = _lib.get("FreeSpPropDll", "cdecl")
    FreeSpPropDll.argtypes = []
    FreeSpPropDll.restype = None
    break

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 14
try:
    SpPropDll = 'SpProp.dll'
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 585
try:
    VCMOPT_USEOWN = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 586
try:
    VCMOPT_USEGLOBAL = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 590
try:
    IDX_RUNMODE_PERF = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 591
try:
    IDX_RUNMODE_MEM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 597
try:
    IDX_PARTIALS_SAVE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 598
try:
    IDX_PARTIALS_DONT = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 602
try:
    XF_COVMTX_UVW_DATE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 603
try:
    XF_COVMTX_XYZ_DATE = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 604
try:
    XF_COVMTX_EQNX_DATE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 605
try:
    XF_COVMTX_UVW_J2K = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 606
try:
    XF_COVMTX_XYZ_J2K = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 607
try:
    XF_COVMTX_EQNX_J2K = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 612
try:
    LSPERT_NONE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 613
try:
    LSPERT_ANALYTIC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 614
try:
    LSPERT_JPL = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 615
try:
    LSPERT_ALL = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 616
try:
    LSPERT_BIG = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 617
try:
    LSPERT_MED = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 618
try:
    LSPERT_SMA = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 624
try:
    STMTYPE_UVW = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 625
try:
    STMTYPE_XYZ = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 626
try:
    STMTYPE_EQNX = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 630
try:
    SPCOORD_ECI = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 631
try:
    SPCOORD_J2K = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 635
try:
    DRGMDL_JAC64 = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 636
try:
    DRGMDL_JAC70 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 637
try:
    DRGMDL_DCA1 = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 638
try:
    DRGMDL_JBH09 = 40
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 639
try:
    DRGMDL_JBHDCA2 = 41
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 643
try:
    XF_4P_GEOIDX = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 644
try:
    XF_4P_BULGEFLG = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 645
try:
    XF_4P_DRAGFLG = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 646
try:
    XF_4P_RADFLG = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 647
try:
    XF_4P_LUNSOL = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 648
try:
    XF_4P_F10 = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 649
try:
    XF_4P_F10AVG = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 650
try:
    XF_4P_AP = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 651
try:
    XF_4P_TRUNC = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 652
try:
    XF_4P_CONVERG = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 653
try:
    XF_4P_OGFLG = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 654
try:
    XF_4P_TIDESFLG = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 655
try:
    XF_4P_INCOORD = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 656
try:
    XF_4P_NTERMS = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 657
try:
    XF_4P_REEVAL = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 658
try:
    XF_4P_INTEGCTRL = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 659
try:
    XF_4P_VARSTEP = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 660
try:
    XF_4P_INITSTEP = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 662
try:
    XF_4P_DCAFILE = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 663
try:
    XF_4P_FLUXFILE = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 664
try:
    XF_4P_GEOFILE = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 665
try:
    XF_4P_JPLFILE = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 666
try:
    XF_4P_JPLSTART = 25
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 667
try:
    XF_4P_JPLSTOP = 26
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 683
try:
    XF_SPAPP_GEODIR = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 684
try:
    XF_SPAPP_BUFSIZE = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 685
try:
    XF_SPAPP_RUNMODE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 686
try:
    XF_SPAPP_SAVEPART = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 687
try:
    XF_SPAPP_SPECTR = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 688
try:
    XF_SPAPP_CONSIDER = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 689
try:
    XF_SPAPP_DECAYALT = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 690
try:
    XF_SPAPP_OUTCOORD = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 691
try:
    XF_SPAPP_VCMOPT = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 697
try:
    XF_SPSAT_SATNUM = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 698
try:
    XF_SPSAT_DS50UTC = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 699
try:
    XF_SPSAT_DS50TAI = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 700
try:
    XF_SPSAT_MU = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 701
try:
    XF_SPSAT_HASCOV = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 702
try:
    XF_SPSAT_INTMODE = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 703
try:
    XF_SPSAT_NTERMS = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 704
try:
    XF_SPSAT_SPECTR = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 725
try:
    SP_TIMETYPE_MSE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 726
try:
    SP_TIMETYPE_DS50UTC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 731
try:
    XA_SPOUT_UTC = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 732
try:
    XA_SPOUT_MSE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 733
try:
    XA_SPOUT_UT1 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 734
try:
    XA_SPOUT_TAI = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 735
try:
    XA_SPOUT_ET = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 736
try:
    XA_SPOUT_REVNUM = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 737
try:
    XA_SPOUT_NTERMS = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 738
try:
    XA_SPOUT_ISSPECTR = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 739
try:
    XA_SPOUT_HASCOVMTX = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 741
try:
    XA_SPOUT_J2KPOSX = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 742
try:
    XA_SPOUT_J2KPOSY = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 743
try:
    XA_SPOUT_J2KPOSZ = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 744
try:
    XA_SPOUT_J2KVELX = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 745
try:
    XA_SPOUT_J2KVELY = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 746
try:
    XA_SPOUT_J2KVELZ = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 747
try:
    XA_SPOUT_ECIPOSX = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 748
try:
    XA_SPOUT_ECIPOSY = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 749
try:
    XA_SPOUT_ECIPOSZ = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 750
try:
    XA_SPOUT_ECIVELX = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 751
try:
    XA_SPOUT_ECIVELY = 20
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 752
try:
    XA_SPOUT_ECIVELZ = 21
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 753
try:
    XA_SPOUT_LAT = 22
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 754
try:
    XA_SPOUT_LON = 23
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 755
try:
    XA_SPOUT_HEIGHT = 24
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 757
try:
    XA_SPOUT_COVTYPE = 30
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 758
try:
    XA_SPOUT_COVMTX = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 760
try:
    XA_SPOUT_J2KACCX = 70
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 761
try:
    XA_SPOUT_J2KACCY = 71
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 762
try:
    XA_SPOUT_J2KACCZ = 72
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 763
try:
    XA_SPOUT_ECIACCX = 73
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 764
try:
    XA_SPOUT_ECIACCY = 74
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 765
try:
    XA_SPOUT_ECIACCZ = 75
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 767
try:
    XA_SPOUT_SIZE = 128
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 771
try:
    XA_SPEXT_UTC = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 772
try:
    XA_SPEXT_MSE = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 773
try:
    XA_SPEXT_UT1 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 774
try:
    XA_SPEXT_TAI = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 775
try:
    XA_SPEXT_ET = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 776
try:
    XA_SPEXT_REVNUM = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 777
try:
    XA_SPEXT_NTERMS = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 778
try:
    XA_SPEXT_ISSPECTR = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 779
try:
    XA_SPEXT_HASCOVMTX = 8
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 781
try:
    XA_SPEXT_COORD = 10
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 782
try:
    XA_SPEXT_POSX = 11
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 783
try:
    XA_SPEXT_POSY = 12
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 784
try:
    XA_SPEXT_POSZ = 13
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 785
try:
    XA_SPEXT_VELX = 14
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 786
try:
    XA_SPEXT_VELY = 15
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 787
try:
    XA_SPEXT_VELZ = 16
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 788
try:
    XA_SPEXT_ACCX = 17
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 789
try:
    XA_SPEXT_ACCY = 18
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 790
try:
    XA_SPEXT_ACCZ = 19
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 792
try:
    XA_SPEXT_COVTYPE = 30
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 793
try:
    XA_SPEXT_COVMTX = 31
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 795
try:
    XA_SPEXT_STMTYPE = 70
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 796
try:
    XA_SPEXT_STM = 71
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 798
try:
    XA_SPEXT_SIZE = 128
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 803
try:
    SP_EPHEM_ECI = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 804
try:
    SP_EPHEM_J2K = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 809
try:
    XA_TIMETYPES_MSE = 0
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 810
try:
    XA_TIMETYPES_UTC = 1
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 811
try:
    XA_TIMETYPES_UT1 = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 812
try:
    XA_TIMETYPES_TAI = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 813
try:
    XA_TIMETYPES_ET = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 815
try:
    XA_TIMETYPES_SIZE = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 819
try:
    XA_SPPARMS_BUFSIZE = 2
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 820
try:
    XA_SPPARMS_RUNMODE = 3
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 821
try:
    XA_SPPARMS_SAVEPART = 4
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 822
try:
    XA_SPPARMS_SPECTR = 5
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 823
try:
    XA_SPPARMS_CONSIDER = 6
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 824
try:
    XA_SPPARMS_DECAYALT = 7
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 825
try:
    XA_SPPARMS_VCMOPT = 9
except:
    pass

# /home/woodkn1/CODE/temp/Sgp4Prop/SampleCode/C/DriverExamples/wrappers/new_SpPropDll.h: 826
try:
    XA_SPPARMS_SIZE = 32
except:
    pass

# No inserted files

# No prefix-stripping

