# Pruebas funcionales con Selenium

![pruebas-selenium](https://github.com/DeysiVarela/Pruebas-Funcionales-Selenium/actions/workflows/pruebas.yml/badge.svg)

Proyecto de automatización funcional para SauceDemo usando Python, Selenium,
pytest y el patrón Page Object Model.

## Instalación

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Ejecución

Ejecutar todas las pruebas y generar el reporte HTML:

```powershell
python -m pytest
```

Ejecutar un grupo específico:

```powershell
python -m pytest tests/test_login.py
python -m pytest tests/test_esperas.py
python -m pytest tests/test_compra.py
python -m pytest tests/test_carrito.py
```

El reporte se genera en `reports/report.html`. Las capturas de pruebas
fallidas se guardan en `screenshots/` y también quedan dentro del reporte.

## Opciones de ejecución

Sin ventana (modo headless):

```powershell
$env:HEADLESS="1"; python -m pytest     # Windows PowerShell
HEADLESS=1 python -m pytest             # macOS / Linux
```

En otro navegador (debe estar instalado):

```powershell
python -m pytest --browser firefox
python -m pytest --browser edge
```

En un Selenium Grid (por ejemplo, levantado con Docker):

```powershell
docker run -d --rm --name grid -p 4444:4444 -p 7900:7900 --shm-size=2g selenium/standalone-chrome
python -m pytest --grid-url http://localhost:4444
docker stop grid
```

## Integración continua

Cada `push` y cada `pull request` ejecuta las pruebas en GitHub Actions
(`.github/workflows/pruebas.yml`), en Chrome y en Firefox, sin ventana. El
reporte y las capturas quedan como artefactos de cada ejecución.

## Estructura

```text
conftest.py          Fixture del navegador, opciones y captura al fallar
pytest.ini           Configuración de pytest y del reporte
pages/               Page Objects: una clase por página
tests/               Pruebas
reports/             Reporte HTML generado
screenshots/         Capturas de pruebas fallidas
.github/workflows/   Integración continua
```

## Casos cubiertos

- Login válido.
- Contraseña incorrecta.
- Usuario bloqueado.
- Espera de carga del inventario.
- Ordenamiento por precio ascendente.
- Agregar un producto al carrito.
- El carrito muestra el producto agregado.
- Quitar un producto del carrito.
- Completar una compra.
