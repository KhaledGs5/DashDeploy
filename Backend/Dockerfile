# Use the official Python image
FROM python:3.9


# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Expose the port Django runs on
EXPOSE 8000

# Run the Django development server
# CMD ["python", "manage.py","runserver"]
