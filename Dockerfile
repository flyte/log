FROM python:3.8-alpine

COPY log.py /log.py

CMD [ "python", "/log.py" ]
