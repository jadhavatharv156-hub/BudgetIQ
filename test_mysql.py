import mysql.connector

print("START")

config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "atharv012",
    "database": "budgetiq",
    "use_pure": True
}

print("Before connect")

db = mysql.connector.connect(**config)

print("Connected")