FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 8051

COPY . .
CMD ["streamlit", "run", "main.py"]
