FROM ermiry/pycerver:latest

WORKDIR /home/api

COPY . .

RUN pip3 install -r ./requirements.txt

CMD ["/bin/bash", "start.sh"]