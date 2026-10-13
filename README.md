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

