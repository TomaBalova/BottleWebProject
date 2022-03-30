from bottle import post, request, template
@post('/home', method='post') 



def my_form(): 
    import pdb
    import json
    #Запись в переменные введенные на форме данные
    questions = {}
    email = request.forms.get('ADRESS') 
    mess = request.forms.get('QUEST')
    questions[email] = mess
    #Проверка на зполнение 
    if ((email and email != '') and (questions[email] and questions[email] != '')): 
        with open('dataJSON.txt', 'a') as outfile:
            json.dump(questions, outfile)
        return howEmail(email, mess)
    else:
       errormess = "Zapolnite vse polya pered otpravkoi formi"
       #pdb.set_trace()
       return errormess
    
import re

regex = re.compile(r'([a-zA-Z0-9]+[.-_])*[a-zA-Z0-9]+@[a-zA-Z0-9-]+(\.[A-Z|a-z]{2,})+') #Регулярное выражение для емаил
def howEmail(mail, mess):
    import pdb
    qestions = {}
    qestions[mail] = mess
    if re.fullmatch(regex, mail):
        #pdb.set_trace()
        return "Thanks! The answer will be sent to the mail %s" % mail
    else:
        #pdb.set_trace()
        return "Invalid email"