#TASK1
def luhn_algorithm(card_number):

    digits = [int(digit) for digit in card_number]
    
    digits.reverse()
    
    total = 0
    for i, digit in enumerate(digits):
        if i % 2 == 1:  
            doubled = digit * 2
            if doubled > 9:  
                doubled -= 9
            total += doubled
        else:
            total += digit
    
    return total % 10 == 0

card_number = "4532015112830366"  
if luhn_algorithm(card_number):

    print("Valid Card")
else:
    print("Invalid Card")

#TASK2
def remove_punctuations(input_string):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
  
    result = ""
    for char in input_string:
        if char not in punctuations:
            result += char
    
    return result

user_input = "Hello, World! How's it going?"
print(remove_punctuations(user_input)) 

#TASK3
def bubble_sort_words(words):
    n = len(words)
    for i in range(n):
        for j in range(0, n-i-1):
            if words[j] > words[j+1]:
                
                words[j], words[j+1] = words[j+1], words[j]
    return words

def sort_text_alphabetically(input_string):

    words = input_string.split()
  
    sorted_words = bubble_sort_words(words)
    
    return " ".join(sorted_words)

user_input = "banana apple orange grape"
print(sort_text_alphabetically(user_input)) 

