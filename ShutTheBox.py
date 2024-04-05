import random
from itertools import combinations

player = int(input("If you'd like to play Shut the Box, press 1. If you'd like the computer to play, press 2:"))
#i probably want input validation on both of these questions but don't fully understand how to do that yet
how_many_plays = 1
if player == 2:
  how_many_plays = int(input("How many times would you like the computer to play?"))

counter = 0
stringscore_list = []
losing_streak_counter = 0
losing_streak_list = []
while counter < how_many_plays:
  nums = list(range(1, 10))
  if player == 1:
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
      return True, combos
    #if the combos list is empty, you lost
    #i don't need to access combos once this is False but i get an error if the first return is a tuple and this isn't so I threw it in here too. Thoughts on this?
    return False, combos 

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
      if player == 1:
        dice_choice = input("Would you like to roll 1 die or 2? ")
        rollvalue = roll_die(dice_choice)
      else:
        rollvalue = roll_die('1')
    else:
      rollvalue = roll_die('2')
      
    if player == 1:
      if rollvalue in [8,11]:
        print(f"You rolled an {rollvalue}")
      else:
        print(f"You rolled a {rollvalue}")

    #turn the returned tuple from the combo function above (true, list of combos) into a mutable list. i know i could just have it return automatically as a list but this felt more understandable in the moment.
    combo_function_list = does_it_add_up(nums, rollvalue)

    if combo_function_list[0] == True:
      if_valid = False
      while if_valid == False:
        if player == 2:
          for i in combo_function_list[1][0]: #takes out the first option in the combo list
            nums.remove(i)
          if_valid = True
        if player == 1:
          choice = input("Pick number(s) to remove, separated by commas:")
          choicelist = [int(i.strip()) for i in choice.split(',')] 
          choicemath = sum(choicelist)
        
          #Ensure the user input adds up to/matches the rolled dice value
          if choicemath != rollvalue:
            print("Your choice doesn't match the roll value")
          #Ensure the user didn't type the same number in twice
          elif has_duplicates(choicelist) == True:
            print("You can't put the same number down twice")
          else:
            #Ensure all requested tiles are still up
            any_nums_down_already = any(i not in nums for i in choicelist)
            if any_nums_down_already:
                print("Your number choice has already been put down")
            else:
              #Good inputs. Knock down tiles
              for i in choicelist:
                nums.remove(i)
              if_valid = True

        if player == 1:
          print(nums)    

    elif combo_function_list[0] == False:
      stringscore = ""
      for i in nums:
        stringscore += str(i)
      losing_streak_counter += 1
      if player == 1:
        print(f"You lost. Good job, good effort! There will come a day when you will successfully shut the box.... BUT IT IS NOT THIS DAY!\nYour score was {int(stringscore):,}.")
      break

  else:
    stringscore = '0'
    losing_streak_list.append(losing_streak_counter)
    losing_streak_counter = 0
    if player == 1:
      print("You won! You shut the box!")
      
  counter += 1
  #my list of scores were all strings like ('123', '45'), etc. but i wanted them to be ints so I could give some of the stats below
  #I'm sure I could've done this more simply but chose this way
  stringscore_list.append(stringscore)
  score_list = [int(i) for i in stringscore_list]
if player == 2:
  print(score_list)
  wins = score_list.count(0)
  print(f"You played {counter} times and shut the box {wins} times! That's a win rate of {round((wins/counter*100), 2)} %.")
  max_bad_score = score_list.count(max(score_list))
  if max_bad_score > 1:
    print(f"Your worst score was {max(score_list)} and you actually got that score {max_bad_score} times. Yikes!")
  else:
    print(f"Your worst score was {max(score_list)}. Yikes!")
  print(f"Your longest stretch between wins was {max(losing_streak_list)} games and your shortest stretch was {min(losing_streak_list)}.")
  




