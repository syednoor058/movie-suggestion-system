mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORs = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml