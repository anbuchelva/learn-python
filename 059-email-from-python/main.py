import smtplib

my_email = "xyz@gmail.com"
my_password = "a strong password"
with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="abc@gmail.com",
        msg="Subject:Hello\n\nThis is a sample email from Python"
    )
