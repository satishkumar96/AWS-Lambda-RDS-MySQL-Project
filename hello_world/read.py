import database_conn


def lambda_handler(event, context):
    conn = database_conn.database()

    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Transactions")
            rows = cursor.fetchall()
            conn.commit()
            return rows
    finally:
        conn.close()
