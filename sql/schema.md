erDiagram
    DIM_CUSTOMER {
      int customer_key PK
      int customer_id UNIQUE
      varchar city
      date signup_date
    }
    DIM_DATE {
      date date_key PK
      int year
      int month
      int day
      int dow
    }
    FACT_ORDERS {
      int order_id PK
      int customer_key FK
      date order_date FK
      double amount
    }

    DIM_CUSTOMER ||--o{ FACT_ORDERS : "customer_key"
    DIM_DATE ||--o{ FACT_ORDERS : "order_date -> date_key"
