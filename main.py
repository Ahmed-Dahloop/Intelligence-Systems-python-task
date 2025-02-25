# text = input()
# vowels = "aeiouAEIOU"
# count = 0
# for char in text:
#     if char in vowels:
#         count += 1
# print(count)

#code 2
# def ll(x, y):
#     return [y + i for i in range(x)]
#
# x = int(input())
# y = int(input())
#
# print(ll(x, y))
# #code 3
# a = []
# for i in range(5):
#     n = int(input())
#     a.append(n)
# print(a)
# a.sort()
# print(a)
#
# a.sort(reverse=True)
# print(a)
# code 4
# def ll(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return "FizzBuzz"
#     elif n % 5 == 0:
#         return "Buzz"
#     elif n % 3 == 0:
#         return "Fizz"
#     else:
#         return n
# for i in range(3):
#     n = int(input())
#     print(ll(n))
# code 5
# def ll(s):
#     return s[::-1]
# s = input()
# print(ll(s))

# code 6
# import math
# r = float(input())
# a = math.pi * r**2
# c= 2 * math.pi * r
#
# print("a:", a)
# print("c:", c)

# #code 7
# import re
# while True:
#     name = input("name: ").strip()
#     if name and not name.isdigit():
#         break
#     print("Invalid")
# while True:
#     email = input("email: ").strip()
#     if re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}", email):
#         break
#     print("Invalid")
# print("name:", name)
# print("email:", email)
# # code 8
# i = input()
# c = i.count("iti")
# print(c)
# def longest_alphabetical_substring(s):
#     longest = current = s[0]  # Start with the first character
#
#     for i in range(1, len(s)):  # Loop through the string
#         if s[i] >= s[i - 1]:  # If letters are in order
#             current += s[i]  # Add to current substring
#         else:
#             if len(current) > len(longest):  # Check if current is longest
#                 longest = current
#             current = s[i]  # Reset current substring
#
#     if len(current) > len(longest):  # Final check
#         longest = current
#
#     print("Longest substring in alphabetical order is:", longest)
#
# # Example usage
# s = input("Enter a string: ")
# longest_alphabetical_substring(s)
