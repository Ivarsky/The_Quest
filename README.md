# The Quest

Juego en pygame sobre una nave que huye de una Tierra moribunda, en busca de un nuevo planeta que colonizar

## Para jugar
1. Clonar el repositorio
```
# con ssh
git clone ssh://...

# con https
git clone https://...
```

2. Abre la carpeta
```
cd the_quest
```

3. Es recomendable usar un entorno virtual antes de instalar las dependencias.
```
python -m venv env

# En MacOs o Linux
source ./env/bin/activate

# En Windows (con cmd/símbolo del sistema)
.\env\Scropts\activate
```

4. Una vez creado y activado el entorno virtual, ya puedes instalar las dependencias
```
pip install -r requirements.txt
```

5. Para arrancar el juego basta con ejecutar desde la línea de comandos:

```
python main.py
```

## Cómo jugar

- Mueve la nave con las teclas FLECHA ARRIBA y FLECHA ABAJO para mover la nave y esquivar asteroides
- Una vez esquivado un determinado numero de asteroides pasas de pantalla
- Si los asteroides golpean la nave 3 veces la nave se destruye y se pierde la partida
- Al llegar a Nueva Tierra ganas la partida
- La tecla R inicia una nueva partida

# Cómo colaborar en este proyecto
1. Clonar el repositorio

```
# con ssh

git clone ssh://...

# con https
git clone https://...
```

2. Abre la carpeta/directorio
```
cd the_quest
```

3. Crear un entorno virtual dentro de la raíz del repositorio
```
python -m venv env

# En MacOs o Linux
source ./env/bin/activate

# En Windows (con cmd/símbolo del sistema)
.\env\Scropts\activate
```

4. instalar dependencias
```
pip install -r requirements-dev.txt
```

5. Abre el codigo en IDE favorito
```
# En VS Code
code .
```

# Atribuciones

El Artwork está creado por Luis Zuno

## Links a sus redes

Twitter: @ansimuz

Patreon: https://www.patreon.com/ansimuz

Tienda: https://ansimuz.itch.io/
