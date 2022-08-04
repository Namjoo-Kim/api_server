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
docker build -t api_server .   
docker run -dp 8000:8000 api_server