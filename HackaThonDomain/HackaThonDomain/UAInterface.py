import idna
import re
import requests
import dnspython as dns
import dns.resolver
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def binary_search(a, x, lo=0, hi=None):
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        midval = a[mid]
        if midval < x:
            lo = mid+1
        elif midval > x: 
            hi = mid
        else:
            return mid
    return -1

def checkEmail(email):
    domain_name = email.split('@')[1]
    pattern = re.compile(r'^\w+@(\w+\.)\w+')
    valid = pattern.match(email)
    if (valid == None) or (len(domain_name) > 63):
        return False
    try:
        #ignore sertificates and warnings
        requests.packages.urllib3.disable_warnings()
        #get mx label of domain
        valid_TLD_flag = checkTLD(domain_name.split('.')[-1])
        #valid_domain_flag = requests.get('https://'+domain_name, allow_redirects=False, verify=False).status_code < 400
        valid_mx_flag = dns.resolver.resolve(".".join(domain_name.split('.')[-2:]), 'MX') 
        return  valid_mx_flag and valid_TLD_flag
    except:
        return False

def checkTLD(tld):
    s = requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt')
    s.encoding = 'utf-8'
    _list = sorted([idna.encode(i, uts46=True, transitional=True) for i in s.text.lower().split('\n')[1:-1]])
    input_text = idna.encode(tld, uts46=True, transitional=True)
    return binary_search(_list, input_text, 0, len(_list)) > 0

def sendmessage():
    
    msg = MIMEMultipart(policy='utf-8')

    message = "Thank you"
    msg.attach(MIMEText(message, 'plain'))
    # setup the parameters of the message
    password = "bfd20380a6"
    msg['From'] = "sweetdreams2@тестовая-зона.рф"
    msg['To'] = "sweetdreams1@тестовая-зона.рф"
    msg['Subject'] = "Subscription"
    server = smtplib.SMTP_SSL(host='srv.ru', port=465)
    server.ehlo()
    server.esmtp_features["smtputf8"] = ""
    server.login(msg['From'], password)
    server.sendmail(msg['From'], msg['To'], msg.as_string())
    server.quit()
    
    # add in the message body
 
def show(email):
    return str(idna.decode(email))




if __name__=='__main__':
    string = input()
    while string != 'end':
        print(string, 'is valid? - ', checkEmail(string))
        string = input()
