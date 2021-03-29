"""
In order to get a superuser, once created the database
you need to grant superuser permission to your admin running this script.

HOW TO:
------
When:
Every time you delete the DB.

1/ Run the app
2/ Create a user with 'admin@nbcv.com' as email
    ---> (or change lines 20/21 on this script).
3/ Stop the app and run this script.
"""
import sqlite3

con = sqlite3.connect('nbcv.db')

with con:
    c = con.cursor()
    c.execute("UPDATE user SET is_superuser = 1 WHERE id == (SELECT id FROM USER WHERE email == 'admin@nbcv.com')")
    data= c.execute("SELECT is_superuser, is_active FROM USER WHERE id == (SELECT id FROM USER WHERE email == 'admin@nbcv.com')")
    print(data.fetchall())