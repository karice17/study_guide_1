"""List Practice
Edit the functions until all of the doctests pass when
you run this file.
"""


def print_list(items):
    """Print each item in the input list.
    
    For example::
    
        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9
    """

    #for each item in items:
    #print item

    

    for item in items:
        print(item)

print_list([1, 2, 6, 3, 9])


def long_words(words):
    """Return words in input list that longer than 4 characters.
    
    For example::
    
        >>> long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
        ['hello', 'muffin', 'muffin']
    
    (If there are duplicates, show both --- notice "muffin" appears
    twice in output)
    
    If no words are longer than 4 characters, return an empty list::
    
        >>> long_words(["all", "are", "tiny"])
        []
    """

    #loop through word in words
    #create empty list of long_words
    #if len of word >= 4 add word to long_words list
    #return long_words
    long_words = []
    
    for word in words:
        if len(word) > 4:
            long_words.append(word)

    return long_words


long_words(["hello", "a", "b", "hi", "muffin", "muffin"])
    


def n_long_words(words, n):
    """Return words in list longer than `n` characters.
    
    For example::
    
        >>> n_long_words(
        ...     ["hello", "hey", "spam", "spam", "muffin", "muffin"],
        ...     3
        ... )
        ['hello', 'spam', 'spam', 'muffin', 'muffin']
        >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
        ['apples', 'bananas']
    """

    #create empty list n_long_words
    #loop through each words in words
    #if len(word) is > n
    #append to long_words list
    #return n_long_words

    n_long_words = []

    for word in words:
        if len(word) > n:
            n_long_words.append(word)
    


    return n_long_words

n_long_words(["hello", "hey", "spam", "spam", "muffin", "muffin"], 3)


def smallest_int(numbers):
    """Find the smallest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `min()`!
    
    For example::
    
        >>> smallest_int([-5, 2, -5, 7])
        -5
        >>> smallest_int([3, 7, 2, 8, 4])
        2
    
    If the input list is empty, return `None`::
    
        >>> smallest_int([]) is None
        True
    """
    #numbers come in an arguement [-5, 2, -5, 7]
    #check if list is empty and set variable to None
    #loop through each number in the list
    # if it's none then smallest is none
    #or if it's a number, then check it against the previous number in the loop

    smallest = None

    for n in numbers:
        if smallest is None or n < smallest:
            smallest = n

    return smallest


def largest_int(numbers):
    """Find the largest integer in a list of integers and return it.
    **DO NOT USE** the built-in function `max()`!
    
    For example::
    
        >>> largest_int([-5, 2, -5, 7])
        7
        >>> largest_int([3, 7, 2, 8, 4])
        8
    
    If the input list is empty, return None::
    
        >>> largest_int([]) is None
        True
    """
    largest = None

    for n in numbers:
        if largest is None or n > largest:
            largest = n

    return largest
    


def halvesies(numbers):
    """Return list of numbers from input list, each divided by two.
    
    For example::
    
        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]
   
    If any of the numbers are odd, make sure you don't round off
    the half::
   
        >>> halvesies([1, 5])
        [0.5, 2.5]
    """

    all_nums_halved = []

    for n in numbers:
        div_by_2 = n / 2
        all_nums_halved.append(float(div_by_2))

    return all_nums_halved

halvesies([2, 6, -2])


def word_lengths(words):
    """Return the length of words in the input list.
    
    For example::
    
        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]
    """
    #create empty list word_lengths
    #for each word in words
    #get length of word
    #add length to list
    #return the list

    compile_word_lengths = []

    for word in words:
        length = len(word)
        compile_word_lengths.append(length)
    
    return compile_word_lengths

word_lengths(["hello", "hey", "hello", "spam"])




def sum_numbers(numbers):
    """Return the sum of all of the numbers in the list.
    Python has a built-in function, `sum()`, which already does
    this --- but for this exercise, you should not use it.
    
    For example::
    
        >>> sum_numbers([1, 2, 3, 10])
        16
    
    Any empty list should return the sum of zero::
    
        >>> sum_numbers([])
        0
    """

    #define variable at 0 running_total = 0
    #loop through each num in numbers
    #add that number to the running_total
    #return running_total

    running_total = 0

    for num in numbers:
        running_total += num

    return running_total


def mult_numbers(numbers):
    """Return product (result of multiplication) of numbers in list.
    
    For example::
    
        >>> mult_numbers([1, 2, 3])
        6
    
    Obviously, if there is a zero in input, the product is zero::
    
        >>> mult_numbers([10, 20, 0, 50])
        0
    
    As explained at http://en.wikipedia.org/wiki/Empty_product,
    if the list is empty, the product should be 1::
    
        >>> mult_numbers([])
        1
    """

    # set running_total = 1
    # loop through each number in numbers
    # multiply it by the running_total
    #return running_total

    running_total = 1

    if bool(numbers) is True:
        for num in numbers:
            running_total *= num

    return running_total






