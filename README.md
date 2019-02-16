# Molinetes #

## Development server ##

First activate virtualenv with pipenv:

```
pipenv shell
```

Second:

```
python3 runweb.py

```
## Create a new resource ##

This command creates a new resource  with a simple test file.

```
env FLASK_NAME='package_dir_name' hygen flask resource --name resource_name

```

## Tests ##

From root directory: 

```
python3 -m pytest tests/ 
```
