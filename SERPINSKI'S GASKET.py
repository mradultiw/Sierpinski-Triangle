from turtle import *

def triangle(base):
    fd(base)
    lt(120)
    fd(base)
    lt(120)
    fd(base)
    seth(0)
    half=base//2
    fd(half)
    lt(60)
    fd(half)
    lt(120)
    fd(half)
    lt(120)
    fd(half)
    seth(0)
    return pos()

def gasket(old_coor,base):
    base_length=elementry_triangle_base*base
    half=base//2
    if base_length==elementry_triangle_base:
        return;
    else:
        coor=triangle(base_length)
    #Right bottom
        gasket(coor,half) 
    #change position
        pu();goto(*old_coor);pd()    
        seth(0);
        coor=pos()
    #left bottom
        gasket(coor,half)
    #change position
        pu();goto(*old_coor);pd()    
        seth(0);lt(60);fd(base_length//2);seth(0)
        coor=pos()
    #top position
        gasket(coor, half)  
def main():
    global elementry_triangle_base
    reset()
    speed(0)
    delay(0)
    ht()
    coor=(-350,-300)
    pu();goto(*coor);pd()
    elementry_triangle_base=6
    s="Enter no. of triangles in base that \
you want:(to get best design enter only \
multiple of two): "
    base=int(eval(input(s,)))
    if base%2!=0:
        raise ValueError
    gasket(coor,base)
    exitonclick()
main()

