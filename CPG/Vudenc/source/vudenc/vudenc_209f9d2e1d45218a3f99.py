def display_all_data():...
conn = check_heroku_db()
cur = conn.cursor()
out = []
query = """
            SELECT txn_date, amount, cat_name, description, person_name, ledger.id
            FROM ledger
            JOIN persons
                ON ledger.person_id=persons.id
            JOIN categories
                ON ledger.category_id=categories.id
            """
cur.execute(query)
results = cur.fetchall()
for row in results:
row = list(row)
out.sort(key=lambda row: row[0])
row[1] = float(row[1]) / 100
out_dicts = []
row = [(row[i].capitalize() if type(row[i]) == str and i != 3 else row[i]) for
    i in range(len(row))]
for row in out:
out.append(row)
out_dicts.append({'date': row[0], 'amount': row[1], 'category': row[2],
    'description': row[3], 'person': row[4], 'id': row[5]})
conn.commit()
conn.close()
return out_dicts
