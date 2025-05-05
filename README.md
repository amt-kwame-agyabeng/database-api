

## Project Structure
```plaintext
api/
├── api-docs/
│ ├── screenshots/ # Screenshots of API responses
│ ├── api_overview.md # General overview of the API
│ └── endpoint.md # Detailed documentation of each endpoint
├── db/
│ ├── screenshot/ # Screenshots of queries and results
│ ├── create-schema.sql # SQL script to create schema
│ ├── insert.sql # SQL script to insert data
│ └── queries.sql # SQL script containing analytical queries
└── README.md # Main documentation file
```

##  How to Run the API
1. Create a Python virtual environment:

python3 -m venv venv
source venv/bin/activate


2. Install dependencies:
pip install -r requirements.txt

3. Run the API:
python3 app.py

## Access API via:
http://<your-ec2-ip>:5000/<endpoint>

## Swagger UI:
http://<your-ec2-ip>:5000/swagger


## API Documentation
See api-docs/api_overview.md for an overview.

See api-docs/endpoint.md for full endpoint descriptions.

Example endpoints:

/top-customers

/monthly-sales

/products-never-ordered

/avg-order-value

/frequent-buyers

## Query Results & Screenshots
Screenshots are located in:

api-docs/screenshots/ – API result screenshots

db/screenshot/ – Raw SQL query result screenshots


## Database
The database is hosted on AWS RDS. SQL scripts are included in the db/ folder:

create-schema.sql: Create all tables.

insert.sql: Insert sample data.

queries.sql: Analytical queries used in the API.

