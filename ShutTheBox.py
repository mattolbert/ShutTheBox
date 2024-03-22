import random
from itertools import combinations

nums = list(range(1, 10))
print(nums)

def does_it_add_up(nums, target_num):
  for r in range(1, len(nums) + 1):
    for combo in combinations(nums, r):
      if sum(combo) == target_num:
        return True
  return False

def roll_die(num_dice):
  if num_dice == '1':
    rollval = random.randint(1, 6)
  elif num_dice == '2':
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    rollval = die1 + die2
  return rollval

def has_duplicates(seq):#i built this because I accidentally typed "1, 1" in as user input and it did all sort of weirdness, I think this fixed it
  return len(seq) != len(set(seq))

while nums:
  if 7 not in nums and 8 not in nums and 9 not in nums:
    dice_choice = input("Would you like to roll 1 die or 2? ")
    rollvalue = roll_die(dice_choice)
  else:
    rollvalue = roll_die('2')
    
  if rollvalue in [8,11]:
    print(f"You rolled an {rollvalue}")
  else:
    print(f"You rolled a {rollvalue}")

  if does_it_add_up(nums, rollvalue):
    if_valid = False
    while if_valid == False:
      choice = input("Pick number(s) to remove, separated by commas:")
      choicelist = [i.strip() for i in choice.split(',')] 
      intlist = [int(i) for i in choicelist]#can this and the line above it all happen at once?
      choicemath = sum(intlist)
      
      if choicemath == rollvalue:
        if has_duplicates(intlist) == True:
          print("You can't put the same number down twice")
          break
        else:
          for i in intlist:
            if i not in nums:
              print("Your number choice has already been put down")
              break       
            nums.remove(i)
            if_valid = True
      else:
        print("Your choice doesn't match the roll value")

    print(nums)    

  else:
    score = ""
    for i in nums:
      score += str(i)
    print(f"You lost. Good job, good effort! Your score was {int(score):,}")
    break 

else:
  print("You won! You shut the box!")




