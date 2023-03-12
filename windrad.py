import numpy as np
import os
import glob
import numpy as np
from pyautogui import typewrite
from dataclasses import dataclass


@dataclass
class Bauwerk:
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0
    btype: str = 'h'

    def __str__(self):
        if self.btype == 'h':
            out = f'Haus\n {self.x= }\n '\
                    f'{self.y= }'
        elif self.btype == 'w':
            out = f'Windrad\n {self.x= }\n '\
                    f'{self.y= }\n {self.z= }'
        else:
            out = "?"
        out = out.replace("self.", "")
        return out


def main():
    gl_filename = set_filename()
    bauwerke = read_file(gl_filename)
    bauwerke = berechne_Abstand(bauwerke)
    # print(type(bauwerke))
    # print_Bauwerke(bauwerke)


def set_filename() -> str:
    cwd = os.getcwd()
    try:
        cwd = cwd + "/data"
        os.chdir(cwd)
        results = glob.glob("*.txt")
        for result in results:
            print(result)
        print("Bitte den Dateinamen eingeben: ")
        typewrite(results[0])
        dateiname = input()

        while dateiname not in results:
            print("Bitte den Dateinamen eingeben: ")
            typewrite(results[0])
            dateiname = input()

    except OSError as err:
        dateiname = ""
    return dateiname


def read_file(filename: str) -> list[Bauwerk]:
    with open(filename, mode="r") as file:
        # Anzahl bestimmt
        tmpStr = file.readline()  # z.B 6  12
        tmpStr = tmpStr.strip()
        tmpList = tmpStr.split()
        anzHS = int(tmpList[0])
        anzWR = int(tmpList[1])
        bauwerke = []

        for i in range(0, anzHS):
            tmpStr = file.readline()  # z.B 6  12
            tmpStr = tmpStr.strip()
            tmpList = tmpStr.split()
            # haus
            btype = 'h'
            Hx = int(tmpList[0])
            Hy = int(tmpList[1])
            Hz = 0
            h = Bauwerk(x=Hx, y=Hy, z=Hz, btype=btype)
            bauwerke.append(h)

        # Windräder einlesen
        for i in range(0, anzWR):
            tmpStr = file.readline()  # z.B 6  12
            tmpStr = tmpStr.strip()
            tmpList = tmpStr.split()
            # Windrad
            btype = 'w'
            Wx = int(tmpList[0])
            Wy = int(tmpList[1])
            Wz = 0
            w = Bauwerk(x=Wx, y=Wy, z=Wz, btype=btype)
            bauwerke.append(w)

        return bauwerke


def print_Bauwerke(bauwerke: list[Bauwerk]):
    haeuser = [x for x in bauwerke if x.btype == 'h']
    windraeder = [x for x in bauwerke if x.btype == 'w']

    print('\033[H\033[3J', end='')

    print("Anzahl Bauwerke", str(len(bauwerke)))
    print("--------------------------")
    print("--------------------------")
    print("Häuser")
    print("----------")
    for h in haeuser:
        print(h)
    print("----------")
    print("----------")

    print("Windraeder")
    print("----------")
    for w in windraeder:
        print(w)


def berechne_Abstand(bauwerke: list[Bauwerk]) -> list[Bauwerk]:
    # berechnet zu jedem Windrad die Abstaende zu allen Häusern
    # der kleinste Abstand wird beim Windrad gespeichert
    haeuser = [x for x in bauwerke if x.btype == 'h']
    windraeder = [x for x in bauwerke if x.btype == 'w']
    abstaende = []

    for w in windraeder:
        abstaende.clear()
        for h in haeuser:
            abstand = abstand_Bauwerke(h, w)
            abstaende.append(abstand)
        abstaende.sort()
        w.z = abstaende[0]
        print(abstaende)
        print(30*"-")
    bauwerke = haeuser + windraeder
    return bauwerke


def abstand_Bauwerke(h: Bauwerk, w: Bauwerk) -> float:
    # berechnet den Abstand zwishen Bauwerk h und Bauwerk w
    abstand = ((h.x - w.x) ** 2 + (h.y - w.y) ** 2)**0.5
    return int(round(abstand, 0))


if __name__ == "__main__":
    main()
