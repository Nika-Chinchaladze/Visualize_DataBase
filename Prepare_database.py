import sqlite3

conn = sqlite3.connect('sales.db')
curr = conn.cursor()

curr.execute('''UPDATE customers 
SET customer_name = 'Chincho' 
WHERE customer_name = 'Nika Chinchaladze'
''')

conn.commit()
conn.close()



# curr.execute('''CREATE TABLE IF NOT EXISTS products(
#     product_id integer,
#     product_name text,
#     price real
# )''')

# curr.execute('''CREATE TABLE IF NOT EXISTS orderdetails(
#     detail_id integer,
#     order_id integer,
#     product_id integer,
#     quantity integer
# )''')

# curr.execute('''CREATE TABLE IF NOT EXISTS employees(
#     employee_id integer,
#     first_name text,
#     last_name text,
#     level text
# )''')

# curr.execute('''CREATE TABLE IF NOT EXISTS customers(
#     customer_id integer,
#     customer_name text,
#     birthdate date,
#     city text,
#     country text
# )''')

# curr.execute('''CREATE TABLE IF NOT EXISTS orders(
#     order_id integer,
#     customer_id integer,
#     employee_id integer,
#     orderdate date
# )''')


# curr.execute('''INSERT INTO customers(customer_id, customer_name, birthdate, city, country)
# VALUES (1, 'Nika Chinchaladze', '1997-05-31', 'Axalcixe', 'Georgia'),
#        (2, 'Leri Chixladze', '1998-09-25', 'Tbilisi', 'Georgia'),
#        (3, 'Lado Quridze', '1996-03-20', 'Lanchxuti', 'Georgia'),
#        (4, 'Mike Tyson', '1980-04-15', 'New-York', 'USA'),
#        (5, 'Margot Robbie', '1990-07-02', 'Dalby', 'Australia');''')

# curr.execute('''INSERT INTO orders(order_id, customer_id, employee_id, orderdate)
# VALUES (100, 1, 1, '2010-10-11'),
#        (101, 2, 3, '2010-10-12'),
#        (102, 3, 2, '2010-10-12'),
#        (103, 4, 2, '2010-10-12'),
#        (104, 5, 3, '2010-10-12'),
#        (105, 1, 2, '2011-03-20'),
#        (106, 1, 1, '2011-03-21'),
#        (107, 1, 1, '2011-03-22'),
#        (108, 2, 1, '2012-06-05'),
#        (109, 2, 3, '2012-06-06'),
#        (110, 2, 1, '2012-06-07'),
#        (111, 2, 2, '2012-06-08'),
#        (112, 3, 1, '2013-09-17'),
#        (113, 3, 2, '2013-09-18'),
#        (114, 3, 2, '2013-09-19'),
#        (115, 3, 2, '2013-09-20'),
#        (116, 3, 2, '2013-09-21'),
#        (117, 3, 1, '2013-09-22'),
#        (118, 3, 1, '2013-09-23'),
#        (119, 4, 1, '2014-02-08'),
#        (120, 4, 2, '2014-02-09'),
#        (121, 4, 2, '2014-02-10'),
#        (122, 4, 2, '2014-02-11'),
#        (123, 4, 2, '2014-02-12'),
#        (124, 4, 1, '2014-02-13'),
#        (125, 4, 3, '2014-02-14'),
#        (126, 4, 1, '2014-02-15'),
#        (127, 5, 1, '2015-04-22'),
#        (128, 5, 1, '2015-04-23'),
#        (129, 5, 1, '2015-04-24'),
#        (130, 5, 3, '2015-04-25');''')

# curr.execute('''INSERT INTO employees(employee_id, first_name, last_name, level)
# VALUES (1, 'Sandra', 'Bullok', 'Junior'),
#        (2, 'Jodie', 'Foster', 'Middle'),
#        (3, 'Nicole', 'Kidman', 'Senior'),
#        (4, 'Angelina', 'Jolie', 'Intern');''')


# curr.execute('''INSERT INTO orderdetails(detail_id, order_id, product_id, quantity)
# VALUES (1, 100, 1, 3),
#        (2, 100, 2, 2),
#        (3, 100, 3, 5),
#        (4, 101, 1, 2),
#        (5, 101, 2, 3),
#        (6, 101, 3, 1),
#        (7, 101, 4, 2),
#        (8, 102, 1, 1),
#        (9, 102, 4, 1),
#        (10, 103, 1, 5),
#        (11, 104, 3, 6),
#        (12, 104, 4, 2),
#        (13, 105, 2, 1),
#        (14, 105, 3, 3),
#        (15, 105, 4, 12),
#        (16, 106, 2, 2),
#        (17, 106, 3, 3),
#        (18, 107, 4, 3),
#        (19, 108, 1, 10),
#        (20, 109, 1, 3),
#        (21, 110, 1, 3),
#        (22, 111, 1, 3),
#        (23, 112, 1, 5),
#        (24, 112, 2, 3),
#        (25, 112, 3, 9),
#        (26, 112, 4, 3),
#        (27, 113, 2, 3),
#        (28, 114, 1, 4),
#        (29, 115, 3, 7),
#        (30, 116, 4, 11),
#        (31, 117, 4, 2),
#        (32, 118, 1, 3),
#        (33, 119, 2, 5),
#        (34, 119, 4, 2),
#        (35, 120, 1, 3),
#        (36, 121, 1, 1),
#        (37, 122, 1, 23),
#        (38, 122, 2, 9),
#        (39, 122, 3, 7),
#        (40, 122, 4, 3),
#        (41, 123, 2, 3),
#        (42, 124, 2, 4),
#        (43, 125, 1, 3),
#        (44, 126, 2, 5),
#        (45, 127, 1, 2),
#        (46, 127, 2, 4),
#        (47, 127, 3, 6),
#        (48, 127, 4, 8),
#        (49, 128, 1, 10),
#        (50, 129, 3, 12),
#        (51, 130, 2, 9),
#        (52, 130, 4, 2);''')


# curr.execute('''INSERT INTO products(product_id, product_name, price)
# VALUES (1, 'Coca-cola', 1.8),
#        (2, 'Fanta', 1.75),
#        (3, 'Cold-Tea', 2.6),
#        (4, 'Natural Juice', 3.4),
#        (5, 'Pepsi', 1.3);''')