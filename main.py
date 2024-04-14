# Importing required modules
import pandas
import datetime as dt
import random
import smtplib

# Defining email credentials
MY_EMAIL = "nirav4141@hotmail.com"
PASSWORD = "Hostile#3456"

# Getting today's date
now = dt.datetime.now()
today_tuple = (now.month, now.day)
print(today_tuple)  # Printing today's month and day

# Reading birthday data from CSV file and converting it to a dictionary
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")

# Creating a dictionary with birthday dates as keys and corresponding data as values
new_dict = {(data["month"], data["day"]): data for data in data_dict}

# Checking if today's date matches any birthday in the data
if today_tuple in new_dict:
    # Extracting email details for the birthday person
    new_email = new_dict[today_tuple]["email"]

    # Selecting a random letter from available options
    letter_list = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
    random_letter_index = random.randint(0, 2)
    random_letter = letter_list[random_letter_index]

    # Reading the contents of the selected letter template
    with open(file=f"letter_templates/{random_letter}") as data:
        letter_text = data.read()
        receiver_name = new_dict[today_tuple]["name"]
        receiver_email = new_dict[today_tuple]["email"]

        # Customizing the letter with the birthday person's name
        new_letter = letter_text.replace("[NAME]", receiver_name)
        print(new_letter)  # Printing the customized letter

        # Sending the birthday email
        with smtplib.SMTP("smtp.office365.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{receiver_email}",
                msg=f"Subject: Happy Birthday {receiver_name}\n\n{new_letter}"
            )
