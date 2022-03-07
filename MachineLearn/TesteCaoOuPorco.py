#features ( 0 Sim, 1 Não)
#Pelo longo ?
#Perna curta?
#Late?

porco1 = [1,0,1]
porco2 = [1,0,0]
porco3 = [0,0,1]

cachorro1 = [1,0,0]
cachorro2 = [0,1,0]
cachorro3 = [0,0,0]

# 1=> porco, 0=> cachorro
dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
classes = [1,1,1,0,0,0]

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(dados, classes)

animal_mistorioso = [1,0,1]
model.predict([animal_mistorioso])

mist1=[0,0,0]
mist2=[0,1,1]
mist3=[1,1,0]

testes = [mist1,mist2,mist3]
previsoes = model.predict(testes)

testes_classes = [0,1,1]
previsoes == testes_classes
print(previsoes)



from sklearn.metrics import accuracy_score
taxa_de_acerto = accuracy_score(testes_classes,previsoes)
print("taxa de acerto: ",taxa_de_acerto*100, "%")