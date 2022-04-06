import database_conn


def lambda_handler(event, context):
    conn = database_conn.database()

    try:
        with conn.cursor() as cursor:
            transaction_id = event['transaction_id']
            sql = "SELECT * FROM Transactions " \
                  "Where transaction_id = %s"
            cursor.execute(sql, transaction_id)
            conn.commit()
            return cursor.fetchall()
    finally:
        conn.close()
