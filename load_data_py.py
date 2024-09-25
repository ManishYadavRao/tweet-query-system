# -*- coding: utf-8 -*-
"""load_data.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13Iuvn2K6UrWljKM8p89U__mjbgI_bOW_
"""

import pandas as pd

# Function to load the tweet data
def load_data(file_path):
    try:
        # Load data from the TSV file
        df = pd.read_csv(file_path, sep='\t')
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Replace with your file path (use the smaller file first if necessary)
file_path = '/content/correct_twitter_202102.tsv'

# Load the data
data = load_data(file_path)

# Inspect the first few rows of the dataset to understand its structure
if data is not None:
    print(data.head())  # Shows the first 5 rows

if data is not None:
    print("Column names in the dataset:")
    print(data.columns)

import pandas as pd

# Function to load the tweet data
def load_data(file_path):
    try:
        # Load data from the TSV file
        df = pd.read_csv(file_path, sep='\t')
        print("Data loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Function to query tweets containing a specific term
def query_tweets_by_term(df, term, text_column):
    # Use the correct column name for the tweet text
    result = df[df[text_column].str.contains(term, case=False, na=False)]

    # Count the number of tweets containing the term
    tweet_count = result.shape[0]

    return tweet_count

# Path to the file (change this to the actual path on your system)
file_path = '/content/correct_twitter_202102.tsv'

# Load the data
data = load_data(file_path)

# Inspect the column names and update with the correct column for tweet text
if data is not None:
    print("Column names in the dataset:")
    print(data.columns)

    # Update with the correct column name after inspecting the columns
    text_column = 'text'  # <-- Replace this with the correct column name

    # Example usage: Searching for the term "music"
    term = "music"
    count = query_tweets_by_term(data, term, text_column)
    print(f"Number of tweets containing '{term}': {count}")

def tweets_per_day(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Convert 'created_at' to datetime and handle time zones
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce', utc=True)

    # Filter out any rows where 'created_at' could not be converted
    filtered_df = filtered_df.dropna(subset=['created_at'])

    # Debugging: Check the data type of 'created_at'
    print("Data type of 'created_at':", filtered_df['created_at'].dtype)

    # Group by date and count the tweets
    tweet_counts = filtered_df.groupby(filtered_df['created_at'].dt.date)['id'].count()

    return tweet_counts

def unique_users(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Count unique users (author_id)
    unique_user_count = filtered_df['author_id'].nunique()

    return unique_user_count

def average_likes(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Calculate the average number of likes
    avg_likes = filtered_df['like_count'].mean()

    return avg_likes

def tweet_locations(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Get unique place IDs
    place_ids = filtered_df['place_id'].dropna().unique()

    return place_ids

def tweets_by_time_of_day(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Extract hour from 'created_at'
    tweet_hours = filtered_df['created_at'].dt.hour

    # Group by hour and count the tweets
    tweet_time_distribution = tweet_hours.value_counts().sort_index()

    return tweet_time_distribution

def top_user(df, term):
    # Filter tweets containing the term
    filtered_df = df[df['text'].str.contains(term, case=False, na=False)]

    # Find the user who posted the most tweets
    top_user_handle = filtered_df['author_handle'].value_counts().idxmax()

    return top_user_handle

term = "music"

# Number of tweets per day
print("Tweets per day:")
print(tweets_per_day(data, term))

# Number of unique users
print(f"Unique users posting about '{term}': {unique_users(data, term)}")

# Average likes
print(f"Average likes on tweets about '{term}': {average_likes(data, term)}")

# Locations (place IDs)
print(f"Locations of tweets about '{term}': {tweet_locations(data, term)}")

# Times of day when tweets were posted
print("Tweets by time of day:")
print(tweets_by_time_of_day(data, term))

# User who posted the most tweets
print(f"User who posted the most tweets about '{term}': {top_user(data, term)}")