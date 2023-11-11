import sqlite3

conn = sqlite3.connect("people.db")

people = [
    "1, 'Fairy', 'Tooth', '2022-10-08 09:15:10'",
    "2, 'Ruprecht', 'Knecht', '2023-11-09 10:16:11'",
    "3, 'Bunny', 'Easter', '2024-12-10 11:17:12'",
]

for person_data in people:
    insert_cmd = f"INSERT INTO person VALUES ({person_data})"
    conn.execute(insert_cmd)
    
conn.commit()