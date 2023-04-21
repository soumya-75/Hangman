import random
import hangman_art
import hangman_words
print(hangman_art.logo)
total=len(hangman_words.word_list)
n=random.randint(0,total-1)
chosen_word=hangman_words.word_list[n]
word_length = len(chosen_word)
lives=6
print(chosen_word)

display=["_"]
num=len(chosen_word)
for i in range(0,num-1):
  display.append("_")

k=word_length
while k>0:
  guess = input("\nGuess a letter: ").lower()
  j=0
  flag=0
  for letter in chosen_word:
    if letter == guess:
      display[j]=letter
      j+=1
      flag=1
    else:
      j+=1
  if flag==0:
      lives-=1
      print(hangman_art.stages[lives+1])    
  print(f"{' '.join(display)}")
  if lives==0:
      k=0
      print(hangman_art.stages[0])
      print("\nYou lose")
  elif "_" not in display:
      k=0
      print("\nYou win.")
      print(f"Lives remaining= {lives}")  
    
