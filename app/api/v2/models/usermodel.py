from app.api.v2.models.dbconfig import Database


class UserModel(Database):

    def __init__(self, firstname=None, lastname=None, othername=None,
                 email=None, password=None):

        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.othername = othername
        self.email = email
        self.password = password

    def register_user(self, firstname, lastname, othername, email, password):
        self.curr.execute(
            '''
        INSERT INTO users(firstname, lastname, othername, email, password)
        VALUES ('{}','{}','{}','{}','{}') RETURNING firstname,
        lastname, othername, email, password'''
            .format(firstname, lastname, othername, email, password))
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
        return dict(
            email=self.email,
            firstname=self.firstname,
            lastname=self.lastname,
            othername=self.othername,
            password=self.password
        )
