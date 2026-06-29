from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.db.config import settings

# Este archivo define la conexion y creacion de session con BD

engine = create_engine(settings.database_url, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# bind=engine - hace que se vea log de BD

# Definir modelos ORM como clases
Base = declarative_base()

# Otra forma - herendando
#class Base(DeclarativeBase):
#    pass

# Entorno de desarrollo, crear tablas en caso de que no existan
# En produccion se usan migraciones
Base.metadata.create_all(bind=engine) 

# Crear sesion -> Cada vez que se entra a un endpoint crea la sesion
# yiel se usa para soltar el recurso cuando sea necesario y poder cerra la db posteriormente
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()