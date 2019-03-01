"""importing modules to be used in usermodel"""
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash
from app.api.v2.models.dbconfig import Database


class UserModel(Database):
    """Base class for all methods in usermodel"""

    def __init__(self, firstname=None, lastname=None, othername=None,
                 email=None, phonenumber=None,
                 password="", passporturl=None, isAdmin=False):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phonenumber = phonenumber
        self.password = generate_password_hash(password)
        self.passporturl = passporturl
        self.isAdmin = isAdmin

    def register_user(self):
        """method to register new user to the table user"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        new_user = '''INSERT INTO users(firstname, lastname, othername, email,\
            phonenumber,password, passporturl, isAdmin)\
                VALUES ('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING firstname,
        lastname, othername, email, phonenumber, password, passporturl, isAdmin'''.format(self.firstname, self.lastname, self.othername, self.email, self.phonenumber, self.password, self.passporturl, self.isAdmin)
        return Database().query_data(new_user)

    def get_user_by_email(self, email):
        """Get user by their email"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        get_email = '''SELECT * FROM users WHERE users.email = '{}';'''.format(
            email)
        return Database().query_data(get_email)

    def get_phoneNumber(self, phoneNumber):
        """Get user with specific phonenumber."""
        get_number = ''' SELECT * FROM users WHERE phoneNumber= '{}'''.format(
            phoneNumber)
        return Database().query_data(get_number)

    def get_user_by_id(self, user_id):
        """Get user by their id"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        single_user = '''SELECT * FROM users WHERE users.user_id = '{}';'''.format(user_id)
        return Database().query_data(single_user)
