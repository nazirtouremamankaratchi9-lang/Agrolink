FROM python:3.9
ENV DB_PASSWORD=AgroLink2024!
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
