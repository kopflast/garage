
import random as rd

"""
    Fahrzeuge - Auto oder Motorrad
                Kennzeichen einzigartig
                Parknummer
    Garage    - Etage
                Parkslots
                Fahrzeug

    Simulation - Fahrzeuge parken ein/aus
                 Einparken - zufälligen Anzahl aus ungeparkten Fahrzeugen
                 Ausparken - zufällige Anzahl aus geparkten
                 
                
"""

class fahrzeug:
    def __init__(self, id, t, kz, s ):
        self.id = id
        self.typ = t
        self.kz = kz
        self.status = s 
  
class slot:
    def __init__(self,etage,stellplatz,status):
        self.stage = etage
        self.slot = stellplatz
        self.status = status



def main():
    
    print("Parkhaussimulation Venece")
    etagen = int(input("Wieviele Etagen soll das PH haben? "))
    stellplaetze = int(input("Wieviele Stellplaetze soll es pro Etage geben? "))
    slots = etagen * stellplaetze
    print("Ihr Parkhaus wird auf " + str(etagen) + " Etagen insgesammt " + str(slots) + " Stellplaetze anbieten.")
    print("Ihr Parkhaus wird erstellt")
    
    parkhaus = [slot]
    x = 0
    for i in range(etagen):
        for y in range(stellplaetze):
            parkhaus.insert(x,slot(i,y+1,"frei"))
            x += 1
            
    print("Anzahl Parkplätze",len(parkhaus)-1 , " geplant ", slots)
    
    
    for i in range(len(parkhaus)-1):
        print("Etage: ",parkhaus[i].stage," Platz: ",parkhaus[i].slot," Aktuell: ",parkhaus[i].status)
        
    
    fListe = [fahrzeug]
    x = slots + 1
    for i in range(x):
        t = rd.randint(0,1)
        kz = ("K-BBQ " + str(i))
        fListe.insert(i,fahrzeug(i,t, kz, False))
        
    print("Fahrzeugliste erstellt")    
    print(len(fListe))
    for i in range(x):
        if fListe[x].typ == 0:
            art = "Auto"
        else:
            art = "Krad"
        print(art," ",fListe[x].id," ",fListe[x].kz," ",fListe[x].status)
        
if __name__ == "__main__":
    main()


