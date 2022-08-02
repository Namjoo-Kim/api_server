# 가상환경 구축
python -m venv ./venv
source ../venv/bin/activate
# 기본 세팅
pip install fastapi  
pip install uvicorn

# requirement 출력
pip freeze> requirements.txt 
# 시작
python -m uvicorn main:app --reload

# dockerfile
docker build -t node-docker-test .   
docker run -dp 81:81 node-docker-test