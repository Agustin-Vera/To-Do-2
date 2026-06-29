# Tecnologías

## FastAPI

- Framework moderno para construir APIs en Python.
- Alto rendimiento (basado en Starlette y ASGI)

## Pydantic

- Librería de validación de datos basada en type hints de Python.

## SQLAlchemy

- ORM (Object Relational Mapper) para trabajar con bases de datos relacionales.

## Distribución

app/
│
├── main.py
│
├── core/
│ ├── config.py
│ └── security.py
│
├── db/
│ ├── session.py
│ └── base.py
│
├── models/
│ ├── user.py
│ └── task.py
│
├── schemas/
│ ├── user.py
│ └── task.py
│
├── repositories/
│ ├── user.py
│ └── task.py
│
├── services/
│ ├── user.py
│ └── task.py
│
├── api/
│ ├── deps.py
│ └── routes/
│ ├── user.py
│ └── task.py
│
└── utils/
└── helpers.py

### Qué va en cada carpeta

**core/**

Configuración global del proyecto.

Ejemplos:

- variables de entorno
- settings
- auth
- constantes globales

**db/**

Todo lo relacionado con la base de datos.

Ejemplos:

- engine
- SessionLocal
- Base
- helpers de conexión

**models/**

Acá van los modelos SQLAlchemy, o sea, las tablas ORM.

**schemas/**

Acá van los modelos Pydantic.

Se suelen separar según el caso de uso:

- TaskCreate
- TaskUpdate
- TaskResponse

**repositories/**

Acá va el acceso directo a datos.

Es la capa que habla con SQLAlchemy: queries, filtros, inserts, deletes.

**services/**

Acá va la lógica de negocio.

Ejemplo:

- validar reglas antes de guardar
- revisar estados permitidos
- calcular fechas
- coordinar varios repositories

**api/routes/**

Acá van las rutas de FastAPI.

Cómo se diferencian mentalmente

Piensa así:

- models/ = cómo se guarda en la base
- schemas/ = cómo entra/sale por la API
- repositories/ = consultas SQLAlchemy
- services/ = reglas del negocio
- api/routes/ = endpoints HTTP
- db/ = conexión y sesión
- core/ = configuración
