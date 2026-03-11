import tensorflow as tf

def load_dataset(path):

    dataset = tf.keras.utils.image_dataset_from_directory(
        path,
        image_size=(224,224),
        batch_size=32
    )

    return dataset
