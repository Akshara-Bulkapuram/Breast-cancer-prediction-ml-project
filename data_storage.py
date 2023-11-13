import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('user_data.db')
c = conn.cursor()

# Create a table to store user data
c.execute('''
    CREATE TABLE IF NOT EXISTS user_data (
        id INTEGER PRIMARY KEY,
        radius_mean REAL,
        perimeter_mean REAL,
        area_mean REAL,
        concavity_mean REAL,
        concave_points_mean REAL,
        area_se REAL,
        radius_worst REAL,
        perimeter_worst REAL,
        area_worst REAL,
        concavity_worst REAL,
        concave_points_worst REAL,
        predicted_class INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
