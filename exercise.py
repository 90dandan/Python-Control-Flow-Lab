# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()

if letter in 'aeiou':
    print(f'the letter {letter} is a vowel')
else:
    print(f'the letter {letter} is a consonant')   


# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = ''

while phrase != 'quit':
    phrase = input('Please enter a word or phrase:')
    print(f'What you entered is {len(phrase)} characters long') 

# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer


age = int(input("Input a dog's age in human years:"))
dog_age = 0
for year in range(1, age + 1):
    if year <= 2:
        dog_age += 10
    if year < 2:
        dog_age += 7
print(f"The dog's age in dog years is {dog_age}")

# if age < 3:
#     dog_age = age+10
# else:
#     dog_age = 20 + (age - 2) * 7



# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


print('Enter the lengths of three side of a triangle:')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a == b == c:
    triangle_type = 'equalateral'
elif a != b or b != c or a != c:
    triangle_type = 'scalene'
else:
    triangle_type = 'isosceles'

print(f'A triangle with sides of {a}, {b} & {c} is a equalateral triangle')


# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hint: The next number is found by adding the two numbers before it


fib = [0, 1]
for i in range(0, 51):
    fib.append(fib[1] + fib[i + 1])
    print(f'term: {i} / number: {fib[i]}')


# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input(f'Enter the month of the year (Jan - Dec: ').lower()
day = int(input(f'Enter the day of the month: '))

if month in ('jan', 'feb', 'mar'):
    if month == 'mar' and day > 19:
        season = 'Spring'
    else:
        season = 'Winter'
elif month in ('apr', 'may', 'jun'):
    if month == 'jun' and day > 20:
        season = 'Summer'
    else:
        season = 'Spring'
elif month in ('jul', 'aug', 'sep'):
    if month == 'sep' and day > 21:
        season = 'Fall'
    else:
        season = 'Summer'
elif month == 'dec' and day > 20:
    season = 'Winter'
else:
    season = 'Fall'

print(f'{month} {day} is in {season}')