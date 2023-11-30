def add_time(start, duration, day=None):
    # Parse start time
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    
    # Parse duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate new time
    new_hour = start_hour + duration_hour
    new_minute = start_minute + duration_minute

    # Adjust for overflow (more than 60 minutes)
    if new_minute >= 60:
        new_hour += 1
        new_minute -= 60

    # Adjust for overflow (more than 12 hours)
    if new_hour >= 12:
        am_pm = "PM" if am_pm == "AM" else "AM"
        new_hour -= 12

    # Calculate days later
    days_later = 0
    while new_hour >= 24:
        new_hour -= 24
        days_later += 1

    # Calculate day of the week
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    if day:
        day = day.lower().capitalize()
        day_index = (days_of_week.index(day) + days_later) % 7
        new_day = days_of_week[day_index]
    else:
        new_day = None

    # Format the result
    result = f"{new_hour}:{new_minute:02} {am_pm}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    if new_day:
        result += f", {new_day}"

    return result
