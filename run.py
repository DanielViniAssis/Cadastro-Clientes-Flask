from app import app
import psycopg2


def main():
    conn = psycopg2.connect('postgres://avnadmin:************************@pg-3e3466ed-dvs-63de.k.aivencloud.com:17219/defaultdb?sslmode=require')

    query_sql = 'SELECT VERSION()'

    cur = conn.cursor()
    cur.execute(query_sql)

    version = cur.fetchone()[0]
    print(version)


if __name__ == "__main__":
    app.run()