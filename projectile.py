from math import *

class idealProjectile:

    def __init__(self, initVel, angle, acc = 9.81):
        self.acc = acc
        self.initVel = initVel
        self.angle = round(radians(angle), 2)
        self.idealRange = round(((initVel**2)*sin(2*radians(angle)))/acc, 4)
        self.idealHeight = round(((initVel*sin(radians(angle)))**2)/acc, 4)
        self.idealFlightTime = round((2*initVel*sin(radians(angle)))/acc, 4)

    def instParamIdeal(self, time):

        x = self.initVel*cos(self.angle)*time
        y = (
            x*tan(self.angle) - (0.5*self.acc*pow(x/cos(self.angle),2)/self.initVel**2)
        )
        v = sqrt(
            (self.initVel*sin(self.angle) - self.acc*time)**2 + (self.initVel*cos(self.angle))**2
        )

        x = round(x,4)
        y = round(y,4)
        v = round(v,4)

        paramList = [x, y, v]

        return(paramList)

class realProjectile(idealProjectile):
    def __init__(self, initVel, angle, mass=0.45, diameter=0.22, dragCoeff=0.5, mediumDensity=1.225):
        super().__init__(initVel, angle)
        self.crossSec = 0.25*pi*(diameter**2)
        self.quadraticDragParam = 0.25*mediumDensity*self.crossSec
        self.acc = sqrt(((self.quadraticDragParam**2)*(initVel**4)) + ((9.81*mass)**2))/mass
        self.dragCoeff = dragCoeff
        self.mediumDensity = mediumDensity
        self.realRange = round(((initVel**2)*sin(2*radians(angle)))/self.acc, 4)
        self.realHeight = round(((initVel*sin(radians(angle)))**2)/self.acc, 4)
        self.realFlightTime = round((2*initVel*sin(radians(angle)))/self.acc, 4)



    @property
    def getDrag(self):
        drag = round(0.5 * self.dragCoeff * self.mediumDensity * self.crossSec * pow(self.initVel, 2),4)
        return(drag)

    def instParamReal(self, time):
        x = self.initVel*cos(self.angle)*time
        y = (
            x*tan(self.angle) - (0.5*self.acc*pow(x/cos(self.angle),2)/self.initVel**2)
        )
        v = sqrt(
            (self.initVel*sin(self.angle) - self.acc*time)**2 + (self.initVel*cos(self.angle))**2
        )

        x = round(x,4)
        y = round(y,4)
        v = round(v,4)

        paramList = [x, y, v]

        return(paramList)



# print(help(realProjectile))
# p = realProjectile(30,45,0.450,0.22)
# print(p.realRange, p.idealRange)
# print(p.instParamReal(p.realFlightTime))
# print(p.getDrag)
