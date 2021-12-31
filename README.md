# Formula 1 final round Twitter Analysis

## Introduction

On December 12th Abu Dhabi hosted the final race on the F1 2021 calendar, the race had great importance due to both champion contestants being tied to this very race, given the major dispute being observed, specially, on the last races.

The race weekend started with tension and finished on a dramatic fashion, with Nicolas Latifi's crash on lap 53 out of 58, questionable decisions from the race director and one last lap showdown to the end of the line Max Verstappen was crowned champion of the world.

Since the beginning of the championship, Twitter has been an important tool to measure how fans and the public are feeling about each race, although, the more intese the battle got on track, more hostile Twitter environment got, that was brought to attention by some jornalists and influencers along the season.

Given all those points, this project will use NLP techniques to make an analysis on Twitter on the 12, 13, 14, and 15th of December to try to understand how fans really felt about how one of the most iconic seasons in F1 ended.

## Goals

### General Goals

To provide an analysis an a better understanding on how F1 fans expressed their feelings on Twitter on the days 12, 13, 14, and 15th of December.

### Specific Goals

- How was the Twitter's reaction in general? Positive or Negative?
- How did people felt about F1? FIA, Lewis Hamilton, and Max Verstappen?
- What was that feeling that most of the people expressed in those days?
- What was the feeling that most of the people expressed towards those same entities?

## Methods

To start the project 50,000 tweets were scraped from Twitter using the snscrape tool along with Python program, tweets were extracted using an upper date limit due to software limitations, it imposes a series of problems like duplication, many tweets may be duplicated since one hashtag may not have the amount of tweets that are going to be scraped.

Another issue is that tweets from previous dates may be extracted too, since the first day may not have the amount of tweets necessary to meet the criteria.

The information scraped from Twitter geerated these columns:

![json columns image](https://github.com/romulocrp/f1_controversial_finale/img/json_columns.png?raw=true)

Out those columns 7 were selected to provide more insight into the matter:

- date
- content
- replyCount
- retweetCount
- likeCount
- lang
- sourceLabel

Also, only tweets on english language were analyzed, they represent more than 50% of all tweets gathered.

All data was cleaned and pre-processed, all HTMLs were cleaned along with all "#" signs, mentions, and emoticons, also, all data was converted to lower case.

## Results

The scraping provided 28 .json files with 50,000 tweets to be cleaned. After all pre-processing phase, one .csv file was created with the database ready to be tockenized, in total, 
