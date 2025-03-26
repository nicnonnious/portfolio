workers = 4
bind = "0.0.0.0:$PORT"
timeout = 120
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
forwarded_allow_ips = '*'
accesslog = '-'
errorlog = '-' 