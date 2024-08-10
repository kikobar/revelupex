import sys
import psycopg2
from config import load_config


def insert_order(reporting_no, order_no, offline_no, created_by, first_opened, last_closed, net_sales, tax, final_total, payments_total):
    """ Insert a new order into the orders table """

    sql = """INSERT INTO orders(reporting_no, order_no, offline_no, created_by, first_opened, last_closed, net_sales, tax, final_total, payments_total)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (reporting_no, order_no, offline_no, created_by, first_opened, last_closed, net_sales, tax, final_total, payments_total))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        print('success')
    

if __name__ == '__main__':
    insert_order(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10])
