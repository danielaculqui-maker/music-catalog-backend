# Music Catalog - Backend

## Autores

- Daniela Culqui
- Cristian Tenorio

## Descripción General

API REST desarrollada con Django y Django REST Framework para la gestión de un catálogo de artistas y álbumes musicales, con autenticación mediante OAuth 2.0.

## Objetivo

Construir una API REST completa en Django que gestione dos entidades relacionadas (Artista y Álbum, relación uno a muchos), protegida con autenticación OAuth 2.0, sin renderizar ninguna vista HTML.

## Requisitos previos

- Python 3.12 o superior instalado
- pip
- Editor de código (recomendado: VS Code)
- Cuenta de Postman (para probar los endpoints)

## Requisitos técnicos

- Django 6.0
- Django REST Framework
- django-oauth-toolkit (autenticación OAuth 2.0)
- django-cors-headers
- Pillow (manejo de imágenes)
- SQLite como base de datos

## Funcionalidades

- API REST con los 4 métodos HTTP (GET, POST, PUT/PATCH, DELETE) para Artistas y Álbumes
- Relación uno a muchos entre Artista y Álbum
- Autenticación y protección de endpoints con OAuth 2.0
- Carga de imágenes para los artistas
- Respuestas en formato JSON

## Estructura del proyecto

```
/config
  settings.py
  urls.py
/catalogo
  models.py
  serializers.py
  views.py
  urls.py
  /migrations
/media
  /artistas
manage.py
requirements.txt
```

## Modelo de datos

**Artista**
- nombre
- biografia
- genero_musical
- fecha_formacion
- foto 

**Album** (relación uno a muchos con Artista)
- artista (clave foránea)
- titulo
- fecha_lanzamiento
- numero_canciones

## Endpoints principales

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|--------------|-----------------|
| POST | /o/token/ | Obtener token de acceso OAuth2 | No |
| GET | /api/artistas/ | Listar artistas | Sí |
| GET | /api/artistas/{id}/ | Detalle de un artista (con sus álbumes) | Sí |
| POST | /api/artistas/ | Crear artista | Sí |
| PUT/PATCH | /api/artistas/{id}/ | Editar artista | Sí |
| DELETE | /api/artistas/{id}/ | Eliminar artista | Sí |
| GET | /api/albumes/ | Listar álbumes | Sí |
| GET | /api/albumes/{id}/ | Detalle de un álbum | Sí |
| POST | /api/albumes/ | Crear álbum | Sí |
| PUT/PATCH | /api/albumes/{id}/ | Editar álbum | Sí |
| DELETE | /api/albumes/{id}/ | Eliminar álbum | Sí |

## Instalación del proyecto

1. Clonar el repositorio

```
git clone https://github.com/danielaculqui-maker/music-catalog-backend.git
cd music-catalog-backend
```

2. Abrir en VS Code la carpeta del repositorio clonado

3. Crear y activar el entorno virtual

```
python -m venv venv
```

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

4. Instalar las dependencias

```
pip install -r requirements.txt
```

5. Aplicar las migraciones

```
python manage.py migrate
```

6. Crear un superusuario

```
python manage.py createsuperuser
```

7. Levantar el servidor

```
python manage.py runserver
```

## Registrar una aplicación OAuth2

1. Con el servidor corriendo, ingresar a `http://127.0.0.1:8000/admin/` e iniciar sesión con el superusuario
2. Ir a **Django OAuth Toolkit → Applications → Add Application**
3. Completar:
   - Client type: `Confidential`
   - Authorization grant type: `Resource owner password-based`
   - Name: `music-catalog-app`
4. Guardar y copiar el **Client id** y **Client secret** generados (el secret no se puede volver a ver después de este paso)

Estos valores se deben usar en el archivo `.env` del frontend.

## Autenticación

Para obtener un token, se debe hacer un `POST` a `/o/token/` con body tipo `x-www-form-urlencoded`:

```
grant_type=password
username=tu_usuario
password=tu_contraseña
client_id=tu_client_id
client_secret=tu_client_secret
```

El token obtenido se debe enviar en cada request protegida, en el header:

```
Authorization: Bearer {access_token}
```

## Comandos útiles

Generar el archivo de dependencias

```
pip freeze > requirements.txt
```

Crear migraciones tras cambios en los modelos

```
python manage.py makemigrations
```

## Comandos git

Verificar los archivos modificados

```
git status
```

Agregar archivos al área de preparación

```
git add .
```

Realizar un commit

```
git commit -m "descripción de cambios"
```

Enviar los cambios a GitHub

```
git push
```

## Nota sobre la raíz del servidor

La ruta raíz (`/`) no tiene ninguna vista asignada de forma intencional, ya que Django funciona únicamente como API REST y no debe renderizar HTML. Es normal obtener un error 404 al ingresar a esa URL directamente.

