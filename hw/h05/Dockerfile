FROM svizor/zoomcamp-model:3.11.5-slim

# Set working directory
WORKDIR ./

# Install dependencies
RUN pip install pipenv

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock ./
COPY model1.bin dv.bin ./
# Install the dependencies
RUN pipenv install --deploy 

# Copy flask app
COPY app.py .

# Expose the port 9696
EXPOSE 9696

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:9696", "app:app"]
