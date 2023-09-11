age = input('enter your age')
#convert the string to int
your_age=int(age)
#determine the ticket price
if your_age<5:
    ticket_price=5
elif your_age < 16:
     ticket_price = 10
else:
     ticket_price=18
# show, the ticket price
print(f"you will pay${ticket_price}for the ticket")

