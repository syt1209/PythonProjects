##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import smtplib
import datetime as dt
import pandas as pd

now = dt.datetime.now()
today = (now.month, now.day)

EMAIL = "ys.developer2020@gmail.com"
password = "0202repoleved.sy"
TO_EMAIL = "ys.developer2020@yahoo.com"

# Get the birthday data
birthday = tuple()
birthday_data = pd.read_csv("birthdays.csv")
birthday_dictionary = {(data_row.month, data_row.day): data_row for (index, data_row) in birthday_data.iterrows()}

template_number = [1, 2, 3]

# check date
if today in birthday_dictionary:
    name = birthday_dictionary[today]["name"]
    # Get a random message
    with open(f"letter_templates/letter_{random.choice(template_number)}.txt") as template:
        template_text = template.read()
    message = template_text.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, password)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject: Happy Birthday\n\n{message}")
