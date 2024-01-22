class Atmosphere:
    """1976 standard atmosphere model"""

    def __init__(self, P, T, R=287.052874):
        self.P = P     # pressure
        self.R = R     # specific gas constant for dry air (default units: [J/(kg*K)])
        self.T = T     # temperature

    def drag_force(self, v, c, A):     # v: velocity, c: drag coefficient, A: cross sectional area
        ρ = self.P/(self.R*self.T)     # density of fluid
        return 0.5*ρ*(v**2)*c*A


if __name__ == '__main__':
    atm_model = Atmosphere(1, 1)
    Fd = atm_model.drag_force(1, 1, 1)

    print(f"Drag force = {Fd} Newtons")


# Sources:
#   [1] Wikipedia: U.S. Standard Atmosphere
#   [2] Wikipedia: Vertical Pressure Variation
#   [3] Wikipedia: Gas Constant
