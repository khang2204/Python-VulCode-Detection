def update_sql(self, column, location_nw, title):...
sql_update = (
    f"UPDATE `artikelen` SET `{column}` = '{location_nw}' WHERE `title` = '{title}'"
    )
print(sql_update)
cursor.execute(sql_update)
return
