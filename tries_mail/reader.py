import csv

# with open('csvexample.csv', newline='') as myFile:
#     reader = csv.reader(myFile)
#     for row in reader:
#         print(row)

def sendmail(attribute):
    name = attribute[0]
    email = attribute[1]
    print("Sending email to {}".format(email))

    # to = email
    # sender = "you.email@gmail.com"
    # subject = "subject"
    # msgPlain = ""
    # msgHtml = "Hi {},<br/>This is a test email".format(first_name)
    # print(sender, to, subject, msgHtml, msgPlain)


def main():
   with open("newcsvexample.csv", "r") as file:
        msg_reader = csv.reader(file, delimiter=',')
        # print(msg_reader)
        # msg_reader.next()
        
        for row in msg_reader:
            sendmail(row)
    return row        
    
            

if __name__ == '__main__':
    i=main()
    # get_credentials()