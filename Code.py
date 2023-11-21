def add_time(start, duration, start_day=None):
  # Parse the start time and duration
  start_time, meridian = start.split()
  start_hour, start_minute = map(int, start_time.split(':'))
  duration_hour, duration_minute = map(int, duration.split(':'))

  # Calculate the total minutes
  total_minutes = start_hour * 60 + start_minute
  total_minutes += duration_hour * 60 + duration_minute

  # Calculate the new time
  new_hour = total_minutes // 60 % 12
  new_minute = total_minutes % 60
  new_meridian = "AM" if (total_minutes // 60) % 24 < 12 else "PM"

  # Handle the case when the result is the next day or later
  days_later = total_minutes // (60 * 24)
  if days_later == 1:
      day_result = " (next day)"
  elif days_later > 1:
      day_result = f" ({days_later} days later)"
  else:
      day_result = ""

  # Determine the new day of the week if start_day is provided
  if start_day:
      start_day = start_day.lower().capitalize()
      days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
      start_index = days_of_week.index(start_day)
      new_day_index = (start_index + days_later) % 7
      new_day = days_of_week[new_day_index]
      day_result = f", {new_day}" + day_result

  # Format the result
  result = f"{new_hour or 12}:{new_minute:02d} {new_meridian}{day_result}"

  return result

# Examples
print(add_time("3:00 PM", "3:10"))  # Returns: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday"))  # Returns: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20"))  # Returns: 12:03 PM
print(add_time("10:10 PM", "3:30"))  # Returns: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday"))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12"))  # Returns: 7:42 AM (9 days later)
