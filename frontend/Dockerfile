FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT

COPY . .
CMD sh setup.sh && streamlit run main.py --server.address=0.0.0.0