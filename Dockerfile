FROM amazon/aws-lambda-python:3.8

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
EXPOSE 8080
CMD [ "app.py" ]]
ENTRYPOINT [ "python" ]