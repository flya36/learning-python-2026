# from sqlalchemy import create_engine, text

# engine = create_engine('mysql://root:fly060712@localhost/test',echo=True)
# conn = engine.connect()

# query = text('select * from students')
# result_set = conn.execute(query)

# for row in result_set:
#     print(row)

# conn.close()

# engine.dispose()



# # 创建表
# import sqlalchemy

# engine = sqlalchemy.create_engine('mysql://root:fly060712@localhost/test')

# meta_data = sqlalchemy.MetaData()

# person = sqlalchemy.Table(
#     'person',meta_data,
#     sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
#     sqlalchemy.Column('name',sqlalchemy.String(128),unique=True,nullable=False),
#     sqlalchemy.Column('birthday',sqlalchemy.Date,nullable=False),
#     sqlalchemy.Column('address',sqlalchemy.String(255),nullable=True)
# )

# meta_data.create_all(engine)

# # 增加操作
# person_insert = person.insert()     #生成insert语句模板
# insert_tom = person_insert.values(name='tom',birthday='2002-10-9')

# with engine.connect() as conn:
#     result = conn.execute(insert_tom)
#     print(result.inserted_primary_key)
#     conn.commit()

# # 插入多条语句
# person_insert = person.insert() 
# with engine.connect() as conn:
#     conn.execute(person_insert,[
#         {'name':'fly','birthday':'2006-7-12'},
#         {'name':'fqq','birthday':'2003-9-23'},
#         {'name':'fzy','birthday':'2008-10-25'},
#     ])
#     conn.commit()

# # 查询
# with engine.connect() as conn:
#     query = person.select()
#     result_set = conn.execute(query)
#     # 1
#     # for row in result_set:
#     #     print(row.name)

#     # 2
#     # result = result_set.fetchall()
#     # print(result)

#     # 3 查找一行
#     result = result_set.fetchone()
#     print(result)
#     # conn.commit


# # 带条件的查询
# with engine.connect() as conn:
#     query = person.select().where(person.c.birthday > '2007-1-1')
#     result_set = conn.execute(query)
#     result = result_set.fetchall()
#     print(result)

# # 更新记录
# with engine.connect() as conn:
#     update_query = person.update().values(address='chongqing').where(person.c.id == 2)
#     conn.execute(update_query)
#     conn.commit()

# # 删除
# with engine.connect() as conn:
#     delete_query = person.delete().where(person.c.id==1)
#     conn.execute(delete_query)
#     conn.commit()


# # 创建一对多关系的表
# department = sqlalchemy.Table(
#     'department',meta_data,
#     sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
#     sqlalchemy.Column('name',sqlalchemy.String(255),nullable=False,unique=True)
# )

# employee = sqlalchemy.Table(
#     'employee',meta_data,
#     sqlalchemy.Column('id',sqlalchemy.Integer,primary_key=True),
#     sqlalchemy.Column('name',sqlalchemy.String(255),nullable=False),
#     sqlalchemy.Column('department_id',sqlalchemy.Integer,sqlalchemy.ForeignKey('department.id'),nullable=False)
# )

# meta_data.create_all(engine)

# with engine.connect() as conn:
#     conn.execute(department.insert(), [
#         {"name": "hr"}, {"name": "it"}
#     ])
#     conn.execute(employee.insert(), [
#         {"department_id": 1, "name": "Jack"},
#         {"department_id": 1, "name": "Tom"},
#         {"department_id": 1, "name": "Mary"},
#         {"department_id": 2, "name": "Smith"},
#         {"department_id": 2, "name": "Rose"},
#         {"department_id": 2, "name": "Leon"},
#     ])

#     conn.commit()

# 查询关联表
# with engine.connect() as conn:
#     join = employee.join(department,department.c.id == employee.c.department_id)
#     query = sqlalchemy.select(join).where(department.c.name == 'hr')

#     print(conn.execute(query).fetchall())

# with engine.connect() as conn:
#     join = employee.join(department,department.c.id == employee.c.department_id)
#     query = sqlalchemy.select(employee).select_from(join).where(department.c.name == 'hr')

#     print(conn.execute(query).fetchall())


# 映射类数据库
from sqlalchemy import Column, Date, Integer, String, create_engine, or_
from sqlalchemy.orm import declarative_base,sessionmaker

engine = create_engine('mysql://root:fly060712@localhost/test',echo=True)
Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer,primary_key=True)
    name = Column(String(128),unique=True,nullable=False)
    birthday = Column(Date,nullable=False)
    address = Column(String(255),nullable=True)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

session = Session()

# p = Person(name='Amy',birthday='2000-9-18',address='unknown')
# session.add(p)

# session.commit()

# 查询所有
# result = session.query(Person).all()

# for person in result:
#     print(person.name,person.address,person.birthday)

# # 带条件的查询
# result = session.query(Person).filter(or_(Person.address =='chongqing',Person.name.startswith('f')))

# for person in result:
#     print(person.name,person.address,person.birthday)

# 修改单条记录
# 1
# result = session.query(Person).filter(Person.id == 3).one()
# result.address = 'chongqing'

# # 2
# session.query(Person).filter(Person.id == 4).update({Person.address:'chongqing'})
# session.commit()