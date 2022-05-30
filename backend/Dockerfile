FROM python:3.9

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /opt/app
COPY src/app .

EXPOSE 80
ENV CONFIG_FILE="server/config/develop.json"

CMD ["python", "app.py"]