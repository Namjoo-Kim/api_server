# FROM python:3.9.13-alpine
FROM python:3.9.13-buster
WORKDIR /usr/src/server
COPY ./ /usr/src/server

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update -qqy --no-install-recommends && apt-get install -qqy --no-install-recommends google-chrome-stable
RUN pip install --no-cache-dir --upgrade pip

# RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "8000"]
# CMD ["python", "-m","uvicorn", "main:app","--reload", "--host","0.0.0.0"]
