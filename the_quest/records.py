import csv
import os

MAX_RECORDS = 10


class Records:

    filename = "records.csv"
    dir_path = os.path.dirname(
        os.path.realpath(__file__)
    )
    # __file__ = corresponde con el path del archivo actual(records.py)

    def __init__(self):
        """
        Crea atributos para la ruta y comprueba si el archivo existe.
        """
        self.game_records = []
        self.data_path = os.path.join(
            os.path.dirname(self.dir_path), "data")
        self.file_path = os.path.join(self.data_path, self.filename)
        self.check_records_file()

    def check_records_file(self):
        if not os.path.isdir(self.data_path):
            os.makedirs(self.data_path)
            print("El directorio data no existe")
        if not os.path.exists(self.file_path):
            self.reset()

    def insert_record(self, name: str, points: int):
        """
        Agrega un registro en el listado de records con el nombre del jugador y los puntos conseguidos.
        La lista de records debe quedar ordenada.
        Se inserta en la posicion que le corresponde de mayor a menor.
        """
        self.game_records.append([name, points])
        self.game_records.sort(key=lambda item: item[1], reverse=True)

    def lowest_score(self):
        """
        Devuelve un entero con el valor de puntos de la ultima de la posicion del listado de records.
        """
        return self.game_records[-1]

    def save(self):
        """
        Guarda el archivo de records
        """
        with open(self.file_path, mode="w") as records_file:
            records_writer = csv.writer(
                records_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            records_writer.writerow(["Jugador", "Puntos"])
            for record in self.game_records[:MAX_RECORDS]:
                records_writer.writerow(record)

    def load(self):
        """
        Carga el archivo si existe.
        """
        with open(self.file_path, mode="r") as records_file:
            records_reader = csv.reader(
                records_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            line_counter = 0
            self.game_records = []
            for line in records_reader:
                line_counter += 1
                if line_counter == 1:
                    continue
                self.game_records.append([line[0], line[1]])

    def reset(self):
        """
        resetea el archivo de records
        """
        print("creado archivo de records vacio")
        self.game_records = []
        for count in range(MAX_RECORDS):
            self.game_records.append(['---', 0])
        self.save()
