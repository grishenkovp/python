# Создание таблицы
create_table_sql = """
            CREATE TABLE IF NOT EXISTS sales (
              id SERIAL PRIMARY KEY,
              date DATE NOT NULL, 
              user_id TEXT NOT NULL,
              product TEXT NOT NULL,
              amount REAL NOT NULL);
        """
test_table_sql = """SELECT * FROM sales LIMIT 10"""