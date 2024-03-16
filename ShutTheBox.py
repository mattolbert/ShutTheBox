import random

#nums = list(range(1, 13))
#def roll():
  #count = 0
  #while nums:
    #die1 = random.randint(1, 6)
   # die2 = random.randint(1, 6)
    #rollvalue = die1 + die2
    #print(nums)
    #print("First die: "+ str(die1) + ", Second die: " + str(die2) + ", #Total: " + str(rollvalue) + "\n")
    #if rollvalue in nums:
     # nums.remove(rollvalue)
      #count += 1
    #else:
      #print(nums, rollvalue)
     # print("You lost! You rolled " + str(count) + " different numbers in a row.")
      #break
  #score = ''.join(map(str, nums))
  #print("Your final score is " + score)
 
  #return rollvalue, nums
#roll()

nums = list(range(1, 13))
print(nums)

while nums:
  die1 = random.randint(1, 6)
  die2 = random.randint(1, 6)
  rollvalue = die1 + die2
  print("You rolled a " + str(rollvalue))
  choice = input("Pick number to remove, separated by commas:")
  choicelist = [i.strip() for i in choice.split(',')]
  choicemath = 0
  for i in choicelist:
    choicemath += int(i)
  if choicemath != rollvalue:
    print("try again!")
  else:
    for i in choicelist:
      if int(i) in nums:
        nums.remove(int(i))
      else:
        print(str(i) + " is already gone")
  print(nums)



