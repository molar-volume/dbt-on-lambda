FROM public.ecr.aws/lambda/python
LABEL Maintainer="Data Engineer 9000"

WORKDIR ${LAMBDA_TASK_ROOT}

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

CMD ["main.handler"]