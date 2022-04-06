import pymysql.err

import database_conn


def lambda_handler(event, context):
    conn = database_conn.database()
    try:
        with conn.cursor() as cursor:
            transaction_id = event['transaction_id']
            amount = event['amount']
            transaction_type = event['transaction_type']

            insert_query = "insert into Transactions(transaction_id, amount, transaction_type) values(%s, %s, %s)"
            cursor.execute(insert_query, (transaction_id, amount, transaction_type))
            conn.commit()
            return "INSERTED SUCCESSFULLY"

    except pymysql.err.IntegrityError:
        return "Error: This Transaction is already exist"

    finally:
        conn.close()