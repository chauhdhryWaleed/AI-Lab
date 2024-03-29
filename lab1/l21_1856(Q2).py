
def remove_space(string):
 return string.replace(" ", "")

def remove_comma(string):
 return string.replace(",", "")

def change_alphabets(string):
  return string.lower()

def my_function(x):
  return x[::-1]



print("Enter a string")
string_a=input()

string_a=remove_space(string_a)
string_a=remove_comma(string_a)
string_a=change_alphabets(string_a)
reversed = my_function(string_a)

print(reversed)
print(string_a)

print(string_a==reversed)