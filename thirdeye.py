import requests, json
import sys
from colorama import Fore
bold = '\033[01m'
print (Fore.RED+"""
               _________________________________        		                    
              |                                 |	
              |                                 |
       ▀▀█▀▀ ░█─░█ ▀█▀ ░█▀▀█ ░█▀▀▄ 　 ░█▀▀▀ ░█──░█ ░█▀▀▀ 
       ─░█── ░█▀▀█ ░█─ ░█▄▄▀ ░█─░█ 　 ░█▀▀▀ ░█▄▄▄█ ░█▀▀▀ 
       ─░█── ░█─░█ ▄█▄ ░█─░█ ░█▄▄▀ 　 ░█▄▄▄ ──░█── ░█▄▄▄
              |                                 |	
              |                                 |		
              |_________________________________|		
             (___________________________________)		                                                  
                                                              v1.0
                                                   Coded By H1mzy0t1 :)
""")
print(Fore.YELLOW+bold+" /^\  A Monkey on your roof /^\ \n")
print(Fore.GREEN+bold+"(1) IP Geolocate ")
print("(2) My IP Geolocate")
print("(3) Domain Age Checker")
print("(4) Whois Lookup")
print("(5) Phone Number Info ")
print("(6) Email Verify ")
print("(7) Exit ")
inpt = str(input(Fore.RED+"[+] " ))
info = (Fore.RED+bold+ "GETTING YOUR INFO............../"+bold)
if inpt == "1":
  print("*If this field remains empty it will show your geolocation!")
  ip = str(input(Fore.BLUE+ "ENTER THE IP : "))
  api = "https://ipapi.co/"
  formate = "/json/"
  print(info)
  try:
    data = requests.get(api+ip+formate).json()	
    print(Fore.WHITE+ "IP Type :",data['version'])
    print("ISP :",data['org'])
    print("City :",data['city'])
    print("Region :",data['region'])
    print("Country :",data['country_name'])
    print("Country Code :",data['country'])
    print("Capital :",data['country_capital'])
    print("Postal :",data['postal'])
    print("Country Calling Code :",data['country_calling_code'])
    print("Currency Code :",data['currency'])
    print("Currency Name :",data['currency_name'])
    print("Country Population :",data['country_population'],"Approx")
  except requests.exceptions.ConnectionError as e:
    print (Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")
elif inpt == "2":
  api = "https://ipapi.co/"
  formate = "/json/"
  print(info)
  try:
    data = requests.get(api+formate).json()
    print(Fore.WHITE+bold+ "IP Type :" , data['version'])
    print("ISP :",data['org'])
    print("City :",data['city'])
    print("Region :",data['region'])
    print("Country :",data['country_name'])
    print("Country Code :",data['country'])
    print("Capital :",data['country_capital'])
    print("Postal :",data['postal'])
    print("Country Calling Code :",data['country_calling_code'])
    print("Currency Code :",data['currency'])
    print("Currency Name :",data['currency_name'])
    print("Country Population :",data['country_population'],"Approx")
           
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")
elif inpt == "3":
  domain = str(input(Fore.BLUE+ "ENTER THE DOMAIN : "))
  api = "https://input.payapi.io/v1/api/fraud/domain/"
  print(info)
  try:
    data = requests.get(api+domain).json()
    print(Fore.WHITE+bold+"Domain : ",data['domain'])
    print("Age :",data['result'],"Days old")
    print("Result :",data['message'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")
elif inpt =="4":
  domainw = str(input(Fore.RED+"ENTER THE DOMAIN : "))
  api2 = "https://api.ip2whois.com/v1?key=YG8PVA9QRQPEEIKQZXZ1H62UDD4GTXZB&domain="
  try:
    data = requests.get(api2+domainw).json()
    print(Fore.WHITE+bold+"Domain :",data['domain'])
    print("Age :",data['domain_age'])
    print("Created :",data['create_date'])
    print("Updated :",data['update_date'])
    print("Expire :",data['expire_date'])
    print("Registrar :", data['registrar'])
    print("Registrant :",data['registrant'])
    print("More info :",data['nameservers'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")
elif inpt == "5":
  print("*Use upper case for country code!") 
  code = str(input(Fore.BLUE+ "ENTER COUNTRY CODE : ")) 
  number = (input("ENTER THE NUMBER : "))
  api = "http://apilayer.net/api/validate?access_key=62cc0533d5b4f9966528d3c104353993&number="
  mid = "&country_code="
  last = "&format=1"
  print(info)
  try:
    data = requests.get(api+number+mid+code+last).json()
    print(Fore.WHITE+bold+"Operation STATUS :",data['valid'])
    print("Prifix :",data['country_prefix'])
    print("Country Code :",data['country_code'])
    print("Country Name :",data['country_name'])
    print("Region :",data['location'])
    print("Carrier :",data['carrier'])
    print("Line Type :",data['line_type'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")

elif inpt == "6":
  inp = (input(Fore.BLUE+bold+"ENTER THE EMAIL : "))
  api3 = "http://apilayer.net/api/check?access_key=5ff3c15f0f2d9227a166ed95b051d83f"
  api3l = "&email="
  print(info)
  try:
    data = requests.get(api3+api3l+inp).json()
    print(Fore.WHITE+"Email : ",data ['email'])
    print("User :",data['user'])
    print("Domain :",data['domain'])
    print("Format :",data['format_valid'])
    print("SMTP :",data['smtp_check'])
  except requests.exceptions.ConnectionError as e:
    print(Fore.RED+bold+"Please check your internet connection!")
  except:
    print (Fore.RED+bold+"SOMETHING WENT WRONG, PLEASE TRY AGAIN")

if inpt == "7":
  print("Exiting..../")
  sys.exit(0)
