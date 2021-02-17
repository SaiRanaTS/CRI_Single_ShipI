import math
from pylab import *
from matplotlib import pyplot as plt

def Plot(Own_Ship_Xpos,Own_Ship_Ypos,Trg_Ship_Xpos,Trg_Ship_Ypos,Own_Ship_ang,Trg_Ship_ang):
    # Plot Pos
    own_posDx = Own_Ship_Xpos
    own_posDy = Own_Ship_Ypos
    Own_DircX = 0
    Own_DircY = 90
    Tar_posDx = Trg_Ship_Xpos
    Tar_posDy = Trg_Ship_Ypos
    Tar_DircX = 0
    Tar_dircY = 120
    ang1 = int(Own_Ship_ang)
    ang2 = int(Trg_Ship_ang)
    xmin = -150
    xmax = 150
    ymin = -150
    ymax = 150
    sine_dego = math.sin(math.radians(ang1))
    cos_dego = math.cos(math.radians(ang1))
    u = 10 * sine_dego
    v = 10 * cos_dego
    sine_degt = math.sin(math.radians(ang2))
    cos_degt = math.cos(math.radians(ang2))
    z = 10 * sine_degt
    p = 10 * cos_degt
    plt.axis('equal')
    Q = plt.quiver(own_posDx, own_posDy, u, v, color='blue', pivot='middle')
    plt.quiverkey(Q, 0.75, 1.02, 1, "Own Ship", labelpos="E")
    P = plt.quiver(Tar_posDx, Tar_posDy, z, p, color='red', pivot='middle')
    plt.quiverkey(P, 0.75, 1.06, 1, "Target ship", labelpos="E")
    plt.title("Ship Positions")
    plt.show()

    return plt