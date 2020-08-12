try:
    print('Welcome to Letter Counter App')
    username = input('What is your Name? ').title().strip()
    print("Hello ", username, "!!")
    print("This app will count the number of times a specific letter occurs in a message")
    message = input("Enter a message: ").lower()
    countLetter = input("Which letter would you like to count the occurrence of? ").lower()
    noOfLetters = message.count(countLetter)
    print(f"Hey {username}, your message has {noOfLetters} {countLetter}'s in it!")
except Exception as err:
    print("Error occurred:", err)
