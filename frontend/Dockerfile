FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
EXPOSE 8501

COPY . .

RUN chmod +x ./run_streamlit.sh

ENTRYPOINT [ "./run_streamlit.sh" ]