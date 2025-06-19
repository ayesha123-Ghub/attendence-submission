import csv
from datetime import datetime

def mark_attendance(name):
    date_str = datetime.now().strftime('%Y-%m-%d')
    time_str = datetime.now().strftime('%H:%M:%S')
    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_str, time_str])
    print(f"Attendance marked for {name} at {time_str} on {date_str}")

def main():
    print("Welcome to the Attendance System")
    while True:
        name = input("Enter your name (or type 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        mark_attendance(name)

if __name__ == "__main__":
    main()
import csv
from datetime import datetime
