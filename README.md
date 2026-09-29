# Pagina con certificado SSL

Pagina web minimo con una conexion segura (HTTPS) para una entrega escolar.

## Contenido

- `index.html` - pagina de demostracion.
- `serve.py` - servidor HTTPS local (usa solo la libreria estandar de Python).
- `ssl/server.crt` y `ssl/server.key` - certificado autofirmado (CN=localhost).

## Como ver HTTPS de forma local

Requiere [Python 3](https://www.python.org/).

```bash
python serve.py
```

Luego abre en tu navegador: <https://localhost:8443>

El navegador mostrara una advertencia porque el certificado es **autofirmado**
(no esta firmado por una autoridad de confianza). Para ver la pagina:

- **Chrome/Edge**: clic en "Avanzado" -> "Continuar a localhost (no es seguro)".
- **Firefox**: clic en "Avanzado" -> "Aceptar el riesgo y continuar".

Despues de eso veras el candado en la barra de direcciones.

## Como obtener un certificado real (candado verde)

Los certificados de confianza los emite el hosting. La forma mas facil y gratis:

1. Crea un repositorio en GitHub y sube los archivos (`index.html` es suficiente).
2. En el repositorio ve a **Settings -> Pages**.
3. En "Source" elige la rama `main` y la carpeta raiz, y guarda.
4. Espera un minuto. GitHub publica la pagina en
   `https://TU_USUARIO.github.io/TU_REPO` con HTTPS valido automaticamente.

No necesitas incluir `ssl/server.crt` ni `server.key` para GitHub Pages; el
certificado lo genera GitHub por ti.
