from db import LaDB
db = LaDB()

def where_condition(record):
  return record.get("type", 0) == 1

results = db.select(
  "users",
  fields = ["id", "email", "organization"],
  where=where_condition,
  order_by=("id", "asc"),
  limit=10
)

print(results)