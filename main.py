from db import LaDB
db = LaDB("datos.ldb")

db.create_table("users")
# {"id":1, "organization":1, "email":"tumamitaentanga@gmail.com", "fullname":"Jorge Nitales Sepulveda Mangueco", "position":"Admin", "avatar":"-", "password":"12345", "phone":"940806215", "type":1}

db.insert_in_table("users", {"id":1, "organization":1, "email":"tumamitaentanga@gmail.com", "fullname":"Jorge Nitales Sepulveda Mangueco", "position":"Admin", "avatar":"-", "password":"12345", "phone":"940806215", "type":1})

users = db.read_table("users")
for user in users:
  print(user)