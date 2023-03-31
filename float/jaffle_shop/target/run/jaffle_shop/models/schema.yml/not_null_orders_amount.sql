select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select amount
from iap_dev.float.orders
where amount is null



      
    ) dbt_internal_test