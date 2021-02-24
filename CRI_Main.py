import math
import numpy
from fractions import Fraction
import numpy as np
from matplotlib import pyplot as plt
import sys
# sys.path.append('../scripts/')
from pylab import *
import CRI_FunExe
import CRI_Functions

import Plot_Chart


# This is the V.1.2 of the CRI Risk Model for Ship by Sai
# This Execution contains two modules: CRI_FunExe and CRI_Functions


###################################################################################################
# :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:Ship Define:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
###################################################################################################
class Ship_Data:
    number_of_ships = 0

    def __init__(self, Xpos, Ypos, v, ang, l):
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.v = v
        self.ang = ang
        self.l = l
        Ship_Data.number_of_ships += 1


###################################################################################################
print('Welcome to V.1.2 of the CRI Risk Model for Ship by Sai ')
print(
    '-*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*-')
print(
    'For this model we need to have 1. X position of Ship, 2. Y position of Ship, 3. Velocity of Ship, 4. Direction Angle of the Ship and 4. Length of the Ship')
print(
    '-*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*--*-*-*-')
osx = 1#float(input('Enter the X Coordinate of Own Ship : '))
osy = 2#float(input('Enter the Y Coordinate of Own Ship : '))
osv = 10#float(input('Enter the Speed of Own Ship (Knots): '))
osa = 60#float(input('Enter the angle of Own Ship (Deg)  : '))
osl = 100#float(input('Enter the length of Own Ship (Mtr) : '))

print('\nEnter the details for Target Ship\n')
print('---------------------------------------------')

tsx = 3#float(input('Enter the X Coordinate of Target Ship : '))
tsy = 2#float(input('Enter the Y Coordinate of Target Ship : '))
tsv = 12#float(input('Enter the Speed of Target Ship (Knots): '))
tsa = 3#float(input('Enter the angle of Target Ship (Deg)  : '))
tsl = 100#float(input('Enter the length of Target Ship (Mtr) : '))

# print('The number of Target Ships are : ', S_No) # Mutli Ship Under construction


###################################################################################################


Own_Ship = Ship_Data(osx, osy, osv, osa, osl)
Trg_Ship = Ship_Data(tsx, tsy, tsv, tsa, tsl)

###################################################################################################

chart = Plot_Chart.Plot(Own_Ship.Xpos, Own_Ship.Ypos, Trg_Ship.Xpos, Trg_Ship.Ypos, Own_Ship.ang, Trg_Ship.ang)
chart.show()




###################################################################################################
#:-)(-::-)(-::-)(-::-)(-::-)(-::-)(-: CRI - Execution Call :-)(-::-)(-::-)(-::-)(-::-)(-::-)(-:
###################################################################################################

CRI = CRI_FunExe.CRI_call(Own_Ship.v, Trg_Ship.v, Own_Ship.Xpos, Own_Ship.Ypos, Trg_Ship.Xpos, Trg_Ship.Ypos,
                          Own_Ship.ang, Trg_Ship.ang)

print('CRI index : ', CRI)

