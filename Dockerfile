FROM python:3.9.13-alpine
# FROM python:3.9.13-buster
WORKDIR /usr/src/server
COPY ./ /usr/src/server
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
# CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "8000"]
CMD ["python", "-m","uvicorn", "main:app","--reload", "--host", "0.0.0.0"]