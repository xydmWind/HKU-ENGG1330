def rectangle_stats(width: int, height: int):
    return width*height, (width+height)*2

width = int(input())
height = int(input())
print(rectangle_stats(width, height))