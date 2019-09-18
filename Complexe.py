from math import pi, cos, sin
from numpy import sqrt, arctan, float64

class Complexe():

    def __init__(self, **kwargs):
        self._re = kwargs.get('re', None)
        self._im = kwargs.get('im', None)
        self._arg = kwargs.get('arg', None)
        self._mod = kwargs.get('mod', None)

        self.calc_re()
        self.calc_im()
        self.calc_arg()
        self.calc_mod()

    def calc_mod(self):
        if self._mod == None:
            self._mod = sqrt(self._re ** 2 + self._im ** 2)

    def calc_arg(self):
        if self._arg == None:
            x, y = self._re, self._im

            if x > 0 or y != 0:
                self._arg = 2*arctan(y/(sqrt(x**2 + y**2) + x))
            elif x < 0 and y == 0:
                self._arg = pi
            else:
                self._mod = 0
                self._arg = None

    def calc_re(self):
        if self._re == None:
            self._re = self.mod * cos(self.arg)

    def calc_im(self):
        if self._im == None:
            self._im = self.mod * sin(self.arg)

    @property
    def re(self):
        return self._re

    @property
    def im(self):
        return self._im

    @property
    def mod(self):
        return self._mod

    @property
    def arg(self):
        return self._arg

    def __add__(self, other):
        return Complexe(re=float64(self.re + other.re), im=float64(self.im + other.im))

    def __radd__(self, n):
        if type(n) == int:
            return Complexe(re=float64(self.re + n), im=float64(self.im))

        return self

    def __sub__(self, other):
        return Complexe(re=float64(self.re - other.re), im=float64(self.im - other.im))

    def __mul__(self, other):
        return Complexe(mod=float64(self.mod * other.mod), arg=float64(self.arg + other.arg))

    def __rmul__(self, n):
        if type(n) == int:
            return Complexe(mod=float64(n * self.mod), arg=float64(self.arg))

        return self

    def __div__(self, other):
        if other.mod != 0:
            return Complexe(mod=float64(self.mod / other.mod), arg=float64(self.arg - other.arg))
        else:
            print("Division by 0")

        return self

    def __pow__(self, n):
        if type(n) == int:
            return Complexe(mod=float64(self.mod ** n), arg=float64(self.arg * n))

        return self

    def __str__(self):
        return "{} + {}i; {}e^({}i)".format(self.re, self.im, self.mod, self.arg)