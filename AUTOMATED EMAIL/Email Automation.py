
from email.message import EmailMessage
from smtplib import SMTP_SSL
import ssl
from email.mime.application import MIMEApplication


sender = "benab2404@gmail.com" 
sender_password = ""
receivers = ["frankappiahboadu23@gmail.com","phlorence1967@gmail.com"]

subject = "APPLICATION FOR EMPLOYMENT AS INTERN"

body = """
IGNORE testing python automated emails

Dear Sir,
 
 
 
                    APPLICATION FOR EMPLOYMENT AS AN INTERN
I am Benjamin Appiah-Boadu, a second-year student at the Kwame Nkrumah University of Science and Technology (KNUST) studying BSc. Computer Engineering (current academic standing First Class Honors CWA ).
I would like to humbly request for an opportunity to work at your highly distinguished firm as an intern in order for me to gain hands-on experience and concurrently; utilize skills and knowledge obtained in computer engineering as well as strong communication & analytical skills acquired in my first year. 
I am an industrious, skillful and proactive individual with strong communication skills, interpersonal skills, analytical and information technology skills:with a high level of proficiency in the use of Microsoft Word, Excel, PowerPoint, Adobe Photoshop and Canva.
I am currently a silver badge in Python on Hacker rank. Furthermore, I have gained some intermediate proficiency in Web Development through React and JavaScript as well as Object Oriented Programming with C++
 I am a natural team player; possess great communication skills and would say I am a very fast learner.
Given my skills and knowledge picked up within my first year, I believe I would be a great fit for your organization; via the application of my skillset to help drive organizational profitability and growth. I am impressed by your track record of achievements and distinguished reputation, and I look forward to joining and contributing to your distinguished firm.
 
Thank you for your time and consideration, and I look forward to hearing from you.
 
Kind Regards,
Benjamin Appiah-Boadu
Email: benab2404@gmail.com 
Mobile: +233270005130 / +233555629019
 
LinkedIn: https://www.linkedin.com/in/bappiahboadu/



"""
fname = "Benjamin Appiah-Boadu CV NEW.pdf"

em = EmailMessage()

EmailMessage()['from'] = sender #passing sender to from parameter toEmail Meassage dioctionary
EmailMessage()['to'] = ','.join(receivers) #passing receiver to to parameter
EmailMessage()['Subject'] = subject
em.set_content(body) # setting content of the mail
"""
with open(file= fname,mode="r",encoding= 'Latin-1') as f:
    attachment = PyPDF2.PdfReader(fname)
    
    EmailMessage.add_attachment(attachment,subtype='pdf',filename=fname)   
"""    

#EmailMessage().set_content(body)
with open(fname, "rb") as f: # opening the file to be attached .
    attachment = MIMEApplication(f.read(), _subtype="pdf") #using the MIMEApplication class to read the pdf and indicating the type .pdf
    attachment.add_header('Content-Disposition', 'attachment', filename=fname)
    em.add_attachment(attachment)

context = ssl.create_default_context()



with  SMTP_SSL(host="smtp.gmail.com" ,port= 465 ,context= context ) as smtp :  #creatingg the SMTP server through host and port and context

    smtp.login(user=sender , password=sender_password) #logging in with username and passwprd of the sender
    smtp.send_message(em,sender,receivers) # contains message , sender address , and receiver address
    smtp.close()



    """
    
    try:
    with SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(sender, sender_password)
        smtp.send_message(em)
    print("Email sent successfully!")
except SMTPRecipientsRefused as e:
    print(f"Error: All recipient addresses were refused. {e.recipients}")
except Exception as e:
    print(f"An error occurred: {e}")

    
    
    """
