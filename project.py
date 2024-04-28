import psycopg2

user = 'postgres'
host = 'localhost'
database = 'n42'
port = 5432
password = '123'

conn = psycopg2.connect(host=host,
                        user=user,
                        database=database,
                        port=port,
                        password=password)

cur = conn.cursor()

# #
#       create table if not  exists users(
# create_table_query = """ create table if not exists users
#       (
#       id  serial primary key,
#       name varchar(50) not null,
#       age int not null,
#       product_id int not null references products(id)
#       )
# """
# cur.execute(create_table_query)
# conn.commit()

# create_table_query2 = """ create table if not exists products
#   (
#    id serial primary key,
#    product_name varchar(20) not null,
#    color varchar(20) not null,
#    price int not null
#
# );
#
# """
# cur.execute(create_table_query2)
# conn.commit()
#

# example for insert

# insert_query2 = """
#      insert into products(product_name,color,price)
#        values
#          ('Telephone','white',300),
#            ('Notebook','black',400)
#
#
#
# """
# cur.execute(insert_query2)
# conn.commit()
#
# insert_query1 = """
#      insert into users(name,age,product_id)
#        values
#          ('John',20,1),
#            ('Jane',17,2 )
#
#
# """
# cur.execute(insert_query1)
# conn.commit()

# example for select_all_query
# select_all_query1 = """
#   select * from users
#    order by id;
# """
# cur.execute(select_all_query1)
# for i in cur.fetchall():
#     print(i)
#
# select_all_query2 = """
#   select * from products
#    order by id;
# """
# cur.execute(select_all_query2)
# for i in cur.fetchall():
#     print(i)

# example for select_one_query

# select_one_query1 = """
#   select * from users
#      where name= %s;
#
# """
# username = input(' ?: ')
# cur.execute(select_one_query1, (username,))
# for i in cur.fetchone():
#     print(i)
#
# select_one_query2 = """
#   select * from products
#     where product_name = %s ;
# """
# product_name = input('?: ')
# cur.execute(select_one_query2, (product_name,))
# for i in cur.fetchone():
#     print(i)

# example for  delete
# def delete_query_product(product_id):
#     delete_into_query1 = """delete from product where id = %s;"""
#
#     cur.execute(delete_into_query1, (product_id,))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# pro_id = delete_query_product(1)
#
# def delete_query_users(user_id):
#     delete_into_query2 = """delete from product where id = %s;"""
#
#     cur.execute(delete_into_query2, (user_id,))
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# user_id = delete_query_users(2)

# example for update

# def update_query_products(product_id, product_name):
#     update_query1 = """update products set product_name = %s where id = %s;"""
#     data = (product_name,product_id )
#     cur.execute(update_query1, data)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# update_query_products(1, 'Phone')
#
# def update_query_users(user_id, user_name):
#     update_query2 = """update users set name = %s where id = %s;"""
#     data = (user_name,user_id )
#     cur.execute(update_query2, data)
#     conn.commit()
#     cur.close()
#     conn.close()


# update_query_users(1, 'Fara')




