import calendar
import datetime
import os
import json

# A dictionary to store notes, with date as key and note as value
notes = {}

# Get current year and month
now = datetime.datetime.now()
year = now.year
month = now.month

# File to store the last run month
LAST_RUN_FILE = "last_run_month.txt"
NOTES_FILE = "notes.json"

# Set the TERM environment variable if not already set
if 'TERM' not in os.environ:
    os.environ['TERM'] = 'xterm-256color'

# Function to check and reset notes if the month has changed
def check_and_reset_notes():
    global notes
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, "r") as file:
            last_run_month = int(file.read().strip())
            if last_run_month != month:
                notes = {}  # Clear notes
                print("Notes reset for the new month.")
    with open(LAST_RUN_FILE, "w") as file:
        file.write(str(month))

# Function to save notes to a file
def save_notes():
    global notes
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f)

# Function to load notes from a file
def load_notes():
    global notes
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)

# Call the functions at the start of the program
check_and_reset_notes()
load_notes()

# Color codes
GREEN = "\033[32m"  # Green text
YELLOW = "\033[33m"  # Yellow text
RED = "\033[31m"  # Red text
RESET = "\033[0m"  # Reset to default color

# Function to display the current month's calendar
def display_calendar():
    cal = calendar.TextCalendar(calendar.SUNDAY)
    month_days = cal.monthdayscalendar(year, month)

    print(f"    {calendar.month_name[month]} {year}")
    print("Su Mo Tu We Th Fr Sa")

    for week in month_days:
        for day in week:
            if day == 0:
                print("  ", end=" ")  # Empty day
            else:
                date = f"{month:02d}-{day:02d}-{year}"
                note_count = len(notes.get(f"{year}-{month:02d}-{day:02d}", []))
                if note_count == 1:
                    color = GREEN
                elif note_count == 2:
                    color = YELLOW
                elif note_count >= 3:
                    color = RED
                else:
                    color = RESET
                print(f"{color}{day:2d}{RESET}", end=" ")
        print()  # Newline at the end of the week


# Function to add a note to a specific day
def add_note():
    day = int(input("Enter the day to add a note: "))
    note = input("Enter your note: ")
    date = f"{year}-{month:02d}-{day:02d}"
    if date in notes:
        notes[date].append(note)
    else:
        notes[date] = [note]
    save_notes()
    clear_terminal()
    print(f"Note added successfully for {date}!")

# Function to view notes for a specific day
def view_notes():
    day = int(input("Enter the day to view notes: "))
    date = f"{month:02d}-{day:02d}-{year}"
    date_key = f"{year}-{month:02d}-{day:02d}"
    if date_key in notes:
        print(f"Notes for {date}: {notes[date_key]}")
    else:
        print(f"No notes found for {date}")

def clear_terminal():
    # Check the OS and run the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')

def display_all_notes():
    if not notes:
        print("No notes available.")
    else:
        for date, note_list in notes.items():
            day = int(date.split('-')[2])
            print(f"Notes for day {day}:")
            for index, note in enumerate(note_list, start=1):
                print(f"  {index}. {note}")

# Function to remove a note from a specific day
def remove_note():
    display_all_notes()
    user_input = input("Enter the day and index of the note to remove (format: day, index): ")
    try:
        day, note_index = map(int, user_input.split(','))
        date = f"{year}-{month:02d}-{day:02d}"
        if date in notes and 0 <= note_index - 1 < len(notes[date]):
            removed_note = notes[date].pop(note_index - 1)
            print(f"Removed note: {removed_note}")
            if not notes[date]:  # If no notes left for the date, remove the date key
                del notes[date]
            save_notes()
        else:
            print("Invalid day or index.")
    except ValueError:
        print("Invalid input format. Please enter in the format: day, index")

# Main loop to run the app
def notes_app():
    while True:
        display_calendar()
        print("\nWelcome to Terminal Notes")
        print("1. View Calendar")
        print("2. Add a Note")
        print("3. View a Note")
        print("4. Remove a Note")
        print("5. Display All Notes")
        print("6. Clear Display")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            clear_terminal()
        elif choice == '2':
            add_note()
        elif choice == '3':
            clear_terminal()
            view_notes()
        elif choice == '4':
            clear_terminal()
            remove_note()
        elif choice == '5':
            clear_terminal()
            display_all_notes()
        elif choice == '6':
            clear_terminal()
        elif choice in {'7', 'q', 'e', 'exit'}:
            clear_terminal()
            print("Notes reset at the end of the month.")
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    display_calendar()

if __name__ == "__main__":
    main()
