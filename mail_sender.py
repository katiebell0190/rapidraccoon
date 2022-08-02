import smtplib
import getpass

#doesn't work yet
#could have a list of addresses #include server/port
def sendmail(from_addr,to_addr_list,cc_address_list, 
            subject, message, login, password,
            smtpserver="smtp.office365.com:587"):


            #this is info about the email header 
            header = 'From: %s\n' %from_addr
            header += 'To: %s\n' %','.join(to_addr_list)
            header += 'Cc: %s\n' % ','.join(cc_address_list)
            header += 'Subject: %s\n' % subject
             
            #this is info about the server
            server = smtplib.SMTP(smtpserver)
            server.starttls()
            server.login(login,password)
            server.send_message(from_addr,to_addr_list,message)
            server.quit()
            print('Email Sent')
pwd = getpass.getpass(prompt='Enter password: ')

sendmail(from_addr='katieb0190@outlook.com',
        to_addr_list=['katieb0190@outlook.com', 'katiebell0190@gmail.com'],
        cc_address_list= 'katiebell0190@gmail.com',
        subject= 'New mail from VSCode',
        message = 'Hello, this is my first email sent automatically',
        login='katieb0190@outlook.com',
        password= pwd)
