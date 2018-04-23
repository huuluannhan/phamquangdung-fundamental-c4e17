n=str(input("Write your sentence: "))
letter_counts={}
for letter in n:
    letter_counts[letter]=letter_counts.get(letter,0)+1
letter_items=list(letter_counts.items())
letter_items.sort()
print("Here are count of letters in your sentence: ")
for i in range(1,len(letter_items),1):
    k=list(letter_items[i])
    for j in range(len(k)):
        if j%2==0:
            print(k[j],": ",end="")
        else:
            print(k[j])
