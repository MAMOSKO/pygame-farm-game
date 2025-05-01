from PIL import Image
import numpy as np

# === DOSYA YOLLARINI BURADAN AYARLA ===
pixel_art_path = "pixel-art-illustration-barn-pixelated-barn-barn-building-farm-icon-pixelated-for-the-pixel-art-game-and-icon-for-website-and-video-game-old-school-retro-vector.jpg"
palette_path = "Sprout Lands defautlt palette snip.PNG"
output_path = "pixel_art_recolored.png"

# === RESİMLERİ YÜKLE ===
pixel_img = Image.open(pixel_art_path).convert("RGBA")
palette_img = Image.open(palette_path).convert("RGB")

pixel_np = np.array(pixel_img)
palette_np = np.array(palette_img)

# === PALET RENKLERİNİ AL ===
palette_colors = np.unique(palette_np.reshape(-1, 3), axis=0)

# === RENGİ EN YAKIN PALET RENGİNE EŞLE ===
def closest_color(color, palette):
    diffs = palette - color
    distances = np.linalg.norm(diffs, axis=1)
    return palette[np.argmin(distances)]

# === YENİ GÖRSELİ OLUŞTUR ===
new_rgb = pixel_np[:, :, :3].copy()
alpha = pixel_np[:, :, 3]

for y in range(pixel_np.shape[0]):
    for x in range(pixel_np.shape[1]):
        if alpha[y, x] > 0:  # sadece şeffaf olmayanlar
            original_color = new_rgb[y, x]
            new_rgb[y, x] = closest_color(original_color, palette_colors)

# === RGBA BİRLEŞTİR VE KAYDET ===
new_rgba = np.dstack((new_rgb, alpha))
new_img = Image.fromarray(new_rgba, "RGBA")
new_img.save(output_path)

print("Yeni görsel kaydedildi:", output_path)
