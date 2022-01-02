from random import randint
from celle import Celle


class Spillebrett:
    def __init__(self, rader, kolonner):
        self._rader = rader
        self._kolonner = kolonner
        self._rutenett = self._lagTomtRutenett()
        self._leggCellerIRutenett()
        self._generer()
        self._generasjonsnummer = 0

    def _lagTomRad(self):
        liste = []
        x = 0
        while x < self._kolonner:
            liste.append(None)
            x += 1
        return liste

    def _lagTomtRutenett(self):
        rutenett = []
        x = 0
        while x < self._rader:
            rutenett.append(self._lagTomRad())
            x += 1
        return rutenett

    def _leggCellerIRutenett(self):
        rutenett = self._rutenett
        rutenettMCeller = []
        for rad in rutenett:
            conv = lambda i: Celle()
            res = [conv(i) for i in rad]
            rutenettMCeller.append(res)
        self._rutenett = rutenettMCeller

    def _generer(self):
        for rad in self._rutenett:
            for kolonne in rad:
                if randint(1, 3) == 3:
                    kolonne.settLevende()

    def tegnBrett(self):
        x = 0
        while x < 15:
            print()
            x += 1

        brettMTegn = []
        for rad in self._rutenett:
            radMTegn = []
            for celle in rad:
                radMTegn.append(celle.hentStatusTegn())
            brettMTegn.append(radMTegn)
        for rad in brettMTegn:
            print(" ".join(rad))

    def hentCelle(self, rad, kolonne):
        nrad = rad + 1
        nkolonne = kolonne + 1
        if 0 < nrad <= self._rader:
            if 0 < nkolonne <= self._kolonner:
                return self._rutenett[rad][kolonne]
        else:
            return None

    def oppdatering(self):
        skalleve = []
        skaldoe = []

        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                celle = self.hentCelle(rad, kolonne)
                naboer = self.finnNabo(rad, kolonne)
                levendenaboer = 0
                for nabo in naboer:
                    if nabo.erLevende():
                        levendenaboer += 1
                if celle.erLevende():
                    if levendenaboer > 3 or levendenaboer < 2:
                        skaldoe.append(celle)
                else:
                    if levendenaboer == 3:
                        skalleve.append(celle)
        self._generasjonsnummer += 1

        for d in skaldoe:
            d.settDoed()
        for c in skalleve:
            c.settLevende()

    def antallLevende(self):
        levende = 0
        for rad in range(self._rader):
            for kolonne in range(self._kolonner):
                if self.hentCelle(rad, kolonne).erLevende():
                    levende += 1
        return levende

    def finnNabo(self, rad, kolonne):
        naboer = []
        for rader in range(rad - 1, rad + 2):
            for kolonner in range(kolonne - 1, kolonne + 2):
                nabo = self.hentCelle(rader, kolonner)
                if nabo is not None and nabo is not self.hentCelle(rad, kolonne):
                    naboer.append(self._rutenett[rader][kolonner])
        return naboer

    def generasjonsTall(self):
        return self._generasjonsnummer

