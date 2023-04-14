## Setup connection to AWS account
1. Create named profile for AWS cli https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
2. In `serverless.yml`, use profile created in step 1.

## Deploy to AWS
1. `sudo npm install -g serverless`
2. `sls deploy`
3. `sls --help` to learn other useful commands, e.g. sls remove

## Customize for your project
1. Replace `ambda/dbt_project` with your custom dbt project. Don't forget about `profiles.yml`.
2. Redirect outputs in `dbt_project.yml` to `/tmp`, because it's the only writable folder in AWS lambda container:
```
packages-install-path: "/tmp/dbt_packages"
log-path: "/tmp/logs"
target-path: "/tmp/target"
```
