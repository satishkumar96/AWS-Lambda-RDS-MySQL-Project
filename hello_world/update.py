import database_conn


def lambda_handler(event, context):
    conn = database_conn.database()

    try:
        with conn.cursor() as cursor:
            sql = "UPDATE Transactions SET amount = %s, transaction_type = %s WHERE transaction_id = %s"
            amount = event['amount']
            transaction_type = event['transaction_type']
            transaction_id = event['transaction_id']
            cursor.execute(sql, (amount, transaction_type, transaction_id))
            conn.commit()
            return "UPDATED SUCCESSFULLY"
    finally:
        conn.close()
