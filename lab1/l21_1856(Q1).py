
def remove_space(string):
 return string.replace(" ", "")

def remove_comma(string):
 return string.replace(",", "")

def change_alphabets(string):
  return string.lower()

def my_function(x): 
  return x[::-1]



print("Enter a string you want to check if it is a palindrome or not: ")
string_a=input()

string_a=remove_space(string_a) #removing spaces from string
string_a=remove_comma(string_a) #removing commas from string
string_a=change_alphabets(string_a) #changing alphabets of string to lower case
reversed = my_function(string_a)  #reversing the string and storing it to later compare to check if it is a paliondrome


if(reversed==string_a):
    print("String you entered is a palindrome ")
else:
    print("String you entered is not a palindrome")
