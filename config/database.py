import psycopg2

def connection_db():

    conn = psycopg2.connect(
        database = "M7_recuperacion",
        user = "postgres",
        password = "pass_postgres1",
        host = "localhost",
        port = "5432"
    )

    print("Connexió establerta correctament")
    return conn