import mysql.connector

def get_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="smarttbot"
    )

    cursor = db.cursor()
    
    return db, cursor

def create_tables():
    _, cursor = get_connection()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS `smarttbot`.`currencies` (
        `exchange_id` INT NOT NULL UNIQUE,
        `currency` VARCHAR(20) NOT NULL UNIQUE,
        PRIMARY KEY (`exchange_id`));
    ''')
