import random

# Koordinat sınırları
x_min, x_max = -3, 23
y_min, y_max = -3, 15

# Seçilebilecek süs türleri
decoration_types = [5,6,7,8,9,14,15,16,18,19,23,24,25,26]

# Yerleştirme sıklığı (0.0 ile 1.0 arası)
# Örneğin 0.05 = %5 ihtimalle süs konur
placement_probability = 0.1

# Süslerin listesi
decorations = []

# Koordinat düzlemini gez
for x in range(x_min, x_max + 1):
    for y in range(y_min, y_max + 1):
        if random.random() < placement_probability:
            block_type = random.choice(decoration_types)
            decorations.append([x, y, block_type])

# Çıktı
print(decorations)
