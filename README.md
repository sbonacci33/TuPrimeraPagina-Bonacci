# TuPrimeraPagina-Bonacci

Este proyecto es una web realizada con Django como parte de una entrega académica. La aplicación se llama **Observatorio de Contenidos Digitales** y permite gestionar informes, categorías, suscripciones de usuarios y búsquedas, siguiendo el patrón **MVT (Model-View-Template)**.

---

## ✔️ Funcionalidades incluidas

- **Herencia de plantillas HTML**
- **3 modelos en base de datos** (`Informe`, `Categoria`, `Suscriptor`)
- **Formularios** para cargar cada uno de los modelos
- **Formulario de búsqueda** de informes (filtra por título y resumen)
- **Suscripción a newsletter** mediante email verificado
- **Diseño responsive** con Bootstrap
- **Visual personalizable** (con logo, imagen de fondo, paleta de colores institucional)

---

## 📁 Estructura de carpetas

```
observatorio/
    models.py
    views.py
    forms.py
    urls.py
    templates/
        observatorio/
            base.html
            home.html
            crear_informe.html
            listar_informes.html
            buscar.html
            suscribirse.html
            detalle_informe.html
    static/
        css/
        js/
        images/
```

---

## 🔍 Cómo probar la web

1. Cloná este repositorio:

```bash
git clone https://github.com/sbonacci33/TuPrimeraPagina-Bonacci.git
cd TuPrimeraPagina-Bonacci
```

2. Activá el entorno virtual (si ya lo tenés creado):

```bash
.env\Scriptsctivate
```

3. Si no tenés uno, crealo:

```bash
python -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt
```

4. Aplicá migraciones:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Iniciá el servidor:

```bash
python manage.py runserver
```

---

## 🧪 Qué funcionalidades probar

1. **Home** – Ver bienvenida con diseño personalizado
2. **Cargar informe** – Formulario para ingresar un nuevo informe
3. **Ver informes** – Lista de informes con título, resumen, autor, categoría
4. **Buscar informes** – Filtra por título o resumen
5. **Suscribirse** – Formulario con validación de correo electrónico
6. **Detalle del informe** – Al hacer clic sobre un informe

---

## ℹ️ Info adicional

- El campo `Autor` de los informes fue agregado recientemente. Si tenés errores, podés borrar los informes previos desde el panel admin.
- En próximas versiones se incluirá registro y login para usuarios autorizados a subir contenido.

---

## 📅 Fecha de entrega

27/05/2025

---

## 👤 Autor

Santiago Bonacci – Observatorio de Contenidos Digitales
