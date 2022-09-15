class Records:

    def init(self):
        """
        Crea atributos para la ruta y comprueba si el archivo existe.
        """
        pass

    def insert_record(self, name: str, points: int):
        """
        Agrega un registro en el listado de records con el nombre del jugador y los puntos conseguidos.
        La lista de records debe quedar ordenada.
        Se inserta en la posicion que le corresponde de mayor a menor.
        """

    def lowest_score(self):
        """
        Devuelve un entero con el valor de puntos de la ultima de la posicion del listado de records.
        """
        pass

    def save(self):
        """
        Guarda el archivo de records
        """
        pass

    def load(self):
        """
        Carga el archivo si existe.
        """
        pass

    def reset(self):
        """
        resetea el archivo de records
        """
        pass
