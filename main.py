from db import LaDB
db = LaDB()

db.insert_in_table("users", {"id": 2,"organization":999, "email":"fail@example.com"})