

def get_file_lines(filename='/usr/share/dict/words'):
    """Return a list of strings on separate lines in the given text file with
    any leading and trailing whitespace characters removed from each line."""
    # Open file and remove whitespace from each line
    with open(filename) as file:
        # Use a set instead of a list for faster lookups
        lines = set(line.strip() for line in file) 

    return lines

# generate permutations of a given list 
def permutation(lst): 
  
    # If lst is empty then there are no permutations 
    if len(lst) == 0: 
        return [] 
  
    # If there is only one element in lst then, only 
    # one permuatation is possible 
    if len(lst) == 1: 
        return [lst] 
  
    l = [] # empty list that will store current permutation 
  
    # Iterate the input(lst) and calculate the permutation 
    for i in range(len(lst)): 
       m = lst[i] 
  
       # Extract lst[i] or m from the list.  remLst is 
       # remaining list 
       remLst = lst[:i] + lst[i+1:] 
  
       # Generating all permutations where m is first 
       # element 
       for p in permutation(remLst): 
           l.append([m] + p) 
    return l 
  
  
# Driver program to test above function 
word = list('TEFON') 
# words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
for p in permutation(word): 

  
    s = ""
  
    # joins elements of list1 by '-' 
    # and stores in sting s 
    s = s.join(p) 
      
    # join use to join a list of 
    # strings to a separator s 
    print(s)

def word_search(words, dictionary):
    '''
        Goes through words [list] and checks if its in the dictionary (set) of word_set
        O(n) -> len of words
        Return word_found -> list of words found in dict.
    '''
    word_found = []
    for word in words:
        if word in dictionary:
            word_found.append(word)

    return word_found

def solve_word_jumble(word_perms):
    """Solve a word jumble by unscrambling four jumbles, then a final jumble.
    Parameters:
    - words: list of strings, each is the scrambled letters for a single word
    - circles: list of strings, each marks whether the letter at that position
        in the solved anagram word will be used to solve the final jumble.
        This string contains only two different characters:
        1. O (letter "oh") = the letter is in the final jumble
        2. _ (underscore) = the letter is not in the final jumble
    - final: list of strings in the same format as circles parameter that shows
        how the final jumble's letters are arranged into a word or phrase."""
    # Get all English words in the built-in dictionary
    # all_words = get_file_lines()
    # TODO: Solve this word jumble with data structures and algorithms
    final_words = []
    word_set = get_file_lines()
    for word in word_perms:
        permuatation = permutation(word)
        word_found = word_search(permuatation, word_set)
        final_words.append(word_found)

    print('hello')
    return final_words


def main():
    # Word Jumble 1. Cartoon prompt for final jumble:
    # "Farley rolled on the barn floor because of his ___."
    words1 = ['TEFON', 'SOKIK', 'NIUMEM', 'SICONU']
    circles1 = ['__O_O', 'OO_O_', '____O_', '___OO_']
    final1 = ['OO', 'OOOOOO']
    solve_word_jumble(words1)

    # Word Jumble 2. Cartoon prompt for final jumble: "What a dog house is."
    words2 = ['TARFD', 'JOBUM', 'TENJUK', 'LETHEM']
    circles2 = ['____O', '_OO__', '_O___O', 'O____O']
    final2 = ['OOOO', 'OOO']
    solve_word_jumble(words2)


if __name__ == '__main__':
    main()



