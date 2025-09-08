# Python CLI To-Do App

Una aplicación de tareas (to-do) multiusuario y segura para la línea de comandos en Python. Cada usuario tiene sus tareas cifradas y protegidas por su contraseña.

## Características
- Registro y login de usuarios
- Contraseñas protegidas con hash y sal
- Cada usuario tiene un archivo cifrado para sus tareas
- Añadir, editar, completar, eliminar y listar tareas
- Añadir notas a las tareas
- Borrar todas las tareas completadas
- Todos los datos de tareas están cifrados usando la contraseña del usuario

## Requisitos
- Python 3.7+
- cryptography

## Instalación
1. Clona o descarga este repositorio.
2. (Recomendado) Crea y activa un entorno virtual:
	```powershell
	python -m venv venv
	.\venv\Scripts\Activate
	```
3. Instala las dependencias:
	```powershell
	pip install cryptography
	```
4. Ejecuta la app:
	```powershell
	python Main.py
	```

## Uso
- Regístrate con un nombre de usuario y contraseña.
- Inicia sesión con tus credenciales.
- Gestiona tus tareas de forma segura desde la CLI.

## Seguridad
- Las contraseñas nunca se guardan en texto plano.
- Las tareas de cada usuario se cifran con una clave derivada de su contraseña y una sal única.


## Crear un ejecutable
Puedes crear un ejecutable standalone usando [PyInstaller](https://pyinstaller.org/):

1. Instala PyInstaller:
	 ```powershell
	 pip install pyinstaller
	 ```
2. Construye el ejecutable:
	 ```powershell
	 pyinstaller --onefile Main.py
	 ```
3. El ejecutable estará en la carpeta `dist`.

**Personalización:**
- Para agregar un icono (formato .ico):
	```powershell
	pyinstaller --onefile --icon=icono.ico Main.py
	```
- Para ocultar la consola (solo para apps con interfaz gráfica):
	```powershell
	pyinstaller --onefile --windowed Main.py
	```

**Nota:** Si usas un entorno virtual, actívalo antes de ejecutar PyInstaller.

## Licencia
MIT
# Python-CLI-To-do-App