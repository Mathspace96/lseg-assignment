
from datetime import datetime
import requests

## fetch time from internet
time_url = 'http://worldtimeapi.org/api/timezone/'
time_zone = 'Asia/Colombo'

def read_time_api():
    url = time_url + time_zone
    res = requests.get(url)
    time = datetime.strptime(res.json()['datetime'], '%Y-%m-%dT%H:%M:%S.%f%z')
    return time

fetched_time = read_time_api()
print(f'fetched time: {fetched_time}')

## read local time
local_time = datetime.now()
print(f'local time: {local_time}')

## compare time


## pull container name
container = 'my_container'

## update home page
values = {
    'container': container, 
    'local_time': local_time, 
    'fetched_time': fetched_time
    }
with open('/home/homepage_template.html', 'r') as fin:
    template = fin.read()
    for key, value in values.items():
        print(f'{{{key}}}')
        template = template.replace(f'{{{key}}}', str(value))
    with open('/usr/share/nginx/html/index.html', 'w') as fout:
        fout.write(template)

print(f'home page updated.')

## send email
import smtplib
email = 'mathspacekr@gmail.com'
email_to = 'test@gmail.com'
password = 'xxxxxxxxxxxxxxxxxxxxxx'

def send_email(email, password, email_to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email_to, message)
    server.quit()

def send_status_email(status):
    message = f'Subject: Time Check\n\nTime check status of {container}: {status}.'
    send_email(email, password, email_to, message)
    print(f'email sent.')


## check result from home page
home_url = 'http://localhost/'

success = False
try:
    res = requests.get(home_url)
    success = res.status_code == 200
except Exception as e:
    print(f'error: {e}')

if success:
    print('home page ok.')
else:
    print('home page failed.')
    # send_status_email('failed')

 