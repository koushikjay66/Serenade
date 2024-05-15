FROM python:3.11


# Where in Continer ? 
WORKDIR /app

# Copy All the things in the work directory of the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 6000
ENV FLASK_APP=main.py

# Run main.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=6000"]