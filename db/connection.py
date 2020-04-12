import pymysql


def db_connection():
    cnx = pymysql.Connect(host='host',
                          user='username',
                          password='password',
                          port=33560,
                          db='local')

    try:
        with cnx.cursor() as cursor:
            sql1 = "SELECT * FROM `client`"
            cursor.execute(sql1)
            # result = cursor.fetchone()
            for row in cursor:
                print(row)

    finally:
        cursor.close()
        cnx.close()


if __name__ == '__main__':
    db_connection()
