import math
height = int(input("What's height of wall? "))
width = int(input("What's width of wall? "))
coverage = 5

def wall_paint_can (co_h = height, co_w = width, co_cov = coverage):
    ans = (co_h * co_w) / co_cov
    print(f" {math.ceil(ans)} cans required .")

wall_paint_can()