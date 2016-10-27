FROM python:2.7

RUN mkdir app
WORKDIR app

COPY requirements requirements
RUN pip install -r requirements/prod.txt

COPY . .

CMD ./run.sh
