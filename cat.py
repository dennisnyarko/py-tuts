#Loops

# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1

# for _ in range(10):
#     print("meow")

# print("meow\n" * 3, end="")

# loop n number of times
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

#loop using functions
# def main():
#     number = get_number()
#     meow(number)

# def get_number():
#     while True:
#         n = int(input("WHat's n? "))
#         if n > 0:
#             break
#     return n

# def meow(n):
#     for _ in range(n):
#         print("meow")

# main()

#using lists
# students = ["Hermoine", "Harry", "Ron"]

# for student in students:
#     print(student)

students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i+1, students[i])
    