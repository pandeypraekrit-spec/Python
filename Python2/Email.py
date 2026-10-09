email = input("Enter an email address: ")


if "@" in email and "." in email and " " not in email and not email.startswith("@"):
    print("Valid email")
else:
    print("Invalid email")