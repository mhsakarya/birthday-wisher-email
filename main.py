import datetime as dt
import pandas as pd
import random as rd
import smtplib

MY_EMAIL = "mmanusx@gmail.com"
PASSWORD = "******"


# today = (today_month, today_day)
now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

# pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24

birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()} ## padas dataframlerde list comprehention bu şekilde yapılıyor
# data_row["month"] = data_row.month

#Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today in birthdays_dict:
    random_letter_num = rd.randint(1, 3)
    with open(f"letter_templates/letter_{random_letter_num}.txt","r") as file:
        letter_template = file.read()
        letter = letter_template.replace("[NAME]", birthdays_dict[today][0])

    persons_email = birthdays_dict[today][1] # Send the letter generated,to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
                            from_addr=MY_EMAIL,
                            to_addrs=persons_email,
                            msg=f"Subject: Happy Birthday\n\n{letter}"

        )



#If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp


# Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
#  Remember to call .starttls()
#  Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.




