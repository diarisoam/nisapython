__author__ = 'mihaja'
from numpy import *
def sphere_volume(radius: number) -> number:
    """
   calculate volume of sphere from radius
   """
    volume = pi*(4/3)*radius**3
    return volume
nombre = input("Enter a number: ")
nombre = int(nombre)
print(sphere_volume(nombre))

def cube_volume(side:number)->number:
    """
   calculate volume of cube from edge
   """
    cube_volume=side**3
    return cube_volume
print(cube_volume(3))
def cone_volume(radius:number,height:number)->number:
    """  o
calculateoume of cone from radius and height
    """
    volume=pi*radius**2*height
    return volume
print(cone_volume(2,1))

def pyramid_volume(length,width,height):
    """
calculate volume of pyramid with rectangular base from length,width and height
    """
    return height*width*length/3
print(pyramid_volume(1,1,1))
def cone_laterale_area(radius,apothem):
    """
calculate laterale area of cone from radius and apothem
    """
    return pi*radius*apothem
print(cone_laterale_area(1,1))
def cylinder_volume(radius,height):
    """
calculate volume of cylinder from radius and height
    """
    return pi*radius**2*height
print(cylinder_volume(6,9))
lknvnsdvnfasdncvsa