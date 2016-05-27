from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.optimizers import SGD, RMSprop
from keras.utils import np_utils
import matplotlib.pyplot as plt
import numpy as np
from scipy import misc
import pandas

class neuralnet(object):

    def __init__(self):
       # Some generic parameters for the learning process
        self.batch_size = 100   
        self.nb_classes = 3 
        self.nb_epoch   = 100    
        self.loadData()

    def loadData(self,trainfile='train.txt',testfile='test.txt',labels_train='labels_train.txt',labels_test='labels_test.txt'):
        '''
   	  Loads data from file into object.
   	  trainfile='train.txt',testfile='test.txt',labels_train='labels_train.txt',labels)test='labels_test.txt'
   	  '''
        self.train = pandas.read_csv(trainfile,header=None)
        self.test = pandas.read_csv(testfile,header=None)
        self.train = self.train.as_matrix()
        self.test = self.test.as_matrix()
        self.train = self.train.transpose() 
        self.test = self.test.transpose() 
        self.labels_train = pandas.read_csv(labels_train,header=None)
        self.labels_test = pandas.read_csv(labels_test,header=None)
        self.labels_train = self.labels_train.as_matrix()
        self.labels_test = self.labels_test.as_matrix()
        self.labels_train = np.resize(self.labels_train, self.labels_train.shape[1])
        self.labels_test = np.resize(self.labels_test, self.labels_test.shape[1])
        self.labels_train = np_utils.to_categorical(self.labels_train,self.nb_classes)
        self.labels_test  = np_utils.to_categorical(self.labels_test,self.nb_classes)

    def buildModel(self):
        self.model = Sequential()
        self.model.add(Dense(80,input_shape=(80,)))
        self.model.add(Activation('relu'))
        self.model.add(Dense(40))
        self.model.add(Activation('relu'))
        self.model.add(Dense(3))
        self.model.add(Activation('softmax'))
        sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
        self.model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=["accuracy"])

    def fit(self):
        self.model.fit(self.train,self.labels_train,
        batch_size=self.batch_size,
        nb_epoch=self.nb_epoch,
        verbose=0,
        validation_data = (self.test,self.labels_test))

    def showResults(self):
        score = self.model.evaluate(self.test,self.labels_test)
        print('Test score:', score[0])
        print('Test accuracy:', score[1])
        return score[1]
