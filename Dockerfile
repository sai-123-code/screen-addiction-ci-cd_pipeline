FROM python:3.13-bookworm
WORKDIR /screenaddiction-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]