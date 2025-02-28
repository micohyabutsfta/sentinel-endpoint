# Use RunPod's recommended PyTorch image
# FROM runpod/pytorch:2.1.2-cuda12.1.1-devel
FROM huggingface/transformers-pytorch-gpu:4.37.0
# Set the working directory inside the container
WORKDIR /app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose the correct port for FastAPI
EXPOSE 8000

# Set the default command to start the server
CMD ["python3", "main.py"]
