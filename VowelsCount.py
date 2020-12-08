Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def countVowels(sentence):
    '''This function counts the vowels'''
    count = 0
    sentence = sentence.lower()
    for c in sentence:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    return count


    if __name__ == '__main__':
     userInput = str(input("Enter the string to check for vowels: "))
     count = countVowels(userInput)
     
    print('Vowel Count: ',count)

    
>>> 
>>> 
>>> 
>>> 
>>> 