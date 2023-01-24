#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


ZONE_TIME = open("scripts/sql/dql/zone_time.sql", 'r').read()


def menu():
    zone_name = input("Enter a Zone Name. Press ENTER for default value: America/New_York: ") or 'America/New_York'
    if zone_name is not None:
        conn = psycopg2.connect(os.environ["DATABASE_URI"])
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute(ZONE_TIME, (zone_name,))
                    print(f"Current Time for selected Zone name: {cur.fetchone()}")
                    cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


if __name__ == '__main__':
    menu()
