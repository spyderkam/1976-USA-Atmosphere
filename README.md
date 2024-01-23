# 1976 USA Standard Atmosphere incorporating an instantaneous drag under certain conditions.

*Mathew David*:

Alright, so our Threat team is building some new software tools to do a new method of threat data generation on SITR. This is going to be a full ground-up change from what we utilized on the old (DSC) contract but all of this data that this new tool will output is what we on the Analysis team use as inputs for our simulation of the GMD element. In short, Threat Team feeds us data they have generated, we put that in our models/sims.

&nbsp;&nbsp;&nbsp;&nbsp;So the first thing they are building is a threat-object trajectory generation and kinematic propagation tool. So they are going to be needing some capabilities, that don't exist in their tool yet, to account for atmospheric considerations on a given threat-object model. So what the Threat team lead wants to shoot for is a 1976 US Standard Atmosphere along with a function to apply instantaneous drag under certain conditions. 

&nbsp;&nbsp;&nbsp;&nbsp;At first, it may sound like a lot but i believe it should only be a python class that encompasses the atmosphere portion and a python function for the instantaneous drag that can be called to if specific criteria is hit. I have asked the lead to give me some skeleton code that you could baseline your work off of if you are still interested.

<null><br>
*Stephen Arnsparger*:

I am going to throw some skeleton code together for you to integrate with the rest of our code base, but for now playing around with some code to closely emulate the 1976 Standard Model would be excellent. The model itself should be able to have an altitude plugged in and pass out a temperature, density, and pressure. The drag model should take in ECEF position and velocity as well as ballistic parameters to output an acceleration due to force vector. 

Some things for you:
-	Checkout: https://www.ngdc.noaa.gov/stp/space-weather/online-publications/miscellaneous/us-standard-atmosphere-1976/us-standard-atmosphere_st76-1562_noaa.pdf.
-	Honestly the wiki is way more understandable than that paper: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere.
-	Geopotential height is not the same thing as standard height, but when messing around on early implementations it isn’t a big deal to just approximate gravity since Kelly is working on our gravity model at the moment. 
-	On the rough draft it isn’t really a problem, but when you actually throw your code into our library please use the Google Python standard. 
