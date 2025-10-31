# use a small python base
FROM python:3.11-alpine

# set working dir
WORKDIR /app

# system deps for sqlite & building wheels
RUN apk add --no-cache gcc musl-dev linux-headers sqlite sqlite-dev

# copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY . .

# create empty sqlite DB file (permissions)
RUN python -c "from app import init_db; init_db(); print('db init done')"

# expose the app port
EXPOSE 8000

# run via gunicorn for production
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app", "--workers", "2"]
