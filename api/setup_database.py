import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """

    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

    return connection

def create_table(connection, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """

    try:
        c = connection.cursor()
        c.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def main():
    
    database = r"/Users/rhua966/Desktop/web-project/api/Data/Data.db"

    sql_create_items_table = """ CREATE TABLE IF NOT EXISTS Items (
                                                "Id"    INTEGER,
                                                "Title" TEXT,
                                                "Type"  TEXT,
                                                "Price" REAL,
                                                "Origin" TEXT,
                                                "URL"   TEXT
                                    ); """

    sql_create_comments_table = """CREATE TABLE IF NOT EXISTS Comments (
                                    "Name"  TEXT,
                                    "Comment"   TEXT,
                                    "IP"    TEXT
                                );"""

    sql_create_credentials_table = """CREATE TABLE IF NOT EXISTS Credentials (
                                        "User"  TEXT,
                                        "Password"  TEXT,
                                        "Scratchpad"    TEXT
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_items_table)
        create_table(conn, sql_create_comments_table)
        create_table(conn, sql_create_credentials_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()