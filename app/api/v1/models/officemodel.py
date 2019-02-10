OFFICES = []


class OfficeModel():
    '''Base class for all methods of offices'''

    def __init__(self, name, office_type):
        '''Defining the constructor method of the class
        and self is the instance of the object'''
        self.name = name
        self.office_type = office_type

    def create(self):
        '''Defining the method create that uses
        attributes of the class OfficeModel'''
        office = {
            "office_id": len(OFFICES)+1,
            "name": self.name,
            "office_type": self.office_type
        }
        return OFFICES.append(office)

    @staticmethod
    def get_all():
        '''Method to get all offices static
        because doesnt use attributes of this class'''
        return OFFICES

    @staticmethod
    def get_by_id(office_id):
        '''Defining method to get
        office by id, and passing parameters to it.'''

        return [office for office in OFFICES if office
                ["office_id"] == office_id]
