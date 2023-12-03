FROM python:3.12

RUN pip install numpy

ADD entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD /entrypoint.sh
VOLUME /code
WORKDIR /code