from app.api.v2.models.dbconfig import Database


class OfficeModel(Database):
    '''Base class for all methods of offices'''

    def __init__(self, name=None, office_type=None):
        super().__init__()
        '''Defining the constructor method of the class
        and self is the instance of the object'''
        self.name = name
        self.office_type = office_type

    def create(self, name, office_type):
        """create office admin only function"""
        self.curr.execute(
            '''
        INSERT INTO office(name, office_type) VALUES
        ('{}','{}') RETURNING name, office_type'''
            .format(name, office_type))
        office = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return office

    @staticmethod
    def get_all_offices():
        """
            method to get all offices from db.
        """
        self.curr.execute(
            """
        SELECT * FROM office
        """)

        offices = self.cursor.fetchall()
        return offices

    # @staticmethod
    # def get_by_id(office_id):
    #     '''Defining method to get
    #     office by id, and passing parameters to it.'''

    #     return [office for office in OFFICES if office
    #             ["office_id"] == office_id]

    def serialize(self):
        return dict(
            id=self.id,
            name=self.name,
            office_type=self.office_type

        )
