import pandas as pd
wine_reviews = pd.read_csv("/Users/a0000/Downloads/winemag-data-130k-v2.csv")
print(wine_reviews.shape)
print(wine_reviews.head(10))

reviews = pd.read_csv("/Users/a0000/Downloads/winemag-data-130k-v2.csv", index_col=0)
print(reviews.country)