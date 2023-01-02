FROM python:3.10-slim

# Install requirements
COPY requirements.txt app/requirements.txt
WORKDIR /app
RUN pip install -r /app/requirements.txt
COPY ./src /app/src
RUN mkdir /pretrained

# Kick off download 
RUN ["python", "src/setup_model.py"]

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]