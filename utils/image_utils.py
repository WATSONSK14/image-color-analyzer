from PIL import Image
import numpy as np
from sklearn.cluster import KMeans

class ImageUtils:
    def __init__(self):
        pass

    def analyze(self, image_path, n_colors=10, max_size=500):
        """
        Görüntüyü analiz eder ve dominant renkleri bulur.
        
        Args:
            image_path: Analiz edilecek görüntü dosyası yolu
            n_colors: Bulunacak renk sayısı (varsayılan: 10)
            max_size: Performans için maksimum görüntü boyutu (varsayılan: 500px)
        
        Returns:
            List of tuples: [(hex_color, percentage), ...]
        """
        img = Image.open(image_path).convert('RGB')
        
        # Performans için büyük resimleri küçült
        if max(img.size) > max_size:
            img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        img_array = np.array(img).reshape(-1, 3)

        kmeans = KMeans(n_clusters=n_colors)
        labels = kmeans.fit_predict(img_array)

        counts = np.bincount(labels)
        centers = np.round(kmeans.cluster_centers_).astype(int)
        centers = np.clip(centers, 0, 255)

        percentages = counts / counts.sum() * 100
        percentages = np.round(percentages, 2)

        hex_colors = ['#{:02X}{:02X}{:02X}'.format(r, g, b) for r, g, b in centers]

        return list(zip(hex_colors, percentages))


