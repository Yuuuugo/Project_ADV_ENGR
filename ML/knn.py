from sklearn import tree

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import plot_confusion_matrix
import json
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


with open("/Users/hugo/Cincinnati/ADV_ENGR/my_env/Project_ADV_ENGR/json/all.json", "r") as read_file:
    data = json.load(read_file)



Review_label = []

for i in range(len(data)):
    a = data[i]["comment"]
    b = data[i]["label"]
    Review_label.append([a,b])


df = pd.DataFrame(Review_label)
df.columns = ["review","label"]

for i in range(len(df)):
    if df["label"][i] == "Bug":
        df["label"][i] = 1
    elif df["label"][i] == "Feature":
        df["label"][i] = 2
    elif df["label"][i] == "Rating":
        df["label"][i] = 3
    elif df["label"][i] == "UserExperience":
        df["label"][i] = 4
        
X_train, X_test, Y_train, Y_test = train_test_split(df['review'],
                                                    df['label'],
                                                    test_size=0.2,
                                                    stratify=df['label'])

print('Size of Training Data ', X_train.shape[0])
print('Size of Test Data ', X_test.shape[0])

countv = CountVectorizer(min_df = 1, ngram_range=(1,5), stop_words="english")
#countv = TfidfVectorizer(min_df = 1, ngram_range=(1,5), stop_words="english")
X_train_tf = countv.fit_transform(X_train)


Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')


X_test_tf = countv.transform(X_test)



""" tree.plot_tree(clf)
plt.show() """



x = []
y = []

for k in range(1,100):
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train_tf,Y_train)

    X_test_tf = countv.transform(X_test)

    Y_pred = clf.predict(X_test_tf)

    """ tree.plot_tree(clf)
    plt.show() """



    x.append(k)
    y.append(accuracy_score (Y_pred,Y_test))



plt.xlabel("k")
plt.ylabel("Accuracy score")
plt.plot(x,y)


plt.show()