###########################################
# Item-Based Collaborative Filtering
###########################################

# Veri seti: https://grouplens.org/datasets/movielens/

# Adım 1: Veri Setinin Hazırlanması
# Adım 2: User Movie Df'inin Oluşturulması
# Adım 3: Item-Based Film Önerilerinin Yapılması
# Adım 4: Çalışma Scriptinin Hazırlanması

######################################
# Adım 1: Veri Setinin Hazırlanması
######################################
import pandas as pd
pd.set_option('display.max_columns', 500)
movie = pd.read_csv('/home/firengiz/Belgeler/recommedation/movie.csv')
rating = pd.read_csv('/home/firengiz/Belgeler/recommedation/rating.csv')
df = movie.merge(rating, how="left", on="movieId")
print(df.head())


######################################
# Adım 2: User Movie Df'inin Oluşturulması
######################################