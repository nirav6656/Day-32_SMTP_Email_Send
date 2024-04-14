##################### Normal Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day
MY_EMAIL = "nirav4141@hotmail.com"
PASSWORD = "Hostile#3456"
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)

now = dt.datetime.now()
today_tuple = (now.month,now.day)
print(today_tuple)

# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
# print(data_dict["month"])
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
new_dict = {(data["month"], data["day"]): data for data in data_dict}


#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:
if today_tuple in new_dict:
    new_email = new_dict[today_tuple]["email"]
    letter_list = ["letter_1.txt","letter_2.txt","letter_3.txt"]
    random_letter_index = random.randint(0,2)
    random_letter = letter_list[random_letter_index]
    print(random_letter)

    with open(file=f"letter_templates/{random_letter}") as data:
        letter_text = data.read()
        receiver_name = new_dict[today_tuple]["name"]
        receiver_email = new_dict[today_tuple]["email"]
        new_letter = letter_text.replace("[NAME]",receiver_name)
        print(new_letter)
        with smtplib.SMTP("smtp.office365.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=f"{receiver_email}",
                msg=f"Subject:Happy Birthday {receiver_name}\n\n{new_letter}"
            )

# random_letter_text =
# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.



