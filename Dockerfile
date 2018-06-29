# Use an official Python runtime as a parent image
FROM python:3.7-rc-slim

# Set the working directory to /app
WORKDIR /home/ahmed1smael/app_runtime

# Copy the current directory contents into the container at /app_runtime
ADD . /home/ahmed1smael/app_runtime

# Run app.py when the container launches
CMD ["python", "tic_tac_toe.py"]