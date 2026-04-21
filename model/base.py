from peewee import Model, SqliteDatabase

db = SqliteDatabase("database.sqlite")
db.connect(reuse_if_open=True)
print("Initialized database")

class BaseModel(Model):
    class Meta:
        database = db