def join_strings(words):
    """Return a string of all input strings joined together.
    Python has a built-in method, `list.join()` --- but for
    this exercise, **you should not use it**.
    
    For example::
    
        >>> join_strings(["spam", "spam", "muffin", "balloonicorn"])
        'spamspammuffinballoonicorn'
    
    For an empty list, you should return an empty string::
    
        >>> join_strings([])
        ''
    """

 
    #create empty string running_string = ""
    #loop through each word in words
    #add each word to the end of running_string
    #return string

    running_string = ""

    for word in words:
        running_string += word

    return running_string




def average(numbers):
    """Return the average (mean) of the list of numbers given.
    
    For example::
    
        >>> average([2, 4])
        3.0
    
    This should handle cases where the result isn't an integer::
    
        >>> average([2, 12, 3])
        5.666666666666667
    
    There is no defined answer if the list given is empty;
    it's fine if this raises an error when given an empty list.
    (Think of the best way to handle an empty input list, though,
    a feel free to provide a good solution here.)
    """
    #if bool(numbers) = True
    #set sum_of_all_numbers = 0
    #count how many numbers are in the list len(numbers)
    #loop through each num in numbers and add it to sum_of_all_numbers
    #divide sum_of_all_numbers by len(numbers)
    #return as a float
    #else print "there is nothing average in nothing. Please enter some numbers to find the average."

    if bool(numbers) is True:
        sum_of_all_numbers = 0
        total_numbers = len(numbers)
        
        for num in numbers:
            sum_of_all_numbers += num

        avg_of_numbers = sum_of_all_numbers / total_numbers

    else:
        print("I cannot give you an average of an empty list")

    return avg_of_numbers

        



def join_strings_with_comma(words):
    """Return ['list', 'of', 'words'] like "list, of, words".
    
    For example::
     
        >>> join_strings_with_comma(
        ...     ["Labrador", "Poodle", "French Bulldog"]
        ...     )
        'Labrador, Poodle, French Bulldog'
    
    If there's only one thing in the list, it should return just that
    thing, of course::
   
        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'
    """

    return ", ".join(words)


    
    


def reverse_list(items):
    """Return the input list, reversed.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> reverse_list([1, 2, 3])
        [3, 2, 1]
        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    
    You should do this without changing the original list::
    
        >>> orig = ["apple", "berry", "cherry"]
        >>> reverse_list(orig)
        ['cherry', 'berry', 'apple']
        >>> orig
        ['apple', 'berry', 'cherry']
    """

    
    return items[:: -1]


def reverse_list_in_place(items):
    """Reverse the input list `in place`.
    Reverse the input list given, but do it "in place" --- that is,
    do not create a new list and return it, but modify the original
    list.
    **Do not use** the python function `reversed()` or the method
    `list.reverse()`.
    
    For example::
    
        >>> orig = [1, 2, 3]
        >>> reverse_list_in_place(orig)
        >>> orig
        [3, 2, 1]
        >>> orig = ["cookies", "love", "I"]
        >>> reverse_list_in_place(orig)
        >>> orig
        ['I', 'love', 'cookies']
    """

    #for each item in the list in the range (length of list //2)
    #example len = 3 3//2 = 1
    for i in range(len(items) // 2):         
        temp = items[i]   #variable temp = items at index 1
        items[i] = items[(i + 1) * -1]  #items at i = items at (-(I+1))  items[1] = items[-2]
        items[(i + 1) * -1] = temp

  


def duplicates(items):
    """Return list of words from input list which were duplicates.
    Return a list of words which are duplicated in the input list.
    The returned list should be in ascending order.
   
    For example::
   
        >>> duplicates(
        ...     ["apple", "banana", "banana", "cherry", "apple"]
        ... )
        ['apple', 'banana']
        >>> duplicates([1, 2, 2, 4, 4, 4, 7])
        [2, 4]
   
    You should do this without changing the original list::
   
        >>> orig = ["apple", "apple", "berry"]
        >>> duplicates(orig)
        ['apple']
        >>> orig
        ['apple', 'apple', 'berry']
    """

    #create empty list repeat
    #use sorted on items to list alphabetically
    #for each word in the range 1 - length of list (start at 1 b/c 0 not a duplicate bc it's the first)
     #if the word at index 1 == word at index 0 then it's a repeat
    #if the word is not in the repeat list

    repeats = []

    items = sorted(items) #creates a new list, keeps original list as is

    for i in range(1, len(items)):
        if items[i] == items[i-1]:
            if items[i] not in repeats:
                repeats.append(items[i])

    return repeats

def find_letter_indices(words, letter):
    """Return list of indices where letter appears in each word.
    Given a list of words and a letter, return a list of integers
    that correspond to the index of the first occurrence of the letter
    in that word.
    **DO NOT** use the `list.index()` method.
    
    For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
        [0, 1, 2]
    
    ("o" is at index 0 in "odd", is at index 1 in "dog", and at
    index 2 in "who")
    
    If the letter doesn't occur in one of the words, use `None` for
    that word in the output list. For example::
    
        >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
        [0, 1, 2, None]
    
    ("o" does not appear in "jumps", so the result for that input is
    `None`.)
    """

    return []


#####################################################################
# END OF PRACTICE: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print("\nALL TESTS PASSED. GOOD WORK!\n")