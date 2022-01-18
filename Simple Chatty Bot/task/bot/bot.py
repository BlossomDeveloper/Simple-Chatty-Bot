# Chat bot program

# define bot's name and year of birth
def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')

# ask user to remind her/his name

def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')

# guess age using age formula
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    user_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(user_age) + "; that's a good time to start programming!")

# ask user to input a number and show that the bot can count
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1

# test asking a question and given different options for user input
# if user don't got the correct answer ask to input a number again
def test(user):
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")

    user = int(input())
    while user != 2:
        print("Please, try again.")
        break
    else:
        print("Completed, have a nice day!")


def end():
    print('Congratulations, have a nice day!')

# call previous functions to see if they work

greet('Apash', '2022')  # change it as you need
remind_name()
guess_age()
count()
test(2)
end()
