# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("C:\\Users\\Jane Imoke\\Desktop\\breast_cancer_pred\\data.csv")
data.head()


# In[3]:


data.drop(["Unnamed: 32", "id"], axis=1, inplace=True)

data.replace({
    "diagnosis": {"B": 0, "M": 1}
}, inplace=True)

data.head()


# In[4]:


data.info()


# In[9]:


def create_model(data):
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split
    from sklearn.linear_model import LogisticRegression

    # on to creating & training the model

    X = data.drop(["diagnosis"], axis=1)
    Y = data["diagnosis"]

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = LogisticRegression()
    model.fit(X_train, Y_train)
    
    return model, scaler


# In[8]:


from sklearn.metrics import accuracy_score, classification_report

# testing the model and checking its accuracy

Y_pred = model.predict(X_test)
print(f"Model accuracy score: {accuracy_score(Y_test, Y_pred)}")
print(f"Classification report: {classification_report(Y_test, Y_pred)}")


# In[11]:


import pickle as pkl

with open("C:\\Users\\Jane Imoke\\Desktop\\breast_cancer_pred\\model.pkl", "wb") as f:
    pkl.dump(model, f)
    
with open("C:\\Users\\Jane Imoke\\Desktop\\breast_cancer_pred\\scaler.pkl", "wb") as f:
    pkl.dump(scaler, f)


# In[ ]:
