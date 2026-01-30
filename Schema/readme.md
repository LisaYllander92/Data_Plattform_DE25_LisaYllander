# Definition of __name__ why?

## Servlet Container
- Hosting of Application (locally)
- FastAPI introduces this new consept
- Removes traditional 'play/start' button
- Requires FastAPI - start command (to run app)

## FastAPI:
* Install: 
```bash
$ pip install "fastapi[standard]"
```
* With uv init:
````bash
uv add "fastapi[standard]"
````
* In virtual environment: 
```bash
uv pip install fastapi
```
* Verify installation through -venv packages
* $ pip list (to see installations)
    * BONUS: COMMAND + F (filter for "success", use CTRL on WINDOWS)
    * ERROR: "Consider adding this to path"
- Keep main.py in root folder (best practise)

- To run/start app (in terminal):
```bash
fastapi dev FILENAME.pt
```
    - IMPORTANT: stand in the same folder as main.py


## Endpoint
- API & URL related 
- Consists of a path: "/examle"
- Accompanied by a HTTP-Method (GET, POST, PUT, DELETE)


## Decorator
- Refers to the (kännetecknas av) @ symbol
- (Different in how function executes)
- Runs logic from external decorator function
    - (Function over function)
- returns JSON data (automatic conversion)

```python
@decorator
def test_function():
```

To run main.py in terminal:
```python
fastapi dev main.py
```
Test in safari:
localhost:8000 (server)

![In terminal](/in_terminal.png)

add /docs:\
![LocalHost](/localhost.png)

## URL

Example URL: https://www.google.se/search?q=bananas
- in this example we see a dynamic parameter
    - q == query (just a variable name)
    - ? == start of query
    - What comes after = is Dynamic_Value (client input)


## Pydantic
* Uses schema (to Define Logical data type structure)
* Class based
* Used for Data Validation
* Facilitates conversion of JSON -> Python objects
* Best practice - separated from its own package
* Includes 'BaseModel' within class parameters
    
## Requests
```python
uv pip install requests
```