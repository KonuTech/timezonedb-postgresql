#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


CREATE_COUNTRY = open("scripts/sql/ddl/create_country.sql", 'r').read()
CREATE_TIME_ZONE = open("scripts/sql/ddl/create_time_zone.sql", 'r').read()
INSERT_COUNTRY = open("scripts/sql/dml/insert_country.sql", 'r').read()
INSERT_TIME_ZONE = open("scripts/sql/dml/insert_time_zone.sql", 'r').read()

# def drop_tables():
#
#     conn = psycopg2.connect(os.environ["DATABASE_URI"])
#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute(CREATE_COUNTRY)
#
#                 # commit the transaction
#                 conn.commit()
#
#                 # close the cursor
#                 cur.close()
#
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#     finally:
#         if conn is not None:
#             conn.close()


def create_tables():

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(CREATE_COUNTRY)
                cur.execute(CREATE_TIME_ZONE)

                # commit the transaction
                conn.commit()

                # close the cursor
                cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def populate_tables():

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(INSERT_COUNTRY)
                cur.execute(INSERT_TIME_ZONE)

                # commit the transaction
                conn.commit()

                # close the cursor
                cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # drop_tables()
    create_tables()
    populate_tables()
