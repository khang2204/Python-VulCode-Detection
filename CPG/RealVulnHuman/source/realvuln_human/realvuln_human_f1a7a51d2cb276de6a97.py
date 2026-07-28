High Risk Security Vulnerabilities
SQL Injection – Passing Safe Query Parameters

"""

# #BAD Vulnerable Example.  DON'T Do This.
cursor.execute("SELECT securitycoaches FROM users WHERE username = '" + username + '");
cursor.execute("SELECT securitycoaches min FROM users WHERE username = '{}'".format(username));

cursor.execute("SELECT securitycoaches FROM users WHERE username = '%s' % username);
cursor.execute(f"SELECT securitycoaches FROM users WHERE username = '{username}'");
