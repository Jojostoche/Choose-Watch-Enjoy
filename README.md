### Test SQL queries
```
source .env/bin/activate

# optional
# edit conf/schema.sql and run
python app/init_db.py

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
