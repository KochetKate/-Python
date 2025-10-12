from Database import Database
from sqlalchemy import text
from config import (
    connection_string, user_email, subject, edit_email,
    edited_email, user_testing
)

db = Database(connection_string)


def test_insert():
    db.insert(user_email, subject)
    connection = db.db.connect()
    result = connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": user_email}
    )
    user = result.fetchone()
    connection.close()
    assert user.user_email == user_email
    db.delete(user.user_id)


def test_update():
    db.insert(edit_email, subject)
    connection = db.db.connect()
    res = connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": edit_email}
    )
    user = res.fetchone()
    db.update(edited_email, user.user_id)
    resi = connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": edited_email}
    )
    user = resi.fetchone()
    connection.close()
    assert user.user_email == edited_email
    db.delete(user.user_id)


def test_delete():
    db.insert(user_testing, subject)
    connection = db.db.connect()
    result = connection.execute(
        text("SELECT * FROM users WHERE user_email = :email"),
        {"email": user_testing}
    )
    user = result.fetchone()

    assert user.user_email == user_testing
    db.delete(user.user_id)
    res_del = connection.execute(
        text("SELECT * FROM users WHERE user_id = :user_id"),
        {"user_id": user.user_id}
    )
    user = res_del.fetchone()
    assert user is None
    connection.close()
