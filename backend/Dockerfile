FROM python:3.9-slim

COPY src/requirements.txt .
RUN pip install -r requirements.txt && rm -rf requirements.txt

WORKDIR /opt/app
COPY src/alchemy_backend .

EXPOSE 80
ENV CONFIG_FILE="server/config/develop.json"

CMD ["python", "app.py"]