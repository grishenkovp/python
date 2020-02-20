import pandas as pd
import postgresql
import psycopg2
import time

# start_time = time.time()
# db = postgresql.open('pq://postgres:admin@localhost:5432/youla')
# print("Database opened successfully")
# records=db.query('Select s.*, v.cnt, c.cnt From public.search as s left join public.view as v on s.search_id=v.search_id '
#                  'left join public.contact as c on s.search_id=c.search_id Limit 10')
# labels=["region_id","user_id","search_id","categoty_id", "subcategory_id","default","use_category","search_text","price_filter",
#         "bs_filter","discount_filter","delivery_filter","distance_filter","publication_filter","use_properties", "sorting_published",
#         "sorting_distance","sorting_price","cnt_v","cnt_c"]
# df=pd.DataFrame.from_records(records,columns=labels)
# print("Operation done successfully")
# print(df)
# print("--- %s seconds ---" % (time.time() - start_time))


start_time = time.time()
conn = psycopg2.connect("dbname='youla' user='postgres' password='admin' host='localhost' port='5432'")
print("Database opened successfully")
cursor = conn.cursor()
cursor.execute('Select s.*, v.cnt, c.cnt From public.search as s left join public.view as v on s.search_id=v.search_id '
               'left join public.contact as c on s.search_id=c.search_id Limit 10')
records = cursor.fetchall()
labels=["region_id","user_id","search_id","categoty_id", "subcategory_id","default","use_category","search_text","price_filter",
        "bs_filter","discount_filter","delivery_filter","distance_filter","publication_filter","use_properties", "sorting_published",
        "sorting_distance","sorting_price","cnt_v","cnt_c"]
df=pd.DataFrame.from_records(records,columns=labels)
print("Operation done successfully")
cursor.close()
conn.close()
print(df)
print("--- %s seconds ---" % (time.time() - start_time))

