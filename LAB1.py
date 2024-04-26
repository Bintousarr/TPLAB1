import math

#fonction distance
def distance(point1, point2):
    return math.sqrt(sum((x2 - x1) ** 2 for x1, x2 in zip(point1, point2)))

# fonction my_map
def my_map(func, list1, list2):
    return [func(*args) for args in zip(list1, list2)]


point1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
point2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]


distances = my_map(distance, point1, point2)

print(distances)
