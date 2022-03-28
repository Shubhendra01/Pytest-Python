print("Menu for area: ")
print("1.Area of rectangle")
print("2.Perimeter of rectangle")
print("3.Area of square")

x = int(input("Enter 1,2 or 3: "))

if x == 1:
    l = eval(input("Enter the lenght of rectangle: "))
    b = eval(input("Enter the breadth of rectangle: "))
    print("Area of rectangle = ", l*b)
elif x == 2:
    c = eval(input("Enter the lenght of rectangle: "))
    w = eval(input("Enter the width of rectangle: "))
    print("Perimeter of rectangle = ", 2*(c+w))
elif x == 3:
    a = eval(input("Enter the side of square: "))
    print("Area of Square= ", a*a)