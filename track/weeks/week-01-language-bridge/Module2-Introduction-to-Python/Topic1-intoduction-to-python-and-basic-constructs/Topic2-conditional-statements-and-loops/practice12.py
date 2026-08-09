text=input("enter a text:")
vowel_count=0


for i in text:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        vowel_count+=1
print("Number of vowels:",vowel_count)