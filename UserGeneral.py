from DBManager import DBManager


def update_user_db(db_obj, client):  # メソッドが呼ばれて１度しか呼ばれないので、initに入れるか関数化する
    conn = db_obj.connector()
    cursor = conn.cursor()
    for user in client:
        mention = user.mention if not '!' in user.mention else user.mention.replace('!', '')
        print(f'user:{user}  mention{mention}')
        # cursor.execute("INSERT INTO user_detail (user_name, user_code, update_at) "
        #                "VALUE (%s, %s, NOW()) "
        #                "ON DUPLICATE KEY UPDATE update_at=values(update_at) ",
        #                [str(user), mention]
        #                )

        cursor.execute("INSERT INTO "   #  一旦テストで
                       "dev (user_name, user_code, update_at) "
                       "value (%s, %s, now())"
                       "ON DUPLICATE KEY UPDATE update_at=values(update_at) ",
                       [str(user), mention]
                       )
    for i in cursor:
        print(i)
    db_obj.commit()
