# try:    
#     x = int(input("What's x "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

#using while loop for exceptions
while True:
    try:    
        x = int(input("What's x "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")    