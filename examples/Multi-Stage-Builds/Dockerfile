# stage1: Build Stage(Python Flask App)
FROM python:3.9-slim AS build-stage
WORKDIR /app
COPY flask-app/requirements.txt /app/
RUN pip install -r requirements.txt
COPY flask-app/ /app/
EXPOSE 5000
CMD ["python3", "app.py"]
# Stage 2: NGINX + Flask
FROM nginx:alpine AS production-stage
WORKDIR /etc/nginx
COPY nginx/nginx.conf nginx.conf
COPY --from=build-stage /app /app
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

