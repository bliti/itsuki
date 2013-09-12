#sql statements for DB as constants.
#Development only. To reduce complexitiy of main.py

#admin

##create user
CREATE_USER = ("INSERT INTO users"
              "(name, phone, email, organization, status, role) "
              "VALUES(?,?,?,?,?,?)")
              

SELECT_ALL_USERS = ("SELECT  id, name, phone, email, organization, status, role "
                    "FROM users")