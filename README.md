# 1. fastapi 세팅
## 1.1 가상환경 구축
python -m venv ./venv
source ../venv/bin/activate
## 1.2 기본 세팅
pip install --upgrade pip
pip install fastapi  
pip install uvicorn
pip install PyMySql
pip install python-dotenv

## 1.3 requirement 출력
pip freeze> requirements.txt 
## 1.4 시작
python -m uvicorn main:app --reload


# 2. docker file 작성
FROM python:3.9-alpine
WORKDIR /usr/src/server
COPY ./ /usr/src/server
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]

# 3. 도커 빌드 및 실행
## 3.1 명령어로 실행
### 3.1.1 빌드
m1(arm) ver  
    docker build -t namjoo11/api_server .   

amd64 ver  
    docker build --platform linux/amd64 -t namjoo11/api_server_amd64 . 

태그 바꾸길 원한다면  
    docker tag api_server namjoo11/api_server  

### 3.1.2 Run
docker run --name fastapi -dp 8000:8000 namjoo11/api_server 

확인해보기  
docker exec -it fastapi /bin/sh

## 3.2 docker compose로 키기
sudo apt install -y docker-compose

build 와 이미지 중 하나만 선택
build는 이미지 없이 소스코드로 운영 됨
### 3.2.1 docker compose.yml 작성

version: '3'

services:
  fastapi:
    build: 
      context: api_server
      # dockerfile: dockerfile # 개발용 도커파일을 따로 뺼떄 쓰는듯
    container_name: fastapi
    # image: namjoo11/api_server  #build와는 같이 쓰지 않는 듯
    restart: always
    ports:
      - 8000:8000
    volumes:
      - ./api_server:/usr/src/server

  react:
    build: 
      context: NJtrend
    #   dockerfile: NJtrend/dockerfile
    container_name: react
    # image: namjoo11/njtrend
    restart: always
    ports:
      - 3000:3000
    links:
      - fastapi
    depends_on:
      - fastapi
    volumes:
      - ./NJtrend:/usr/src/app

### 3.2.2 실행
docker-compose up  -d 

# 4. docker push
docker push namjoo11/api_server