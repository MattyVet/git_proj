from datetime import datetime

name = input('Enter you name: ')

while True:
    date_str = input('Enter your date of birthday (dd.mm.YYYY): ')
    try:
        birth_date = datetime.striptime(date_str, "%d.%m.%Y")
        break
    except ValueError:
        print('Error: Invalid date format, using dd.mm.YYYY')

today = datetime.today()

age = today.year - birth_date.year
if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

n = int(input('Enter the number of greetings: '))

[print(f"Hello {name}!") for _ in range(n)]

print(['Your age: {age}', f'Happy birthday!!!\nNow your age: {age}'][(today.month, today.day) == (birth_date.month, birth_date.day)])
