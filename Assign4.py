'''Assign4
Jacob Smith
V00700979

Assignment 4 takes a txt file, in this case Hound of the Baskervilles and:
1) Creates a file which contains the entire text reversed
2) Creates a ciphertext using XOR
3) Decrypts the ciphertext to make sure it was properly encrypted
4) Creates a histogram for the original text, reversed text, ciphertext, and deciphered text

It also contains functions to count the number of lines, words, and characters
of any of the texts. Also a function to calculate the average word length.
'''

import math

def init_counters(n):
    ''' init_counters sent a n creates and returns
    a list of ncounters set to zero
    '''
    counts = []
    for i in range(n):
        counts.append(0)

    return counts

def print_counts(counts):
    ''' given a collections of counts print them
    '''
    label = 0
    for count in counts:
        if label < 10:
            print '',
        print label, '| ',
        print count
        label += 1

def line_count():
    ''' reads the text and counts the number of lines
    '''
    f = open('hound.txt', 'r')

    line_counter = 0
    for line in f:
        line_counter += 1

    return line_counter

def total_word_count(counts):
    ''' total_word_count given counts returns
        the sum of the counts of all the counters
        above zero
    '''

    word_counter = 0
    
    for i in range(len(counts)):
        word_counter += counts[i]
        
    return word_counter

def total_char_count(counts):
    ''' total_char_count given counts returns
        the sum of the (counts * word length) of all the counters
        above zero
    '''

    char_counter = 0

    for i in range(len(counts)):
        char_counter += counts[i] * i
        
    return char_counter

def avg_word_length(char_counter, word_counter):
    ''' avg_word_length returns the total char count
        by the total word count
    '''

    avg_length = char_counter / word_counter
    
    return avg_length

def adjust_range(counts, max_range):
    ''' adjust_range will apply a log base 2 conversion
    to all the counts greater than 1 if the maximum count is greater
    than max_range.
    '''
    if max(counts) > max_range:
        for i in range(len(counts)):
            if counts[i] > 1:
                counts[i] = int(round(math.log(counts[i],2)))
            # else leave counts of 1 alone.
        
    return counts

def histogram(counts, title):
    ''' histogram sent a title and collection of counts will
    print the title followed by an asterisk for each value
    of n in the list of counts passed.  Each row is labelled
    from zero.
    '''
    counts = adjust_range(counts, 40)
    
    label = 0
    print
    print title
    
    for count in counts:
        if label < 10:
            print '',
        print label, '|',
        
        for i in range(count):
            print '*',
        print
        label += 1


def return_words(text):
    ''' given a text string return words in that string
    '''
    return text.split()

def strip_nonalpha(word):
    '''strip non_alpha will examine the passed word character
    by character assembling a new word whil dropping non
    alphas but keeping numerics which represent year labels and
    expresions like 12th.  A word with no alphanumeric characters
    will be returned as length zero.  Acromyms are returned as
    words.
    '''
    retword = ''
    for char in word:
        if char.isalpha() or char.isdigit():
            retword += char

    return retword
    
def update_counts(counts, text):
    ''' update counts given counts and text will
    increase by one the appropriate counter in counts
    for the word length(s) in text.  Counts is returned
    '''
    words = return_words(text)
    for word in words:
        if (not word.isalpha()):
            word = strip_nonalpha(word)
        # suppress cases of zero length after alpha strip
        if len(word) > 0:
            counts[len(word)] += 1
    return counts

def reverse_text():
    ''' reads the text and creates a file which contains the text reversed
    '''
    f = open('hound.txt','r')
    g = open('dnuoh.txt','w')

    text_f = f.read()
    
    for i in range (len(text_f)):
        g.write(text_f[len(text_f)-1-i])
    
    f.close
    g.close
    
    return

def cipher_text():
    ''' reads the original text and the reversed text and will XOR every character
    and create a ciphertext with the result
    '''
    f = open('ciphertext.txt','w')
    g = open('dnuoh.txt','r')
    h = open('hound.txt','r')

    text_g = g.read()
    text_h = h.read()

    '''This checks if a value of 26 is the result of XOR is 26, I avoid this number
    since when turned into a character it becomes the End Of File character. This
    makes it impossible to read the cipher text! So I leave any characters as they
    were in the original file. Since if you change the value, you won't know what the
    character was in the first place.
    '''
    for i in range (len(text_g)):
        if ord(text_g[i])^ord(text_h[i]) != 26:
            f.write(chr(ord(text_g[i])^ord(text_h[i])))
        else:
            f.write(text_h[i])

    f.close
    g.close
    h.close
    
    return

def decipher_text():
    ''' reads the ciphertext and and reversed text and creates another file
    which is the same as the original, just to make sure it was encrypted properly
    '''
    f = open('ciphertext.txt','r')
    g = open('dnuoh.txt','r')
    h = open('deciphertext.txt','w')
    
    text_f = f.read()
    text_g = g.read()

    ''' checks, once again if the result of XOR is 26, if it is, I know that
    the character is the same as it was in the original text. Therefore, the character
    will not be changed.
    '''
    for i in range (len(text_f)):
        if ord(text_f[i])^ord(text_g[i]) != 26:
            h.write(chr(ord(text_f[i])^ord(text_g[i])))
        else:
            h.write(text_f[i])

    f.close
    g.close
    h.close

    return

def text_hist():
    ''' creates a histogram for the original text file
    '''
    counts = init_counters(20)
    
    f = open('hound.txt','r')
    for line in f:
        counts = update_counts(counts, line)
    f.close

    histogram(counts, 'hound.txt')
    
    return

def pad_hist():
    ''' creates a histogram for the reversed text
    '''
    counts = init_counters(20)
    
    f = open('dnuoh.txt','r')
    for line in f:
        counts = update_counts(counts, line)
    f.close

    histogram(counts, 'dnuoh.txt')
    
    return

def ciph_hist():
    ''' creates a histogram for the ciphertext
    '''
    counts = init_counters(50)
    
    f = open('ciphertext.txt','r')
    for line in f:
        counts = update_counts(counts, line)
    f.close

    histogram(counts, 'ciphertext.txt')
    
    return

def deciph_hist():
    ''' creates a histogram for the decrypted text
    '''
    counts = init_counters(20)

    f = open('deciphertext.txt','r')
    for line in f:
        counts = update_counts(counts, line)
    f.close
    
    histogram(counts, 'deciphertext.txt')
    
    return
                  
def prompt_filename():
    ''' prompt_filneame returns the name of the file to be processed
    '''
    return raw_input('Enter the name of the file to be processed\n===>')

def main():
    #hardcode for testing    
    #fn = prompt_filename()
    #print fn

    '''
    This whole comment contains the functions to figure out the number of
    lines, words, and characters, as well as the average word length

    
    counts = init_counters(20)
    
    f = open('hound.txt','r')
    for line in f:
        counts = update_counts(counts, line)
    f.close
    
    line_counter = line_count()
    print "Number of lines:",
    print line_counter

    word_counter = total_word_count(counts)
    print
    print "Number of words:", word_counter

    char_counter = total_char_count(counts)
    print
    print "Number of characters:", char_counter

    avg_length = avg_word_length(char_counter, word_counter)
    print
    print "Average word length:", avg_length
    
    print
    print_counts(counts)
    '''

    '''Everything is done in the functions because I like to keep the main function
    as neat and minimalistic as possible, functions are called within the functions
    if need be
    '''
    reverse_text()
    cipher_text()
    decipher_text()

    text_hist()
    pad_hist()
    ciph_hist()
    deciph_hist()


main()
