# 🚀 Levantando el Proyecto Django

¡Bienvenido! 🎉 En este tutorial, aprenderás a configurar y ejecutar nuestro proyecto Django desde cero. 🐍✨

## 📌 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- **Python** (versión 3.8 o superior) 🐍  
- **Pip** (gestor de paquetes de Python) 📦  
- **Virtualenv** (ya incluido en el proyecto) 🏕️  

## 🛠️ Instalación y Configuración

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/ElizabethEscobar04/tendenciastda2025
cd tendenciastda2025_entrega
```

### 2️⃣ Activar el Entorno Virtual

El entorno virtual (`venv`) ya está incluido en el proyecto, por lo que solo debes activarlo:

```bash
# macOS/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Aplicar Migraciones y Cargar Datos Iniciales

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Crear un Superusuario (Opcional)

Si deseas acceder al **panel de administración de Django**, ejecuta:

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar el Servidor 🚀

```bash
python manage.py runserver
```

Ahora, abre tu navegador y visita:

```
http://127.0.0.1:8000/
```

🎉 ¡Tu aplicación Django está corriendo! 🎈

---

## 📡 Endpoints de la API

Aquí están los principales endpoints de la API:

| Módulo         | Endpoint                                          |
|---------------|--------------------------------------------------|
| **Clientes**  | `http://localhost:8000/cliente/api/v1/cliente`   |
| **Reservas**  | `http://localhost:8000/reserva/api/v1/reserva`   |
| **Establecimientos** | `http://localhost:8000/establecimiento/api/v1/establecimiento` |

---

## 📂 Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
proyecto-django/
│── venv/              # Entorno virtual
│── manage.py          # Comando de administración
│── cliente/           # Aplicación de gestion de clientes
│── establecimiento/   # Aplicación de gestion de establecimientos
│── reserva/           # Aplicación de gestion de reservas
│── global_project/    # Configuración del proyecto
│── usuario/           # Aplicacion de gestion de usuarios
│── cliente/           # Aplicación de clientes
│── establecimiento/   # Aplicación de establecimientos
│── reserva/           # Aplicación de reservas
│── global_project/    # Configuración del proyecto
│   │── settings.py    # Configuración general
│   │── serializers.py # Serializadores
│   │── views.py       # Vistas de usuarios
│   │── urls.py        # Enrutamiento
│   │── wsgi.py        # Servidor WSGI
│   └── asgi.py        # Servidor ASGI (opcional)
```

---

## 🔐 Autenticación con Tokens

El proyecto utiliza `rest_framework.authtoken` para la autenticación mediante tokens.  
Hemos creado dos usuarios de prueba que puedes utilizar:

```json
{
    "username": "usuario1",
    "password": "usuario1Pass"
}
```

```json
{
    "username": "usuario2",
    "password": "usuario2Pass"
}
```

### 🔑 Obtener un Token de Autenticación

Para iniciar sesión, envía una petición `POST` a la siguiente URL con las credenciales de usuario en el **body**:

```http
POST http://localhost:8000/login/
```

### 🔎 Acceder a un Endpoint Protegido

Una vez que obtengas el token de autenticación, puedes probar un **endpoint protegido** enviando el token en el encabezado de la solicitud:

```http
POST http://localhost:8000/profile/

# Headers
Authorization: Token <tu_token>
```


## 📝 Registrar tu propio usuario
Puedes registrar tu propio usuario enviando una peticion `POST` a la siguiente url con los datos de tu usuario dentro del **body**.
```http
POST http://localhost:8000/register/

# BODY
{
    "username": [Tu_usuario],
    "password": [Tu_password],
    "email": [Tu_email]
}
```
---
🚀 ¡Feliz programación con Django! 🦄🔥
