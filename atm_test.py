# Alright, so our Threat team is building some new software tools to do a new method of threat data generation on SITR. This is going to be a full ground-up change from what we utilized on the old (DSC) contract but all of this data that this new tool will output is what we on the Analysis team use as inputs for our simulation of the GMD element. In short, Threat Team feeds us data they have generated, we put that in our models/sims.
# So the first thing they are building is a threat-object trajectory generation and kinematic propagation tool. So they are going to be needing some capabilities, that don't exist in their tool yet, to account for atmospheric considerations on a given threat-object model. So what the Threat team lead wants to shoot for is a 1976 US Standard Atmosphere along with a function to apply instantaneous drag under certain conditions. 
# At first, it may sound like a lot but i believe it should only be a python class that encompasses the atmosphere portion and a python function for the instantaneous drag that can be called to if specific criteria is hit. I have asked the lead to give me some skeleton code that you could baseline your work off of if you are still interested. 



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
