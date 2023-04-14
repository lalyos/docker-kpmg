FROM  python:3.9

RUN python -m pip install --upgrade pip
COPY requirements.txt /app/

WORKDIR /app
RUN pip install -r requirements.txt

COPY . /app/
EXPOSE 5000
ENV FLASK_ENV=development
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=1
CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0" ]