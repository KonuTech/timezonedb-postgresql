#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()

# DIMENSIONS = ["COUNTRY", "TIME_ZONE"]
DROP_COUNTRY = open("scripts/sql/ddl/drop_country.sql", 'r').read()
DROP_TIME_ZONE = open("scripts/sql/ddl/drop_time_zone.sql", 'r').read()
CREATE_COUNTRY = open("scripts/sql/ddl/create_country.sql", 'r').read()
CREATE_TIME_ZONE = open("scripts/sql/ddl/create_time_zone.sql", 'r').read()
INSERT_COUNTRY = open("scripts/sql/dml/insert_country.sql", 'r').read()
INSERT_TIME_ZONE = open("scripts/sql/dml/insert_time_zone.sql", 'r').read()


def call(query):

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)

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
    call(DROP_COUNTRY)
    call(DROP_TIME_ZONE)
    call(CREATE_COUNTRY)
    call(CREATE_TIME_ZONE)
    call(INSERT_COUNTRY)
    call(INSERT_TIME_ZONE)
