'''
 Meta-indicator demo: Intelligent Media Sentiment Index
'''
import numpy as np
import pandas as pd
import json
import time
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

import numpy as np
import pandas as pd
import json
import time
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle

def create_dataset():

    # Creating training data from news sites sentiment
    news_sites = {"Decrypt":[],
                  "Forbes":[],
                  "U.Today":[],
                  "Cointelegraph":[],
                  "BeInCrypto":[],
                  'Bitcoin.com':[],
                  'Bitcoinist':[],
                  'Blockworks':[],
                  'Bitcoin Magazine':[],
                  'The Block':[],
                  'Crypto Daily':[],
                  'CoinGape':[],
                  'The Daily Hodl':[],
                  'AMBCrypto':[],
                  'CryptoPotato':[]}

    labels = []
    start_date = datetime.strptime('2022-04-06','%Y-%m-%d')
    end_date = datetime.strptime('2023-04-29','%Y-%m-%d')
    while start_date < end_date:
        print("> Adding data for ",start_date)
        todays_news = pd.read_csv('datasets/daily_news_data/'+start_date.strftime('%Y-%m-%d')+'_coingecko.csv')
        todays_coins = pd.read_csv('datasets/daily_coin_data/'+start_date.strftime('%Y-%m-%d')+'_all_coins.csv')
        start_date += timedelta(days=1)
        for site, sentiments in news_sites.items():
            site_news = todays_news[todays_news['source'].str.contains(site)]

            # If no news today then add the latest known sentiment
            if len(site_news) == 0:
                if len(sentiments) == 0:
                    news_sites[site].append(0)
                else:
                    news_sites[site].append(sentiments[len(sentiments)-1])
            else:
                news_sites[site].append(site_news['flair_sentiment_title'].mean())

        # Labels based on future marketcap 14 days from now
        marketcap_today = todays_coins['market-cap'].sum()
        labeling_day = start_date + timedelta(days=30)
        label_coins = pd.read_csv('datasets/daily_coin_data/' + labeling_day.strftime('%Y-%m-%d') + '_all_coins.csv')
        marketcap_future = label_coins['market-cap'].sum()
        if marketcap_future >= marketcap_today:
            labels.append(1) # Increased or stayed the same
        else:
            labels.append(0) # Decreased

    for site, sentiments in news_sites.items():
        print(site,"->",sentiments)
    print(labels)
    df = pd.DataFrame(news_sites)
    df['labels'] = labels
    df.to_csv("imsi_dataset.csv")

def trai_imsi(media_weights=False):
    print("> Creating IMSI Index and Media Weights")

    # Training model for prediction of marketcap based on sentiment
    dataset = pd.read_csv('imsi_dataset.csv',index_col=0)
    y = dataset['labels'].values
    dataset.drop('labels', axis=1, inplace=True)
    X = dataset.values
    feature_labels=dataset.columns.values

    # Everyday I'm shuffling!!!!
    indices = np.arange(len(X))
    np.random.shuffle(indices)
    X = X[indices]
    y = y[indices]

    if media_weights:
        # Media Imortance
        rf = RandomForestClassifier(random_state=0)
        #rf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.01)
        rf.fit(X,y)
        fi = rf.feature_importances_
        from matplotlib import pyplot as plt
        plt.figure()
        plt.barh(feature_labels, fi, align='center')
        plt.show()
        print(feature_labels)
        print(fi)
        return feature_labels, fi

    # Cross val evaluation of a potential model
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=10, random_state=0, shuffle=True)
    accuracies = []
    f1 = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        rf = RandomForestClassifier(random_state=0)
        #rf = GradientBoostingClassifier(n_estimators=100,learning_rate=0.01)
        rf.fit(X_train, y_train)
        predictions = rf.predict(X_test)
        accuracies.append(accuracy_score(y_test,predictions))
        f1.append(f1_score(y_test, predictions))
    print(accuracies)
    print(f1)
    print(np.average(accuracies),"F1",np.average(f1))

def finetune_imsi_model():
    # Training model for prediction of marketcap based on sentiment
    dataset = pd.read_csv('imsi_dataset.csv', index_col=0)
    y = dataset['labels'].values
    dataset.drop('labels', axis=1, inplace=True)
    X = dataset.values

    from sklearn.model_selection import GridSearchCV
    #rf = RandomForestClassifier(random_state=0)
    rf = GradientBoostingClassifier()
    parameters = {'n_estimators': [50, 100, 150,
                                   200,300,400,500],'learning_rate':[0.001, 0.01,0.05,0.1]}
    search_model = GridSearchCV(rf, parameters, scoring='accuracy', cv=10, verbose=3)  # cv=10. Uses 10-folds
    search_model.fit(X, y)
    print("GridSearch - Best Hyperparameters:", search_model.best_params_, "Best:", search_model.best_score_)
    # 0.05 - 500

# TODO - TO improve performance maybe use Average sentiment instead of FLAIR ONLY
def export_imsi_index():
    sites, weights = trai_imsi(media_weights=True)
    imsi_index = []

    start_date = datetime.strptime('2022-04-06', '%Y-%m-%d')
    end_date = datetime.strptime('2023-04-29', '%Y-%m-%d')
    while start_date < end_date:
        print("> Creating IMSI Index for",start_date)
        imsi = 0
        todays_news = pd.read_csv('datasets/daily_news_data/' + start_date.strftime('%Y-%m-%d') + '_coingecko.csv')

        available_publishers_today = len(sites)
        redistributed_weight = 0
        for i in range(len(sites)):
            site_news = todays_news[todays_news['source'].str.contains(sites[i])]
            if site_news.empty:
                available_publishers_today -= 1
                redistributed_weight += weights[i]

        for i in range(len(sites)):
            site_news = todays_news[todays_news['source'].str.contains(sites[i])]
            if not site_news.empty:
                site_sentiment_av = site_news['flair_sentiment_title'].mean()
                imsi += site_sentiment_av * (weights[i] + redistributed_weight/available_publishers_today)
               #else:
             #   print(">> NO ARTICLE FROM",sites[i],available_publishers_today," ",redistributed_weight)
        imsi_index.append(imsi)
        start_date += timedelta(days=1)

    print("Sites:",sites)
    print("Weights:",list(weights))
    print("IMSI: ",imsi_index)

    # Smooth IMSI rolling window 7 days
    window = 7
    imsi_index_smooth = [sum(imsi_index[i:i + window]) / window for i in range(len(imsi_index) - window-1)]
    print(len(imsi_index))
    print(len(imsi_index_smooth))
    print("IMSI SMOOTH:",imsi_index_smooth)
    # TODO - Automatically export these to make it easier to transfer to front-end

if __name__ == '__main__':
    print("> Intelligent Media Sentiment Index")
    #create_dataset()

    # TODO - If I have time make the models better
    #trai_imsi(media_weights=False)
    #finetune_imsi_model()

    # This
    export_imsi_index()
