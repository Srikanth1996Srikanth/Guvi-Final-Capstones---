{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec6d06f1-8c28-4c56-ad86-777a2ccc70d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "import pandas as pd\n",
    "from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer\n",
    "from textblob import TextBlob, Word\n",
    "import nltk\n",
    "from nltk.stem.snowball import SnowballStemmer\n",
    "%matplotlib inline\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "nltk.download('wordnet')\n",
    "from nltk.tokenize import word_tokenize\n",
    "nltk.download('punkt')\n",
    "from nltk.corpus import stopwords\n",
    "nltk.download('stopwords')\n",
    "import seaborn as  sns\n",
    "import matplotlib.pyplot as plt\n",
    "import regex as re\n",
    "from wordcloud import WordCloud\n",
    "from nltk.sentiment.vader import SentimentIntensityAnalyzer\n",
    "\n",
    "\n",
    "class SentimentAnalysis:\n",
    "\n",
    "    def __init__(self):\n",
    "        self.tweets = []\n",
    "        self.tweetText = []\n",
    "\n",
    "    def DownloadData(self):\n",
    "        # authenticating\n",
    "        consumerKey = 'your key here'\n",
    "        consumerSecret = 'your key here'\n",
    "        accessToken = 'your key here'\n",
    "        accessTokenSecret = 'your key here'\n",
    "        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)\n",
    "        auth.set_access_token(accessToken, accessTokenSecret)\n",
    "        api = tweepy.API(auth)\n",
    "\n",
    "        # input for term to be searched and how many tweets to search\n",
    "        searchTerm = input(\"Enter Keyword/Tag to search about: \")\n",
    "        NoOfTerms = int(input(\"Enter how many tweets to search: \"))\n",
    "\n",
    "        # searching for tweets\n",
    "        self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = \"en\").items(NoOfTerms)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
