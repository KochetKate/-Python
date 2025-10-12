from sqlalchemy import create_engine, text


class Database:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def insert(self, user_email, subject):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("""
            INSERT INTO users (user_id, user_email, subject_id)
            VALUES ((SELECT MAX(user_id) + 1 FROM users),
            :user_email, :subject_id)
        """)
        connection.execute(sql, {
            "user_email": user_email,
            "subject_id": subject
        })
        transaction.commit()
        connection.close()

    def update(self, new_email, user_id):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("""
            UPDATE users SET user_email = :user_email
            WHERE user_id = :user_id
        """)
        connection.execute(sql, {
            "user_email": new_email,
            "user_id": user_id
        })
        transaction.commit()
        connection.close()

    def delete(self, user_id):
        connection = self.db.connect()
        transaction = connection.begin()
        sql = text("DELETE FROM users WHERE user_id = :user_id")
        connection.execute(sql, {
            "user_id": user_id
        })
        transaction.commit()
        connection.close()
