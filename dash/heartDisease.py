# -*- coding: utf-8 -*-


def classify_patient(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    import numpy as np
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.model_selection import train_test_split

    data=dataset = pd.read_csv('./heart.csv')
    shape = dataset.shape

    #dataset.info()
    #dataset.describe()
    #dataset.hist()


    # Feature Scaling
    from sklearn.preprocessing import StandardScaler

    dataset = pd.get_dummies(dataset, columns = ['cp','restecg', 'slope', 'ca', 'thal'])
    standardScaler = StandardScaler()
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    dataset[columns_to_scale] = standardScaler.fit_transform(dataset[columns_to_scale])


    y = dataset['target']
    X = dataset.drop(['target'], axis = 1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)


    from sklearn.neighbors import KNeighborsClassifier

    # determine value of best k
    #knn_scores = []
    #for k in range(1,21):
     #   knn_classifier = KNeighborsClassifier(n_neighbors = k)
      #  knn_classifier.fit(X_train, y_train)
       # knn_scores.append(knn_classifier.score(X_test, y_test))

    knn_classifier = KNeighborsClassifier(n_neighbors = 8)
    knn_classifier.fit(X_train, y_train)


    knn_classifier.score(X_test,y_test)
  
    cp_0=cp_1=cp_2=cp_3=0
    restecg_0=restecg_1=restecg_2=0
    slope_0=slope_1=slope_2=0
    ca_0=ca_1=ca_2=ca_3=ca_4=0 
    thal_0=thal_1=thal_2=thal_3=0
    
    
    if cp == 3:
        cp_0=1
    elif cp==2:
        cp_1=1
    elif cp==1:
        cp_2=1
    elif cp==0:
        cp_3=1
        
    if restecg==0:
       restecg_0=1
    elif restecg==1:
        restecg_1=1
    elif restecg==2:
       restecg_2=1
        
    if slope==0:
        slope_0=1
    elif slope==2:
       slope_2=1
    else :
       slope_1=1
    if ca==0:
        ca_0=1
    elif ca==1:
        ca_1=1
    elif ca==2:
        ca_2=1
    elif ca==3:
        ca_3=1
    elif ca==4:
        ca_4=1
        
    if thal==0:
        thal_0=1
    elif thal==1:
        thal_1=1
    elif thal==2:
        thal_2=1
    elif thal==3:
        thal_3=1
        
    data=pd.DataFrame({'age':[age],'sex':[sex],'cp_0':[cp_0],'cp_1':[cp_1],'cp_2':[cp_2],'cp_3':[cp_3]
    ,'trestbps':[trestbps],'chol':[chol],'fbs':[fbs],
    'restecg_0':[restecg_0],'restecg_1':[restecg_1],'restecg_2':[restecg_2],'thalach':[thalach],'exang':[exang],'oldpeak':[oldpeak]
    ,'slope_0':[slope_0],'slope_1':[slope_1],'slope_2':[slope_2],'ca_0':[ca_0],'ca_1':[ca_1],'ca_2':[ca_2],'ca_3':[ca_3],'ca_4':[ca_4],
    'thal_0':[thal_0],'thal_1':[thal_1],'thal_2':[thal_2],'thal_3':[thal_3]})
    #print(data.info())
   # data = pd.get_dummies(data, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
    standardScaler = StandardScaler()
    columns_to_scale = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
    data[columns_to_scale] = standardScaler.fit_transform(data[columns_to_scale])
    from sklearn import metrics
    return knn_classifier.predict(data), metrics.accuracy_score(knn_classifier.predict(X_test),y_test), shape































