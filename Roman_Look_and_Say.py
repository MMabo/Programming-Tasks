##Repeating a numeral up to three times represents addition of the number.
##For example, III represents 1 + 1 + 1 = 3.
##Only I, X, C, and M can be repeated; V, L, and D cannot be, and there is no need to do so.


##IV	4 = 5 - 1
##IX	9 = 10 - 1
##XL	40 = 50 - 10
##XC	90 = 100 - 10
##CD	400 = 500 - 100
##CM	900 = 1000 - 100

def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num


user = input('')
user = user.split(' ')
#print(user)

numeral = user[0]
n = int(user[1])
for _ in range(n):
    roman_numerals = []

    char = numeral[0]
    index = 0
    roman_look_say = ''
    count = 0

    while index < len(numeral):
        #print(roman_numerals)
        #print(index)
        if char == numeral[index]:
            count += 1
        else:
            roman_numerals.append(int_to_Roman(count))
            roman_numerals.append(char)
            char = numeral[index]
            count = 1
        index += 1

    roman_numerals.append(int_to_Roman(count))
    roman_numerals.append(char)

    roman_look_say = ''.join(roman_numerals)
    numeral = roman_look_say
#print(roman_look_say)

print(roman_look_say.count('I'),roman_look_say.count('V'))
