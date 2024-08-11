import sys
import psycopg2
from config import load_config


def insert_payment(order_no, type, card_type, last_4_cc_digits, date, raw_date, station, employee, transport_id, transaction_status, customer_paid, customer_change, total, rounding_delta):
    """ Insert a new order into the orders table """

    sql = """INSERT INTO payments(order_no, type, card_type, last_4_cc_digits, date, raw_date, station, employee, transport_id, transaction_status, customer_paid, customer_change, total, rounding_delta)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (order_no, type, card_type, last_4_cc_digits, date, raw_date, station, employee, transport_id, transaction_status, customer_paid, customer_change, total, rounding_delta))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        print('success')
    

if __name__ == '__main__':
    insert_payment(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9], sys.argv[10], sys.argv[11], sys.argv[12], sys.argv[13], sys.argv[14])
