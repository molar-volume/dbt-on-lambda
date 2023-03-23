# iap-float-ingestion-dbt-flow-test

## Setup connection to AWS account
1. Create named profile for AWS cli https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
2. In `serverless.yml`, use profile created in step 1.

## Running locally
1. `sudo npm install -g serverless`
2. `sls deploy`
3. `sls --help` to learn other useful commands, e.g. sls remove

## Next steps
1. Create actual dbt project in `float/dbt`
2. Script `retrieve_sec.py` should retrieve Snowflake credentials from AWS Secret Manager and write them to `.env` file (see `run_dbt.sh`)

## Alternative approach
Instead of shell script `run_dbt.sh`, a python script can be created to run the DBT models.
Then you would have standard python lambda function.
1. Create `main.py` with lambda handler (which retrieves Snowflake secrets and run DBT code).
2. Modify Dockerfile (remove entrypoint and change `CMD ["main.handler"]` ).
