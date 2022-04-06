import database_conn


def lambda_handler(event, context):
    conn = database_conn.database()

    try:
        with conn.cursor() as cursor:
            sql = "DELETE FROM Transactions WHERE transaction_id = %s"
            transaction_id = event['transaction_id']
            cursor.execute(sql, transaction_id)
            conn.commit()
            return "DELETED SUCCESSFULLY"
    finally:
        conn.close()