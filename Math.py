import math
import json

# 1
def degree_to_radian(degree):
    return degree * (math.pi / 180)

degree_value = 15
radian_value = round(degree_to_radian(degree_value), 6)

# 2
radian_json = json.dumps({"degree": degree_value, "radian": radian_value})
print("Radian conversion:", radian_json)

# 3
def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height

trapezoid_data = {
    "height": 5,
    "base1": 5,
    "base2": 6,
    "area": trapezoid_area(5, 5, 6)
}

print("Trapezoid area:", json.dumps(trapezoid_data))

# 4
def regular_polygon_area(sides, length):
    return (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))

polygon_data = {
    "sides": 4,
    "side_length": 25,
    "area": regular_polygon_area(4, 25)
}

print("Polygon area in:", json.dumps(polygon_data))

# 5
def parallelogram_area(base, height):
    return base * height

parallelogram_data = {
    "base": 5,
    "height": 6,
    "area": parallelogram_area(5, 6)
}

print("Parallelogram area in:", json.dumps(parallelogram_data))
