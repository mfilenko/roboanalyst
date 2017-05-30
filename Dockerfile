FROM artursmet/python-2.7-node-6

RUN mkdir /roboanalyst
WORKDIR /roboanalyst
COPY . .
RUN pip install -r requirements.txt
RUN npm install

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
