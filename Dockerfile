FROM python:3.10-slim

# Install necessary packages
RUN apt-get update && \
    apt-get utils && \
    apt-get install -y --no-install-recommends && \
    apt-get install -y python3-pip

# Set working directory
ENV APP_HOME /project
WORKDIR $APP_HOME
COPY . /project

# Install dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the application
ENTRYPOINT ["python3", "manage.py", "runserver"]