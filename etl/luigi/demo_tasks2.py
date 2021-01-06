import pandas as pd
import numpy as np
import sqlite3
import luigi


class FileTransformation(luigi.Task):
    param1 = luigi.Parameter(default="data_old")
    param2 = luigi.Parameter(default="data_new")

    def output(self):
        return luigi.LocalTarget('data_new.csv')

    def run(self):
        df = pd.read_csv('{}.csv'.format(self.param1),
                         sep=";",
                         header=None,
                         names=["date", "region", "manager", "amount"],
                         parse_dates=["date"],
                         dayfirst=True)

        df["bonus"] = np.where(df["amount"] > 200, 50, 0)
        df.to_csv('{}.csv'.format(self.param2),sep=";",index=False)


class LoadData(luigi.Task):
    param3 = luigi.Parameter(default="data_new")
    param4 = luigi.Parameter(default="db_test")

    def requires(self):
        return FileTransformation()

    def run(self):
        def load_data():
            con = sqlite3.connect('{}.db'.format(self.param4))
            cur = con.cursor()
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
                                    amount INT,
                                    bonus INT
                                );
                            """)
            df = pd.read_csv('{}.csv'.format(self.param3),
                             sep=";",
                             parse_dates=["date"])
            df.to_sql("sales", con=con, if_exists='append', index=False)
            cur.close()
            con.close()

        load_data()

if __name__ == '__main__':
    luigi.run()
