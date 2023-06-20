import json
import jsonpath


class JsonUtil:

    @staticmethod
    def mysqlJson(param):
        return json.loads(json.dumps(param))

    pass
