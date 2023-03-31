FROM public.ecr.aws/lambda/python
LABEL Maintainer="Data Engineer 9000"

COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]
