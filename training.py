import keras
from tensorflow.keras import layers

from sklearn.model_selection import train_test_split


def train_model(data, num_epochs=50):
    labels = data['Survived']
    dataframe = data.drop(['Survived'], axis=1)
    train_data, test_data, train_labels, test_labels = train_test_split(dataframe, labels, test_size=0.2, random_state=1)
    input = layers.Input(shape=(4, 1, 1))
    layer_build = layers.Flatten()(input)
    layer_build = layers.Dense(57, activation='relu')(layer_build)
    layer_build = layers.Dense(57, activation='relu')(layer_build)
    output = layers.Dense(1, activation='sigmoid')(layer_build)
    model = keras.Model(inputs=input, outputs=output)
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(train_data, train_labels, epochs=num_epochs)
    model.summary()

    return model
