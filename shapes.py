# import math
#
#
# class Shapes:
#     def __init__(self, x) -> None:
#         self.x = x
#
#     def area(self):
#         pass
#
#     def perimeter(self):
#         pass
#
#
# class TwoD(Shapes):
#     def __init__(self, x, y) -> None:
#         super().__init__(x)
#         self.y = y
#
#     def area(self):
#         return super(TwoD, self).area()
#
#     def perimeter(self):
#         return super().perimeter()
#
#
# class ThreeD(Shapes):
#     def __init__(self, x, y, z) -> None:
#         super().__init__(x)
#         self.y = y
#         self.z = z
#
#     def area(self):
#         return super(ThreeD, self).area()
#
#     def perimeter(self):
#         return super().perimeter()
#
#
# class Circle(TwoD):
#     def __init__(self, radius, y) -> None:
#         super().__init__(radius, y)
#         self.radius = self.x
#
#     def area(self):
#         return math.pi * (self.radius ** 2)
#
#     def perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# circle = Circle(5, 6)
# print(circle.perimeter())
#
#
# class Square(TwoD):
#     def __init__(self, x: int, y: int) -> None:
#         super().__init__(x, y)
#
#     def area(self):
#         return self.x ** 2
#
#     def perimeter(self):
#         return 4 * self.x
#
#
# class Triangle(TwoD):
#     def __init__(self, x: int, y: int) -> None:
#         super().__init__(x, y)
#
#     def area(self):
#         return 1 / 2 * self.x * self.y
#
#
# class Sphere(ThreeD):
#     def __init__(self, x, y, z) -> None:
#         super().__init__(x, y, z)
#
#     def area(self):
#         return 4*math.pi*(self.x**2)
#
#     def perimeter(self):
#         return 2*math.pi*self.x
#
# class Cube(ThreeD):
#     def __init__(self, x, y, z) -> None:
#         super().__init__(x,y,z)
#
#     def area(self):
#         return 6*(self.x**2)
#
#     def perimeter(self):
#         return 12*self.x
#
# class Tetrahedron(ThreeD):
#     def __init__(self, x, y, z) -> None:
#         super().__init__(x,y,z)
#
#     def area(self):
#         return math.sqrt(3)*(self.x**2)
#
#     def perimeter(self):
#         return 6*self.x
#


class Physics(object):
    def physics_method(self):
        print ('physics')

class ExampleSim(Physics):
    def physics_method(self):
        print ('example sim')

class PhysicsMod(Physics):
    def physics_method(self):
        print ('physics mod')

class ExampleSimMod(PhysicsMod, ExampleSim):
    pass

e = ExampleSimMod()
e.physics_method()
