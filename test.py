import pytesseract as pytes
from PIL import Image

from selenium import webdriver
import time

cd='C:\\Users\\theja\\Downloads\\chromedriver_win32\\chromedriver.exe'
driver=webdriver.Chrome(cd)


email = ""
password = ""

driver.get("https://www.tinkercad.com/dashboard")
time.sleep(2)

google = driver.find_element_by_xpath('//*[@id="content"]/div/main/ng-component/main/section/div/div/div/div/div[1]/a[2]/span[2]')
google.click()

driver.find_element_by_xpath('//*[@id="userName"]').send_keys(email)
user_next=driver.find_element_by_xpath('//*[@id="verify_user_btn"]')
user_next.click()  
time.sleep(2)

driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
pwd_next = driver.find_element_by_xpath('//*[@id="btnSubmit"]')
pwd_next.click()
time.sleep(5)

driver.get('https://www.tinkercad.com/things/ifpLsfTwlEr')
time.sleep(1)

#Tinker this
driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary"]').click()
time.sleep(2)


#Code
driver.find_element_by_id('CODE_EDITOR_ID').click()
time.sleep(2)

#Serial Monitor
driver.find_element_by_id('SERIAL_MONITOR_ID').click()
time.sleep(2)

#Simulate
driver.find_element_by_id('SIMULATION_ID').click()


def tinker(a):
    serial_input = driver.find_element_by_xpath('//div[@class="code_panel__serial__bottom js-code_panel__serial__bottom js-code_editor__serial-monitor__bottom clearfix"]/input')
    serial_input.send_keys(a) #  input high
    send = driver.find_element_by_xpath('//div[@class="code_panel__serial__bottom js-code_panel__serial__bottom js-code_editor__serial-monitor__bottom clearfix"]/div/a/div').click()

# extracting text form image
pytes.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# separating digits,vowels,consonants and special character


def password_extract(img):
    image = Image.open(img)
    text = pytes.image_to_string(image)
    #print(text)
    text_list = list(text)
    print(text_list)
    text_list.remove('\x0c')
    text_list.remove('\n')
    special_ch_list = []
    vowels_list = []
    consonant_list = []
    digits_list =[]
    for i in text_list:
        if i.isalpha():
            if (i== 'a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels_list.append(i)
            else:
                consonant_list.append(i)
        elif i.isdigit():
            digits_list.append(i)
        else:
            special_ch_list.append(i)
    

    #creating the password combination

    no_vowels = len(vowels_list)
    no_consonants = len(consonant_list)
    no_digits = len(digits_list)
    no_spclch = len(special_ch_list)

    return no_vowels,no_consonants,no_digits,no_spclch



time.sleep(10)
NV,NC,ND,NS = password_extract('to1.png')
print(NV)
print(NC)
print(ND)
print(NS)
print("\n")

flag = 0

if (NV == 3):
    flag = flag+1
    print(flag)
    tinker(1)
    time.sleep(4)
if (NC == 2):
    flag = flag+1
    print(flag)
    tinker(2)
    time.sleep(4)
if (ND == 2):
    flag = flag+1
    print(flag)
    tinker(3)
    time.sleep(4)
if (NS == 1):
    flag = flag+1
    print(flag)
    tinker(4)
print("checking code")
time.sleep(2)
if (flag == 4):
    print("door open")
    tinker(5)
else:
    print("wrong password")
    tinker(11)

print('\n')
time.sleep(15)
tinker(12)
time.sleep(5)

nv,nc,nd,ns = password_extract('close.jfif')
print(nv)
print(nc)
print(nd)
print(ns)
print("\n")

flag = 0

if (nv == 1):
    flag = flag+1
    print(flag)
    tinker(1)
    time.sleep(4)
if (nc == 2):
    flag = flag+1
    print(flag)
    tinker(2)
    time.sleep(4)
if (nd == 2):
    flag = flag+1
    print(flag)
    tinker(3)
    time.sleep(4)
if (ns == 3):
    flag = flag+1
    print(flag)
    tinker(4)
    time.sleep(4)
print("code checking") 
time.sleep(2)
if (flag == 4):
    print("door close")
    tinker(10)
else:
    print("wrong password")
    tinker(11)

time.sleep(20)
tinker(13)
