import datetime
import asyncio
from collections import defaultdict
import base64

today = datetime.datetime.utcnow().date()
start_of_today = datetime.datetime.combine(
    today, datetime.datetime.min.time())


class MongoDb:
    """
    """

    def __init__(self, client) -> None:
        self.client = client
        self.indices = self.client["indices"]
        self.configuration = self.client["configuration"]
        self.vendors = self.client["vendors"]
        self.status = self.client["status"]

