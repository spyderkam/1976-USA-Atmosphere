# 1976 USA Standard Atmosphere incorporating an instantaneous drag under certain conditions.

*Mathew David*:

&nbsp;&nbsp;&nbsp;&nbsp;Alright, so our Threat team is building some new software tools to do a new method of threat data generation on SITR. This is going to be a full ground-up change from what we utilized on the old (DSC) contract but all of this data that this new tool will output is what we on the Analysis team use as inputs for our simulation of the GMD element. In short, Threat Team feeds us data they have generated, we put that in our models/sims.

&nbsp;&nbsp;&nbsp;&nbsp;So the first thing they are building is a threat-object trajectory generation and kinematic propagation tool. So they are going to be needing some capabilities, that don't exist in their tool yet, to account for atmospheric considerations on a given threat-object model. So what the Threat team lead wants to shoot for is a 1976 US Standard Atmosphere along with a function to apply instantaneous drag under certain conditions. 

&nbsp;&nbsp;&nbsp;&nbsp;At first, it may sound like a lot but i believe it should only be a python class that encompasses the atmosphere portion and a python function for the instantaneous drag that can be called to if specific criteria is hit. I have asked the lead to give me some skeleton code that you could baseline your work off of if you are still interested.
