from datetime import datetime


def days_to_birthday(user_date):

    current_date = datetime.now()
    user_date = user_date.replace(year = current_date.year)
    delta_days = user_date - current_date
        
    if 0 < delta_days.days:
        return f'Лишилось до Дня народження: {delta_days.days} днів.'
    else:
        user_date = user_date.replace(year=user_date.year + 1)
        delta_days = user_date - current_date
        if 0 < delta_days.days:
            return f'Лишилось до Дня народження: {delta_days.days} днів.'


birthday = input('Please, input date in format dd/mm/yyyy ')

try:
    date_birthday = datetime.strptime(birthday, '%d/%m/%Y')
    days_to_birthday(date_birthday)
except ValueError:
    print (f'Please, input date in format dd/mm/yyyy ')
