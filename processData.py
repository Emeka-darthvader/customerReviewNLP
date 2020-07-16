#Reviews data is sampled in order to speed up computations.
reviews_df = reviews_df.sample(frac = 0.1, replace = False, random_state=42)

# remove 'No Negative' or 'No Positive' from text
reviews_df["review"] = reviews_df["review"].apply(lambda x: x.replace("No Negative", "").replace("No Positive", ""))

