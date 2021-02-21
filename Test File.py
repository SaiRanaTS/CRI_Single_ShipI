
import CRI_Functions


Own_Ship_Xpos = 2
Own_Ship_Ypos = 4

Trg_Ship_Xpos = 5
Trg_Ship_Ypos = 2

Own_Ship_ang= 60

Rc = 45
Tc = 365
VTO = 14


DTA = CRI_Functions.Relat_Motion_para(Own_Ship_Xpos, Own_Ship_Ypos, Trg_Ship_Xpos, Trg_Ship_Ypos, Own_Ship_ang, Rc,
                                      Tc, VTO)

DCPA = DTA[0]
TCPA = DTA[1]
AlphaOT = DTA[2]
D_btwnS = DTA[3]

print('---------------------------------------------')
print('DCPA : ', DCPA)
print('TCPA : ', TCPA)
print('Alpha OT : ', AlphaOT)
print('Distance Between the Ships - D : ', D_btwnS)
print('---------------------------------------------')



