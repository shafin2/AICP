
def calcArea(s):
    area = 1.5 * 1.732 * s
    return area

def calcPeri(s):
    perimeter = 6 * s
    return perimeter

def calcAngleSum():
    angle = 120
    sum_of_angles = 6 * angle
    return sum_of_angles

def display(area, perimeter, angle_sum):
    print(f"Area of hexagon: {area}")
    print(f"Perimeter of hexagon: {perimeter}")
    print(f"Sum of all angles of hexagon: {angle_sum}")

def calcAreaSquare(length):
    area_square = length ** 2
    return area_square

def calcPeriSquare(length):
    perimeter_square = 4 * length
    return perimeter_square

def displaySquare(area_square, perimeter_square):
    print(f"Area of square: {area_square}")
    print(f"Perimeter of square: {perimeter_square}")
while True:
    print("Press 1 to calculate area, perimeter and sum of angles of hexagon")
    print("Press 2 to calculate area and perimeter of square")
    print("Press any other key to exit")

    user_input = input("Enter your choice: ")

    if user_input == '1':
        s = 1 
        area = calcArea(s)
        perimeter = calcPeri(s)
        angle_sum = calcAngleSum()
        display(area, perimeter, angle_sum)
        continue
    elif user_input == '2':
        length_square = 2
        area_square = calcAreaSquare(length_square)
        perimeter_square = calcPeriSquare(length_square)
        displaySquare(area_square, perimeter_square)
        continue
    else:
        break
