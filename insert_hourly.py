import sys
import psycopg2
from config import load_config


def insert_hourly(date, time, transactions, guests, items, avg_sales, sales, percent_sales):
    """ Insert a new record into the guests table """

    sql = """INSERT INTO guests(date, time, transactions, guests, items, avg_sales, sales, percent_sales)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"""
    
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (date, time, transactions, guests, items, avg_sales, sales, percent_sales))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        print('success')
    

if __name__ == '__main__':
    insert_hourly(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8])
