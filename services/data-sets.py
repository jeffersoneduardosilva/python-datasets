import matplotlib.pyplot as plt
import numpy as np
import requests
import json

plt.rcdefaults()

r = requests.get('http://www.mocky.io/v2/5ec830b52f00008a00db6ef1')
response = r.text
data = json.loads(response)
music_list = data['musicas']

musicas = []
acessos = []
for m in music_list:
    musicas.append(m['nome'])
    acessos.append(m['acessos'])
indice = np.arange(len(musicas))

# plt.bar(indice, acessos)
# plt.xticks(indice, musicas)
# plt.ylabel('Acessos')
# plt.title('Ranking Musicas Metallica Abril - 2020')
# plt.show()


cores = ['lightblue', 'green', 'white', 'red', 'pink']
explode = (0.1, 0, 0, 0, 0)
total = sum(acessos)
plt.pie(acessos, explode=explode, labels=musicas, colors=cores, autopct=lambda p: '{:.0f}'.format(p * total / 100), shadow=True, startangle=90)

plt.axis('equal')
plt.show()

