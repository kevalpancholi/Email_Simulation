# An email simulation
class Email:
    # Creating four class variables
    def __init__(self, email_contents, from_address):
        self.has_been_read = False
        self.email_contents = email_contents
        self.is_spam = False
        self.from_address = from_address

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

# Create a new email object and add that to the inbox list
def add_email(email_contents, from_address):
    email = Email(email_contents, from_address)
    inbox.append(email)

def get_count():
    return len(inbox)

# Read the desired email by selecting the corresponding index and mark it as read after
def get_email(i):
    email = inbox[i]
    email.mark_as_read()
    return email

# Get all the unread emails
def get_unread_emails():
    return [email for email in inbox if not email.has_been_read]

# Get all the spam emails
def get_spam_emails():
    return [email for email in inbox if email.is_spam]

# Delete the email corresponding to the index
def delete(i):
    del inbox[i]

inbox = []

# Create 4 dummy emails
add_email("Hello, how are you?", "john@example.com")
add_email("Yo, how are you?", "kevin@example.com")
add_email("Yello, how are you?", "gertrude@example.com")
add_email("Hi, how are you?", "joella@example.com")

user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/delete/quit?")
    user_choice_lower = user_choice.lower()
    if user_choice_lower == "read":
        # Read email
        if not inbox:
            print("There are no emails in the inbox.")
            continue

        for i, email in enumerate(inbox):
            print(f"{i}: From: {email.from_address}")

        index = int(input("Enter the index of the email you want to read: "))
        email = get_email(index)
        print(f"From: {email.from_address}")
        print(email.email_contents)
    elif user_choice_lower == "mark spam":
        # Mark email as spam
        if not inbox:
            print("There are no emails in the inbox.")
            continue

        for i, email in enumerate(inbox):
            print(f"{i}: From: {email.from_address}")

        index = int(input("Enter the index of the email you want to mark as spam: "))
        email = inbox[index]
        email.mark_as_spam()
        print("Email marked as spam.")
    elif user_choice_lower == "delete":
        # Delete an email
        if not inbox:
            print("There are no emails in the inbox.")
            continue

        for i, email in enumerate(inbox):
            print(f"{i}: From: {email.from_address}")

        index = int(input("Enter the index of the email you want to delete: "))
        delete(index)
        print("Email deleted.")
    elif user_choice_lower == "quit":
        # Quit
        print("Goodbye")
        break
    else:
        print("Oops - incorrect input")

# print(get_count())
# print(get_spam_emails())
# print(get_unread_emails())