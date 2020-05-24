import matplotlib.pyplot as plt
import numpy as np
import requests
import json

plt.rcdefaults()

r = requests.get('http://www.mocky.io/v2/5ec864622f00001219db6fac')
response = r.text
data = json.loads(response)
music_list = data['musicas']

musicas = []
acessos = []
for m in music_list:
    musicas.append(m['nome'])
    acessos.append(m['acessos'])
indice = np.arange(len(musicas))

plt.bar(indice, acessos)
plt.xticks(indice, musicas)
plt.ylabel('Acessos')
plt.title('Ranking Musicas Rock - 2020')
plt.show()

