#!/bin/bash
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
enableXsrfProtection = false\n\
\n\
" > ~/.streamlit/config.toml

streamlit run main.py