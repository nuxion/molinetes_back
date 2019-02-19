from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

## models shortcuts for direct import
from .credenciales import Credencial
from .eventos import Evento
from .molinetes import Molinete
from .lecturas import Lectura
from .users import User, Rol
