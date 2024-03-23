import json

class LaDB:
  def __init__(self, file='datos.ldb'):
    self.file = file
    self.data = self.load_data()

  def load_data(self):
    try:
      with open(self.file, 'r') as file:
        return json.load(file)
    except FileNotFoundError:
      return {}
    except json.JSONDecodeError:
      print("Warning: Error decoding data. Initializing with empty data.")
      return {}

  def save_data(self):
    with open(self.file, 'w') as file:
      json.dump(self.data, file, indent=4)

  def create_table(self, table_name):
    if table_name not in self.data:
      self.data[table_name] = []
      self.save_data()
      return True
    return False

  def insert_in_table(self, table_name, register):
    if table_name in self.data:
      self.data[table_name].append(register)
      self.save_data()
      return True
    return False

  def read_table(self, table_name):
    return self.data.get(table_name, [])