
import random as rd

job = """
    * PARKHAUS SIMULATION
    
    -> Elemente der Anwendung:
    Fahrzeuge  - Auto oder Motorrad
                 Kennzeichen einzigartig
                 Parknummer
    Garage     - Etage
                 Parkslots
                 Fahrzeug
    Simulation - Fahrzeuge parken ein/aus
                 Einparken - ungeparkte Fahrzeugen fahren ins Parkhaus
                 Ausparken - geparkten Fahrzeuge verlassen das Parkhaus
    
    -> Anleitung:
    Beantworten Sie zunächst zwei Fragen. Wieviele Etagen soll das neue
    Parkhaus haben und wieviele Parkplätze stehen pro Etage zur Verfü-
    gung? Es wird ein Parkhaus mit identischen Etagen erstellt.
"""

menu = """
    
    A = zeige Parkplätze
    B = zeige KFZ-Liste
    C = zeige Anzahl freier Stellplätze
    D = zeige Anzahl KFZ auf der Strasse
    I = einparken eines KFZ
    O = ausparken eines KFZ
    S = suche KFZ nach KZ
    Q = Programmende

"""

def setPH(phEtg , phPl): # Setup Parkhaus
    parkhaus = []
    for i in range(phEtg):
        for y in range(1,phPl+1):
            parkhaus.append({"Etage": i ,"Platz": y ,"Aktuell":"frei"})
    return parkhaus

def setKFZ (phPlAll): # Setup Fahrzeuge
    kfzlst = []
    for i in range(phPlAll+1):
        t = rd.randint(0,1)
        if t == 0:
            tset = "Auto"
        else:
            tset = "Krad"            
        kfzlst.append({"ID": i,"Typ": tset ,"kz": ("K-BBQ " + str(i)),"Zustand":"fährt"})
    return kfzlst

def showPH(parkhaus): # Zeige Parkhaus
    for platz in parkhaus:
        print(platz)

def showKFZ(kfzlst): # Zeige Fahrzeuge
    for kfz in kfzlst:     
        print(kfz)    

def checkPH(parkhaus): # Zeige freie Parkplätze
    count = 0
    for slot in parkhaus:
        if slot["Aktuell"] == "frei":
            count += 1
    print("Anzahl freier Parkplätze: ", count)

def checkKFZ(kfzlst): # Fahrzeuge auf der Strasse
    count = 0
    for kfz in kfzlst:
        if kfz["Zustand"] == "fährt":
            count += 1
    print("Anzahl KFZ auf der Straße: ", count)

def zustandKFZ(kfzlst,kennz): # Zustand KFZ nach Kennzeichen
    found = 0
    for kfz in kfzlst:
        if kfz["kz"] == kennz:
            print("Das KFZ ", kfz["Zustand"])
            found = 1        
    if found == 0:
        print("Kennzeichen nicht gefunden!")

def einparken(lstall , kennz):
    print(kennz)

def ausparken(lstall , kennz):
    print(kennz)

def main():
    # Setup
    print(job)
    
    phEtg = int(input("Anzahl Etagen?: "))
    phPl = int(input("Anzahl Parkplätze?: "))
    phPlAll = phEtg * phPl
    parkhaus = setPH(phEtg , phPl)
    kfzlst = setKFZ(phPlAll)
    lstall = []
    kl = 0
    ph = 1
    
    # Mainloop    
    run = True
    while run:
        print(menu)
        ok = input("Auswahl? ").upper()
        if ok == "Q":
            run = False
        elif ok == "A":
            showPH(parkhaus)
        elif ok == "B":
            showKFZ(kfzlst)
        elif ok == "C":
            checkPH(parkhaus)
        elif ok == "D":
            checkKFZ(kfzlst)
        elif ok == "I":
            kennz = input("Bitte geben Sie ein Kennzeichen ein: ")
            lstall.insert(kl, kfzlst)
            lstall.insert(ph, parkhaus)
            einparken(lstall,kennz)
        elif ok == "O":
            kennz = input("Bitte geben Sie ein Kennzeichen ein: ")
            lstall.insert(kl, kfzlst)
            lstall.insert(ph, parkhaus)
            ausparken(lstall,kennz)
        elif ok == "S":
            kennz = input("Bitte geben Sie ein Kennzeichen ein: ")
            zustandKFZ(kfzlst , kennz) 
        else:
            print("Eingabe ohne Funktion!")
        
if __name__ == "__main__":
    main()
