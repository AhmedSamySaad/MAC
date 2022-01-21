# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Configuring Virtual Environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#These commands install the cv2 dependencies that are normally present on the local machine
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# I commented the following two lines to run as a root user
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# Added timeout 600 because the inference is taking too long and the workers fail before returning a result
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--timeout", "600", "app:app"]
