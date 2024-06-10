import os

# Initialize the diary dictionary
diary = {}

# Function to load diary from a text file
def load_diary(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for line in file:
                date, note = line.strip().split(':', 1)
                diary[date] = note

# Function to save diary to a text file
def save_diary(file_name):
    with open(file_name, 'w') as file:
        for date, note in diary.items():
            file.write(f"{date}:{note}\n")

# Function to validate date input
def get_valid_date():
    while True:
        try:
            day = int(input("\n\n---------------\nEnter Date (dd): "))
            month = int(input("Enter Month (mm): "))
            year = int(input("Enter Year (yyyy): "))
            print("\n---------------\n\n")
            if 1 <= day <= 31 and 1 <= month <= 12 and 2000 <= year <= 2025:
                date = f"{month:02d}-{day:02d}-{year}"
                return date
            else:
                print("\n\n---------------\nInvalid date. Please enter valid numbers for \nday (1-31),\nmonth (1-12), and\nyear (2000-2025).\n")
        except ValueError:
            print("\n\n---------------\nInvalid input. Please enter numbers only.\n")

# Function to add a new entry
def add_entry():
    while True:
        date = get_valid_date()
        confirm = input(f"\n\n---------------\nWriting on {date}\nYes? Press '1'\nNo? Press '2'\n")
        if confirm == '1':
            note = input("\n\n --------------- Enter your note: ---------------\n")
            diary[date] = note
            print("\n\n---------------\n!!! Note added successfully !!!\n---------------\n\n")
            break

# Function to show all dates
def show_dates():
    if diary:
        print("\n\n---------------\nDates you have written on:\n")
        for date in diary:
            print(date)
            print("---------------\n\n")
    else:
        print("\n\n---------------\nNo entries found.\n---------------\n\n")

# Function to show entry for a specific date
def show_entry():
    date = get_valid_date()
    if date in diary:
        print(f"\n\n---------------\nNote for {date}: {diary[date]}\n---------------\n\n")
    else:
        print("\n\n---------------\nNo entry found for this date.\n---------------\n\n")

# Function to delete an entry
def delete_entry():
    date = get_valid_date()
    if date in diary:
        del diary[date]
        print("\n\n---------------\nEntry deleted successfully.\n---------------\n\n")
    else:
        print("\n\n---------------\nNo entry found for this date.\n---------------\n\n")

# Main function to run the diary application
def main():
    file_name = 'diary.txt'
    load_diary(file_name)
    
    while True:
        print("\n\n---------------\n1. Show the list of dates you wrote.")
        print("2. Show your writing of a specific date")
        print("3. Write a new page")
        print("4. Delete a page")
        print("5. Press '0' to end the app\n---------------\n")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_dates()
        elif choice == '2':
            show_entry()
        elif choice == '3':
            add_entry()
        elif choice == '4':
            delete_entry()
        elif choice == '0':
            save_diary(file_name)
            print("\n\n---------------\nDiary saved.\nCreated by Nafiul Khalid with Love:)\nSee You Again!\n---------------\n\n")
            break
        else:
            print("\n--------------- Invalid choice. Please try again. ---------------\n")

if __name__ == "__main__":
    main()
