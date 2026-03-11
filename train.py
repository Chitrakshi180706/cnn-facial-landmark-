import tensorflow as tf
from models.cnn_model import create_model
from utils.data_loader import load_dataset

dataset_path = "dataset"

train_dataset = load_dataset(dataset_path)

model = create_model()

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

history = model.fit(
    train_dataset,
    epochs=10
)

model.save("landmark_model.h5")
