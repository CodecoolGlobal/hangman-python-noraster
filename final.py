
import random


# <<< create 2 lists from txt >>>

def read(txt):
    f = open(txt, "r")
    list_of_words = f.readlines()
    countries = []
    capitals = []
    string = ' '.join(list_of_words).strip()
    list_of_items = string.split('|')
    string2 = ' '.join(list_of_items)
    list_of_words_final = string2.split('\n')
    for item in list_of_words_final:
        lines_of_c_c = item.strip().split('  ')
    
        countries.append(lines_of_c_c[0].strip())
    
        capitals.append(lines_of_c_c[1].strip())
    return countries, capitals

list_of_countries, list_of_capitals = read('countries-and-capitals.txt')



# <<< choose difficulty from 3 values >>>


def choose_difficulty():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        if difficulty != '1' and difficulty!= '2' and difficulty!= '3':
            print ('Wrong number. Give me an other;' ) 
        else:
            return difficulty

difficulty_level = choose_difficulty()


# <<< count the lives from difficulty level >>>

def get_diff_level(dif):
   
    lives = 0
    if dif == '1':
        lives = 6
    elif dif == '2':
        lives = 5
    elif dif == '3':
        lives = 4
   
    return lives

lives = get_diff_level(difficulty_level)
# print(lives)



# <<< get the secret word woth upper case, and the original word to compara >>>

def get_word(list_capitals, list_countries):
    word1 = random.choice(list_countries)
    word2 = random.choice(list_capitals)
    list = [word1, word2]
    word = random.choice(list)
    if word in list_capitals:
        list_capitals.remove(word)
    elif word in list_countries:
        list_countries.remove(word)
   
    return word.upper(), word
    

the_secret_word, original_case_word = get_word(list_of_capitals, list_of_countries)




# <<< play the game >>>>




def play_the_game(word, original_word, lives):
    original_word_as_list = list(original_word)

    word_with_underscores = ''
    print(word)
    print('\n')
  
    for u in word:
        if u == ' ':
            u = ' '
        else:
            u = '_'
        word_with_underscores += u

   
    guessed = False
    guessed_letters = []
   
    
    print('let\'s play!')
    print(display_hangman(lives))
    
    print('\n')
    while not guessed and lives > 0:
        hack = list(word_with_underscores)
        underscores_with_space = ' '.join(hack)
        print(underscores_with_space)
        print('\n')
        print(f'Your lives count:  {lives}')
        
        print('\n')
        guess = input('please guess a vowel or a consonant or a word: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('you already guessed the letter', guess)
            elif guess not in word:
                print(guess, 'is not in the word')
                lives -= 1
                guessed_letters.append(guess)
            else:
                print('well done', guess, 'is in the word!')
                guessed_letters.append(guess)
                
                word_as_list = list(word_with_underscores) 
                # print(word_as_list) # ['_', '_', '_', '_', '_', ' ', '_', '_', '_', '_']
                secret_word_as_list = list(word)
                # print(secret_word_as_list) # ['P', 'H', 'N', 'O', 'M', ' ', 'P', 'E', 'N', 'H']
                
                
                check = all(item in guessed_letters for item in secret_word_as_list)
                
                # gives the indexes of matching letters
                indexes = [i for i, letter in enumerate(word) if letter == guess] # [1,3]
                
                for i in indexes:
                    if original_word_as_list[i].islower() == True:
                        word_as_list[i] = guess.lower()
                        
                    else:
                        word_as_list[i] = guess
                        
                    word_with_underscores = ''.join(word_as_list) 
                    if check or '_' not in word_with_underscores:
                        guessed = True
  
        print(display_hangman(lives))
        
        
    if guessed:
        print('congrats, you guessed the word! you win!')
    else:
        print('sorry, you run out of tries, the word was: ' + word)
                



def display_hangman(lives):
    states = [
        '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', 
 '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', 
 '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
     '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
   '''
  +---+
  |   |
      |
      |
      |
      |
=========''']
    return states[lives]


  
# <<< controller >>>>

def main():
    upper_word, original_word = get_word(list_of_capitals, list_of_countries)
  
    play_the_game(upper_word, original_word, lives)
    while input('play again? (Y/N)').upper() == 'Y':
     
        upper_word, original_word = get_word(list_of_capitals, list_of_countries)
        play_the_game(upper_word, original_word, lives)

if __name__ == '__main__':
    main() 

