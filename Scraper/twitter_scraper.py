import os

dates = ["2021-12-13", "2021-12-14", "2021-12-15", "2021-12-16"]

hashtags = ["f1", "formula1", "formulaone", "fia", "abudhabigp", "maxverstappen33", "lewishamilton44"]

for hashtag in hashtags:
    for date in dates:
        os.system(f"snscrape --jsonl --max-results 50000 twitter-hashtag '{hashtag} until:{date}' > hash{hashtag}{date}.json")
        print(f"Scrape {hashtag} on {date} done!")
    print(f"Scrape of {hashtag} done!")

print("All done!")
