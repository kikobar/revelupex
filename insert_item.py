import sys
import psycopg2
from config import load_config


def insert_item(date, cla, name, sku, barcode, category, subcategory, quantity, total):
    """ Insert a new record into the items table """

    sql = """INSERT INTO items(date, class, name, sku, barcode, category, subcategory, quantity, total)
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (date, cla, name, sku, barcode, category, subcategory, quantity, total))

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        print('success')
    

if __name__ == '__main__':
    insert_item(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7], sys.argv[8], sys.argv[9])
