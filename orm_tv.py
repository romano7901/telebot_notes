import datetime
from peewee import *
from config import username,password,host

conn = PostgresqlDatabase('postgres', user=username, password=password, host=host, port=5432)

class BaseModel(Model):
    class Meta:
        database = conn


class Notes(BaseModel):
    id      = PrimaryKeyField(null=False)
    note    = TextField(null=True)
    user_id = IntegerField(null=True)
    datetime = DateTimeField(default=datetime.datetime.now)
    class Meta:
        db_table = "notes"
        indexes = (
            ('user_id',False),
        )



