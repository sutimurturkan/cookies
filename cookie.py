class Cookie:
    def __init__(self) -> None:
        self.freq = {}
        self.cookies = set()

    def read_log(self, filename: str) -> None:
        with open(filename, "r") as log:
            for line in log.readlines()[1:]:
                cookie, timestamp = line.rstrip().split(",")
                date, time = self.reformat(timestamp)
                self.cookies.add(cookie)
                if self.freq.get((cookie, date)):
                    self.freq[(cookie, date)].append(time)
                else:
                    self.freq[(cookie, date)] = [time]

    def reformat(self, timestamp: str) -> str:
        date, time = timestamp.split("T")
        return date, time

    def get_freq(self, date: str) -> list:
        max_freq = 0
        result = []
        for cookie in self.cookies:
            if self.freq.get((cookie, date)):
                times = self.freq.get((cookie, date))
                if max_freq < len(times):
                    max_freq = len(times)
                    result = [cookie]
                elif max_freq == len(times):
                    result.append(cookie)
        return result