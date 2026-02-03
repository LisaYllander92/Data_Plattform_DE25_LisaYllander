## PostgreSQL & fastapi

### Installations:
* `$ uv add "fastapi[standard]"` - if you haven't already installed it

```bash
uv add "psycopg[binary]"
```

````bash
uv add "psycopg[pool]"
````

### run app
fastapi dev main.py

### Storing data - philosophy

* What's the purpose of our data?
  * Bulk uploading
  * JSON data storage
  * Unorganized data
  * postgreSQL
* What's the datatype of said data?
  * unorganized
  * unstructured
  * JSON
### Database - postgreSQL
  * A newly database does NOT contain any TABLES by default.
  * Step #1 - create new Table (products)
```postgresql
CREATE TABLE IF NOT EXISTS product_raw (
id BIGSERIAL PRIMARY KEY,
created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
product JSONB NOT NULL                 
);
```
* Step #2 - implement function for Insert (fastAPI)


### Diffrens between uvcorn vs fastapi dev main.py