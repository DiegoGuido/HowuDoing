from termcolor import colored

print(colored( "\U00002585", 'red'), colored( "\U00002585", 'green'))


print('How u feelin 2day? (Enter the number)')

how = input('1.-Good \n2.-Bad \n')

number = int(how)

if number == 1:
    print(colored('\U00002585', 'green'))
elif number == 2:
    print(colored( "\U00002585", 'red'))
