import json
from functools import wraps


def json_io(f):
    @wraps(f)
    def io(self, url, payload=None):
        if payload is not None and isinstance(payload, str):
            payload = json.loads(payload)
        return json.dumps(f(self, url, payload))
    return io


class RestAPI:
    def __init__(self, database=None):
        if database is None:
            database = {"users": []}
        self.database = database

    @json_io
    def get(self, url, payload=None):
        if payload is not None:
            answer = []
            for i in payload["users"]:
                answer.append(self.database["users"][self.__find_user(i)])
            return {"users": sorted(answer, key=lambda x: x["name"])}
        else:
            return self.database

    @json_io
    def post(self, url, payload=None):
        if url == '/add':
            return self.__add(url, payload)
        elif url == '/iou':
            return self.__iou(url, payload)

    def __find_user(self, name):
        for i, index in zip(self.database["users"], range(len(self.database["users"]))):
            if i["name"] == name:
                return index
        return None

    def __add(self, url, payload=None):
        if payload is not None:
            self.database["users"].append({"name": payload["user"], "owes": {}, "owed_by": {}, "balance": 0.0})
            return self.database["users"][-1]
        return {}

    def __syncing(self, item):
        for i in item["owes"].copy():
            if i in item["owed_by"]:
                if item["owed_by"][i] == item["owes"][i]:
                    del item["owed_by"][i]
                    del item["owes"][i]
                elif item["owed_by"][i] > item["owes"][i]:
                    item["owed_by"][i] = item["owed_by"][i] - item["owes"][i]
                    del item["owes"][i]
                else:
                    item["owes"][i] = item["owes"][i] - item["owed_by"][i]
                    del item["owed_by"][i]
        return item

    def __iou(self, url, payload=None):
        if payload is not None:
            lender_index = self.__find_user(payload["lender"])
            borrower_index = self.__find_user(payload["borrower"])
            lender = self.database["users"][lender_index]
            borrower = self.database["users"][borrower_index]
            lender["balance"] += payload["amount"]
            borrower["balance"] -= payload["amount"]

            if borrower["name"] in lender["owed_by"]:
                lender["owed_by"] += payload["amount"]
            else:
                lender["owed_by"][borrower["name"]] = payload["amount"]

            if lender["name"] in borrower["owes"]:
                borrower["owes"] += payload["amount"]
            else:
                borrower["owes"][lender["name"]] = payload["amount"]

            lender = self.__syncing(lender)
            borrower = self.__syncing(borrower)
            self.database["users"][lender_index] = lender
            self.database["users"][borrower_index] = borrower
            return {"users": sorted([lender, borrower], key=lambda x: x["name"])}
        return {}
