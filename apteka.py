import psycopg2
from prettytable import PrettyTable



conn = psycopg2.connect(
    dbname="Apteka",
    user="postgres",
    password="Sevinch0205!",
    host="localhost", #127.0.0.1
    port="5432"
)

cur = conn.cursor()


s2 = ''' 
create table if not exists Dorilar(
    id serial primary key
    name varchar(100) not null
    price decimal(10, 2)
    make varchar(50) not null
    count int
);
'''

def insert_func(table_name):
    cur.execute(f"select *from {table_name}")
    columns = [i[0] for i in cur.description]

    data = []
    s_ = len(columns)*'%s,'
    s = s_[:-1]
    for i in columns[1:]:
        field = input(f"{i} ni kiriting: ")
        data.append(field)
    columns = ','.join(columns[1:])
    data_ = [int(i) if i.isdigit() else i for i in data]

    insert_query = f"""insert into {table_name} ({columns}) values{tuple(data_)}"""
    cur.execute(insert_query)
    print('Dori qoshildi', insert_query)


# def view_all(table_name):
#     table = PrettyTable()
#     cur.execute(f"select *from {table_name}")
#     columns = [i[0] for i in cur.description]
#     table.field_names = columns
#     table.add_rows(cur.fetchall())
#     print(table)


def search_func(table_name):
    name = input('Dori nomini kiriting: ')
    cur.execute(f"select *from {table_name} where name = '{name}'")
    if not None:
        table = PrettyTable()
        columns = [i[0] for i in cur.description]
        table.field_names = columns
        table.add_rows(cur.fetchall())
        print(table)
        print(cur.fetchall())
    else:
        print("Bizda bu maxsulot mavjud emas!")

search_func('dorilar')


conn.commit()
conn.close()