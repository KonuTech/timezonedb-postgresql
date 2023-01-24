#!/usr/bin/python
import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()


ZONE_TIME = open("scripts/sql/dql/zone_time.sql", 'r').read()


def menu():
    zone_name = input("Provide a Zone Name.\nPress ENTER for America/New_York.\n") or 'America/New_York'
    if zone_name is not None:
        conn = psycopg2.connect(os.environ["DATABASE_URI"])
        try:
            with conn:
                with conn.cursor() as cur:
                    like_pattern = '%{}%'.format(zone_name)
                    cur.execute(ZONE_TIME, (like_pattern ,))
                    print(f"Current Time for {zone_name}:\n{cur.fetchone()}")
                    cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()
    else:
        print("Invalid input selected.Please try again.")


if __name__ == '__main__':
    menu()
