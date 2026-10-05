def move(point,offset):
    x,y=point
    dx,dy=offset
    return(x+dx,y+dy)
x=int(input())
y=int(input())
dx=int(input())
dy=int(input())
print(move((x,y),(dx,dy)))
