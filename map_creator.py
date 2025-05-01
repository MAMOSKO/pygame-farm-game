import json

grasses = []

for y in range(1, 13):
    for x in range(1, 21):
        grasses.append([x, y, 12])

data = {
    "grasses": grasses
}

# Elle biçimlendirme: her iç listeyi tek satırda yaz
with open("grass_map.txt", "w") as f:
    f.write('{\n  "grasses": [\n')
    for i, g in enumerate(grasses):
        line = f'    {json.dumps(g)}'
        if i != len(grasses) - 1:
            line += ','
        f.write(line + '\n')
    f.write('  ]\n}')