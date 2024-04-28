import psycopg2

conn = None
cur = None

try:
    with psycopg2.connect(
            dbname='n42',
            user='postgres',
            password='1',
            host='localhost',
            port=5432
    ) as conn:
        with conn.cursor() as cur:
            # example for create
           #  create_table_query = """ create table if not exists products1
           # # ( id serial primary key,
           # #   name varchar(20) not null,
           # #   color varchar(20) not null,
           # #   price int not null
           # #  );
           # # """
            #  cur.execute(create_table_query)
            #  conn.commit()

            #      example for select all
            #  select_products1_query = '''select * from products1;'''
            #  cur.execute(select_products1_query)

            # example for select one
        # select_one_product_query = '''select * from products1 where name = 'John';'''
        # cur.execute(select_one_product_query)

        # example for insert
        # insert_into_query = '''insert into products1(name,color,price) values (%s,%s,%s)'''
        # insert_data_list = [('Phone', 'white', 200), ('Notebook', 'black', 100), ('mouse', 'blue', 390)]
        # cur.executemany(insert_into_query, insert_data_list)
        # conn.commit()

        # example for update
        # update_query = ''' update products set  name = 'Telephone' where id = 1  '''
        # cur.execute(update_query)
        # conn.commit()

        # example for delete
        # delete_query = ''' delete from products where id = 2
        # '''
        # cur.execute(delete_query)
        # conn.commit()

except psycopg2.OperationalError as e:
    print(e)

else:
# print('Successfully inserted')
# print('Successfully updated')
# print('Successfully deleted')


# for products in cur.fetchall():
#     print(products)

# for product in cur.fetchone():
#     print(product)
pass

