# API Endpoints Documentation

## 1. `/top-customers`
- **Method**: `GET`
- **Description**: Returns the top customers based on the total amount spent/spending.
- **Request Parameters**: None.
- **Response Example**:

```json
[
  {
    "name": "Alice Smith",
    "total_spent": "1671.00"
  },
  {
    "name": "Charlie Zhang",
    "total_spent": "1200.00"
  },
  {
    "name": "Bob Jones",
    "total_spent": "800.00"
  }
]
```

## 2. `/monthly-sales`
- **Method**: `GET`
- **Description**:Returns the total sales for each month.
- **Request Parameters**: None.
- **Response Example**:

```json
[
  {
    "month": "2023-11",
    "total_sales": "1371.00"
  },
  {
    "month": "2023-12",
    "total_sales": "300.00"
  }
]
```


## 3. `/products-never-ordered`
- **Method**: `GET`
- **Description**: Returns a list of products that have never been ordered.
- **Request Parameters**: None.
- **Response Example**:

[]

## 4. `/avg-order-value`
- **Method**: `GET`
- **Description**: Returns the average order value grouped by country
- **Request Parameters**: None.
- **Response Example**:

```json
[
  {
    "avg_order_value": "835.500000",
    "country": "USA"
  },
  {
    "avg_order_value": "800.000000",
    "country": "Canada"
  },
  {
    "avg_order_value": "1200.000000",
    "country": "UK"
  }
]
```


## 5. `/frequent-buyers`
- **Method**: `GET`
- **Description**: Returns customers who have placed more than one order
- **Request Parameters**: None.
- **Response Example**:

```json
[
  {
    "name": "Alice Smith",
    "order_count": 2
  }
]
```
