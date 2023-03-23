#!/bin/bash
set -e

echo "Exporting Snowflake credentials as environment variables to be used by dbt"

# should be changed for e.g. python script which retrieves env variables from Secret Manager and loads them to env variables
#source .env

echo "Running dbt:"
echo ""
dbt deps --profiles-dir ./dbt --project-dir ./dbt
echo ""
dbt debug --profiles-dir ./dbt --project-dir ./dbt
echo ""
dbt run --profiles-dir ./dbt --project-dir ./dbt
echo ""
dbt test --profiles-dir ./dbt --project-dir ./dbt
echo ""
dbt source freshness --profiles-dir ./dbt --project-dir ./dbt
dbt docs generate --profiles-dir ./dbt --project-dir ./dbt
echo ""

echo "Copying dbt outputs to s3://dbt-documentation-$ENV/$PROJECT_NAME/ for hosting"
aws s3 cp --recursive --exclude="*" --include="*.json" --include="*.html" dbt/target/\
    s3://dbt-documentation-$ENV/$PROJECT_NAME/