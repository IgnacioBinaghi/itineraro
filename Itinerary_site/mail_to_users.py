import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'binaghiignacio@gmail.com'
EMAIL_PASSWORD = 'lghlezkkfpnddkaw'




def sendEmail(email, text):
	msg = EmailMessage()
	msg['Subject'] = 'Your Personalized Itinerary'
	msg['From'] = 'binaghiignacio@gmail.com'
	msg['To'] = email
	msg.set_content(text, subtype='html')


	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
	    smtp.send_message(msg)
