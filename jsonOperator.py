import json


class JsonOperator:
    def __init__(self, filename):
        self.filename = filename

    def read_json(self):
        try:
            with open(self.filename, 'r') as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            return None

    def write_json(self, data={}):
        with open(self.filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)