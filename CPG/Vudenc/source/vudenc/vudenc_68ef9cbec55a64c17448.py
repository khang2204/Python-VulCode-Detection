def create():...
co = connect()
cu = co.cursor()
cu.execute(
    'CREATE TABLE players(id serial NOT NULL,name text NOT NULL, country text NOT NULL, code text, CONSTRAINT players_pkey PRIMARY KEY (id))WITH (OIDS=FALSE);'
    )
cu.execute('ALTER TABLE players OWNER TO postgres;')
cu.execute(
    'CREATE TABLE matches (id serial NOT NULL, p1 text NOT NULL, p2 text NOT NULL, "timestamp" text NOT NULL,CONSTRAINT matches_pkey PRIMARY KEY (id))WITH (OIDS=FALSE);'
    )
cu.execute('ALTER TABLE matches OWNER TO postgres;')
co.commit()
cu.close()
co.close()
return 0
