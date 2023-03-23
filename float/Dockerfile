FROM public.ecr.aws/lambda/python
LABEL Maintainer="Data Engineer 9000"

ENV ENV dev
ENV PROJECT_NAME float
ENV INSTALL_PATH /usr/src/app

RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
RUN chmod 755 run_dbt.sh
# we run everything through sh, so we can execute all we'd like
ENTRYPOINT [ "/bin/sh", "-c" ]
CMD ["./run_dbt.sh"]
