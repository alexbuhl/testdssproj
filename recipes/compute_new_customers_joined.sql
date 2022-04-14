SELECT 
    "new_customers"."customer_id" AS "customer_id",
    "new_customers"."birth" AS "birth",
    "new_customers"."price_first_item_purchased" AS "price_first_item_purchased",
    "new_customers"."gender" AS "gender",
    "web_new_visitors"."ip" AS "ip",
    "web_new_visitors"."pages_visited" AS "pages_visited",
    "web_new_visitors"."campain" AS "campain"
  FROM "CUSTOMER_LIFETIME_VALUE_new_customers" "new_customers"
  LEFT JOIN "CUSTOMER_LIFETIME_VALUE_web_new_visitors" "web_new_visitors"
    ON "new_customers"."customer_id" = "web_new_visitors"."customer_id"