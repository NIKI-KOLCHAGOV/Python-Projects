import math

class Vec3:
    def __init__(self, e0=0, e1=0, e2=0):
        e0 = float(e0); e1 = float(e1); e2 = float(e2)
        self.e = [e0, e1, e2]

    def x(self):
        return self.e[0]
    def y(self):
        return self.e[1]
    def z(self):
        return self.e[2]


    def __neg__(self):
        return Vec3(-self.e[0], -self.e[1], -self.e[2])

    def __getitem__(self, i):
        return self.e[i]

    def __setitem__(self, i, value):
        self.e[i] = value

    def __iadd__(self, v):
        self.e[0] += v.e[0]
        self.e[1] += v.e[1]
        self.e[2] += v.e[2]
        return self

    def __imul__(self, t):
        self.e[0] *= t
        self.e[1] *= t
        self.e[2] *= t
        return self

    def __itruediv__(self, t):
        t = float(t)
        return self.__imul__(1/t)

    def length(self):
        return math.sqrt(self.length_squared())

    def length_squared(self):
        return self.e[0] * self.e[0] + self.e[1] * self.e[1] + self.e[2] * self.e[2]

    def unit_vector(self, v):
        return v / v.length()

    def __str__(self):
        return f"{self.e[0]} {self.e[1]} {self.e[2]}"

# point3 is just an alias for Vec3, but useful for geometric clarity in the code.
point3 = Vec3

# Vector Utility Functions

def vec3_add(u, v):
    return Vec3(u.e[0] + v.e[0], u.e[1] + v.e[1], u.e[2] + v.e[2])

def vec3_sub(u, v):
    return Vec3(u.e[0] - v.e[0], u.e[1] - v.e[1], u.e[2] - v.e[2])

def vec3_mul(u, v):
    return Vec3(u.e[0] * v.e[0], u.e[1] * v.e[1], u.e[2] * v.e[2])

def scalar_mul(t, v):
    return Vec3(t * v.e[0], t * v.e[1], t * v.e[2])

def vec3_div(v, t):
    return (1/t) * v

def dot(u, v):
    return u.e[0] * v.e[0] + u.e[1] * v.e[1] + u.e[2] * v.e[2]

def cross(u, v):
    return Vec3(u.e[1] * v.e[2] - u.e[2] * v.e[1],
                u.e[2] * v.e[0] - u.e[0] * v.e[2],
                u.e[0] * v.e[1] - u.e[1] * v.e[0])

#def unit_vector(v):
#    return v / v.length()