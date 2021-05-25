FROM ermiry/pycerver:release-0.6.3

WORKDIR /home/api

COPY . .

RUN pip3 install -r ./requirements.txt

CMD ["/bin/bash", "start.sh"]