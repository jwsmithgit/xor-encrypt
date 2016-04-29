''' xor encrypt
    formerly CSC 110 Assignment 4
    Jacob Smith

    xor encrypt takes a txt file, in this case Hound of the Baskervilles and:
    1) Creates a file which contains the entire text reversed
    2) Creates a ciphertext using XOR
    3) Decrypts the ciphertext to make sure it was properly encrypted
    4) Creates and prints a histogram for the original text, reversed text, ciphertext, and deciphered text

    It also contains functions to count the number of lines, words, and characters
    of any of the texts. Also a function to calculate the average word length.
'''

import math

def get_line_count(filename):
    ''' reads the text and counts the number of lines
    '''
    line_count = 0
    
    with open(filename, 'r') as f:
        for line in f:
            line_count += 1

    return line_count

def get_word_count(filename):
    ''' word_count given file returns
    the number of words in the file
    '''
    word_count = 0
    
    with open(filename, 'r') as f:
        text = f.read()
        words = text.split()
        
        stripped_words = []
        for word in words:
            stripped_word = strip_nonalpha(word)
            if stripped_word:
                stripped_words.append(stripped_word)
            
        word_count = len(stripped_words)
        
    return word_count

def get_char_count(filename):
    ''' get_char_count given a file returns
    the number of charcters in the file
    '''
    char_count = 0

    with open(filename, 'r') as f:
        text = f.read()
        char_count = len(strip_nonalpha(text))
        
    return char_count

def get_avg_word_length(filename):
    ''' avg_word_length returns the char count
    by the word count
    '''
    char_count = get_char_count(filename)
    word_count = get_word_count(filename)
    
    avg_length = char_count / word_count
    
    return avg_length
    
def strip_nonalpha(text):
    '''strip_nonalpha removes nonalpha characters from a string
    '''
    return ''.join(filter(str.isalnum, text))

def reverse_text(infile, outfile):
    ''' reads the text and creates a file which contains the text reversed
    '''
    with open(infile, 'r') as f, open(outfile, 'w') as g:
        text = f.read()
        g.write(text[::-1])
    
    return

def cipher_text(infile, cipherfile, outfile):
    ''' reads the original text and the reversed text and will XOR every character
    and create a ciphertext with the result
    '''
    with open(infile,'r') as f, open(cipherfile,'r') as g, open(outfile,'w') as h:
        intext = f.read()
        ciphertext = g.read()
        
        outtext = ''
        for i, c in zip(intext, ciphertext):
            outtext += chr(ord(i) ^ ord(c))
        h.write(outtext)
    
    return
        
def get_histogram(filename):
    ''' creates a histogram for the original text file
    '''
    words = []
    with open(filename,'r') as f:
        words = f.read().split()
    
    stripped_words = []
    for word in words:
        stripped_word = strip_nonalpha(word)
        if stripped_word:
            stripped_words.append(stripped_word)
    sorted_words = sorted(stripped_words, key=len)
    
    histogram = [0 for x in range(len(sorted_words[-1])+1)]
    for word in sorted_words:
        histogram[len(word)] += 1
    histogram = adjust_range(histogram, 20)

    return histogram
    
def adjust_range(list_, max_range):
    ''' adjust_range will apply a log base 2 conversion
    to all the values greater than 1 if the maximum count is greater
    than max_range.
    '''
    if max(list_) > max_range:
        for i, value in enumerate(list_):
            if value:
                list_[i] = int(math.ceil(math.log(value,2)))
        
    return list_
    
def print_histogram(counts, title):
    ''' histogram sent a title and collection of counts will
    print the title followed by an asterisk for each value
    of n in the list of counts passed.  Each row is labelled
    from zero.
    '''
    label = 0
    print()
    print(title)
    
    for count in counts:
        if label < 10:
            print('', end=' ')
        print(label, end=' ')
        print('|', end=' ')
        
        for i in range(count):
            print('*', end=' ')
        print()
        label += 1
                  
def prompt_filename():
    ''' prompt_filneame returns the name of the file to be processed
    '''
    return input('Enter the name of the file to be processed\n===>')

def main():
    filename = prompt_filename()
    files = (filename, 'reverse.txt', 'cipher.txt', 'decipher.txt')
    
    reverse_text(filename, 'reverse.txt')
    cipher_text(filename, 'reverse.txt', 'cipher.txt')
    cipher_text('cipher.txt', 'reverse.txt', 'decipher.txt')

    histograms = []
    for file in files:
        histogram = get_histogram(file)
        print_histogram(histogram, file)
        histograms.append(histogram)

main()
