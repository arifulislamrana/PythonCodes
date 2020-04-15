try:
    print("File open")
    x = 5
    y = 0
    z = int(input("enter an integer: "))    # if non integer is given then it will produce error
    print(z)
    print(x/y)      # integer can not be divided by zero

except Exception as e:
    print("Error name: ", e)

finally:
    print("File closed")
