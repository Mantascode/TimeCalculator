def add_time(*args):

    start_in_minutes = args[0].split(':')
    check_am_pm = start_in_minutes[1].split(' ')
    if check_am_pm[1] == 'AM':
        start_in_minutes = int(start_in_minutes[0]) * 60 + int(check_am_pm[0])
    else:
        start_in_minutes = (int(start_in_minutes[0]) + 12) * 60 + int(check_am_pm[0])

    duration_in_minutes = args[1].split(':')
    duration_in_minutes = int(duration_in_minutes[0]) * 60 + int(duration_in_minutes[1])

    new_time_in_minutes = start_in_minutes + duration_in_minutes
    days = new_time_in_minutes // 1440
    hours = (new_time_in_minutes - days * 1440) // 60
    minutes = (new_time_in_minutes - days * 1440) % 60

    if days == 1:
        days_text = ' (next day)'
    elif days > 1:
        days_text = f' ({days} days later)'
    else:
        days_text = ''

    if hours > 12:
        hours_text = hours - 12
        if minutes < 10:
            minutes_text = f'0{minutes} PM'
        else:
            minutes_text = f'{minutes} PM'
    elif hours == 12:
        hours_text = hours
        if minutes < 10:
            minutes_text = f'0{minutes} PM'
        else:
            minutes_text = f'{minutes} PM'
    elif hours == 0:
        hours_text = 12
        if minutes < 10:
            minutes_text = f'0{minutes} AM'
        else:
            minutes_text = f'{minutes} AM'
    else:
        hours_text = hours
        if minutes < 10:
            minutes_text = f'0{minutes} AM'
        else:
            minutes_text = f'{minutes} AM'

    if len(args) == 3:
        days_week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

        given_day = args[2].lower()

        if given_day in days_week:
            index = days_week.index(given_day)
            plus_days = days % 7
            new_week_day_index = index + plus_days

            if new_week_day_index > 6:
                new_week_day_index = new_week_day_index - 7

            new_week_day = days_week[new_week_day_index].capitalize()

        result = f'{hours_text}:{minutes_text}, {new_week_day}{days_text}'
        return result

    else:
        result = f'{hours_text}:{minutes_text}{days_text}'
        return result

print(add_time('11:59 PM', '24:05', 'WednESday'))