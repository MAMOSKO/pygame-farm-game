import os

def rename_png_files(folder_path, prefix):
    # Klasördeki tüm dosyaları al
    files = os.listdir(folder_path)
    
    # Sadece .png uzantılı dosyaları filtrele ve alfabetik sırala
    png_files = sorted([f for f in files if f.lower().endswith('.png')])
    
    for index, filename in enumerate(png_files, start=0):
        old_path = os.path.join(folder_path, filename)
        new_filename = f"{prefix}{index}.png"
        new_path = os.path.join(folder_path, new_filename)
        
        os.rename(old_path, new_path)
        print(f"Renamed: {filename} -> {new_filename}")

# Kullanım örneği
rename_png_files("Biom", "biom")
