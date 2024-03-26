from db import LaDB
db = LaDB()

results = db.drop("users")

print(results)