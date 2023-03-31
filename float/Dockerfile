FROM public.ecr.aws/lambda/python
LABEL Maintainer="Data Engineer 9000"

ENV ENV dev
ENV PROJECT_NAME float
# ENV INSTALL_PATH /usr/src/app

# RUN mkdir -p $INSTALL_PATH
# WORKDIR $INSTALL_PATH

COPY requirements.txt .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]
