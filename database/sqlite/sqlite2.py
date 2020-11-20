import sqlite3
import pandas as pd


def test_db():
    con = sqlite3.connect('test.db')
    cur = con.cursor()

    # ************** Добавление записей в БД. Вариант 1 ******************

    # with con:
    #     cur.execute("""
    #         CREATE TABLE product (
    #             id INT NOT NULL PRIMARY KEY,
    #             name TEXT,
    #             amount INTEGER
    #         );
    #     """)
    #
    # query = 'INSERT INTO product (id, name, amount) values(?, ?, ?)'
    #
    # data = [
    #     (1, 'pr1', 25),
    #     (2, 'pr2', 50),
    #     (3, 'pr3', 75)
    # ]
    #
    # with con:
    #     cur.executemany(query, data)

    # ************** Добавление записей в БД. Вариант 2 ******************
    #     data2 = (4, "pr4", 1000)
    #     with con:
    #         cur.execute("INSERT INTO product (id, name, amount) values(?, ?, ?)", data2)

    # ************** Получение записей из БД. Вариант 1. Все строки ******************
    #     print(cur.execute("SELECT * FROM product WHERE  amount <= 50").fetchall())

    # ************** Получение записей из БД. Вариант 2. Только одна строка ******************
    #     print(cur.execute("SELECT * FROM product WHERE amount <= 50").fetchone())

    # ************** Связь между таблицами ******************

    # with con:
    #     cur.execute("""
    #         CREATE TABLE region (
    #             id INT NOT NULL PRIMARY KEY,
    #             name TEXT
    #         );
    #     """)
    # with con:
    #     cur.execute("""
    #         CREATE TABLE product_region (
    #             product_id INT,
    #             region_id INT,
    #             PRIMARY KEY(product_id, region_id),
    #             FOREIGN KEY(product_id) REFERENCES product(id),
    #             FOREIGN KEY(region_id) REFERENCES region(id)
    #         );
    #     """)

    # data3 = [
    #     (1, "region1"),
    #     (2, "region2"),
    #     (3, "region3")
    # ]
    # with con:
    #     cur.executemany("INSERT INTO region VALUES(?, ?)", data3)
    #

    # data4 = [
    #     (1, 2),
    #     (2, 1),
    #     (3, 2),
    #     (4, 3),
    # ]
    # with con:
    #     cur.executemany("INSERT INTO product_region VALUES(?, ?)", data4)
    #
    # print(cur.execute("""
    #     SELECT product.name, product.amount, region.name
    #     FROM product, region, product_region
    #     WHERE (product.id = product_region.product_id AND
    #            region.id = product_region.region_id)
    #     """).fetchall())
    # ************** Добавление записей в БД. Библиотека Pandas ******************
    with con:
        cur.execute("""
                DROP TABLE IF EXISTS sales;
            """)
        cur.execute("""
                        CREATE TABLE sales (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            date INT,
                            region TEXT,
                            manager TEXT,
                            product TEXT,
                            amount INT
                        );
                    """)
    df1 = pd.read_csv('sales1.csv', sep=';', parse_dates=['date'], dayfirst=True)
    # print(df1)
    df1.to_sql("sales", con=con, if_exists='append', index=False)
    df2 = pd.read_csv('sales2.csv', sep=';', parse_dates=['date'], dayfirst=True)
    # print(df2)
    df2.to_sql("sales", con=con, if_exists="append", index=False)

    df3 = pd.read_sql("SELECT * FROM sales;", con)
    print(df3)

    cur.close()
    con.close()


if __name__ == '__main__':
    test_db()
