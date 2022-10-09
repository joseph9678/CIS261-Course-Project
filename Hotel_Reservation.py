from datetime import date, datetime
import locale

print('The Hotel Reservation program')

checking = 'y'
while checking.lower() == 'y':
    while True:
        try:
            arr_date_input = input('\nEnter arrival date (YYYY-MM-DD): ')
            formatted_arr_date = datetime.strptime(arr_date_input, "%Y-%m-%d")
        except ValueError:
            print('Invalid date format. Try again.\n')
            continue
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)
        if formatted_arr_date < today:
            print('Arrival date must be today or later. Try again.')
        else:
            break
    while True:
        try:
            dept_date_input = input('Enter departure date (YYYY-MM-DD): ')
            formatted_dept_date = datetime.strptime(dept_date_input, "%Y-%m-%d")
        except ValueError:
            print('Invalid date format. Try again.\n')
            continue
        if formatted_dept_date <= formatted_arr_date:
            print('Departure date must be after arrival date. Try again.\n')
        else:
            break
    rate = 85.0
    message = ''
    if formatted_arr_date.month == 8:
        rate = 105.0
        message = '(High Season)'
    number_of_nights = (formatted_dept_date - formatted_arr_date).days
    cost = number_of_nights*rate

    date_format = "%B %d, %Y"
    locale.setlocale(locale.LC_ALL, "en_US")
    print()
    print(f'Arrivale Date:  {formatted_arr_date:{date_format}}')
    print(f'Departure Date: {formatted_dept_date:{date_format}}')
    print(f'Nightly Rate:   {locale.currency(rate)} {message}')
    print(f'Total Nights:   {number_of_nights}')
    print(f'Total Price:    {locale.currency(cost)}\n')
    
    checking = input('Continue? (y/n): ')
print('\nBye!')
