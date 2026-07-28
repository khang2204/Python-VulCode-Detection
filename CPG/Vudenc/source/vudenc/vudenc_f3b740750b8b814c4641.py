def init_db(self):...
self.execute("""
            DROP TABLE core;
        """)
self.execute("""
            DROP TABLE users;
        """)
self.execute("""
            DROP TABLE file_system;
        """)
self.execute("""
            DROP TABLE file_storage;
        """)
self.execute(
    """
            CREATE TABLE core (
                index   TEXT,
                data    BYTEA
            );
            CREATE TABLE users (
                handle          TEXT,
                password        TEXT,
                usergroups      TEXT,
                ip_address      TEXT[],
                events          TEXT[],
                usr_name        TEXT,
                usr_description TEXT,
                usr_email       TEXT,
                usr_followers   TEXT[],
                usr_friends     TEXT[]
            );
            CREATE TABLE file_system(
                uuid        TEXT,
                file_name   TEXT,
                owner       TEXT,
                upload_time DOUBLE PRECISION,
                sub_folders TEXT[],
                sub_files   TEXT[][]
            );
            CREATE TABLE file_storage (
                uuid    TEXT,
                size    BIGINT,
                count   BIGINT,
                hash    TEXT,
                content BYTEA
            );
        """
    )
return
