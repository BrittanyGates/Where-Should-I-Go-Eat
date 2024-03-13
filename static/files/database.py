import sqlite3


def create_connection():
    """
    This function creates a database connection to the SQLite database
    :return: The connection object or nothing
    """

    connection = None

    try:
        
        connection = sqlite3.connect("/static/files/restaurant_urls")
        return connection
    except Exception as err:
        print(err)

    return connection


def create_table(connection, create_table_sql):
    """
    This function creats a table from the create_table_sql statement
    :param connection: The connection object
    :param create_table_sql: The CREATE TABLE statement
    :return:
    """

    try:
        db_cursor = connection.cursor()
        db_cursor.execute(create_table_sql)
    except Exception as err:
        print(err)


def main():
    database = r"/static/files/restaurant_urls.db"

    sql_create_restaurant_urls_table = """
    CREATE TABLE IF NOT EXISTS restaurant_urls (
        restaurant_id INTEGER PIMARY KEY, 
        restaurant_name TEXT NOT NULL, 
        restaurant_url TEXT NOT NULL)
    """

    # Create the database connection
    conn = create_connection(database)

    # Create the tables
    if conn is not None:
        # Create the restaurant_urls table
        create_table(conn, sql_create_restaurant_urls_table)
    else:
        print("Cannot create the database connection.")


if __name__ == "__main__":
    main()
