FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
EXPOSE 8501

COPY . .
CMD sh setup.sh && streamlit run main.py --server.address=0.0.0.0