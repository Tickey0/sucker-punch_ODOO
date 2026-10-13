# sucker-punch
JSON-2 API Client for Point of Sale

## Dependencies
- https://docs.astral.sh/uv/

## Project created with uv
```
uv init
```
## Create python virtual environment
```
uv venv
```
or
```
python3.14 -m venv .venv
```
## Activate python virtual environment
```
source .venv/bin/activate
```
or
```
. .venv/bin/activate
```
or on powershell
```
.venv\Scripts\Activate.ps1
```
## Install dependencies
```
uv sync
```
## Utilities
Util commands
### Add ruff
```
uv add --dev ruff
```
### Check syntax
```
ruff check
```
### Format
```
ruff format
```
## Run
```
uv run sucker-punch
```
## Designer
```
uvx --from pyside6-essentials pyside6-designer
```
## Structure Projects
📁 nombre_proyecto
│
├── 📁 assets                 # Recursos estáticos
│   ├── 📁 images             # Logos, íconos y gráficos (.png, .svg)
│   └── 📁 styles             # Hojas de estilo de Qt (.qss)
│
├── 📁 src                    # Código fuente principal de la aplicación
│   │
│   ├── 📁 models             # Modelos de datos y entidades de negocio
│   │   ├── __init__.py
│   │   └── cliente_model.py
│   │
│   ├── 📁 viewmodels         # Lógica de presentación y enlace de datos
│   │   ├── __init__.py
│   │   ├── base_viewmodel.py # Clase base con mecanismos de propiedades/señales
│   │   └── main_viewmodel.py
│   │
│   ├── 📁 views              # Interfaz de usuario (Componentes de PySide)
│   │   ├── 📁 ui             # Opcional: Archivos .ui de Qt Designer
│   │   │   └── main_window.ui
│   │   ├── __init__.py
│   │   └── main_view.py      # Clase de PySide (MainWindow) sin lógica de negocio
│   │
│   └── 📁 services           # Conectores y lógica externa (BD, APIs, Archivos)
│       ├── __init__.py
│       ├── database_service.py
│       └── config_service.py
│
├── .gitignore                # Archivos a ignorar en Git (__pycache__, venv)
├── config.py                 # Configuraciones globales de la app
├── main.py                   # Punto de entrada (Inicializa QApplication y las capas)
├── README.md                 # Documentación del proyecto
└── requirements.txt          # Dependencias (pyside6, etc.)

