import aiosqlite


class Database:
    def __init__(self, db='users.db'):
        self.db = db


    async def create_table(self):
        async with aiosqlite.connect(self.db) as database:
            await database.execute('''
                CREATE TABLE IF NOT EXISTS user (
                    tg_id INTEGER PRIMARY KEY,
                    username TEXT  NOT NULL,
                    city TEXT,
                    coins TEXT,
                    chipr_key TEXT,
                    token TEXT,
                    status TEXT
                )
            ''')
            await database.commit()


    async def add_data(self, tg_id, username, chipr_key, token, status='default'):
        async with aiosqlite.connect(self.db) as  database:
            async with database.execute("SELECT * FROM user WHERE tg_id =?", (tg_id,)) as cursor:
                result = await cursor.fetchone()
                if not result:
                    await database.execute("INSERT INTO user (tg_id, username, chipr_key, token, status) VALUES (?, ?, ?, ?, ?)", (tg_id, username, chipr_key, token, status))
                    await database.commit()

    async def get_data(self, tg_id) -> dict:
        async with aiosqlite.connect(self.db) as  database:
            async with database.execute("SELECT * FROM user WHERE tg_id =?", (tg_id,)) as cursor:
                results = await cursor.fetchall()
                for result in results:
                    return {
                        'city': result[2],
                        'coins': result[3],
                        'chipr_key': result[4],
                        'token': result[5],
                        'status': result[6]
                    }
    async def add_keys(self, tg_id, chiprkey, token):
        async with aiosqlite.connect(self.db) as  database:
            await database.execute("UPDATE user SET chipr_key =?, token =? WHERE tg_id =?", (chiprkey, token, tg_id))
            await database.commit()


    async def update_user(self, tg_id, city=None, coins=None):
        async with aiosqlite.connect(self.db) as  database:
            query = "UPDATE user SET "
            params = []
            update = []

            if city is not None:
                update.append("city =?")
                params.append(city)

            if coins is not None:
                update.append("coins =?")
                params.append(coins)


            update.append("status =?")
            params.append("custom")

            if not update:
                return
            
            query += ", ".join(update) + " WHERE tg_id = ?"
            params.append(tg_id)


            await database.execute(query, tuple(params))
            await database.commit()

    async def check_status(self, tg_id):
        async with aiosqlite.connect(self.db) as  database:
            async with database.execute("SELECT status FROM user WHERE tg_id =?", (tg_id,)) as cursor:
                result = await cursor.fetchone()
                return result[0]
            

    async def check_user_token(self, user_token) -> bool:
        async with aiosqlite.connect(self.db) as database:
            async with database.execute("SELECT chipr_key FROM user WHERE token=?", (user_token,)) as cursor:
                key = await cursor.fetchone()
                if key:
                    return True
                return False
    
    async def get_key(self, token):
        async with aiosqlite.connect(self.db) as database:
            async with database.execute("SELECT chipr_key FROM user WHERE token=?", (token,)) as cursor:
                keys = await cursor.fetchall()
                for key in keys:
                    return key[0]
                    
    

