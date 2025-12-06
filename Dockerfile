# 1. Use official Python image (like a pre-built mini OS with Python)
FROM python:3.11-slim

# 2. Set working directory inside the container
WORKDIR /app

# 3. Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the project files into the container
COPY . .

# 5. Environment variable (API key will be passed when running the container)
ENV OPENAI_API_KEY=""

# 6. Default command to run when container starts
CMD ["python", "main.py"]
