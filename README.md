# To-Do

Simple app for task managment

## Backend

### Crear venv

python -m venv .venv

Activar venv

- Linux: source backend/.venv/bin/activate

- Windows: .venv\Scripts\Activate.ps1

### Instalar FastAPI

pip install "fastapi[standard]"

### Ejecución - Desarrollo

fastapi dev main.py

### Ejecución Producción (Hardcodeado)

docker build -t myimage .

docker run -d --name mycontainer -p 80:80 -e DB_HOST=host.docker.internal -e DB_PORT=3306 -e DB_NAME=to-do -e DB_USER=postgres -e DB_PASSWORD=admin myimage

### Requiriments.txt

Este archivo fija librerias para proyecto, en un futuro permite recrear el proyecto FastAPI con las mismas dependencias (se debe ejecutar el comando cada vez que se agregan librerias)

pip freeze > requirements.txt

## Frontend

npx create-react-router@latest frontend

### Ejecución

npm run dev

Instalación de dependencias con npm: Si

## Base de Datos (Contenedor)

docker compose up -d

cambio de pruebas

f{ñklmdsfkñ{msdf
fpos´fñmsdfñ}}
fs,dl.ñfmsklñ{dfm
sdfklnfklñsf}
