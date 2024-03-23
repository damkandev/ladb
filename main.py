from db import LaDB
# Creamos LaDB y le pasamos el archivo (datos.ldb)
db = LaDB("datos.ldb")
# Creamos una tabla
# Insertamos los datos en la tabla
db.insert_in_table("users", {"id":2, "organization":4, "email":"tumamitaentanga@gmail.com", "fullname":"Jorge Nitales Sepulveda Mangueco", "position":"Admin", "avatar":"-", "password":"12345", "phone":"940806215", "type":1})
# SELECT * FROM users
users = db.read_table("users")
for user in users:
  print(user)