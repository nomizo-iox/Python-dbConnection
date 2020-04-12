import pymysql


def db_connection():
    # Connect to database
    conn = pymysql.Connect(host='host',
                           user='username',
                           password='password',
                           port=33560,
                           db='local')

    try:
        with conn.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO `client` (`first_name`, `last_name`,`sex`, `email`, `username`, `password`) " \
                  "VALUE (%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, ('Tony', 'Stark', 'M', 'tstark@gmail.com', 'sexy_genius-08', 'mark_70'))

            # Connection is not autocommit by default.  So you must commit to save your changes.
        conn.commit()

        with conn.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `client` WHERE `email`=%s"
            cursor.execute(sql, ('tstark@gmail.com',))
            result = cursor.fetchone()
            print(result)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    db_connection()
