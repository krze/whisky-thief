# Send an HTML email with an embedded image and a plain text message for
# email clients that don't want to display the HTML.

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
import datetime

class EmailSender:
    
    def send_files(self, files):
        # Define these once; use them twice!
        strFrom = 'whiskythief1@gmail.com'
        strTo = 'krze@tumblr.com'

        # Create the root message and fill in the from, to, and subject headers
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = 'ENEMY SPOTTED AT ' + str(datetime.datetime.now())
        msgRoot['From'] = strFrom
        msgRoot['To'] = strTo
        msgRoot.preamble = 'This is a multi-part message in MIME format.'

        # Encapsulate the plain and HTML versions of the message body in an
        # 'alternative' part, so message agents can decide which they want to display.
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)

        msgText = MIMEText('This is the alternative plain text message.')
        msgAlternative.attach(msgText)

        imageNum = 1
        msgHTML =''
        imgSrc = '<img src="cid:'
        
        for image_dir in files:
            fp = open(image_dir, 'rb')
            msgImage = MIMEImage(fp.read())
            fp.close()
            imageID = 'image' + str(imageNum)
                           
            msgImage.add_header('Content-ID', '<' + imageID + '>')
            msgRoot.attach(msgImage)
            msgHTML = msgHTML + '<br>' + imgSrc + imageID + '">'
            imageNum += 1
        
                # We reference the image in the IMG SRC attribute by the ID we give it below
        msgText = MIMEText(msgHTML, 'html')
        msgAlternative.attach(msgText)

        password = 'ello'

        with open('password', 'r') as fin:
            password = fin.read()

        # Send the email (this example assumes SMTP authentication is required)
        import smtplib
        smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #smtp.connect('smtp.gmail.com', 465)
        smtp.ehlo()
        smtp.login('whiskythief1@gmail.com', password)
        smtp.sendmail(strFrom, strTo, msgRoot.as_string())
        smtp.quit()
