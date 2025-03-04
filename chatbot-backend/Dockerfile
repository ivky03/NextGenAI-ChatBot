# Use official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy dependencies first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose Cloud Run's default port (8080)
EXPOSE 8080

# ✅ Start FastAPI with Uvicorn on PORT 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
