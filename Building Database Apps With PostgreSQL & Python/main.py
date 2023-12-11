import psycopg2

dbname = "students"
user = "postgres"
password = "1234"
host = "localhost"
port = "5432"
CONN = None

def connection():
    return psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)

try:
    CONN = connection()
    print("Connected to the database")

    def create_table():
        cur = CONN.cursor()
        name = input("Enter table name: ")
        query = f"CREATE TABLE {name} (ID SERIAL, TITLE TEXT, DESCRIPTION TEXT);"
        cur.execute(query)
        CONN.commit()
        CONN.close()
        

    def insert_table():
        title = input("title: ")
        desc = input("description: ")
        table_name = input("Enter table name: ")  # Prompt for table name
        query = f'INSERT INTO {table_name} (TITLE, DESCRIPTION) VALUES (%s, %s);'
        cur = CONN.cursor()
        cur.execute(query, (title, desc))
        CONN.commit()
        print("data inserted")
        
    def select_data():
        table_name = input("Enter table name: ")  # Prompt for table name
        query = f'SELECT * from {table_name} ;'
        cur = CONN.cursor()
        cur.execute(query)
        CONN.commit()
        rows = cur.fetchall()
        for row in rows:
            print(row)
        CONN.close()        

except psycopg2.OperationalError as e:
    print("Could not connect to the database:", e)

# create_table()
# insert_table()
select_data()
