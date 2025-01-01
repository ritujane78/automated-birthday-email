##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()


data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")


def send_birthday_email(name, email):
    letter_numbers = [1,2,3]
    # print(email)
    with open(f"letter_templates/letter_{random.choice(letter_numbers)}.txt") as letter_file:
        letter = letter_file.read()
    final_letter = letter.replace("[NAME]", name)
    # print(final_letter)
    my_email = os.getenv("MY_EMAIL")
    password = os.getenv("PASSWORD")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject: Happy Birthday {name}\n\n {final_letter}")


now = dt.datetime.now()
for each_birthday in data_dict:
    if each_birthday["month"] == now.month and each_birthday["day"] == now.day:
        send_birthday_email(each_birthday["name"], each_birthday["email"])




