import random
from itertools import combinations

nums = list(range(1, 13))
print(nums)

#determine if any combo of remaining numbers adds up to the dice roll. To be fair, I ended up googling how to do this, I don't know if I could have figured out a way to do it on my own but curious what you guys think.
def does_it_add_up(nums, target_num):
  for r in range(1, len(nums) + 1):
    for combo in combinations(nums, r):
      if sum(combo) == target_num:
        return True
  return False

while nums:
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  rollvalue = die1 + die2
  #changes the word "a" to "an" in cases of rolling 8 or 11, for grammatical effect
  if rollvalue == 8 or rollvalue == 11:
    print("You rolled an " + str(rollvalue))
  else:
    print("You rolled a " + str(rollvalue))

  if does_it_add_up(nums, rollvalue):
    if_valid = False
    while if_valid == False:
      choice = input("Pick number to remove, separated by commas:")
      choicelist = [i.strip() for i in choice.split(',')] 
    
      choicemath = 0
      for i in choicelist:
        choicemath += int(i)
      
      for i in choicelist:
        if choicemath == rollvalue and int(i) in nums:
          nums.remove(int(i))
          if_valid = True
        else:
          print("Try again")
      
  else:
    score = ""
    for i in nums:
      score += str(i)
    print("You lost. Great game though! Your final score was " + (f"{int(score):,}")) #i looked up online how to format this to add commas into the score value, I don't really understand it.
    break 
    
  
  print(nums)



