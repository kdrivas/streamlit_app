FROM python:3.8-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE $PORT
EXPOSE 8501

COPY . .

RUN mkdir -p ~/.streamlit/
RUN bash -c 'echo -e "\
[browser]\n\
serverAddress = whispering-peak-59110.herokuapp.com\n\
[server]\n\
headless = true\n\
enableXsrfProtection = false\n\
enableCORS = false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml'

RUN chmod +x ./run_streamlit.sh

ENTRYPOINT [ "./run_streamlit.sh" ]