FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
EXPOSE 8501

COPY . .

ENTRYPOINT sh setup.sh && streamlit run --server.port $PORT main.py