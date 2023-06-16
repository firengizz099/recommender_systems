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

print(df.head())
print(df.shape)

print(df['title'].nunique())

print(df['title'].value_counts().head())
comment_counts = pd.DataFrame(df['title'].value_counts())
rare_movies = comment_counts[comment_counts['title'] <= 1000].index #bunlar az yoruma sahip filmler 
comman_movies = df[~df['title'].isin(rare_movies)]
print(comman_movies.shape)
print(comman_movies['title'].nunique())
print(df['title'].nunique())

user_movie_df = comman_movies.pivot_table(index=['userId'], columns=['title'], values='rating')
print(user_movie_df)
print(user_movie_df.columns)


######################################
# Adım 3: Item-Based Film Önerilerinin Yapılması
######################################

movie_name = 'Matrix, The (1999)'
movie_name = "Ocean's Twelve (2004)"
movie_name = user_movie_df[movie_name]
print(movie_name)

print(user_movie_df.corrwith(movie_name).sort_values(ascending=False).head(10))

movie_name = pd.Series(user_movie_df.columns).sample(1).values[0]
print(movie_name)


# keyword girilir user_movie_df'sine gidilir sutunlarinda gezer eger yazilan keyword sutunlarin birinde varsa bunu getirecek
def check_film(keyword, user_movie_df):
    return [col for col in user_movie_df.columns if keyword in col]

check_film('Sherlock', user_movie_df)