## Table of Contents
- [OLAP Vs OLTP Databases](#olap-vs-oltp-databses)
- [Normal Forms in Databases](#normal-forms-in-database)
- [Joins in Database](#joins-in-database)
- [Difference Between SQL and No-SQL](#differences-between-sql-and-nosql)

## OLAP VS OLTP Database
| **Aspect**      | **OLAP (Online Analytical Processing)**                                                                 | **OLTP (Online Transaction Processing)**                                                    |
|------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **Purpose**      | Used for data analysis, reporting, and decision-making.                                                | Used for managing real-time transactional data.                                            |
| **Examples**     | - Data Warehouses<br>- Business Intelligence (BI) systems<br>- Analytical dashboards                   | - Banking systems<br>- E-commerce platforms<br>- Point-of-sale (POS) systems              |
| **Use Cases**    | - Sales trend analysis<br>- Customer behavior insights<br>- Forecasting                                | - Recording bank transactions<br>- Processing online orders<br>- Updating inventory       |
| **Tools/Databases** | - Amazon Redshift<br>- Google BigQuery<br>- Snowflake<br>- Microsoft SQL Server Analysis Services (SSAS) | - MySQL<br>- PostgreSQL<br>- Oracle Database<br>- Microsoft SQL Server                    | 

<sub>[back to top](#table-of-contents)</sub>

## Normal Forms in Database

| **Normal Form**         | **Definition**                                                                                     | **Key Rule**                                                                                     |
|--------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| **1NF (First Normal Form)** | Ensure data is in atomic units (no repeating groups or arrays).                                  | Each cell contains a single value, and each column has unique attributes.                       |
| **2NF (Second Normal Form)** | Achieved when in 1NF and all non-key attributes are fully functionally dependent on the entire primary key. | Eliminate **partial dependencies** (attributes depending on part of a composite key).            |
| **3NF (Third Normal Form)** | Achieved when in 2NF and no non-key attribute is transitively dependent on the primary key.     | Remove **transitive dependencies** (non-key attributes depend on other non-key attributes).      |
| **BCNF (Boyce-Codd Normal Form)** | Achieved when in 3NF and every determinant (left side of a functional dependency) is a superkey.         | Eliminate functional dependencies where a non-superkey determines another attribute.             |

<sub>[back to top](#table-of-contents)</sub>

## Joins in Database
| **Type of Join**   | **Description**                                                                                              | **Example**                                                                 |
|--------------------|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| **INNER JOIN**     | Returns rows when there is a match in both tables. If no match, the row is excluded.                        | Returns customers who have orders.                                         |
| **LEFT JOIN (LEFT OUTER JOIN)** | Returns all rows from the left table, and the matched rows from the right table. If no match, returns NULL for right table columns. | Returns all customers, even those without orders.                          |
| **RIGHT JOIN (RIGHT OUTER JOIN)** | Returns all rows from the right table, and the matched rows from the left table. If no match, returns NULL for left table columns.  | Returns all orders, even those without a customer.                         |
| **FULL JOIN (FULL OUTER JOIN)** | Returns rows when there is a match in one of the tables. Returns NULL for non-matching rows from both tables. | Returns all customers and all orders, with NULL where there’s no match.   |
| **CROSS JOIN**     | Returns the Cartesian product of both tables (each row of the first table combined with each row of the second table). | Returns all combinations of customers and products.                        |
| **SELF JOIN**      | Joins a table with itself to combine rows based on a related column.                                          | Returns employees and their managers from the same "employees" table.      |

<sub>[back to top](#table-of-contents)</sub>


## Differences between SQL and NoSQL

| Feature               | SQL (Relational)                           | NoSQL (Non-relational)                     |
|-----------------------|--------------------------------------------|--------------------------------------------|
| **Data Model**         | Structured (tables, rows, columns)         | Flexible (key-value, document, graph)      |
| **Schema**             | Fixed schema                               | Schema-less or flexible                    |
| **Scalability**        | Vertical (scaling up)                      | Horizontal (scaling out)                   |
| **Consistency**        | ACID (strong consistency)                  | BASE (eventual consistency)                |
| **Query Language**     | SQL (Structured queries)                   | No standard query language (varies by type)|
| **Transactions**       | Supports transactions with ACID properties | Limited transactional support              |
| **Best For**           | Structured data, complex relationships     | Large-scale, unstructured data, real-time  |


<sub>[back to top](#table-of-contents)</sub>
