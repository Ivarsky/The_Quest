
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

        if len(scores_of_records) < 10:
            # si hay menos de 10 puntuaciones guardadas en la base de datos, devuelve un 0
            # permitiendo cualquier nueva puntuacion entrar a la lista de records
            return 0

        lowest_score = min(scores_of_records)
        return lowest_score

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
