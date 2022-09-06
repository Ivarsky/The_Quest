# the_quest

Juego en pygame sobre una nave que huye de una Tierra moribunda, en busca de un nuevo planeta que colonizar

## Cómo colaborar en este proyecto

Primero debes clonar este repositorio en tu PC.

Es recomendable usar un entorno virtual antes de instalar las dependencias.

```
python -m venv env

# En MacOs o Linux
source ./env/bin/activate

# En Windows (con cmd/símbolo del sistema)
.\env\Scropts\activate
```

Una vez creado y activado el entorno virtual, ya puedes instalar las dependencias

```
pip install -r requirements.txt
```

Para arrancar el juego basta con ejecutar desde la línea de comandos:

```
main.py
```
## Cómo jugar

- Mueve la nave con las teclas FLECHA ARRIBA y FLECHA ABAJO para mover la nave y esquivar asteroides
- Una vez esquivado un determinado numero de asteroides pasas de pantalla
- Si los asteroides golpean la nave 3 veces la nave se destruye y se pierde la partida
- Al llegar a Nueva Tierra ganas la partida
- La tecla R inicia una nueva partida