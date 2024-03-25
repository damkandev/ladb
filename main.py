from db import LaDB
db = LaDB()

def where_condition(record):
  return record.get("type", 0) == 0

results = db.select(
  "users",
  fields = ["id", "email"],
  join={"organizations": ("organization", "id")},
  order_by=("id", "asc"),
)

print(results)