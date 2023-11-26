import cv2
import numpy as np

# Resmi okuyoruz
img = cv2.imread("pirinc.jpg", 0)

# 150 eşik değerini seçip eşikleme uyguluyoruz
ret, thresholded = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

# istenmeyen noktalar için gürültü azaltma uyguluyoruz
kernel = np.ones((5, 5), np.uint8)
thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)

# birbiri ile bağlantılı pikselleri bileşenlerine göre etiketliyoruz ve sayıyoruz
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(thresholded, connectivity=8)

# İlk etiketi (arka plan) çıkarıyoruz
num_pirinc_taneleri = num_labels - 1

print(f"Pirinç Taneleri Sayısı: {num_pirinc_taneleri}")


cv2.imshow("orijinal resim", img)
cv2.imshow("isleme ugrayan resim", thresholded)
cv2.waitKey(0)
cv2.destroyAllWindows()
