import pandas as pd


# function to load reviews
#bad reviews have overall ratings < 5
#good reviews have overall ratings >= 5
#get hotel review data from https://www.kaggle.com/jiashenliu/515k-hotel-reviews-data-in-europe/data#

def load_data():
    # read data
    reviews_df = pd.read_csv("data/Hotel_Reviews.csv")
    # append the positive and negative text reviews
    reviews_df["review"] = reviews_df["Negative_Review"] + reviews_df["Positive_Review"]
    # create the label
    reviews_df["is_bad_review"] = reviews_df["Reviewer_Score"].apply(lambda x: 1 if x < 5 else 0)
    # select only relevant columns
    reviews_df = reviews_df[["review", "is_bad_review"]]
    print(reviews_df.head())


load_data()

