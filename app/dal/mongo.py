class MongoDb:
    """
    """

    def __init__(self, client) -> None:
        self.client = client
        self.natal = self.client["natal"]

    async def get_natal_card(self, natal) -> list:
        results = {}
        for key, obj in natal.items():
            collection = self.natal[key]
            document = await collection.find_one({"sign": obj.sign}, {"sign": 1, "text": 1, "_id": 0})
            results[key] = document
        return results