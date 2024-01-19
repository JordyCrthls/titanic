from predictions import evaluation
from preprocessing import get_clean_data
from training import train_model


if __name__ == '__main__':
    data = get_clean_data()
    model = train_model(data)
    evaluation(model, data)
