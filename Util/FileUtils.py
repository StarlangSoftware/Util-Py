class FileUtils(object):

    @staticmethod
    def readHashMap(fileName: str) -> dict:
        result = dict()
        file = open(fileName, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            items = line.strip().split()
            result[items[0]] = items[1]
        return result
