1. put your own dbt project here
2. do not forget to include profiles.yml, look at the `jaffle shop` example
3. in `main.py` change the folder name: chdir("jaffle_shop") -> chdir("dbt_project")
4. important thing is to redirect outputs in `dbt_project.yml` to /tmp, because it's the only writable dir in AWS lambda container:
        packages-install-path: "/tmp/dbt_packages"
        log-path: "/tmp/logs"
        target-path: "/tmp/target"