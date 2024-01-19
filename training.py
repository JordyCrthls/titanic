import keras
from tensorflow.keras import layers

from sklearn.model_selection import train_test_split


def train_model(data, num_epochs=50):
    dataframe = data.drop(['Survived'], axis=1)

    train_data, unused_train, test_data, unused_test = train_test_split(dataframe, data['Survived'], test_size=0.9)
    input = layers.Input(shape=(4, 1, 1))
    layer_build = layers.Flatten()(input)
    layer_build = layers.Dense(57, activation='relu')(layer_build)
    layer_build = layers.Dense(57, activation='relu')(layer_build)
    output = layers.Dense(1, activation='sigmoid')(layer_build)
    model = keras.Model(inputs=input, outputs=output)
    model.compile(optimizer='adam', loss='binary_crossentropy')
    model.fit(train_data, test_data, epochs=num_epochs)
    model.summary()

    return model
