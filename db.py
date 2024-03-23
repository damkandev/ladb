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

  def create_table(self, table_name, primary_key = None, foreign_keys = None):
    if table_name not in self.data:
      self.data[table_name] = {"records": [], "primary_key": primary_key, "foreign_keys": foreign_keys or {}}
      self.save_data()
      return True
    return False

  def insert_in_table(self, table_name, record):
    if table_name in self.data:
      table_info = self.data[table_name]
      pk = table_info["primary_key"]

      # Verificar unicidad de la PK
      if pk and any(r[pk] == record[pk] for r in table_info["records"]):
        print(f"Error: duplicated in the primary key '{pk}'.")
        return False

      # Verificar claves foraneas
      for fk, ref in table_info.get("foreign_keys", {}).items():
        ref_table, ref_pk = ref
        if not any(r[ref_pk] == record[fk] for r in self.data[ref_table]["records"]):
          print(f"Error: Foreign key constraint failed for '{fk}' referencing '{ref_table}.{ref_pk}'")
          return False
      table_info["records"].append(record)
      self.save_data()
      return True
    return False

  def read_table(self, table_name):
    return self.data.get(table_name, [])