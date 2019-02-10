PARTIES = []


class PartyModel():
    '''This is the base class of all methods of parties'''

    def __init__(self, name, hqaddress, logourl):
        '''Instatiating the class and defining the object of the class'''
        self.name = name
        self.hqaddress = hqaddress
        self.logourl = logourl

    def create(self):
        party = {
            "party_id": len(PARTIES)+1,
            "name": self.name,
            "hqaddress": self.hqaddress,
            "logourl": self.logourl
        }
        return PARTIES.append(party)

    @staticmethod
    def get_all():
        '''Method to get all parties static
        because it doesnt use attributes of the class'''
        return PARTIES

    @staticmethod
    def get_specific_party(party_id):
        '''Method to specific party static
        because it doesnt use attributes of the class'''
        return [party for party in PARTIES if party["party_id"] == party_id]

    @staticmethod
    def delete_party(party_id):
        '''Method of deleting party by id'''
        deleted = False
        for party in PARTIES:
            if party['party_id'] == party_id:
                PARTIES.remove(party)
                deleted = True
        return deleted

    @staticmethod
    def edit_party(party_id, name):
        '''Method of editing party static since doesnt
         use the attributes of the class therefore pass parameters'''
        updated = False
        for party in PARTIES:
            if(party["party_id"] == party_id):
                party["name"] = name
                updated = True
        return updated
