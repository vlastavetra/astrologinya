class MongoDb:
    """
    """

    def __init__(self, client) -> None:
        self.client = client
        self.natal = self.client["natal"]

    async def get_natal_card(self) -> list:
        cursor = self.natal["moon"].find({})
        documents = [{key: value for key, value in doc.items() if key != "_id"} async for doc in cursor]
        return documents