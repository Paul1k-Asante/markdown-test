#Let's start a coffee shop together! w're
# going to build a coffee shop using some new 
# python programming concepts!! 

#Let build a Robot Barista!!
#print(input("What is your name?"))

#variables is a method of storing data for reuse.

#  NB; What ever the input function takes from the user, it convert it into a string. 
# input("GH") = it first print out that 'GH' and accept input data by user.
# But ptint("GH") = only displays the info 'GH' and doesn't accept input from user.

# the input function input("What is your name?")
# It displays what is your name? and allow user to input their data 'Name'
# BUT does not print their 'name' out or displays it out
# It is print(input) and that when it officially displays the user 'name'

# NB; the print function does not allows input data or accept input from users
#  It only displays what the programmer tell it to display;
#  i.e. print("What is your name") but NO input
# SO therefore we says input("What is your name") and allows you to input it 
# But does not print it or displays it
# Therefore, finally; print(input) and What is 'input' = Your name
# print(input("What is your name")) = print out input of what is your name OR of the data
# issued by the user.# 
 
# Variable is a method of storing data for reuse.

# Again when input command comes before print command;
# it takes all the input command features "GH" and accept the user's data
# before it execute the print command function. 
          # 'this is it' ; and could be a print function 
# like input("Have it! \n)
# it display 'have it!' out and accept input of 'Have it' i.e. 'Thank You.' from user. 
# the input can be in the variable i.e. Container = input("Have it")
# This means the Container is the input of / after Have it by the user
# which maybe input("Have it") is Thank you
# so Container is Thank You. so everywher we see container  = 'Thank you' which is the reply.
# To know the type of data we are looking at;
# we use the function called 'type' by;
# tying print(type(variable))
# NB Very Well;
# What ever data a user input into the computer is a 'string'
#   so if price = 8 which is variable in integer
#   and  quantity = "10" The input data by user which is therefore a 'string'
#   so if total = price * quantity; is like int * string which means
#   8 tens or 8*"10", 8*"10", 8*"10"...."10" to 8 so 1010101010101010
#   OR 8 * "a" which is a to 8 times..... aaaaaaaa
# so we convert data 
# since it multipling; we have to change all vales to integer
# like this, so the string which is quantity is to be type like
#  price * int(quantity)  NB: integer because there is No "" in the ()
#  and int is in front int()
#NB; P = (13) is integer but if we want to make an integer a string
#   P = ("13")
# NB ; String ("Am in") + integer 4 is type Error:
# can only concatenate str to str but not str to int
# unless we convert it 
# Therefore ("Am in " + str(4))
# NB; To use the if function for the variable defined;
# the if function is to come under the variable defined.



print("Hello, Welcome to Network Coffee Shop!!")

name = input("What is your name?\n") 

if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today.")


menu = "Black Coffee, Espreeso,Latte, Rich"

print(name + ", what would you like from our menu today? Here are what we serving.\n\n" + menu) 


order = input("Make your selection.\n") 

if order == ("o"):
    print("ok")

else:
    print("sorry your order is not available")
    exit()

quantity = input("How many " + order + "'s would you like?\n")
price = 8
total = price * int(quantity)

print("\nThat sounds good " + name )
print("\nYour total is: $" + str(total))
print("\nThank You")
print("\nwe'll have your " + quantity + " " + order + "'s ready for you in a moment.")







