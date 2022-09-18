
import sqlite3
from unicodedata import name


""""
SELECT id, name, TotalScore FROM records ORDER BY TotalScore DESC
"""


class DBManager:
    def __init__(self, route):
        self.route = route

    def load(self):

        query = "SELECT id, name, TotalScore FROM records ORDER BY TotalScore DESC LIMIT 10"

        # 1. conectar con la database
        connection = sqlite3.connect(self.route)

        # 2. abrir un cursor
        cursor = connection.cursor()

        # 3. ejecutar consulta SQL
        cursor.execute(query)

        # 4. tratar los datos

        #   4.1 obtener los nombres de columnas
        #       (('nombre_columna', ...), (), ()...)
        #   4.2 pedir todos los datos (registros)
        #   4.3 recorrer los resultados:
        #       4.3.1 crear un diccionario
        #           - recorrer la lista de los nombre de columnas
        #           - para cada columna: nombre + valor
        #       4.3.2 guardar en la lista de records
        #   [{nom_col1}:{val_col1}]...

        self.records = []
        column_names = []

        # description devuelve como esta definida cada columna, no lo que hay en ellas.
        for desc_column in cursor.description:
            # Dentro de desc_column el primer valor es el nombre de la columna
            column_names.append(desc_column[0])
        # column_names va a devolver el nombre de cada columna = [id, name, TotalScore]

        data = cursor.fetchall()
        for i in data:
            record = {}
            index = 0
            for name in column_names:
                record[name] = i[index]
                index += 1
            self.records.append(record)

        connection.close()

        return self.records

    def lowest_top10_score(self):
        # obtenemos el record mas bajo de todos
        scores_of_records = []
        records = self.load()
        for record in records:
            scores_of_records.append(record["TotalScore"])

        if len(scores_of_records) > 10:
            lowest_score = min(scores_of_records)
            return lowest_score
        else:
            # si hay menos de 10 puntuaciones guardadas en la base de datos, devuelve un 0
            # permitiendo cualquier nueva puntuacion entrar a la lista de records
            return 0

    def update(self, name, TotalScore):
        query = "UPDATE records SET name = (?), TotalScore = (?) WHERE TotalScore = (?)"
        connection = sqlite3.connect(self.route)
        cursor = connection.cursor()
        cursor.execute(query, (name, TotalScore))
        connection.commit()
        connection.close()

    def save(self, name, TotalScore):
        query = "INSERT INTO records (name, TotalScore) VALUES (?, ?)"
        connection = sqlite3.connect(self.route)
        cursor = connection.cursor()
        cursor.execute(query, (name, TotalScore))
        connection.commit()
        connection.close()

    def reset(self):
        query = "DELETE FROM records"
        connection = sqlite3.connect(self.route)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()


'''
class Records:  # FIXME: adaptar para sqlite

    filename = "records.db"
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
'''
