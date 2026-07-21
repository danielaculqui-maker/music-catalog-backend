# Music Catalog - Backend

API REST desarrollada con Django y Django REST Framework para la gestión de un catálogo de artistas y álbumes musicales, con autenticación mediante OAuth 2.0.

## 🛠️ Tecnologías

- Python 3.12
- Django 6.0
- Django REST Framework
- django-oauth-toolkit (autenticación OAuth 2.0)
- django-cors-headers
- Pillow (manejo de imágenes)
- SQLite (base de datos local)

## 📋 Requisitos previos

- Python 3.12 o superior instalado
- pip

## 🚀 Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/TU_USUARIO/music-catalog-backend.git
cd music-catalog-backend
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

Mac/Linux:
```bash
source venv/bin/activate
```

### 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar las migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario

```bash
python manage.py createsuperuser
```

Vas a necesitar este usuario para acceder al panel de administración y para autenticarte en la API.

### 6. Registrar una aplicación OAuth2

1. Levantar el servidor (ver paso siguiente)
2. Ir a `http://127.0.0.1:8000/admin/` e iniciar sesión con el superusuario
3. Ir a **Django OAuth Toolkit → Applications → Add Application**
4. Completar:
   - **Client type**: `Confidential`
   - **Authorization grant type**: `Resource owner password-based`
   - **Name**: `music-catalog-app`
5. Guardar y copiar el **Client id** y **Client secret** generados (el secret no se puede volver a ver después)

### 7. Levantar el servidor

```bash
python manage.py runserver
```

El servidor queda disponible en `http://127.0.0.1:8000/`

> ⚠️ La raíz (`/`) no tiene ninguna vista asignada a propósito, ya que Django funciona únicamente como API REST (no renderiza HTML). Es normal ver un error 404 al entrar a esa URL.

## 📡 Endpoints principales

| Método | Endpoint | Descripción | Requiere token |
|--------|----------|--------------|-----------------|
| POST | `/o/token/` | Obtener token de acceso OAuth2 | No |
| GET | `/api/artistas/` | Listar artistas | Sí |
| GET | `/api/artistas/{id}/` | Detalle de un artista (incluye sus álbumes) | Sí |
| POST | `/api/artistas/` | Crear artista | Sí |
| PUT/PATCH | `/api/artistas/{id}/` | Editar artista | Sí |
| DELETE | `/api/artistas/{id}/` | Eliminar artista | Sí |
| GET | `/api/albumes/` | Listar álbumes | Sí |
| GET | `/api/albumes/{id}/` | Detalle de un álbum | Sí |
| POST | `/api/albumes/` | Crear álbum | Sí |
| PUT/PATCH | `/api/albumes/{id}/` | Editar álbum | Sí |
| DELETE | `/api/albumes/{id}/` | Eliminar álbum | Sí |

## 🔐 Autenticación

Todos los endpoints bajo `/api/` requieren un token OAuth2 válido.

Para obtenerlo, hacer un `POST` a `/o/token/` con body tipo `x-www-form-urlencoded`:

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

## 📁 Modelo de datos

**Artista**
- nombre
- biografia
- genero_musical
- fecha_formacion
- foto (opcional)

**Album** (relación uno a muchos con Artista)
- artista (clave foránea)
- titulo
- fecha_lanzamiento
- numero_canciones

## 👥 Autores

- Daniela Culqui
- Cristian Tenorio