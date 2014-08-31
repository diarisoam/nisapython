__autho_ = 'mihaja'
from numpy import *

###################  VOLUME OF A SPHERE###################
def sphere_volume(radius: number) -> number:
    """
   it calculates the volume of a sphere from its radius
   :param radius: the  radius of the shere
   """
    volume = pi*(4/3)*radius**3
    return volume
print("############  SPHERE  ############")
radius = input("Enter the radius of the sphere: ")
radius = int(radius)
print("the volume of your sphere is ",sphere_volume(radius))
print("\n")

###################  VOLUME OF A CUBE  #####################
def cube_volume(side:number)->number:
    """
   it calculates the volume of a cube from its edge
   :param side: the side of the cube
   """
    cube_volume=side**3
    return cube_volume
print("########  CUBE  #########")
side=input("enter the side of the cube")
side=int(side)
print("the volume of your cube is ",cube_volume(side))
print("\n")

###################  VOLUME OF A CONE  #####################
def cone_volume(radius:number,height:number)->number:
    """
it calculates the volume of a cone from its radius and height
    :param radius: the radius of the base of the cone
    :param height: the height of the cone
    """
    volume=pi*radius**2*height
    return volume
print("#######  CONE  #######")
radius=input("enter the radius of the cone")
radius=int(radius)
height=input("enter the height of the cone")
height=int(height)
print("the volume of your cone is ",cone_volume(radius,height))
print("\n")

###################  VOLUME OF A PYRAMID  ###################
def pyramid_volume(length,width,height):
    """
it calculates the volume of a pyramid with rectangular base from its length,width and height
:param length: the length of the pyramid
:param width: the with of the pyramid
:param height: the height of the pyramid
    """
    return height*width*length/3
print("########  PYRAMID  ###########")
length=input("enter the length of the pyramid")
length=int(length)
width=input("enter the width of the pyramid")
width=int(width)
height=input("enter the height of the pyranid")
height=int(height)
print("the volume of your pyramid is",pyramid_volume(length,width,height))
print("\n")

###################i#  LATERALE AREA OF A CONE  #########
def cone_laterale_area(radius,apothem):
    """
it calculates the laterale area of a cone from its radius and apothem
    """
    return pi*radius*apothem
print("#######  CONE  ########")
radius=input("enter the radius of your cone")
radius=int(radius)
apothem=input("enter the apothem of your cone")
apothem=int(apothem)
print("the laterale area of your cone is ",cone_laterale_area(radius,apothem))
print("\n")

####################  VOLUME OF A CYLINDER  ##################
def cylinder_volume(radius,height):
    """
    calculate volume of cylinder from radius and height
    :param radius: the side radius of the base of the cylender
    :param height: the side height of the cylender
    """
    return pi*radius**2*height
print("##########  CYLINDER  ##########")
radius=input("enter the radius of your cylinder")
radius=int(radius)
height=input("enter the height of your cylinder")
height=int(height)
print("the volume of your cylinder is",cylinder_volume(radius,height))
print("\n")

###################  AREA OF A RECTANGLE  #####################
def area_rectangle(width,length):
    """
it calcules the area of a rectangle from its width and length
    :param width:  the  width of the rectangle
    :param length: the  length of the rectangle
    :return:
    """
    return width*length
print("###########  RECTANGLE  ###########")
widh=input("enter the width of your rectangle")
width=int(width)
length=input("enter the length of your rectangle")
length=int(length)
print("the area of your rectangle is",area_rectangle(width,length))
print("\n")

###################  AREA OF A CIRCLE  #########
def circle_area(radius):
    """
    :param radius:the radius of the circle
    :return:
    """
    return 2*pi*radius**2
print("##########  CIRCLE  #############")
radius=input("enter the radius of your circle")
radius=int(radius)
print("the area of your circle is ",circle_area(radius))
print("\n")

#################  VOLUME OF A CUBOID  ###############
def cuboid_volume(length,width,height):
    """
it calculates the volume of a pyramid with rectangular base from its length,width and height
:param length: the length of the pyramid
:param width: the with of the pyramid
:param height: the height of the pyramid
    """
    return height*width*length
print("########  CUBOID  ###########")
length=input("enter the length of the cuboid")
length=int(length)
width=input("enter the width of the cuboid")
width=int(width)
height=input("enter the height of the cuboid")
height=int(height)
print("the volume of your cuboid is",cuboid_volume(length,width,height))
print("\n")