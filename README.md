# Pruebas funcionales con Selenium

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
```

El reporte se genera en `reports/report.html`. Las capturas de pruebas
fallidas se guardan en `screenshots/`.

## Casos cubiertos

- Login válido.
- Contraseña incorrecta.
- Usuario bloqueado.
- Espera de carga del inventario.
- Ordenamiento por precio ascendente.
- Agregar un producto al carrito.
- Completar una compra.
