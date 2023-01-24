#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


CURRENT_TIME = open("scripts/sql/dql/current_time.sql", 'r').read()
ZONE_NAME_PROMPT = input("""Enter a Zone Name.
Press ENTER for default value: America/New_York:
""")


def current_time(zone_name='America/New_York'):

    conn = psycopg2.connect(os.environ["DATABASE_URI"])
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(CURRENT_TIME, (zone_name,))
                print(f"Current Time for selected Zone name: {cur.fetchone()}")

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
    current_time()
