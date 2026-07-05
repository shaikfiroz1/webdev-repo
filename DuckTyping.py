class EmailNotification:

        def send(self):
            print ("Sending email ")



class SMSNotification: 

        def send(self):
            print ("Sending SMS ")



def notify(notification):

    notification.send()

notify(SMSNotification())
notify(EmailNotification())
