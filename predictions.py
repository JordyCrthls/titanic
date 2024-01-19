import pandas as pd


def try_out(model, parameters):
    prediction = model.predict(pd.DataFrame([parameters]))[0][0]
    rounded_prediction = round(prediction, 3) * 100
    # survived: True, False
    # Pclass: 1, 2, 3
    # Sex: male, female
    # Embarked: S, C, Q
    print("Survival rate is", round(rounded_prediction, 3), "%")
    return prediction


def evaluation(model, data):
    correct = 0
    total = data.shape[0]
    testing = data.drop(['Survived'], axis=1)
    predictions = model.predict(testing)
    predictions = [1 if p > 0.5 else 0 for p in predictions]
    correct = sum(predictions == data['Survived'])
    percentage_correct = (correct/total) * 100

    print(f'Corectness is {percentage_correct}%')