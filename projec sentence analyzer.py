#MINI PROJECT "SENTENCE ANALYZER"
print("()=======SENTENCE ANALYZER=======()\n")
sentence=input("Type a sentence:")
print("===============\n")
vowels= "a","e","i","o","u"
counter=0
vowel_counter=0
uppercase_counter=0
space_counter=0
lowercase_counter=0
digit_counter=0
word_counter=0
word=sentence.split()

for i in sentence:
    counter=counter+1
    if(i.lower() in vowels):
        vowel_counter=vowel_counter+1
    if(i.isupper()):
        uppercase_counter=uppercase_counter+1
    if(i.isspace()):
        space_counter=space_counter+1
    if(i.islower()):
        lowercase_counter=lowercase_counter+1
    if(i.isdigit()):
        digit_counter=digit_counter+1

for k in word:
    word_counter=word_counter+1



    
print("Total characters in sentence\t:",counter)
print("-----------------------------------")
print("No of vowels in sentence\t:",vowel_counter) 
print("-----------------------------------")
print("No of Uppercase in sentence\t:",uppercase_counter)   
print("-----------------------------------")    
print("No of spaces in sentence\t:",space_counter)
print("-----------------------------------")
print("No of Lowercase in sentence \t:",lowercase_counter) 
print("-----------------------------------")
print("No of digits in sentence\t:",digit_counter)
print("-----------------------------------")
print("No of words in sentence\t\t:",word_counter)
print("-----------------------------------")
        


