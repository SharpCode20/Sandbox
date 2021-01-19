# Python program to unscramble words. 
# Searches through text file.
   
# opening the text file 
with open('C:/Users/ryans/Pictures/wordlist.txt','r') as file:

    # Input scrambled word.
    s = input('Input scrambled word: ')
    print(s)
   
    # reading each line     
    for line in file:

        for word in line.split():
       
            if s == "":
                print[s]
            else:
                ans = []
                for an in s[1:]:
                    for pos in range(len(an)+1):
                            ans.append(an[:pos]+s[0]+an[pos:])
                            print(ans)
