FROM python:3.9-alpine
WORKDIR /api
COPY ./ ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 81
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "81"]

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
# FROM node:12-alpine
# WORKDIR /app
# COPY package*.json /app
# RUN npm install
# COPY . /app
# CMD [ "npm", "start" ]
# EXPOSE 8001