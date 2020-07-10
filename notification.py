#!/usr/bin/python

import smtplib
from scrapper import global_data

if global_data:


    # sender address
    senderAddr = 'sarabjeet.mannu.singh@gmail.com'

    # receiver address
    receiverAddr = 'sarabjeet.mannu.singh@gmail.com'

    # message for email
    subject = "Subject: <Covid Daily Update> " + '\n'

    opening = "Hello There, Good Morning. " + '\n' + '\n'\
              "Please find below the current case report for Covid-19" + '\n' + '\n' + '\n'

    message = 'Global Cases: ' + global_data[0] + '\n' + \
               'Total Deaths: ' + global_data[1] + '\n' + \
               'Total Recovered :' + global_data[2] + '\n' + '\n' + '\n'

    closing = "Thanks for reading." + '\n' \
              + " Have a good day ahead."

    finalMessage = subject + opening + message + closing

    # email server,
    emailServer = smtplib.SMTP('smtp.gmail.com', 587)
    emailServer.starttls()

    # add own account login details,
    emailServer.login(senderAddr, "ixobipltldcktjex")

    # send the email
    emailServer.sendmail(senderAddr, receiverAddr, finalMessage)

    # disconnect from the server
    emailServer.quit()

else:
    print("ERROR!!")
