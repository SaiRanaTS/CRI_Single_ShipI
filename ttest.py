
alpha_OT = -530



if alpha_OT < 0:
    alpha_OT = alpha_OT + 360
elif alpha_OT > 360:
    alpha_OT = alpha_OT - 360
else:
    pass

print('Alpha OT = ', alpha_OT)