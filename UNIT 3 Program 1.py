import math as m

def calc_circle(r):
    return m.pi * r ** 2

def calc_rectangle(l, w):
    return l * w

def calc_triangle(b, h):
    return 0.5 * b * h


def main():
    print("Select a shape:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter choice: ")

    if choice == "1":
        r = float(input("Enter radius: "))
        res = calc_circle(r)
        print(f"Area of circle: {res:.2f}")

    elif choice == "2":
        l = float(input("Enter length: "))
        w = float(input("Enter width: "))
        res = calc_rectangle(l, w)
        print(f"Area of rectangle: {res:.2f}")

    elif choice == "3":
        b = float(input("Enter base: "))
        h = float(input("Enter height: "))
        res = calc_triangle(b, h)
        print(f"Area of triangle: {res:.2f}")

    else:
        print("Invalid selection.")


if __name__ == "__main__":
    main()