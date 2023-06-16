# recommender_systems
# arl.py
Bu kodun temel amacı, birliktelik analizi kullanarak perakende veri setindeki ürünler arasındaki ilişkileri bulmak ve sepet aşamasındaki kullanıcılara ürün önerilerinde bulunmaktır. İlk olarak veri seti önişleme adımlarından geçirilir, ardından birliktelik kuralları çıkarılır. Daha sonra belirli bir ürün için öneri yapmak için bir fonksiyon kullanılır.

# content_based_recommender.py
Bu kodun temel amacı, içerik temelli (content-based) bir tavsiye sistemi geliştirmektir. Bu sistem, filmlerin "overview" (genel bakış) metinlerini kullanarak benzer filmler önerir. İşlemler üç adımda gerçekleştirilir:

TF-IDF Matrisinin Oluşturulması: Veri setindeki filmlerin "overview" metinlerinden TF-IDF matrisi oluşturulur. Bu matris, her filmin metnini temsil eden bir vektörle ifade edilir.

Cosine Similarity Matrisinin Oluşturulması: TF-IDF matrisi kullanılarak cosine similarity matrisi oluşturulur. Bu matris, her filmin diğer filmlerle olan benzerlik skorlarını içerir.

Benzerliklere Göre Önerilerin Yapılması: Verilen bir film için, benzerlik skorlarına göre en yakın filmler belirlenir ve öneriler yapılır.

Fonksiyonlar aracılığıyla belirli bir film için öneri yapılabilir veya daha genel olarak tüm işlemler tek bir işlevde gerçekleştirilebilir.
