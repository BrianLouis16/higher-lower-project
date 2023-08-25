from game_data import data
from art import logo
from vs import VS
import random
from replit import clear
print(logo)

data = data

def followers_count(data_entry):
    return data_entry.get("follower_count"), data_entry.get("name")



def user():
  choice_1 = random.choice(data)
  choice_2 = random.choice(data)
  info_1 = choice_1
  info_2 = choice_2
  name_1 = info_1.get("name", "N/A")
  name_2 = info_2.get("name", "N/A")
  description_1 = info_1.get("description", "N/A")
  description_2 = info_2.get("description", "N/A")
  country_1 = info_1.get("country", "N/A")
  country_2 = info_2.get("country", "N/A")
  
  print(f"Info for option A:Name: {name_1} Description: {description_1} Country: {country_1}")
  print(VS)
  print(f"Info for option B: Name: {name_2} Description: {description_2} Country: {country_2}")


  A = followers_count(choice_1)
  B = followers_count(choice_2)
  print(A,B)


  while True:
      user_input = input("Which one is popular (A/B): ").lower()
    
      if user_input == "a":
          user_choice = A
          opponent = B
          break
      elif user_input == "b":
          user_choice = B
          opponent = A
          break
      else:
          print("Invalid input. Please enter 'A' or 'B'.")

  return user_choice, opponent


point = 0
while True:
    user_result, opponent_result = user()
    if user_result > opponent_result:
        point += 1
        clear()
        print(f"You're right!. Points: {point}")
    elif opponent_result > user_result:
        print(f"You lose. Points: {point}")
        break
