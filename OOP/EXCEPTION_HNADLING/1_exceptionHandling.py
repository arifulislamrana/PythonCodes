try:
    print(5/0)  # here its is infinity which is an error for programming

except Exception:  # except Exception will catch the error and be executed if error occurs
    print("Math Error")

finally:    # if there is an error or not  this block might be execute
    print("try something new")