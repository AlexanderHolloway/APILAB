import sqlalchemy
from PGPass import pgpassword

engine = sqlalchemy.create_engine(f"postgresql://postgres:{pgpassword}@localhost:5432/BigMouth")

class Database():
    def __init__(self):
        self.con = engine.connect()

    def create_song_table(self):
        sql = """
        CREATE TABLE IF NOT EXISTS SONGS (
        SONG_NAME TEXT PRIMARY KEY,
        ARTIST TEXT NOT NULL,
        ALBUM_TYPE TEXT,
        ALBUM_NAME TEXT,
        ALBUM_YEAR INTEGER,
        LYRICS TEXT
        )
        """
        self.con.execute(sql)

    def delete_song_table(self):
        sql = '''
        drop table songs'''
        self.con.execute(sql)

    # def delete_songs(self, song_name):
    #     sql = "delete from SONGS where SONG_NAME = ?"
    #     cur = self.con.cursor()
    #     cur.execute(sql, song_name)

    def delete_songs(self, song_name):
        sql = f"delete from SONGS where SONG_NAME = {song_name}"
        self.con.execute(sql)

    # def insert(self, row):
    #     try:
    #         c = self.con.cursor()
    #         sql = ''' INSERT INTO SONGS (SONG_NAME, ARTIST, ALBUM_TYPE, ALBUM_NAME, ALBUM_YEAR,
    #                 LYRICS) VALUES (?, ?, ?, ?, ?, ?);
    #             '''
    #         c.execute(sql, row)
    #         self.con.commit()
    #     except Exception as error:
    #         print('ERROR: ID already exists in PRIMARY KEY column {}'.format(row), error)

    def insert(self, row):
        values = tuple(row)
        sql = f'''INSERT INTO SONGS (SONG_NAME, ARTIST, ALBUM_TYPE, ALBUM_NAME, ALBUM_YEAR,LYRICS)
                 VALUES {values};'''
        try:
            self.con.execute(sql)
        except Exception as error:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(row), error)

