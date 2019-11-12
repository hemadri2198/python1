import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
# Authentication 
s.login("ashikaramesh@gmail.com", "password") 
  
# message to be sent 
message = """\
Subject: Testing
Hi
"""
  
# sending the mail 
s.sendmail("ashikaramesh98@gmail.com", "chandana.manjunath98@gmail.com", message) 
  
# terminating the session 
s.quit() 
