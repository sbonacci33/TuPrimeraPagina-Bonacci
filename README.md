# TuPrimeraPagina-Bonacci

Este es un proyecto desarrollado en el marco del curso **Python Flex de Coderhouse**. El objetivo fue construir una primera web en Django, aplicando el patrón **MVT (Model-View-Template)** con herencia de plantillas y funcionalidades completas de carga, visualización y búsqueda de datos.

---

## 📌 Descripción del proyecto

Se trata de un portal institucional en desarrollo, orientado al análisis de datos de consumo. Se propone como una plataforma profesional para publicar informes, organizar información y ofrecer contenido útil a los usuarios.

En esta primera versión, se implementó:

- Carga de informes
- Listado de informes publicados
- Búsqueda de informes por título y resumen
- Formulario de suscripción con validación
- Interfaz simple, clara y responsiva (con Bootstrap)

---

## 🎯 Objetivos de esta entrega

- Aplicar el patrón MVT de Django
- Crear al menos 3 clases en `models.py`
- Implementar formularios para insertar datos en cada clase
- Incluir al menos un formulario para buscar en la base de datos
- Utilizar herencia de plantillas (`base.html`) correctamente
- Subir el proyecto a un repositorio GitHub de forma ordenada

---

## 🧱 Estructura y modelos

El proyecto cuenta con una sola app: `observatorio`.

Se desarrollaron los siguientes modelos en `models.py`:

- `Informe`: contiene título, resumen, contenido, fecha, categoría y autor.
- `Categoria`: agrupa los informes por temática.
- `Suscriptor`: almacena nombre, apellido, email y fecha de suscripción.
- `ConsultaUsuario`: guarda términos que se ingresan en el buscador.

> Cada modelo tiene su formulario correspondiente en la web para insertar datos.

---

## 🧭 ¿Cómo navegar el sitio?

Una vez el proyecto esté corriendo (`python manage.py runserver`):

1. **Inicio** → Página principal.
2. **Ver Informes** → Muestra los informes cargados.
3. **Cargar Informe** → Formulario para cargar un nuevo informe.
4. **Buscar** → Campo para buscar por título o resumen.
5. **Suscribirse** → Formulario con validación para recibir novedades.

---

## 🔍 Funcionalidad de búsqueda

La búsqueda se realiza desde la barra superior y permite filtrar informes por **palabras en el título o en el resumen**.

---

## 💡 A futuro

Este portal es una base funcional con proyección de crecimiento. Entre las mejoras pensadas:

- Autenticación y registro de usuarios colaboradores.
- Agregado de comentarios en informes.
- Editor enriquecido para los textos.
- Paginación de resultados.
- Integración con IA para responder consultas.
- Mejora visual completa con estilo profesional personalizado.

---

## 🙋 Sobre mí

Soy **Santiago Bonacci**, comunicador social, investigador y docente, en formación para recorrer nuevos espacios profesionales. Este proyecto es parte de mi trayectoria técnica en programación, con vistas a ampliar mis oportunidades laborales y crear herramientas digitales útiles para ofrecer servicios en el futuro.

---

## 📦 Instrucciones para correr el proyecto

1. Cloná el repositorio:

```bash
git clone https://github.com/sbonacci33/TuPrimeraPagina-Bonacci.git
cd TuPrimeraPagina-Bonacci
```

2. Activá un entorno virtual (recomendado):

```bash
python -m venv venv
venv\Scripts\activate      # En Windows
# o source venv/bin/activate en Linux/Mac
```

3. Instalá Django:

```bash
pip install django
```

4. Ejecutá las migraciones:

```bash
python manage.py migrate
```

5. Corré el servidor:

```bash
python manage.py runserver
```

---

## 🔗 Repositorio

📍 GitHub: [TuPrimeraPagina-Bonacci](https://github.com/sbonacci33/TuPrimeraPagina-Bonacci)

---

Este README cumple con el requisito de indicar qué funcionalidades están implementadas y cómo se accede a ellas.
