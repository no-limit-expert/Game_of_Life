class Celle:
    def __init__(self):
        self._status = "doed"

    def settDoed(self):
        self._status = "doed"

    def settLevende(self):
        self._status = "levende"

    def erLevende(self):
        if self._status == "levende":
            return True
        else:
            return False

    def hentStatusTegn(self):
        if self.erLevende():
            return "O"
        else:
            return " "
