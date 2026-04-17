mkdir -p .streamlit/
echo "[theme]
primaryColor='#ff851b'
backgroundColor='#001f3f'
secondaryBackgroundColor='#001529'
textColor='#ffffff'
font='sans serif'
[server]
headless = true
port = $PORT
enableCORS = false
" > .streamlit/config.toml
