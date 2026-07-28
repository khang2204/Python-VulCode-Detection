def ratingChange(Name, ELO, Played, W, L):...
db.execute(
    "UPDATE players SET ELO = %i, Played = %i, W = %i, L = %i WHERE Name = '%s' COLLATE NOCASE"
     % (ELO, Played, W, L, Name))
database.commit()
