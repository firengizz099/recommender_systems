#############################
# Model-Based Collaborative Filtering: Matrix Factorization
#############################

# !pip install surprise
import pandas as pd
from surprise import Reader, SVD, Dataset, accuracy
from surprise.model_selection import GridSearchCV, train_test_split, cross_validate
pd.set_option('display.max_columns', None)

# Adım 1: Veri Setinin Hazırlanması
# Adım 2: Modelleme
# Adım 3: Model Tuning
# Adım 4: Final Model ve Tahmin

#############################
# Adım 1: Veri Setinin Hazırlanması
#############################

movie = pd.read_csv('/home/firengiz/Belgeler/recommedation/movie.csv')
rating = pd.read_csv('/home/firengiz/Belgeler/recommedation/rating.csv')
df = movie.merge(rating, how="left", on="movieId")
print(df.head())

movie_ids = [130219, 365, 4422, 541]
movies = ["The Dark Knight (2011)",
          "Cries and Whispers (Viskningar och rop) (1972)",
          "Forrest Gump (1994)",
          "Blade Runner (1982)"]

sample_df = df[df.moviesId.isin(movie_ids)]
print(sample_df)

user_movie_df = sample_df.pivot_table(index=['userId'], 
                                      columns=['title'], 
                                      values=['rating'])
print(user_movie_df.shape)

reader = Reader(rating_scale=(1,5))

data = Dataset.load_from_df(sample_df[['userId',
                                      'movieId',
                                      'rating']],reader)

##############################
# Adım 2: Modelleme
##############################

trainset, testset = train_test_split(data, test_size=.25)
svd_model = SVD()
svd_model.fit(trainset)
predictions = svd_model.test(testset)
print(predictions)

print(accuracy.rmse(predictions))

print(sample_df[sample_df['userId'] == 1])

print(svd_model.predict(uid=1.0, iid=541, verbose=True))

##############################
# Adım 3: Model Tuning
############################## 

param_grid = {'n_epochs': [5, 10, 20], 
              'lr_all': [0.002, 0.005, 0.007]}

gs = GridSearchCV(SVD,
                  param_grid,
                  measures=['rmse', 'mae'],
                  cv=3, 
                  n_jobs=-1,
                  joblib_verbose=True)

print(gs.fit(data))

print(gs.best_score['rmse'])

print(gs.best_params['rmse'])


##############################
# Adım 4: Final Model ve Tahmin
##############################

dir(svd_model)

svd_model = SVD(**gs.best_params['rmse'])

data = data.build_full_tarinset()
svd_model.fit(data)

print(svd_model.predict(uid=1.0, iid=541, verbose=True))

#