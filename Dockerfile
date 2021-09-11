FROM python:3.8
COPY . .
RUN pip install -r requirments.txt
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "-k", "uvicorn.workers.UvicornH11Worker"]