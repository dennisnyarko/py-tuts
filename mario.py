# #vertical loop
# def main():
#     print_column(3)

# #loop different way (vertical)
# def print_column(height):
#     print("#\n" * height, end="")
    
# main()

#horizontal loop
# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()