from sqlalchemy import create_engine
engine = create_engine('sqlite:///college.db', echo = True)
from sqlalchemy.sql.expression import update


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

# Creating a table
employees = Table(
   'employees', meta,
   Column('id', Integer, primary_key = True),
   Column('name', String),
   Column('lastname', String)
)
# Inserting values in database
conn = engine.connect()

conn.execute(employees.insert(), [
   {'name':'Vaquar','lastname':'Khan'},
   {'name': 'Mohsin', 'lastname': 'Shaikh'},
   {'name': 'Abrar', 'lastname': 'Husain'},
   {'name': 'Zeeshan', 'lastname':'Ali'},

])
# Inserting a single value in database
ins = employees.insert().values(name = 'razique', lastname = 'husain')
ins1 = employees.insert().values(name = 'yasir', lastname = 'ali')
result = conn.execute(ins)
result1 = conn.execute(ins1)

# Deleting a value in database
delete_user = employees.delete().where(employees.c.name == 'Abrar')
conn.execute(delete_user)
e= employees.select()
conn.execute(e).fetchall()


