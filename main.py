import pandas as pd
import numpy as np
from tabulate import tabulate

# Excel dosyasını oku
file_path = 'C:\\Users\\Meltem\\Desktop\\soru3_data.xlsx'
data = pd.read_excel(file_path, header=None)

# Veri çerçevesini numpy array'e çevir
image = data.to_numpy()

# Gauss filtresi (kernel)
gauss_kernel = np.array([[1, 2, 1],
                         [2, 4, 2],
                         [1, 2, 1]]) / 16.0

# Yeni görüntü boyutu (30x30 olacak)
filtered_image = np.zeros((30, 30))

# Filtre boyutu
k_size = gauss_kernel.shape[0]
offset = k_size // 2

# Gauss filtresini uygula
for i in range(offset, image.shape[0] - offset):
    for j in range(offset, image.shape[1] - offset):
        # Filtre bölgesi
        region = image[i - offset:i + offset + 1, j - offset:j + offset + 1]
        # Filtreyi uygula
        filtered_value = np.sum(region * gauss_kernel)
        filtered_image[i - offset, j - offset] = filtered_value

# Filtrelenmiş görüntüyü tablo olarak göster
filtered_image_df = pd.DataFrame(filtered_image)
print(tabulate(filtered_image_df, headers='keys', tablefmt='grid'))
