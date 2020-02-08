FROM python:alpine

WORKDIR /usr/src/app

COPY flask_backend/requirements.txt ./
RUN apk update && apk add nginx && pip install --no-cache-dir -r requirements.txt && ln -sf /dev/stdout /var/log/nginx/access.log && ln -sf /dev/stderr /var/log/nginx/error.log
COPY deployment/nginx.conf /etc/nginx/nginx.conf
COPY flask_backend ./backend
COPY frontend/dist ./frontend

EXPOSE 8000

WORKDIR /usr/src/app/backend

CMD gunicorn -b 0.0.0.0:5000  --daemon app:app & nginx -g 'daemon off;'