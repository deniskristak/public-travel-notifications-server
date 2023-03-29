from helpers.db_connection import DbConnector


def setup_db():
    conn = DbConnector()
    cursor = conn.get_cursor()

    cursor.execute(
        'CREATE TABLE IF NOT EXISTS `device_tokens` (`device_token` VARCHAR(200) NOT NULL,PRIMARY KEY (`device_token`));'
    )


if __name__ == "__main__":
    setup_db()
