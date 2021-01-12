import datetime as dt
import smtplib
import random

now = dt.datetime.now()
today = now.weekday()
my_email = "ys.developer2020@gmail.com"
password = "0202repoleved.sy"
to_email = "ys.developer2020@yahoo.com"


if today == 1:
    with open("quotes.txt", encoding='utf-8') as f:
        quotes = f.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email,
                            msg=f"Subject: Quote\n\n{quote}")
