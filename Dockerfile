FROM nginx:1.21.6

COPY ./basic.py /home/

COPY ./homepage_template.html /home/

COPY ./run.sh /home/

WORKDIR /home

RUN apt update

RUN apt install python3-pip -y

RUN pip3 install requests

RUN apt install cron -y

RUN crontab -l | { cat; echo "* * * * * /usr/bin/python3 /home/basic.py >> /home/basic.log 2>&1"; } | crontab -

CMD sh /home/run.sh

EXPOSE 80