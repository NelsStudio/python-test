# try:
#     data = int(input("enter number"))
# except:
#     print("An exception occurred")
# Q12. Write a Python statement to check if the number stored in the variable num is even.
# num = 5
# # if num == 2 * 2:
# #     print('this even')
# # else:
# #     num == 3 * 3
# #     print("this is not even")
# if num % 2 == 0:
#     print('this is even')
# else:
#     num % 3 == 0
#     print("this is not even")
# names = ['Ali', 'Sara', 'Ahmed']
# for n in names:
#     print(n)
# fruits = ['Apple', 'Orange', 'Sugar Apple', 'Candy Blosam']
# fruits.append('banana')
# print(fruits)
# num = int(input("Enter a Number !!!"))
# if num > 0:
#     print("this is positive")
# elif num < 0:
#     print("this is negative")
# else
#     print("This is zero")
# num = int(input("Enter any number !!!"))
# total = 0
# for n in range(1, num + 1):
#     total += n
# print("Sum is ", total)
# input = input("Enter names separated by commas ! ")
# names = input.split(",")
# for name in names:
#     print("Hello", name + "!")
# word = input("Enter a word")
# vowels = 'aeiou'
# for letter in vowels:
#     print(f"{letter}: {word.count(letter)}")
# import random
# random_list = [1, 4, 6, 8, 10]
# print(random.choice(random_list))
# import random
# player = input('Rock,Paper,Scissors ?')
# computer = random.choice(["rock", "paper", "scissors"])
# print("Computer chose", computer)

# if player == computer:
#     print("its a tie")
# elif player in ["rock", "paper", "scissors"]:
#     win = {"rock": "paper", "scissors": "paper", "rock": "scissors"}
#     if win[player] == computer:
#         print("you won !")
#     else:
#         print("you lost !")
# else:
#     print("invalid chocie !")


import requests

response = requests.get("https://randomuser.me/api/")

person = response.json()

print(person["results"][0]["name"]["first"])


sd = "d"
