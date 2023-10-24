Prueba Tecnica - MONI
=====================

## Instalacion

1. Requisitos:
    - docker

2. Levantar el backend:
```
    $ sudo docker run -d -p 127.0.0.1:8000:8000 --name moni_api gringo00/moni:v1
```

3. Levantar el frontend:
```
    $ sudo docker run -d -p 127.0.0.1:3000:3000 --name moni_client gringo00/moni:client
```

4. Crear superusuario para usar sus credenciales
```
    $ sudo docker exec -it moni_api python3 manage.py createsuperuser
```
