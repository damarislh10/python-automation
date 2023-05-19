name = 'Damaris %s'

print(name)

# Es una funcion 

def main(num):
    if num > 3:
        print("Soy menor")
    elif num < 3:
        print("Soy mayor")
    else :
        print("Somos neutrales")


main(0)

def loopst():
    n = 3
    """  for i in range(5):
        print(i) """
    """     condi = "si" if 3 > 2 else 3
    print(condi)

    while n > 2:
        print("Soy mayor")
        n = 1
    else:
        print("Soy menor")
    """
    for x in range(5):
     for y in range(5):
        # terminate the innermost loop
        if y > 1:
            break
        # show coordinates on the screen
        print(f"({x},{y})")

loopst()


