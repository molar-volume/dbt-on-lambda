
  create or replace   view iap_dev.float.stg_orders
  
   as (
    with source as (
    select * from iap_dev.float.raw_orders

),

renamed as (

    select
        id as order_id,
        user_id as customer_id,
        order_date,
        status

    from source

)

select * from renamed
  );
