
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
def main():
    print("Parkhaus Simulation")
    phEtg = 3
    phPl = 5
    phPlAll = phEtg * phPl
    
    parkhaus = []    
    for i in range(phEtg):
        for y in range(1,phPl+1):
            parkhaus.append({"Etage": i ,"Platz": y ,"Aktuell":"frei"})
    
    for platz in parkhaus:
        print(platz)
    
  
    kfzlst = []
    for i in range(phPlAll+1):
        t = rd.randint(0,1)
        if t == 0:
            tset = "Auto"
        else:
            tset = "Krad"
            
        kfzlst.append({"ID": i,"Typ": tset ,"kz": ("K-BBQ " + str(i)),"Zustand":"fährt"})
        
    for kfz in kfzlst:     
        print(kfz)
    
        
if __name__ == "__main__":
    main()
