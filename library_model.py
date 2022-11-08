import pandas as pd


def get_publisher(conn):
    return pd.read_sql("SELECT * FROM publisher", conn)


def get_author(conn):
    return pd.read_sql("SELECT * FROM author", conn)


def get_genre(conn):
    return pd.read_sql("SELECT * FROM genre", conn)