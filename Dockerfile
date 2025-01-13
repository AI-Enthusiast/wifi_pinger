FROM python
WORKDIR /ping_google
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "ping_google.py"]