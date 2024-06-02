# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables to avoid user interaction during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Tesseract OCR and development libraries
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libtesseract-dev \
    python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the Streamlit app file into the container
COPY . /app

RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Install Streamlit and any other necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Streamlit port
EXPOSE 8501

# Command to run the Streamlit app
CMD ["streamlit", "run", "click.py"]
