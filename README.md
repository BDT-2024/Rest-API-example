# Rest API example

This is a simple example of a REST API using [FastAPI](https://fastapi.tiangolo.com/).

## Running the project

First install the requirements:

```bash
pip install -r requirements.txt
```

Then run the server:

```bash
cd src
uvicorn main:app --host 0.0.0.0 --reload
```