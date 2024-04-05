import random
from itertools import combinations

counter = 0
score_list = []
while counter < 10:
  nums = list(range(1, 10))
  print(nums)

  def does_it_add_up(nums, target_num):
    combos = []
    for r in range(1, len(nums) + 1):
      for combo in combinations(nums, r):
        #if any combinations of available nums match the dice roll, add that combo to the combos list
        if sum(combo) == target_num:
          combos.append(combo)
    #if the combos list isn't empty, play on
    if len(combos) > 0:
      #print(combos)
      return True, combos
    #if the combos list is empty, you lost
    return False, combos #i don't need to access combos once this is False but i get an error if the first return is a tuple and this isn't so I threw it in here too. Thoughts?

  def roll_die(num_dice):
    if num_dice == '1':
      rollval = random.randint(1, 6)
    elif num_dice == '2':
      die1 = random.randint(1, 6)
      die2 = random.randint(1, 6)
      rollval = die1 + die2
    return rollval

  def has_duplicates(seq):
    return len(seq) != len(set(seq))

  while nums:
    if 7 not in nums and 8 not in nums and 9 not in nums:
      # dice_choice = input("Would you like to roll 1 die or 2? ")
      rollvalue = roll_die('1')
    else:
      rollvalue = roll_die('2')
      
    if rollvalue in [8,11]:
      print(f"You rolled an {rollvalue}")
    else:
      print(f"You rolled a {rollvalue}")

  #turn the returned tuple from the combo function above (true, list of combos) into a mutable list. i know i could just have it return automatically as a list but this felt more understandable in the moment.
    combo_function_list = does_it_add_up(nums, rollvalue)

    if combo_function_list[0] == True:
      if_valid = False
      while if_valid == False:
        for i in combo_function_list[1][0]: #takes out the first option in the combo list
          nums.remove(i)
        if_valid = True
        #if the number of the roll value is still available, put that number down automatically
        # if rollvalue in nums:
        #   nums.remove(rollvalue)
        #   if_valid = True        
        # else:
        #   choice = input("Pick number(s) to remove, separated by commas:")
        #   choicelist = [int(i.strip()) for i in choice.split(',')] 
        #   choicemath = sum(choicelist)
        
        #   #Ensure the user input adds up to/matches the rolled dice value
        #   if choicemath != rollvalue:
        #     print("Your choice doesn't match the roll value")
        #   #Ensure the user didn't type the same number in twice
        #   elif has_duplicates(choicelist) == True:
        #     print("You can't put the same number down twice")
        #   else:
        #     # Ensure all requested tiles are still up
        #     any_nums_down_already = any(i not in nums for i in choicelist)
        #     if any_nums_down_already:
        #         print("Your number choice has already been put down")
        #     else:
        #       #Good inputs. Knock down tiles
        #       for i in choicelist:
        #         nums.remove(i)
        #       if_valid = True

      print(nums)    

    elif combo_function_list[0] == False:
      score = ""
      for i in nums:
        score += str(i)
      print(f"You lost. Good job, good effort! There will come a day when you will successfully shut the box.... BUT IT IS NOT THIS DAY!\nYour score was {int(score):,}.")
      break 

  else:
    print("You won! You shut the box!")
    score = 0
  
  counter += 1
  score_list.append(score)
print(score_list)
wins = score_list.count(0)
print(f"You played {counter} times and shut the box {wins} times! That's a win rate of {int(wins/counter*100)}%.")
  




