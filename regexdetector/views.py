from django.shortcuts import render

#! Python

'''
Programa que toma un texto copiado el el
cortapapeles, extrae todos los numeros de tel.
y direcciones de email que encuentre en el,
y por ultimo copia en el corta papeles
un string conteniendo solo los telefonos y los mails
'''

import re, pyperclip

def get_email_and_phone(request):
    #primero guardo el texto en una variable
    text = pyperclip.paste()

    #creo la regex para el numero de telefono y otra para email
    phoneRegex = re.compile(r'''(
        (\(?\+54\)?)?             #codigo de Argentina
        (\s*|-|\.)?         #separador
        (\(?\d{2,5}\)?)     #codigo de area
        (\s*|-|\.)          #separador
        (\d{3,5})           #caracteriztica
        (\s*|-|\.)?         #separador
        (\d{2,5})           #extension
    )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+   #usuario
        @
        [a-zA-Z0-9.-]+      #tipo de mail(gmail, outlook, yahoo, etc)
        (\.[a-zA-Z]{2,4}){1,3}   #punto y algo mas (ej: .com)
    )''', re.VERBOSE)

    #inicializo dos listas, una va a contener los
    #numeros de telefono y la otra las direcciones de email.

    phones = []
    emails = []

    #busco todos los match el el texto para cada Regex

    moPhone = phoneRegex.findall(text)

    moEmail = emailRegex.findall(text)

    #meto en las listas los matching objects correspondientes

    for number in moPhone:
        phones.append(number[0])

    for adress in moEmail:
        emails.append(adress[0])

    #creo una string para ser copiada en el cortapapeles
    #donde tenga toda la informacion extraida

    to_be_copied = 'Phone numbers:\n' + '\n'.join(phones)\
                    + '\n\nEmails:\n' + '\n'.join(emails)


    pyperclip.copy(to_be_copied)

    return render(request, 'matching.html', {'to_be_copied': to_be_copied})


def home(request):
    return render(request, 'home.html')