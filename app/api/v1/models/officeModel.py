offices = []


class OfficeModel():
    def __init__(self, office_id, name, office_type):
        self.office_id = office_id
        self.name = name
        self.office_type = office_type

    def create(self):
        office = {
            "office_id": self.office_id,
            "name": self.name,
            "office_type": self.office_type
        }
        return offices.append(office)

    @staticmethod
    def get_all():
        return offices

    # @staticmethod
    # def get_by_id(office_id):
    #     return[office for office in offices if office[office_id] == office_id]
    #     # for office in offices:
    #     #     if office['office_id'] == (office_id):
    #     #         return office
    #     # return False
