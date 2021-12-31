import pandas as pd

def col_drop(path, hashtag, date):
    """Filters columns from JSON files"""
    df = pd.read_json(path, lines = True)
    dfc = df[["date", "content", "replyCount", "retweetCount", "likeCount", "lang", "sourceLabel"]]
    dfc.to_csv(f"{hashtag}{date}.csv")

def csv_appender(list_of_paths, hashtag):
    """Appends all files into one"""
    df1 = pd.read_csv(list_of_paths[0])
    for path in list_of_paths[1:len(list_of_paths)]:
        df2 = pd.read_csv(path)
        df1 = df1.append(df2)
    df1 = df1.reset_index()
    df1.to_csv(f"{hashtag}.csv")



if __name__ == "__main__":
    dates = ["2021-12-13", "2021-12-14", "2021-12-15", "2021-12-16"]
    hashtags = ["f1", "formula1", "formulaone", "fia", "abudhabigp", "maxverstappen33", "lewishamilton44"]
    csv_paths = [f"{hashtag}{date}.csv" for hashtag in hashtags for date in dates]
    csvs = [f"{hashtag}.csv" for hashtag in hashtags]

    for hashtag in hashtags:
        for date in dates:
            col_drop(f"hash{hashtag}{date}.json", hashtag, date)
            print(f"{hashtag} and {date} done!")
        print(f"{hashtag} done!")

    print("Column dropping done!")

    csv_appender(csv_paths, "f1_final_tweets")
    
    print("f1_final_tweets.csv done!")

    
    df = pd.read_csv('f1_final_tweets.csv', low_memory=False)
    df = df.drop(df[df.date == "0"].index)
    df = df.drop(["Unnamed: 0", "index", "Unnamed: 0.1"], axis=1)
    df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d %H:%M:%S')
    df = df.drop_duplicates()
    print(df.dtypes)
    print(df.shape)
