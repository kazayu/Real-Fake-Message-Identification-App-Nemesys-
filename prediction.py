import pickle

#doc_new = ['obama is running for president in 2016']
def find1(var):
    return detecting_fake_news1(var)

def find2(var):
    return detecting_fake_news2(var)
    
#function to run for prediction
def detecting_fake_news1(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
    prediction = load_model.predict([var])
  # prob = load_model.predict_proba([var])

    return (prediction[0])


def detecting_fake_news2(var):    
#retrieving the best model for prediction call
    load_model = pickle.load(open('final_model.sav', 'rb'))
   # prediction = load_model.predict([var])
    prob = load_model.predict_proba([var])

    a=prob[0][1]
    b=a*100
    if(b<50):
        return ("Low Possibility")
    elif(b>=50 and b<=60):
        return("Medium Possibility")
    else:
        return("High Possibility")


#if __name__ == '__main__':
 #   detecting_fake_news(var)