import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    return distance

def main():
    x1 = float(input())
    y1 = float(input())
    z1 = float(input())
    x2 = float(input())
    y2 = float(input())
    z2 = float(input())

    distance = calculate_distance(x1, y1, z1, x2, y2, z2)
    print(f"{distance:.16f}")

if __name__ == "__main__":
    main()
