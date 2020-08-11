# set base image
FROM python:3.7

# set the working directory in the contianer
WORKDIR /code

# copy the dependencies to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD ["python", "./palomar_observatory.py"]
