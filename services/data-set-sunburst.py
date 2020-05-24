import plotly.graph_objects as go
import requests
import json
import plotly.express as px


r = requests.get('http://www.mocky.io/v2/5ec864622f00001219db6fac')
response = r.text
data = json.loads(response)
music_list = data['musicas']

musicas = []
acessos = []
meses = []
for m in music_list:
    musicas.append(m['nome'])
    acessos.append(m['acessos'])
    meses.append(m['mes'])




data = dict(
    character=[musicas],
    parent=[meses],
    value=[acessos])

fig =px.sunburst(
    data,
    names='character',
    parents='parent',
    values='value',
)
fig.show()

# data = dict(
#     character=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
#     parent=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
#     value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
#
# fig =px.sunburst(
#     data,
#     names='character',
#     parents='parent',
#     values='value',
# )
# fig.show()