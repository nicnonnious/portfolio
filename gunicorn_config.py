workers = 4
bind = "0.0.0.0:10000"
timeout = 120
worker_class = "sync"
forwarded_allow_ips = '*'
secure_scheme_headers = {'X-Forwarded-Proto': 'https'}
accesslog = "-"
errorlog = "-" 