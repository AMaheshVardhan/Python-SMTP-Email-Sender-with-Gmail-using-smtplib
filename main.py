import smtplib
my_email = "From Email Address"
password = "Email Password"
connection = smtplib.SMTP("smtp.gmail.com") #Depends upon you mail id
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="to Email Address", msg="Subject:Hello\n\nEesaraina Poora")
connection.close()
