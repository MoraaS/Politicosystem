from app.api.v2.models.dbconfig import Database


class UserModel(Database):

    def __init__(self, firstname=None, lastname=None, othername=None,
                 email=None, phonenumber=None,
                 password=None, passporturl=None):
        super().__init__()

        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.phonenumber = phonenumber
        self.password = password
        self.passporturl = passporturl

    def register_user(self, firstname, lastname, othername, email, phonenumber,
                      password, passporturl):
        self.curr.execute(
            '''
        INSERT INTO users(firstname, lastname, othername, email, phonenumber,
        password, passporturl)
        VALUES ('{}','{}','{}','{}','{}',md5('{}'),'{}') RETURNING firstname,
        lastname, othername, email, phonenumber, password, passporturl'''
            .format(firstname, lastname, othername, email, phonenumber,
            password, passporturl))
        user = self.curr.fetchone()
        self.save()
        return user

    def get_user_by_email(self, email):
        self.curr.execute('''
            SELECT * FROM users WHERE users.email = '{}';
            '''.format(email))
        getemail = self.curr.fetchone()
        self.save()
        return getemail

    def serialize(self):
        '''convert user data to dictionary'''
        return dict(
            email=self.email,
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            phonenumber=self.phonenumber,
            password=self.password,
            passporturl=self.passporturl
        )
