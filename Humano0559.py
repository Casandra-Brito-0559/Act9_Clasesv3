print("Actividad 9 clase humano")
print("Casandra Brito Mat: 22308051280559")

# zona de class

class Humano0559:
    #zona de atributos dentro de la clase
    edad=0
    genero=" "
    colordepelo=" "
    peso=0
    estatura=0
    
    #zona de funciones dentro de la clase
    def correr0559(selft,n):
        print(f"{n} esta corriendo ")
        
    def caminar0559(selft,n):
        print (f"{n} esta caminando")
        
    def hablar0559(selft,n):
        print(f"{n} esta hablando")
    
# zona de creacion de objetos
Cass=Humano0559()
Angela=Humano0559()

#zona de uso de objetos
print("--Resultados para Cass--")

Cass.edad=17
Cass.genero="Femenino"
Cass.peso=51
Cass.colordepelo="Negro"
Cass.estatura=1.61
print(f"Edad: {Cass.edad}")
print(f"Genero: {Cass.genero}")
print(f"Peso: {Cass.peso} kg")
print(f"Color de pelo: {Cass.colordepelo}")
print(f"Estatura: {Cass.estatura}")
Cass.correr0559("Cass")
Cass.caminar0559("Cass")
Cass.hablar0559("Cass")

print("--Resultados para Angela--")

Angela.edad=20
Angela.genero="Femenino"
Angela.peso=58
Angela.colordepelo="Cafe"
Angela.estatura=1.68
print(f"Edad: {Angela.edad}")
print(f"Genero: {Angela.genero}")
print(f"Peso: {Angela.peso} kg")
print(f"Color de pelo: {Angela.colordepelo}")
print(f"Estatura: {Angela.estatura}")
Angela.correr0559("Angela")
Angela.caminar0559("Angela")
Angela.hablar0559("Angela")
