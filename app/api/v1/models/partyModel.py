parties = []


class partyModel():
    def __init__(self, party_id, name, hqAddress, logoUrl):
        self.party_id = party_id
        self.name = name
        self.hqAddress = hqAddress
        self.logoUrl = logoUrl

    def create(self):
        party = {
            "party_id": self.party_id,
            "name": self.name,
            "hqAddress": self.hqAddress,
            "logoUrl": self.logoUrl
        }
        return parties.append(party)

    @staticmethod
    def get_all():
        return parties

    @staticmethod
    def get_specific_party(party_id):

        return [party for party in parties if["party_id"] == party_id]
