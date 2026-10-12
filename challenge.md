# Challenge: The Intruder (Web / SQLi - 150 pts)

## Challenge Metadata
- **Category:** Web
- **Difficulty:** Intermediate
- **Score:** 150 points
- **Flag Format:** `flag{lowercase_text}`

---

## Context and Objective

You have been hired to perform a security audit on a logistics company's web infrastructure. The development team has implemented an employee lookup portal querying the `datos_publicos` table, but we suspect the search gateway code does not properly sanitize inputs, allowing the original query to be altered.

Our intelligence service claims the administrator keeps a hidden table in this same database named `secret_data`, which contains critical information and access tokens. 

**Your objective:**
1. Confirm the injection vulnerability in the search engine.
2. Map the internal structure of the database to identify the columns of the `secret_data` table.
3. Extract the hidden flag.

*Note: It is not necessary to resort to Blind SQLi. The application will render the data on screen if you manage to assemble the correct syntax using the appropriate set operation.*

---

## Environment Access
Direct your attacks to the following portal:
- **URL:** `http://X.X.X.X:8000/` *(The systems team will provide the final IP)*

---

## Available Hints

- **Hint 1 [0 Points]:** To merge the results of your malicious query with those of the original query, you must use the `UNION` logical operator. Remember that for the union to be valid, both queries must project the exact same number of columns (arity).

- **Hint 2 [10 Points]:** In the SQLite engine, the schema data dictionary equivalent to Oracle's `ALL_TABLES` is called `sqlite_master`. You can query it for both the table names (`type='table'`) and their creation statements in the `sql` column.