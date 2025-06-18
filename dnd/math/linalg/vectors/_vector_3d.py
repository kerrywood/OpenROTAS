from ctypes import c_double
from math import acos, atan2, cos, pi, sin, sqrt


class Vector3D(list[float]):

    LENGTH: int = 3

    def __init__(self, x: float, y: float, z: float):
        """3D vector

        :param x: x component
        :type x: float
        :param y: y component
        :type y: float
        :param z: z component
        :type z: float
        """
        super().__init__([x, y, z])

    @classmethod
    def z_axis(cls):
        return cls(0, 0, 1)

    @classmethod
    def from_c_array(cls, c_array):
        return cls(c_array[0], c_array[1], c_array[2])

    @classmethod
    def from_spherical(cls, r: float, ra: float, dec: float):
        cd: float = cos(dec)
        return cls(cd * cos(ra), cd * sin(ra), sin(dec)).scaled(r)

    @staticmethod
    def null_pointer():
        return (c_double * Vector3D.LENGTH)()

    @property
    def x(self) -> float:
        return self[0]

    @property
    def y(self) -> float:
        return self[1]

    @property
    def z(self) -> float:
        return self[2]

    def to_c_array(self):
        return (c_double * 3)(self[0], self[1], self[2])

    def scaled(self, scalar: float) -> "Vector3D":
        return Vector3D(self[0] * scalar, self[1] * scalar, self[2] * scalar)

    def magnitude(self) -> float:
        return sqrt(self[0] * self[0] + self[1] * self[1] + self[2] * self[2])

    def dot(self, other: "Vector3D") -> float:
        return self[0] * other[0] + self[1] * other[1] + self[2] * other[2]

    def angle(self, other: "Vector3D") -> float:
        arg = self.dot(other) / (self.magnitude() * other.magnitude())
        trunc_arg = _truncate_floating_point_error(arg)
        return acos(trunc_arg)

    def cross(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(
            self[1] * other[2] - self[2] * other[1],
            self[2] * other[0] - self[0] * other[2],
            self[0] * other[1] - self[1] * other[0],
        )

    def minus(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self[0] - other[0], self[1] - other[1], self[2] - other[2])

    def plus(self, other: "Vector3D") -> "Vector3D":
        return Vector3D(self[0] + other[0], self[1] + other[1], self[2] + other[2])

    def spherical(self) -> "Vector3D":
        ra: float = atan2(self.y, self.x)
        if ra < 0:
            ra += 2 * pi
        dec: float = atan2(self.z, sqrt(self.x * self.x + self.y * self.y))
        return Vector3D(self.magnitude(), ra, dec)

    def normalized(self) -> "Vector3D":
        mag = self.magnitude()
        return self.scaled(1 / mag)

    def distance(self, other: "Vector3D") -> float:
        return self.minus(other).magnitude()

    def copy(self) -> "Vector3D":
        return Vector3D(self[0], self[1], self[2])


def _truncate_floating_point_error(arg: float) -> float:
    result = arg
    if arg < -1:
        result = -1
    elif arg > 1:
        result = 1
    return result
