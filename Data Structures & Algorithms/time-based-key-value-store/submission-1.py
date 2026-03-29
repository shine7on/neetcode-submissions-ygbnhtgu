class TimeMap:

    def __init__(self):
        self.timemap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [[timestamp, value]]
        else:
            self.timemap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ''
        else:
            values = list(self.timemap[key])
            values.sort()
            print(values)
            temp = ''
            for value in values:
                print(value[0])
                if value[0] < timestamp:
                    temp = value[1]
                elif value[0] == timestamp:
                    return value[1]
                else:
                    return temp
            return temp