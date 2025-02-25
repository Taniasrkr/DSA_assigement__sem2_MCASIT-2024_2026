#Write a program that create a dictionary with the frequency of the
# vowels from an inputted string. For example: input:’institute’.
# Output:{‘i’:2,’u’:1,’e’:1}

class frequeuncy:
    def CountVowels(s):
        vowles='aeiou'
        frequeuncy = {}

        for char in s.lower():
            if char in vowles:
                frequeuncy[char]=frequeuncy.get(char, 0)+1
                
        return frequeuncy
        
    input_sting=input("enter a sting:  ")
    result = CountVowels(input_sting)
    print(result)

