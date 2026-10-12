# Write-up: The Intruder (Web / SQLi)

## 1. Vulnerability Analysis and Arity

The portal features an employee search form. Upon entering a single quote (`'`), the application returns a syntax error from the SQLite engine, confirming that the input is being concatenated directly into the query.

The first algorithmic step is to determine the arity (number of columns) of the original query to satisfy the compatibility of the `UNION` operator. We proceed via iterative integer injection until the query executes without throwing a column mismatch error:

- Payload 1: `' UNION SELECT 1--` (Error: *SELECTs to the left and right of UNION do not have the same number of result columns*)

- Payload 2: `' UNION SELECT 1, 2--` (Success: The numbers 1 and 2 are rendered on the interface).

The original query returns exactly 2 columns.

## 2. Schema Reconnaissance (Data Dictionary)

Since we are operating on SQLite, we must query the internal `sqlite_master` table to extract the metadata. We need to project two columns to maintain balance. We will extract the table name and the original SQL statement that created it (which will reveal its column names).

- **Payload:** `' UNION SELECT name, sql FROM sqlite_master WHERE type='table'--`

The application renders several rows. We locate the target table mentioned in the audit brief:
- `name`: `secret_data`
- `sql`: `CREATE TABLE secret_data (id INTEGER, valor TEXT, nombre_clave TEXT)`

## 3. Data Extraction (Exfiltration)

We know the table name (`secret_data`) and its column names. Knowing that we must maintain a two-column projection, we extract the attributes containing the sensitive information:

- **Payload:** `' UNION SELECT nombre_clave, valor FROM secret_data--`

Upon executing this vector, the application renders the confidential row in the results table, giving us the solution to the challenge.

---

**Flag for validation in CTFd:** `flag{un10n_b4s3d_m4st3r}`