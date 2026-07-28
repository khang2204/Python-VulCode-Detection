def create_basic_user(self, userID, fName, lName, email, password):...
password2 = generate_password_hash(password)
query = (
    "INSERT INTO `testdb`.`user` (`ID`, `FName`, `LName`, `Email`, `Pass`, `Role`) VALUES ('"
     + userID + "', '" + fName + "', '" + lName + "', '" + email + "', '" +
    password2 + "', '0')")
self.cursor.execute(query)
self.connection.commit()
