
  create or replace   view iap_dev.float.stg_customers
  
   as (
    with source as (
    select * from iap_dev.float.raw_customers

),

renamed as (

    select
        id as customer_id,
        first_name,
        last_name

    from source

)

select * from renamed
  );

