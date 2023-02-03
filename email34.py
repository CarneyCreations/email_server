# Defining class and initiating it.
class Email(object):
    """ A class for adding email objects to a mailbox. """
    def __init__(self, from_address, email_contents,
                 has_been_read=False, is_spam=False):
        self.from_address = from_address
        self.email_contents = email_contents
        self.has_been_read = has_been_read
        self.is_spam = is_spam


    def __str__(self):
        """ Converts output from object to a string.
        :return: (str) Converted output.
        """
        output = f"\n{cyan}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{end}\n"
        output += f"{yellow}Senders address: {end}{self.from_address} \n"
        output += f"{yellow}Email contents: {end}{self.email_contents} \n"
        output += f"{yellow}Has been read: {end}{self.has_been_read} \n"
        output += f"{yellow}Spam mail: {end}{self.is_spam} \n"
        output += f"{cyan}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{end}"
        return output


    def get_has_been_read(self):
        """ Checks whether the email object has been read.
        :return: (bool) The object has been opened or not.
        """
        return self.has_been_read


    def set_mark_as_read(self):
        """ Reassigns the objects status from unread to opened/viewed.
        :return: (bool) Object has been viewed.
        """
        self.has_been_read = True
        return self.has_been_read


    def set_mark_as_spam(self):
        """ Reassigns the objects status confirming it is spam mail.
        :return: (bool) Object is spam.
        """
        self.is_spam = True
        return self.is_spam


def add_email():
    """ Asks for the new emails sender and content. This is then
    instantiated as a new object."""
    new_email_object = Email(input("Who sent the email: "),
                             input("Input the contents: "))
    inbox.append(new_email_object)
    return new_email_object


def get_count():
    """ Returns the total number of emails in the "inbox"."""
    return len(inbox)


def get_email(which_email):
    """ Returns a single, user specified email dictated by an input."""
    return inbox[which_email]


def get_unread_emails():
    """ Outputs all emails which are unopened."""
    unread_inbox = []
    for unread_email in inbox:
        if not unread_email.get_has_been_read():
            unread_inbox.append(unread_email)
    return unread_inbox


def get_spam_emails():
    """ Outputs any emails which have been marked as spam."""
    spam_list = []
    for spam_email in inbox:
        if spam_email.is_spam:
            spam_list.append(spam_email)
    return spam_list


def edit_menu(email_choice):
    """ Opens a menu where the user can delete an email or move it to the
    spam email folder.
    :param: (str) Users input of which email to edit.
    """
    edit_email = input(f"{red}1 :{end} Mark As Spam\n"
                       f"{red}2 :{end} Delete Email\n"
                       f"{red}3 :{end} Return To Main Menu\n"
                       ": ")
    # Mark as spam.
    if edit_email == "1":
        current_email.set_mark_as_spam()
        print(f"\n{green}Moved to the spam folder.{end}")

    # Delete email.
    elif edit_email == "2":
        delete = input(f"\n{red}Are you sure you wish to delete this email?"
                       f"{end} \nType {yellow}yes{end} if so: ").lower()
        if delete == "yes":
            inbox.pop(email_choice)
            print(f"{green}\nEmail has been deleted.{end}")
        print("\nReturning to the main menu.")


# Email objects.
email_one = Email("joshcarney@hotmail.co.uk", "Good afternoon young sir")
email_two = Email("d_burman@hotmail.co.uk", "Whats happening boy?!")
email_three = Email("richie_t@hotmail.co.uk", "How is programming going?")

inbox = [email_one, email_two, email_three]

menu_selection = ""
email_selection = 0

# Style modification variables.
pink = '\033[95m'
cyan = '\033[96m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
end = '\033[0m'
bold = '\033[1m'

# Calling email count function.
inbox_total = get_count()


while menu_selection != "quit":
    # Main menu page.
    print(f"\n{pink}>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>{end}")
    print("\t Joshua Carney's email service menu\n"
          f"{pink}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{end}\n"
          f"     {red} 1 :{end}  Inbox ({inbox_total}) \n"
          f"     {red} 2 :{end}  Import New Email \n"
          f"     {red} 3 :{end}  View Unread ({len(get_unread_emails())}) \n"
          f"     {red} 4 :{end}  View Spam Folder ({len(get_spam_emails())}) \n"
          f"     {red} 5 :{end}  Send \n"
          f"     {red} 6 :{end}  Quit ")
    menu_selection = input(f"{pink}"
                           f">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
                           f"{end}\nWhich email action would you like to "
                           f"perform?: ").lower()
    print(f"{pink}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<{end}\n")


    # Select and read an email which automatically gets marked as read later on.
    if menu_selection == "open inbox" or menu_selection == "1":
        print(f"{cyan}Inbox ({inbox_total} emails in total){end}")

        # Displays an email count alongside the email_contents of each message.
        view_email = [print(red, i, ":", end, e.email_contents)
                      for i, e in enumerate(inbox, start=1)]
        while True:
            try:
                email_selection = int(input("\nPlease select the email which "
                                            "you would like \nto open: "))
            except ValueError:
                print(f"\n{red}Please enter a number, "
                      f"no special characters or letters are allowed.{end}\n")
                continue

            if 0 < email_selection <= inbox_total:      # If entry is valid.
                break
            else:
                print(f"\n{red}Please enter a valid email number.{end}")

        converted_index = email_selection - 1
        current_email = inbox[converted_index]      # Assigned for readability.
        print(get_email(converted_index))           # Returns the chosen email.

        # Set the current, selected email as viewed.
        current_email.has_been_read = inbox[converted_index].set_mark_as_read()
        print(f"{green}Email status has been changed to {bold}read.{end}\n")

        # Calls the email edit menu using the users email_selection as a
        # parameter.
        edit_menu(email_selection)


    # Add a new email to the inbox.
    elif menu_selection == "import new email" or menu_selection == "2":
        print(f"{cyan}Import New Email{end}")
        add_email()
        print(f"{green}The new email has been successfully added to your inbox."
              f"{end}")


    # Prints out the contents of all unread emails.
    elif menu_selection == "3":
        print(f"{cyan}Unread Emails{end}")
        unread = [print(u) for u in get_unread_emails()]
        if len(get_unread_emails()) < 1:
            print(f"This folder is empty.")


    # Prints out all spam emails.
    elif menu_selection == "spam folder" or menu_selection == "4":
        print(f"{cyan}Spam Folder{end}")
        xo = [print(i) for i in get_spam_emails()]
        if len(get_spam_emails()) < 1:
            print(f"This folder is empty.")


    # Send an email.
    elif menu_selection == "send" or menu_selection == "5":
        print(f"{cyan}Outbox{end}")
        send_address = input("Who you would like to send a message to: ")
        send_content = input("What would you like to include in your message: ")
        print(f"{green}\nYour message has been sent to {send_address}.{end}")


    # Exit program.
    elif menu_selection == "quit" or menu_selection == "6":
        print("Goodbye")


    # Invalid menu selection.
    else:
        print(f"{red}Oops - incorrect input.{end}")
