from shapely.geometry import *
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = [8.00, 5.00]
plt.rcParams["figure.autolayout"]

listx = []
listy = []
listr = []

sides = int(input("What should be the side of polygon : "))

for i in range(0, sides):
    pointsX = int(input(f"Coordinates of x{i+1} : "))
    listx.append(pointsX)


for i in range(0, sides):
    pointsY = int(input(f"Coordinates of y{i+1} : "))
    listy.append(pointsY)


coord = []

for a, b in zip(listx, listy):
    coord.append((a, b))

print("\nCo-ordinates of vertices :", coord)


for i in range(0, sides):
    polygon1 = Polygon(coord)

print("Centriod :", polygon1.centroid)

pointsX, pointsY = polygon1.exterior.xy
plt.plot(pointsX, pointsY, c="blue")

x, y = polygon1.centroid.xy
plt.scatter(x, y, c="red")
for xi, yi in zip(x, y):
    plt.text(xi, yi, xi, va="bottom", ha="right")
for xi, yi in zip(x, y):
    plt.text(xi, yi, yi, va="bottom", ha="left")

pointsX, pointsY = polygon1.exterior.xy
plt.scatter(pointsX, pointsY, c="green")

plt.show()
