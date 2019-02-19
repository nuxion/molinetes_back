# Molinetes #
---

## Project setup ##

```bash
git clone https://github.com/nuxion/molinetes_back
cd molinetes_back
```
Las dependencias fueron manejadas con [pipenv](https://pipenv.readthedocs.io/en/latest/)
```bash
pipenv shell
pipenv install
```
### Base de datos ###

Para cualquiera de los ambientes esta definido sqlite.
Es necesario inicializar la base de datos:

```bash
env FLASK_APP='cli.py' flask db init
env FLASK_APP='cli.py' flask db migrate
env FLASK_APP='cli.py' flask db upgrade
```
> Si da error por que falta la carpeta **instance** es necesario crearla en el root del proecto.

**Opcional**
Para agregarle algunos datos de test a la base se puede ejectuar:
```bash
env FLASK_APP='cli.py' flask populate-db
```

### Ejecucion de la aplicacion ###
```bash
python3 runweb.py

```

or

```bash
env FLASK_APP="molinetes:create_app()" flask run
```
---
## REST API ##

### Credenciales ###
uri | method | params | descripcion
--- | --- | --- | ---
/api/v1/credenciales | GET | | Lista todas las credenciales.
/api/v1/credenciales/[id] | GET | id | Obtiene una id especifico segundo id en la uri
/api/v1/credenciales | POST |nombre, molinete_id, evento_cod | Crea una nueva credencial.
/api/v1/credenciales/[id] | PUT |nombre, molinete_id, evento_cod | Modifica una credencial existente, es neceario pasar el id atraves de la uri.
/api/v1/credenciales/[id] | DELETE | id | elimina una credencial segun parametro de la uri.

### Eventos ###
uri | method | params | descripcion
--- | --- | --- | ---
/api/v1/eventos | GET | | Lista todods los eventos
/api/v1/eventos/[id] | GET | id | Obtiene un evento especifico segun id en la uri
/api/v1/eventos | POST |nombre, cod | Crea un nuevo evento
/api/v1/eventos/[id] | PUT |nombre, cod | Modifica un evento existente, es neceario pasar el id atraves de la uri.
/api/v1/eventos/[id] | DELETE | id | elimina un evento segun parametro de la uri.

```bash
http POST http://127.0.0.1:5000/api/v1/eventos nombre=ACDC cod=20190218
```

### Molinetes  ###
uri | method | params | descripcion
--- | --- | --- | ---
/api/v1/eventos | GET | | Lista todos los molinetes
/api/v1/eventos/[id] | GET | id | Obtiene un molinete especifico segun id en la uri
/api/v1/eventos | POST | evento_cod | Crea un nuevo molinete
/api/v1/eventos/[id] | PUT | evento_cod | Modifica un molinete existente, es neceario pasar el id atraves de la uri.
/api/v1/eventos/[id] | DELETE | id | elimina un molinete segun parametro de la uri.

### Lecturas  ###
uri | method | params | descripcion
--- | --- | --- | ---
/api/v1/lecturas | GET | | Lista todas las lecturas registradas

### Actions  ###
uri | method | params | descripcion
--- | --- | --- | ---
/api/v1/actions/register | POST | credencial_id, molinete_id, evento_id | registra la credencial, timestamp lo genera automaticamente.

ejemplo:
```bash
http POST http://127.0.0.1:5000/api/v1/actions/register credencial_id=1 molinete_id=1 evento_id=1
```


## Development Notes ##
### Create a new resource ###

This command creates a new resource  with a simple test file.

```
env FLASK_NAME='package_dir_name' hygen flask resource --name resource_name

```

### Tests ###

From root directory: 

```
python3 -m pytest tests/ 
```
