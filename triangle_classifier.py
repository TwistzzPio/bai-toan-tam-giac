def classify_triangle(side1, side2, side3):
    if is_valid_triangle(side1, side2, side3):
        if side1 == side2 == side3:
            return "Equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"
        elif side1 ** 2 + side2 ** 2 == side3 ** 2 or side1 ** 2 + side3 ** 2 == side2 ** 2 or side2 ** 2 + side3 ** 2 == side1 ** 2:
            return "Right Triangle"
        else:
            return "Scalene"
    else:
        return "NotATriangle"

def is_valid_triangle(side1, side2, side3):
    return side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1

def is_right_triangle(side1, side2, side3):
    sides = [side1, side2, side3]
    max_side = max(sides)
    sides.remove(max_side)
    return max_side ** 2 == sides[0] ** 2 + sides[1] ** 2

def get_user_input():
    try:
        side1 = float(input("Enter the length of the first side: "))
        side2 = float(input("Enter the length of the second side: "))
        side3 = float(input("Enter the length of the third side: "))
        return side1, side2, side3
    except ValueError:
        print("Please enter valid numbers for the lengths of the sides.")
        return get_user_input()

def main():
    print("Triangle Classifier")
    print("-------------------")
    side1, side2, side3 = get_user_input()
    triangle_type = classify_triangle(side1, side2, side3)
    print("Triangle type:", triangle_type)

if __name__ == "__main__":
    main()
