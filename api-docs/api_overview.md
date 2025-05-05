# API Overview

This API provides various analytics , querying a MySQL database hosted on AWS RDS. The following functionalities are provided:

- **Top Customers**: Returns the top spending customers.
- **Monthly Sales**: Provides the total sales for each month.
- **Products Never Ordered**: Lists products that have never been ordered.
- **Average Order Value**: Provides the average order value, grouped by country.
- **Frequent Buyers**: Returns customers who have placed more than one order.

The API is built using Flask and connects to a MySQL database hosted on AWS RDS.

## Swagger UI
To interact with the API, visit the Swagger UI at the following URL:  
`http://54.75.1.79:5000/swagger`