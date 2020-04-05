import os
import requests, sys
from tkinter import *
from decimal import *
import random
from random import randint
import keyboard
import pyautogui
import time
from time import sleep
from colorama import init
from colorama import Fore, Back, Style
import webbrowser
import socket
import urllib.request
import json
import hashlib
from pif import get_public_ip
import shutil
from os import system
init()
MAIN_dIr = os.getcwd()
system('title start')
class main(object):
	'''тут короче скелет кода, правда я ваще забыл питон, будет трудно T_T поддержите уж меня...'''
	def __init__(self, name, age,gender, moder):
		self.name = name
		self.age = age
		self.moder = moder

	def pakejss(self):
		system('title install')
		print('у вас установленны пакеты?')
		print('а надо... Ну так и быть - вам помогу')
		os.startfile(MAIN_dIr+'/Textic/requests.py')
		sleep(8)
	def info(self):
		print('Your name :'+name)
		print('Age :'+str(age))
		print('your gender :'+gender)
		print('You :'+str(moder))
		print('\n\nAnd if you use my soft \n--------------------\n I love you, my dear friend\n\n')

	def Allinfo(self, moder):
		print('visit creator page and wait ten second')
		webbrowser.open_new_tab('https://vk.com/landlordravens')
		time.sleep(10)
		os.system('cls')
		print('this program - first script on this five mounth (and sory for English, it\'s...)')
		print('\a\a\anice time for sleep, yeah? -No')
		if moder == "Anime":
			webbrowser.open_new_tab('https://jut.su')
			print('it\'s for you , my '+moder)
		elif moder == "Game":
			webbrowser.open_new_tab('https://utorrentgames.org')
			print('it\'s for you , my '+moder)
		elif moder == "Music":
			webbrowser.open_new_tab('https://vk.com/music_omega')
			print('it\'s for you , my '+moder)
		elif moder == "Programmer":
			webbrowser.open_new_tab('https://proglib.io/p/python-oop/')
			print('it\'s for you , my '+moder)
		elif moder == "Hacker":
			webbrowser.open_new_tab('https://vk.com/grozny272ravens')
			print('it\'s for you , my '+moder)
		elif moder == "Diar":
			webbrowser.open_new_tab('https://vk.com')
			print('it\'s for you , my '+moder)
		else:
			print('чёт я ахуел, держи вылет')
			time.sleep(4)
			quit()
	def agecontrol(self,age):
		if age > 90:
			quit()
		elif age <10:
			quit()
		else:
			pass
	
	def menu(self):
		system('title menu')
		
		os.system('cls')
		print('Textic')
		print('repairsys')
		print('games')
		print('mySound')
		print('download')
		print('messeger')
		print('txt')
		print('oliver\nmy_info\nall_info')
		print('quit\n\n')
	def Textic(self):
		os.chdir(os.getcwd()+'/Textic')
		os.startfile('Texic2.8_DeveloperVersion.py')
		os.chdir(MAIN_dIr)
	def repairsys(self):
		print('запустите от имени админа, если можете')
		system('pause')
		system('title repairsys')
		system('chkdsk')
		print('подготовка к починке системы...')
		time.sleep(1)
		system('cls')
		system('color 73')
		print('скан файлов')
		system('tree')
		system('cls')
		print('тэкс, посмотрим что по серийникам...')
		system('wmic computersystem get model')
		system('wmic bios get serialnumber')
		print('собо красок не сыграло, чекаем дальше')
		time.sleep(1)
		system('ver')
		system('gpresult /R')
		system('verify')
		system('systeminfo')
		system('netstat -t')
		system('ipconfig')
		system('tree')
		system('ipconfig /flushdns')
		system('sfc /scannow')
		system('netstat –an')
		system('tasklist')
		system('openfiles')
		system('driverquery')
	def MySound(self):
		print(Fore.RED+'Yandex - private')
		print(Fore.BLUE+'VK - :-)')
		print(Fore.YELLOW+'SoundCloud - nice')
		webbrowser.open_new_tab('https://vk.com/wall496836599_274')
		webbrowser.open_new_tab('https://soundcloud.com/mr-robot-380773851')
	def download(self):
		menu.print1()
		menu.pakejss()
		webbrowser.open_new_tab('https://sun9-32.userapi.com/c846217/v846217554/18d570/cPoasemKihs.jpg')
		webbrowser.open_new_tab('https://download.sublimetext.com/Sublime%20Text%20Build%203211%20Setup.exe')
		webbrowser.open_new_tab('C:\ ')
		if sys.platform == "linux" or sys.platform == "linux2":
			webbrowser.open_new_tab('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.zip')
			system('git clone https://github.com/thelinuxchoice/shellphish.git')
			system('git clone https://github.com/foxlitegor/fisher.git')
		elif sys.platform == "darwin":
			webbrowser.open_new_tab('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-darwin-amd64.zip')
		elif sys.platform == "win32":
			webbrowser.open_new_tab('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-386.zip')
		else:
			webbrowser.open_new_tab('https://ngrok.com/download')

	def games1(self):
		print('1-ArcadeGame')
		print('2-WebGame')
		print('3-BonuseGame')
		
	def oliver_start(self):
		print('Oliver - it\'s math support))))')
		system('title oliter')
		break
		print('калькулятор')
		print('математический художник')

	def playinggame(self,gama):
		self.gama = gama
		if gama == 1:
			print('1)game1\n2)game2\n3)game3')
		elif gama == 2:
			print('1)game1\n2)game2')
		else:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('bonusegame.py')
			os.chdir(MAIN_dIr)
	def games(self,gama,number):
		self.number = number
		if gama == 1 and number == 1:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('game1.py')
			os.chdir(MAIN_dIr)
		elif gama == 1 and number == 2:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('game2.py')
			os.chdir(MAIN_dIr)
		elif gama == 1 and number == 3:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('game3.py')
			os.chdir(MAIN_dIr)
		elif gama == 2 and number ==1:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('wgame1.py')
			os.chdir(MAIN_dIr)
		elif gama == 2 and number == 2:
			os.chdir(os.getcwd()+'/Textic')
			os.startfile('wgame2.py')
			os.chdir(MAIN_dIr)
		else:
			print('Tы не то выбрал')
	def quit(self):
		system('title quit')
		print('good luck, bye-bye '+name)
		time.sleep(2)
		quit()

	def colors(self,Ui):
		self.Ui = Ui
		system('color 0'+str(Ui))
	def print1(self):
		print('##############################')
		print('###---#|##|##--##-----###-####')
		print('####|##|/#|#|##|###|####|#|###')
		print('####|##|#/|#|######|###|###|##')
		print('####|##|##|##--####|##|-----|#')
		print('####|##########|######|#####|#')
		print('###---######---#######|#####|#')
		print('##############################')
	'''чё тут вообще происходит? - спасити....'''



