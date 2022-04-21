FROM public.ecr.aws/lambda/python:3.8

COPY app.py download_nltk.py requirements.txt ./

RUN python3.8 -m pip install -r requirements.txt -t . && \
    python3.8 download_nltk.py

# Command can be overwritten by providing a different command in the template directly.
CMD ["app.lambda_handler"]
