### Test SQL queries
```
source .env/bin/activate
```
# optional
# edit conf/schema.sql and run

```
python app/init_db.py
```
# delete db

```
rm database.db

python
import app.db as db
db = db.db_handler()
db.query('select * from user')

```

### Generate password hash
```
source .env/bin/activate
python 
import app.utils as utils
utils.hash_sha1('test')

```
### create routes
@app.routes('/user')
def user():
db = get_db()
users = db.query("SELECT first_name,last_name FROM user")
return render_template('users.html', users=users)

### copy file
cp (file ( /app....)) (file (/app....))


