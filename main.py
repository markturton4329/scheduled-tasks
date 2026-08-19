##################### Extra Hard Starting Project ######################
import smtplib, os
import pandas as pd
import random
import datetime as dt

APP_PASSWORD = os.environ['APP_PASSWORD']
USER_EMAIL = os.environ['USER_EMAIL']

try:
    datafile = pd.read_csv("./birthdays.csv")
    data_dict = datafile.to_dict("records")
except FileNotFoundError:
    data_dict = []

now = dt.datetime.now()

for data in data_dict:
    if now.day == data["day"] and now.month == data["month"]:
        letter_number = random.randint(1,3)
        filename = f"./letter_templates/letter_{letter_number}.txt"

        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
            lines[0] = lines[0].replace("[NAME]", data["name"])
            email_message = "".join(lines)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(USER_EMAIL, APP_PASSWORD)
            server.sendmail(USER_EMAIL,
                            data["email"],
                            f'Subject: Happy Birthday!\n\n{email_message}')

