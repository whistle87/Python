time_seconds = int(input("Enter time in seconds: "))
time_minutes = time_seconds // 60
time_hours = time_minutes // 60
print(f'Time in format hh:mm:ss: {time_hours}:{time_minutes}:{time_seconds}')
