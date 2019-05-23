import sqlite3

DATABASE = 'database.db'
SCHEMA = './conf/schema.sql'

class db_handler:
    """
        Handle connection and queries to SQLite
    """
    
    def __init__(self):
        """
            Constructor
        """
        try:
            # connect to the DB
            self.conn = sqlite3.connect(DATABASE)
            self.conn.row_factory = sqlite3.Row
        except (Exception) as error:
            print(error)

    def query(self, query, args=(), one=False):
        """
            Query the DB
        """
        cur = self.conn.execute(query, args)
	rd = None
        if one:
	    row = cur.fetchone()
	    if row:
	    	rd = dict(zip(zip(*cur.description)[0], row)) 
        else:
	    rows = cur.fetchall()
	    if rows:
	    	rd = [dict(zip(zip(*cur.description)[0], row)) for row in rows]
	return rd if rd else None
    
    def edit(self, query, args=()):
        """
            Insert in the DB
        """
        self.conn.execute(query, args)
        self.conn.commit()

    def init(self):
        """
            Init DB schema
        """
        with open(SCHEMA, 'r') as f:
            self.conn.cursor().executescript(f.read())
        self.conn.commit()

    def close(self):
        """
            Close DB connection
        """
        if self.conn is not None:
            self.conn.close()
    
    def get_user_password(self, username):
	"""
	    Get user password
	"""
        rd = self.query('SELECT passwd_hash FROM user WHERE username=?', (username,), one=True)
        return rd['passwd_hash'] if rd else None

    def add_user(self, username, passwd_hash, firstname, lastname, email, role):
        """
            Add a new user
        """
        self.edit('INSERT INTO user (username, passwd_hash, first_name, last_name, email, role_id) VALUES (?,?,?,?,?,?)', (username, passwd_hash, firstname, lastname, email, role,))

    def add_film(self, original_title, original_language, duration, date, grade, age, studio_id, actor_id):
        """
            Add a new film
        """
        self.edit('INSERT INTO film (original_title, original_language, duration, date, grade, age) VALUES (?,?,?,?,?,?)', (original_title, original_language, duration, date, grade, age,))
        film = self.query("SELECT last_insert_rowid() AS id", one=True)
	film_id = film['id']
	print("Film ID: ", film_id)
        self.edit('INSERT INTO film_studio (film_id, studio_id) VALUES (?,?)', (film_id, studio_id,))
        self.edit('INSERT INTO film_actor (film_id, actor_id) VALUES (?,?)', (film_id, actor_id,))
 
    def add_actor(self, name):
        """
            Add a new actor
        """
        self.edit('INSERT INTO actor (name) VALUES (?)', (name,))
	
	
    def add_studio(self, name, zip_code, country, website):
        """
            Add a new studio
        """
        self.edit('INSERT INTO studio (name, zip_code, country, website) VALUES (?,?,?,?)', (name, zip_code, country, website,))
