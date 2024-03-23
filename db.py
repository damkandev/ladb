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

  def create(self, key, value):
    if key in self.data:
      return False
    self.data[key] = value
    self.save_data()
    return True

  def read(self, key):
    return self.data.get(key)

  def update(self, key, value):
    if key in self.data:
      self.data[key] = value
      self.save_data()
      return True
    return False

  def delete(self, key):
    if key in self.data:
      del self.data[key]
      self.save_data()
      return True
    return False