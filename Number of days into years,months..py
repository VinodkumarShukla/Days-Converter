def convert_days(days):
    # Calculate years, weeks, and days
    years = days // 365
    weeks = (days % 365) // 7
    remaining_days = (days % 365) % 7

    return years, weeks, remaining_days

# Example usage:
total_days = int(input("Enter the number of days: "))

# Convert days to years, weeks, and days
years, weeks, remaining_days = convert_days(total_days)

# Display the result
print(f"{total_days} days is approximately {years} years, {weeks} weeks, and {remaining_days} days.")