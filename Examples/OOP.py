class shape():
    def __init__(self, vertices, edges):
        self._vertices = vertices
        self._edges = edges

class rect(shape):
    def __init__(self, length, breadth):
        super().__init__(4, 4)
        self.__length = length
        self.__breadth = breadth
    
    def area(self):
        return self.__length * self.__breadth

    def perimeter(self):
        return 2 * self.__length + 2 * self.__breadth

    def getVertices(self):
        return self._vertices

    def getEdges(self):
        return self._edges

    def __str__(self):
        return str(self.area) + str(self.perimeter)

class square(rect):
    def __init__(self, length):
        super().__init__(length, length)

class triangle(shape):
    def __init__(self, base, height):
        super().__init__(3, 3)
        self.__base = base
        self.__height = height

    def area(self):
        return 0.5 * self.__base * self.__height

    def __str__(self):
        return str(self.area)

triangle = triangle(10, 50)
rectangle = rect(10, 40)
square = square(100)

print(square.area())
print(rectangle.getEdges())