#________math area of shapes_________#
def get_func(ls):
    def square (side):
        return side*side
    def circle(Radius):
        return Radius*Radius*3.141592653589793
    def rectangle(length,width):
        return length*width
    def triangle(Height,base):
        return Height*base/2
    funcs = []
    for shape in ls:
        if shape == 'square':
            funcs.append(square)
        elif shape ==  'circle':
            funcs.append(circle)
        elif shape ==  'rectangle':
            funcs.append(rectangle)
        elif shape ==  'triangle':
            funcs.append(triangle)
    return funcs
#______________example____________#
#ls = get_func(['square', 'circle', 'rectangle', 'triangle'])

# print(ls[0](1))      # 1
# print(ls[1](2))      # 12.566370614359172
# print(ls[2](2, 4))   # 8
# print(ls[3](4, 5))   # 10.0