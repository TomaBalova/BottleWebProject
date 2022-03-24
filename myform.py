from bottle import post, request 
@post('/home', method='post') 


def my_form(): 
    mail = request.forms.get('ADRESS') 
    mess = request.forms.get('QUEST')
    
    if ((mail and mail != '') and (mess and mess != '')): return howEmail(mail)
    else:
       errormess = "Zapolnite vse polya pered otpravkoi formi"

       return errormess
import re

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})$')
def howEmail(mail):
    if re.fullmatch(regex, mail):
      return "Thanks! The answer will be sent to the mail %s" % mail
    else:
      return "Invalid email"