print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
name = os.getlogin()
os.system('cls')
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
age = int(input('age :/ '))
os.system('cls')
print(Fore.RED+'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n[1)male/2)female]')
gender= input('gender :/ ')
os.system('cls')
print('1-Anime')
print('2-Game')
print('3-Music')
print('4-prog.')
print('5-Hacker')
print('6-test')
moder = str(input('Choose your class:'))
print(moder)
if moder == "1":
	moder = r'''Anime'''
elif moder == "2":
	moder = r'''Game'''
elif moder == "3":
	moder = r'''Music'''
elif moder == "4":
	moder = r'''Programmer'''
elif moder == "5":
	moder = r'''Hacker'''
elif moder == "6":
	moder = r'''Diar'''
else:
	print('чёт я ахуел, держи вылет')
	time.sleep(4)
	quit()
if gender =="1":
	gender = r'''male'''
elif gender == "2":
	gender = r'''female'''
else:
	pass
os.system('cls')
menu = main(name, age,gender, moder)
print(menu.print1())
print('установить пакеты для firstscript.py ???')
Main_Vopr_Auto_Instal = input('[Y/N]')
Main_Vopr_Auto_Instal = Main_Vopr_Auto_Instal.upper()
if Main_Vopr_Auto_Instal == Y or Main_Vopr_Auto_Instal == "1":
	menu.pakejss()
	
else:
	print('как хочешь)))')
while True:
	menu.agecontrol(age)
	Ui = randint(1,8)
	menu.colors(Ui)
	Ui=Ui+1
	print(menu.menu())
	menu.colors(Ui)
	print('→Д→Р→Е→В→О→М→И→Р→А→К→О→Д→Е→Р→О→В→')
	menu.colors(Ui)
	stroka = input('@console:/')
	if stroka == '':
		menu.colors(Ui)
		print('опа, пасхалочка')
		print('\n\a\a\n\a\a\n\a')
	elif stroka == 'Textic':
		menu.colors(Ui)
		menu.Textic()
	elif stroka == 'quit':
		menu.colors(Ui)
		menu.quit()
	elif stroka == 'repairsys':
		menu.colors(Ui)
		menu.repairsys()
	elif stroka == 'games':
		menu.colors(Ui)
		menu.games1()
		gama= int(input('choose:'))
		#мотри ы ооп, это типа он выбрал категорию и щас выберет конкретный номер игры
		menu.playinggame(gama)
		if gama <3:
			gamenumber = int(input('choose number'))
			menu.games(gama,gamenumber)
		else:
			pass
	elif stroka == 'my_info':
		menu.info()
		system('pause')
	elif stroka == 'all_info':
		menu.Allinfo(moder)
		system('pause')
	elif stroka == 'MySound':
		menu.MySound()
	elif stroka == 'download':
		menu.download()
	elif stroka == 'messeger':
		menu.messeger()
	elif stroka == 'txt':
		menu.txt()
	elif stroka == 'oliver':
		menu.oliver()
	else:
		print(Fore.RED+'')
		print('uncnown comand')
		time.sleep(1)
