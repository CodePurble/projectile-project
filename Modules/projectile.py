"""
This is a Python 3 implementation of projectile motion under various conditions. All results are rounded to 4 decimal places
"""

from math import pow
from math import radians
from math import sin
from math import cos
from math import tan
from math import sqrt
from math import pi
from enum import IntEnum

class SpinDirection(IntEnum):
    top = 1
    back = 2
    left = 3
    right = 4

class IdealProjectile:
    """
    An object moving through a vacuum with or without spin
    (All units are SI except unless specified)

    Attributes:
        initVel: Initial velocity
        angle: Launch angle
        acc: Net acceleration of object
        idealRange: Maximum range
        idealHeight: Maximum height achieved
        idealFlightTime: Total flight time
    """

    def __init__(self, initVel, angle, acc = 9.81):
        self.acc = acc
        self.initVel = initVel
        self.angle = round(radians(angle), 2)
        self.idealRange = round(((initVel ** 2) * sin(2 * radians(angle))) / acc, 4)
        self.idealHeight = round(((initVel * sin(radians(angle))) ** 2) / acc, 4)
        self.idealFlightTime = round((2 * initVel * sin(radians(angle))) / acc, 4)

    def Inst_Param_Ideal(self, time):
        """
        Calculate instantaneous velocity, x and y coordinates under ideal conditions

        Args:
            time: Time at which said properties must be calculated\n
        Returns:
            Calculated results as a list [x, y, v]
        """

        x = self.initVel * cos(self.angle) * time
        y = (
            x * tan(self.angle) - (0.5 * self.acc * pow(x / cos(self.angle), 2) / self.initVel ** 2)
        )
        v = sqrt(
            (self.initVel * sin(self.angle) - self.acc * time) ** 2 + (self.initVel * cos(self.angle)) ** 2
        )

        x = round(x, 4)
        y = round(y, 4)
        v = round(v, 4)

        paramList = [x, y, v]

        return(paramList)

class ProjectileInMedium(IdealProjectile):
    """
    An object moving through a specified medium with or without spin
    (All units are SI except unless specified)

    Attributes:
        initVel: Initial velocity
        angle: Launch angle
        crossSec: Cross sectional area
        mass: Mass of object (default 0.45 kg)
        diameter: Diameter of object (default 0.22 m)
        dragCoeff: Coefficient of drag of medium (default 0.5)
        mediumDensity: Density of medium (default 1.225 kg/m^3)
        acc: Net acceleration of object
        realRange: Maximum range
        realHeight: Maximum height achieved
        realFlightTime: Total flight time
        quadraticDragParam: Quadratic drag parameter
    """
    def __init__(self, initVel, angle, mass=0.45, diameter=0.22, dragCoeff=0.5, mediumDensity=1.225):
        super().__init__(initVel, angle)
        self.mass = mass
        self.crossSec = 0.25 * pi * (diameter ** 2)
        self.quadraticDragParam = 0.25 * mediumDensity * self.crossSec
        self.acc = sqrt(((self.quadraticDragParam ** 2) * (initVel ** 4)) + ((9.81 * mass) ** 2)) / mass
        self.dragCoeff = dragCoeff
        self.mediumDensity = mediumDensity
        self.realRange = round(((initVel ** 2) * sin(2 * radians(angle))) / self.acc, 4)
        self.realHeight = round(((initVel * sin(radians(angle))) ** 2) / self.acc, 4)
        self.realFlightTime = round((2 * initVel * sin(radians(angle))) / self.acc, 4)
        self.diameter = diameter



    @property
    def Get_Drag(self):
        drag = round(0.5 * self.dragCoeff * self.mediumDensity * self.crossSec * pow(self.initVel, 2),4)
        return(drag)

    def Inst_Param_Resistance(self, time):
        """
        Calculate instantaneous velocity, x and y coordinates considering resistance from medium

        Args:    
            time: Time at which said properties must be calculated
        Returns:
            Calculated results as a list [x, y, v]
        """
        try:
            x = self.initVel * cos(self.angle) * time
            y = (
                x * tan(self.angle) - (0.5 * self.acc * pow(x / cos(self.angle), 2) / self.initVel ** 2)
                )
            v = sqrt(
                (self.initVel * sin(self.angle) - self.acc * time) ** 2 + (self.initVel * cos(self.angle)) ** 2
                )

            x = round(x, 4)
            y = round(y, 4)
            v = round(v, 4)

            paramList = [x, y, v]

            return(paramList)
        
        except ZeroDivisionError:
            return([0, 0, 0])

    def Vortex_Strength(self, revs):
        """
        Calculate vortex strength

        Args:
            revs: revolutions ball is taking per second
        Returns: vortex strength
        """
        vortexStrength = ((2 * pi * self.diameter/2 * 0.01) ** 2) * revs
        return(vortexStrength)

    def Inst_Magnus_Force(self, time, revs, spinType):
        """
        Approximate force on ball due to the Magnus effect
        
        Args:
            revs: revolutions ball is taking per second
            time: Time at which said properties must be calculated
            spinType: top/back/left/right
        Returns:
            Magnus force
        """
        magnusForce = self.Vortex_Strength(revs) * self.Inst_Param_Resistance(time)[2] * self.mediumDensity * self.diameter
        return([round(magnusForce, 4), SpinDirection.spinType.value])
    
    def Inst_Param_Magnus(self, time):
        pass