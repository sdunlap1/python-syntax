def print_upper_words(words, must_start_with=None):
    """
    Print each word on a separate line in uppercase. 
    Only prints words that start with letters in 'must_start_with'.
    
    - words: list of words
    - must_start_with: set of letters; if specified, only words starting with one of these letters are printed
    
    Example:
        print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
    """
    for word in words:
      # If must_start_with is set, convert it to uppercase for comparison
      if must_start_with:
         starts_with_filtered = set(letter.upper() for letter in must_start_with)
         # Check if the first letter of the word (in uppercase) is in the filtered set
         if word[0].upper() in starts_with_filtered:
            print(word.upper())
      else:
        # If must_start_with not provided, just print the word in uppercase
        print(word.upper())    

# this should print "HELLO", "HEY", "YO", and "YES"
print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
must_start_with={"h", "y"})


def print_e_words(words):
    """
    Print each word on a separate line in uppercase if it starts with 'e' or 'E'.
    
    - words: list of words
    
    Example:
        print_e_words(["elephant", "Eagle", "hello", "hey", "goodbye", "yo", "yes"])
    """
    for word in words:
        if word[0].lower() == "e": # Check if the word starts with 'e' or 'E'
          print(word.upper())

print("\nWords starting with 'e', in uppercase:")
print_e_words(["elephant", "Eagle", "hello", "hey", "goodbye", "yo", "yes"])