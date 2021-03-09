FROM python:3.8-slim-buster

# Where everything goes  for things like COPY and CMD and RUN
WORKDIR /code

# Pip requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project
COPY src/ .

# Run the project
CMD ["python", "./main.py"]