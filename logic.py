total_days = int(input("Gimme your total play days: "))
total_hours = int(input("Gimme your total play hours: "))
total_minutes = int(input("Gimme your total play minutes: "))

# Umrechnung in Stunden
total_playtime_hours = total_days * 24 + total_hours + total_minutes / 60

print(f"Okay, Nerd. Let's see how many hours you have spent on this game: {total_playtime_hours:.2f} hours.")
