import math


def calc_circle(diameter, verdubbelaar=1):
    '''
    \n
    This is a function to calculate a circle:

    params:

    * diameter (required) - e.g. (14)
    * verdubbelar (optional) - e.g. (10) 
    '''

    straal = diameter / 2
    circle = (straal * straal) * math.pi
    circle *= verdubbelaar
    return circle, straal, diameter
