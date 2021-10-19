{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [],
   "source": [
    "import keras\n",
    "from keras.utils import to_categorical\n",
    "import pickle\n",
    "from sklearn import preprocessing\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from keras.utils import plot_model\n",
    "from IPython.display import SVG\n",
    "from keras.utils.vis_utils import model_to_dot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [],
   "source": [
    "def setting():\n",
    "    info = {\n",
    "        'data_path' : \"dataset_training/video_phases_background_removed.pickle\"\n",
    "    }\n",
    "    return info\n",
    "\n",
    "def loaddata(filepath):\n",
    "    with open(filepath, 'rb') as file:\n",
    "        data = pickle.load(file)\n",
    "    return data\n",
    "\n",
    "def vector_cat(label_name, le):\n",
    "    vec = np.zeros(len(list(le.classes_)))\n",
    "    vec[int(le.transform([label_name]))] = 1\n",
    "    return vec\n",
    "\n",
    "def shuffle(vec1, vec2):\n",
    "    c = list(zip(vec1,vec2))\n",
    "    random.shuffle(c)\n",
    "    vec1[:], vec2[:] = zip(*c)\n",
    "    return vec1, vec2\n",
    "\n",
    "def set_x_y(data):\n",
    "    \n",
    "    labels = list(data.keys())\n",
    "    le = preprocessing.LabelEncoder()\n",
    "    le.fit(labels)\n",
    "    x = []\n",
    "    y = []\n",
    "    for key in data.keys():\n",
    "        for img in data[key]:\n",
    "            x.append(img.flatten())\n",
    "            y.append(vector_cat(key, le))\n",
    "    return x,y, le\n",
    "\n",
    "def train_test_shuffle(x,y):\n",
    "    train, label = shuffle(x,y)\n",
    "    train = np.array(train)\n",
    "    label = np.array(label)\n",
    "    if len(train)%2 == 1:\n",
    "        train = np.split(train[:-1,:],2); label = np.split(label[:-1,:],2)\n",
    "    else:\n",
    "        train = np.split(train,2); label = np.split(label,2)\n",
    "    train_x = train[0] #train_x\n",
    "    train_y = label[0] #train_y\n",
    "    test_x = train[1] #test_x\n",
    "    test_y = label[1] #test_y\n",
    "    return train_x, train_y, test_x, test_y    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Epoch 1/150\n",
      "5644/5644 [==============================] - 33s 6ms/step - loss: 5.3939 - acc: 0.6634\n",
      "Epoch 2/150\n",
      "5644/5644 [==============================] - 30s 5ms/step - loss: 5.3885 - acc: 0.6639\n",
      "Epoch 3/150\n",
      "5644/5644 [==============================] - 30s 5ms/step - loss: 5.3885 - acc: 0.6639\n",
      "Epoch 4/150\n",
      "4080/5644 [====================>.........] - ETA: 8s - loss: 5.3953 - acc: 0.6634"
     ]
    }
   ],
   "source": [
    "# main\n",
    "\n",
    "## Setting\n",
    "info = setting()\n",
    "data = loaddata(info['data_path'])\n",
    "x, y, le = set_x_y(data)\n",
    "train_x, train_y, test_x, test_y = train_test_shuffle(x,y)\n",
    "size_input = train_x[0].shape[0]\n",
    "\n",
    "## Learning\n",
    "model = Sequential()\n",
    "model.add(Dense(100, input_dim=size_input, activation='relu'))\n",
    "model.add(Dense(30, activation='relu'))\n",
    "model.add(Dense(len(le.classes_), activation='sigmoid'))\n",
    "# Compile model\n",
    "model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])\n",
    "# Fit the model\n",
    "model.fit(train_x, train_y, epochs=150, batch_size=10)\n",
    "# evaluate the model\n",
    "scores = model.evaluate(train_x, train_y)\n",
    "print(\"\\n%s: %.2f%%\" % (model.metrics_names[1], scores[1]*100))\n",
    "\n",
    "# 10. Evaluate model on test data\n",
    "score = model.evaluate(test_x, test_y, verbose=0)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
