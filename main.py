from db import LaDB
db = LaDB("datos.ldb")

db.create("usuario1", {"nombre":"Juan", "edad":20})

usuario = db.read("usuario1")
print(usuario)

db.update("usuario1", {"nombre":"José", "edad":21})

usuario = db.read("usuario1")
print(usuario)
