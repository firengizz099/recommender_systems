# **recommender_systems**
![App Screenshot](https://github.com/firengizz099/recommender_systems/blob/main/1_T4-XpKM2jRioTd5f_gwX1g.png?raw=true)

# **arl.py**
Bu kodun temel amacı, birliktelik analizi kullanarak perakende veri setindeki ürünler arasındaki ilişkileri bulmak ve sepet aşamasındaki kullanıcılara ürün önerilerinde bulunmaktır. İlk olarak veri seti önişleme adımlarından geçirilir, ardından birliktelik kuralları çıkarılır. Daha sonra belirli bir ürün için öneri yapmak için bir fonksiyon kullanılır.

# **content_based_recommender.py**
Bu kodun temel amacı, içerik temelli (content-based) bir tavsiye sistemi geliştirmektir. Bu sistem, filmlerin "overview" (genel bakış) metinlerini kullanarak benzer filmler önerir. İşlemler üç adımda gerçekleştirilir:

TF-IDF Matrisinin Oluşturulması: Veri setindeki filmlerin "overview" metinlerinden TF-IDF matrisi oluşturulur. Bu matris, her filmin metnini temsil eden bir vektörle ifade edilir.

Cosine Similarity Matrisinin Oluşturulması: TF-IDF matrisi kullanılarak cosine similarity matrisi oluşturulur. Bu matris, her filmin diğer filmlerle olan benzerlik skorlarını içerir.

Benzerliklere Göre Önerilerin Yapılması: Verilen bir film için, benzerlik skorlarına göre en yakın filmler belirlenir ve öneriler yapılır.

Fonksiyonlar aracılığıyla belirli bir film için öneri yapılabilir veya daha genel olarak tüm işlemler tek bir işlevde gerçekleştirilebilir.

# **item_based.py**

Bu kodun temel amacı, item-based collaborative filtering (öğe-tabanlı işbirlikçi filtreleme) kullanarak film önerileri yapmaktır. İşlemler dört adımda gerçekleştirilir:

Veri Setinin Hazırlanması: Film ve derecelendirme verileri birleştirilerek bir veri çerçevesi oluşturulur.
User Movie Df'inin Oluşturulması: Veri çerçevesi kullanılarak kullanıcı-film matrisi oluşturulur. Her satır bir kullanıcıyı, her sütun bir filmi temsil eder ve değerler kullanıcının o filme verdiği puanları içerir.

Item-Based Film Önerilerinin Yapılması: Belirli bir film için, diğer filmlerle olan benzerlik skorları hesaplanır. Seçilen filmle benzerlik skorlarına göre en yüksek puan alan filmler önerilir.

Çalışma Scriptinin Hazırlanması: Yukarıdaki adımlar bir script içinde bir araya getirilir.

Fonksiyonlar aracılığıyla belirli bir film için öneri yapılabilir veya daha genel olarak tüm işlemler tek bir işlevde gerçekleştirilebilir. Ayrıca, "check_film" fonksiyonu belirli bir anahtar kelimeye sahip filmleri bulmak için kullanılabilir.

# **user_based.py**

Bu kod, user-based collaborative filtering (kullanıcı-tabanlı işbirlikçi filtreleme) kullanarak bir kullanıcıya film önerileri yapmayı amaçlar. İşlemler altı adımda gerçekleştirilir:

create_user_movie_df fonksiyonu, veri setinden kullanıcı-film matrisini oluşturur. Bu matris, her satırda bir kullanıcıyı ve her sütunda bir filmi temsil eder. Değerler, kullanıcının o filme verdiği puanları içerir.

user_based_recommender fonksiyonu, belirli bir kullanıcıya film önerileri yapar. Fonksiyona, öneri yapılacak kullanıcı, kullanıcı-film matrisi, benzerlik eşiği (cor_th), puan eşiği (score) ve puanlama oranı (ratio) gibi parametreler geçirilir.

İlk olarak, belirtilen kullanıcının izlediği filmler ve bu filmleri izleyen diğer kullanıcılar belirlenir
Ardından, belirli bir benzerlik eşiğini geçen kullanıcıların benzerlik skorları hesaplanır ve en benzer kullanıcılar belirlenir.
Bu benzer kullanıcıların puanladığı filmler ve ağırlıklandırılmış puanları kullanılarak bir öneri skoru hesaplanır.
**Son olarak, belirli bir puan eşiğini aşan ve en yüksek öneri skoruna sahip filmler önerilir.**
**Bu kod, veri seti üzerinde kullanıcı-tabanlı işbirlikçi filtreleme uygulayarak belirli bir kullanıcıya film önerileri yapmak için kullanılır.**

# **matrix_factorization.py**
Bu kod, model tabanlı işbirlikçi filtreleme yöntemi olan Matrix Factorization (Matris Ayrıştırma) yöntemini kullanarak bir öneri sistemini oluşturmayı amaçlamaktadır. İşlemler aşağıdaki adımlar üzerinden gerçekleştirilmektedir:

Adım 1: Veri Setinin Hazırlanması

"movie.csv" ve "rating.csv" dosyaları okunarak veri setleri elde edilir.
"movie" ve "rating" veri setleri "movieId" sütunu üzerinden birleştirilerek "df" veri seti oluşturulur.
**Örnek olarak belirlenen 4 filmin verileri "sample_df" veri setine atanır.**
**Kullanıcı ve film arasındaki ilişkileri içeren bir pivot tablo olan "user_movie_df" oluşturulur.**
**Veri seti "reader" kullanılarak "data" nesnesine dönüştürülür.**
**Adım 2: Modelleme**

**Veri seti, eğitim ve test kümelerine ayrılır.**
**"SVD" modeli tanımlanır ve eğitim kümesi üzerinde uyumlandırılır.**
**Test kümesi üzerinde tahminlemeler yapılır.**
**Tahminlemelerin performansı "RMSE" metriği kullanılarak değerlendirilir.
Adım 3: Model Tuning**

**GridSearchCV yöntemi kullanılarak en iyi hiperparametreler belirlenir.**
**Parametre grid'i ve performans metrikleri tanımlanır.**
**GridSearchCV modeli veri üzerinde uyumlandırılır ve en iyi skor ve parametreler elde edilir.**
**Adım 4: Final Model ve Tahmin**

**En iyi parametreler kullanılarak final SVD modeli oluşturulur.**
Tüm veri seti üzerinde model eğitimi gerçekleştirilir.
**Belirli bir kullanıcı ve film için tahminleme yapılır.**
Kodun amacı, veri setinden bir öneri sistemini oluşturmak, modeli eğitmek, performansını değerlendirmek, en iyi parametreleri bulmak ve son olarak kullanıcının belirli bir film için tahminlemesini yapmaktır.
