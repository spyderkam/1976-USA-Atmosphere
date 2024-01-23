import scipy.integrate as integrate
import numpy as np


g = -9.81     # This varies for altitude but will be assumed constant here.
class Atmosphere:
    """1976 standard atmosphere model"""

    def __init__(self, h0=-1524, P0=101325, R=287.052874):
        self.R = R           # specific gas constant for dry air (default units: [J/(kg*K)])
        self.h0 = -1524      # geopotential altitude at sea level (boudary condition)
        self.P0 = 101325     # pressure at sea level (boudary condition)

    def T(self, h):     # See "find_T_vs_h_curve.py" for how this math expresssion temp was obtained.
        return 0.000000000000000027*h**4 - 0.000000000006074933*h**3 + 0.000000422889669793*h**2 - 0.009918936624872612*h + 289.661267963331567898

    def P(self, h):     # h is geopotential altitude
        return np.exp( (g/self.R)*integrate.quad(lambda h: 1/T(h), self.h0, h)[0] + np.log(self.P0) )

    def ρ(self, h):     # density
        return P(h)/(self.R*T(h))

"""
    def drag_force(self, v, c, A):     # v: velocity, c: drag coefficient, A: cross sectional area
        ρ = self.P/(self.R*self.T)     # density of fluid
        return 0.5*ρ*(v**2)*c*A
"""


if __name__ == '__main__':
    atm_model = Atmosphere()
    T = atm_model.T
    P = atm_model.P
    ρ = atm_model.ρ

    hmax = 76200
    h = hmax

    print(f"For h = {h}, T = {T(h)}, P = {P(h)}, and ρ = {ρ(h)}.")
