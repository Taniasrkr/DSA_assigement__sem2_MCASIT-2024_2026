
# Write a function that takes a string as a parameter and returns a string
# with every successive repetitive character replaced with a star(*). For
# example, ‘balloon’ is returned as ‘bal*o*n’.

str=input("enter text : ")
dict={}

def replace_char(str):
    for i in range(len(str)-1):
        if str[i] in dict:
            str=str[:i]+ "*" + str[i+1:]
        dict[str[i]]=i
    return str

print(replace_char(str))