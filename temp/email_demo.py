import smtplib

sender = "x7maximus2486@gmail.com"  # Replace with your Mailtrap email
receiver = "akashmasaadi6@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a test e-mail message."""


with smtplib.SMTP("smtp.mailtrap.io", 587) as server:
    server.starttls()
    server.login("api", "e0ae880f0c97a485ab8098db5b58b667")
    server.sendmail(sender, receiver, message)
print('Email sent successfully!')
