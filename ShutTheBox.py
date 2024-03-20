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

while nums:
  if 7 not in nums and 8 not in nums and 9 not in nums:
    dice_choice = input("Would you like to roll 1 die or 2? ")
    if dice_choice == "1":
      rollvalue = random.randint(1, 6)
    else:
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      rollvalue = die1 + die2
  else: #i understand that this is not super elegant, I do want to try to simplify it, prob no need to have the same block twice in a row here
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    rollvalue = die1 + die2
    
  
  if rollvalue == 8 or rollvalue == 11:
    print("You rolled an " + str(rollvalue))
  else:
    print("You rolled a " + str(rollvalue))

  if does_it_add_up(nums, rollvalue):
    if_valid = False
    while if_valid == False:
      choice = input("Pick number(s) to remove, separated by commas:")
      choicelist = [i.strip() for i in choice.split(',')] 
    
      #need to update this following Dalys comment
      choicemath = 0
      for i in choicelist:
        choicemath += int(i)
      
      for i in choicelist:
        if choicemath == rollvalue and int(i) in nums:
          nums.remove(int(i))
          if_valid = True
        else:
          print("Try again") #will update these error messages to make them clearer
    print(nums)    
  else:
    score = ""
    for i in nums:
      score += str(i)
    print(f"You lost. Good job, good effort! Your score was {int(score):,}")
    break 

else:
  print("You won! You shut the box!") #i did shut the box once but this didn't appear so I need to find a way to troubleshoot that




