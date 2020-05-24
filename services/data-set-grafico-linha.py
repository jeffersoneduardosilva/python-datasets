import matplotlib.pyplot as plt
import requests
import json

r = requests.get('http://www.mocky.io/v2/5ec864622f00001219db6fac')
response = r.text
data = json.loads(response)
music_list = data['musicas']

musicas = []
acessos = []
for m in music_list:
    musicas.append(m['mes'])
    acessos.append(m['acessos'])

plt.plot(musicas, acessos, color='green')
plt.scatter(musicas, acessos, color='red')
plt.show()

