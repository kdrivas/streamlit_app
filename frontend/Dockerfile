FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
ENV SERVER_PORT=inference:8080

COPY . .
CMD sh setup.sh && streamlit run --server.port $PORT main.py