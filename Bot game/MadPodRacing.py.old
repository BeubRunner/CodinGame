import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# Paramètre de la course -----------------------------------------------------------------------------------------------
"""
nb_checkpoint = 3 # max(chiffre inscrit sur les checkpoints)
total_tours = 3 # nombre de tours pour finir la course
total_checkpoint = (nb_checkpoint + 1) * total_tours
"""

# Déclarations initiales de variables ----------------------------------------------------------------------------------
"""
nb_checkpoint_valides = 0
nb_tours_valides = nb_checkpoint_valides / nb_checkpoint
"""
x_prev = 0
y_prev = 0
opponent_x_prev = 0
opponent_y_prev = 0


# game loop -------------------------------------------------------------------------------------------------------------
while True:
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    # next_checkpoint_dist: distance to the next checkpoint
    # next_checkpoint_angle: angle between your pod orientation and the direction of the next checkpoint
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # Thurst gestion -------------------
    thrust = 100
    # Condition d'angle
    angle_max_power = (-100 <= next_checkpoint_angle <= 100)
    # Condition de distance
    dist_medium_power = (next_checkpoint_dist <= 2000 )
    dist_min_power = (next_checkpoint_dist <= 1000 )
    # Thrust level suivant conditions
    if dist_medium_power :
        thrust = 100
    if dist_min_power :
        thrust = 30
    if not angle_max_power :
        thrust = 0
        
    # Boost gestion ------------------------
    # No boost safe mode
    no_boost = ((next_checkpoint_dist <= 4000) or (-20 <= next_checkpoint_angle <= 20))
    # Stratégie 1 - proximité adverse
    """
    if ((abs(x - opponent_x) <= 2*1000) and (abs(y - opponent_y) <= 2*1000)) :
        thrust = "BOOST"
    """
    # Stratégie 2 - meme direction
    if (not no_boost and ( -1/64 <= abs((y - y_prev)/(x - x_prev)) - abs((opponent_y - opponent_y_prev)/(opponent_x - opponent_x_prev)) <= 1/64 ) ): 
        thrust = "BOOST"
    x_prev = x
    y_prev = y
    opponent_x_prev = opponent_x
    opponent_y_prev = opponent_y

    #Let's RAAAACE !! ----------------------
    print(str(next_checkpoint_x) + " " + str(next_checkpoint_y) + " " + str(thrust))

    # ---------------------------------------------------------------------------------------------------------------
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)