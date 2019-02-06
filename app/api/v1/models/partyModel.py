parties = []


class partyModel():
    def __init__(self, name, hqAddress, logoUrl):
        self.party_id = len(parties)
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

        return [party for party in parties if party["party_id"] == party_id]

    @staticmethod
    def delete_party(party_id):
        deleted = False
        for party in parties:
            if party['party_id'] == party_id:
                parties.remove(party)
                deleted = True
        return deleted
