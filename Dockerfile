# 1. Start with a Python environment
FROM python:3.9-slim

# 2. Create a folder named 'app' inside the container to hold our files
WORKDIR /app

# 3. Copy the requirements file into the container
COPY requirements.txt .

# 4. Install the libraries (Pandas, Matplotlib, Seaborn) inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your script and your CSV file into the container
COPY . .

# 6. Tell Docker to run your script when the container starts
CMD ["python", "analysis.py"]