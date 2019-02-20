from app.api.v2.models.dbconfig import Database
from psycopg2.extras import RealDictCursor
from werkzeug.security import generate_password_hash


class UserModel(Database):

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
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute(
            '''
        INSERT INTO users(firstname, lastname, othername, email, phonenumber,
        password, passporturl, isAdmin)
        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}') RETURNING firstname,
        lastname, othername, email, phonenumber, password, passporturl, isAdmin'''
            .format(self.firstname, self.lastname, self.othername, self.email, self.phonenumber, self.password, self.passporturl, self.isAdmin))
        user = self.curr.fetchone()
        self.save()
        return user

    def get_user_by_email(self, email):
        """Get user by their email"""
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)
        self.curr.execute('''
            SELECT * FROM users WHERE users.email = '{}';
            '''.format(email))
        user_email = self.curr.fetchone()
        print(user_email)
        self.save()
        return user_email

    def get_phoneNumber(self, phoneNumber):
        """Get user with specific phonenumber."""

        self.curr.execute(
            ''' SELECT * FROM users WHERE\
                phoneNumber= '{}'''.format(phoneNumber))
        user_number = self.curr.fetchone()
        self.save()
        return user_user

    def serialize(self):
        '''convert user data to dictionary'''
        return dict(
            email=self.email,
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            phonenumber=self.phonenumber,
            password=self.password,
            passporturl=self.passporturl,
            isAdmin=self.isAdmin
        )
