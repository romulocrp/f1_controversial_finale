import pandas as pd
import matplotlib.pyplot as plt
import contractions
import html

def tweet_cleaner(series):
    """Cleans all data and get it ready to tokenize."""
    series = series.str.replace(r"@[A-Za-z0-9_]+", "")
    series = series.str.replace(r"https://[^ ]+", "")
    series = series.str.replace(r"www.[^ ]+", "")
    for j in range(len(series)):
        series[j] = contractions.fix(series[j])
    series = series.str.replace("\W+", " ").str.strip()
    series = series.str.lower()
    series = series.apply(html.escape)
    for w in range(len(series)):
        if " amp " in series[w]:
            series = series.str.replace(" amp ", " & ")
        else:
            continue
    return series

def boxplot_graph(series):
    lenght_of_tweet = [len(t) for t in series]
    lenght_dist, ax = plt.subplots(figsize=(5, 15))
    plt.boxplot(lenght_of_tweet)
    plt.show()

if __name__ == "__main__":
    df = pd.read_csv("f1_final_en.csv", encoding="utf8")
    df = df.drop(["Unnamed: 0", "Unnamed: 0.1"], axis=1)
    boxplot_graph(df["content"])
    df["content"] = tweet_cleaner(df["content"])
    boxplot_graph(df["content"])
    df.to_csv("clean_f1_tweets.csv")