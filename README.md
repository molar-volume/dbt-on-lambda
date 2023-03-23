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
2. Create python script that retrieves credentials for Snowflake.
3. See `run_dbt.sh` and uncomment 