
# 🃏 TCG Trader

**TCG Trader** es una aplicación creada con **Django** y **Tailwind CSS** que permite a los usuarios:
- **Registrarse** y crear su perfil.
- **Subir cartas** coleccionables.
- **Interactuar** con otros usuarios para realizar intercambios.

Este proyecto busca fomentar una comunidad de amantes de los juegos de cartas a través del intercambio y gestión de colecciones digitales.

---

## 🚀 Requisitos de instalación

### 1. Dependencias principales:
- Python 3.8+ 
- Django 
- Tailwind CSS 
- [Cloudinary](https://cloudinary.com/) para gestión de imágenes

### 2. Configuración del entorno:
Debes crear un archivo `.env` en la raíz del proyecto con la siguiente configuración:

```bash
DEBUG=True
TEMPLATE_DEBUG=True
CLOUDINARY_CLOUD_NAME=<nombre_cloud>
CLOUDINARY_API_KEY=<api_key>
CLOUDINARY_API_SECRET=<api_secret>
```

💡 **Nota:** Regístrate en [Cloudinary](https://cloudinary.com/) para obtener tus credenciales API.

---

## 🛠️ Instrucciones de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/EnriqueKloosterman/tcg_trader_django.git
   ```

2. **Crear un entorno virtual e instalar dependencias:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Migrar la base de datos:**
   ```bash
   python manage.py migrate
   ```

4. **Iniciar Tailwind CSS:**  
   Tailwind necesita correr en segundo plano para compilar los estilos.
   ```bash
   python manage.py tailwind start
   ```

5. **Ejecutar el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

---

## 📦 Dependencias del Proyecto

Las dependencias principales se encuentran en el archivo `requirements.txt`. Algunas de las más relevantes son:
- Django
- Tailwind CSS
- Django Cloudinary Storage

---

## 🔧 Troubleshooting

- **Error de Tailwind:** Si los estilos no se aplican correctamente, asegúrate de que Tailwind está corriendo con `python manage.py tailwind start`.
- **Migraciones fallidas:** Si encuentras problemas al migrar la base de datos, intenta eliminar las migraciones y volver a generarlas:
  ```bash
  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
  python manage.py makemigrations
  python manage.py migrate
  ```

---

## 📬 Contacto

Si tienes preguntas o necesitas ayuda, no dudes en contactarme:  
📧 **kloostermanen@gmail.com**

---

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes utilizar, modificar y distribuir el código bajo los términos de esta licencia.

