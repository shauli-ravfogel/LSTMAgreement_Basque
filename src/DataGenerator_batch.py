import random

"""
an abstract class for creating training example, based on the training corpus.
derived class override create_example method according to the requierments. 
"""

class DataGenerator(object):

 def __init__(self, data_dicts, voc, D2I, A2I, E2I):
   self.data_dicts = data_dicts
   self.voc = voc
   self.W2I = dict((char, index) for index, char in enumerate(sorted(self.voc)))
   self.I2W = dict((index, char) for index, char in enumerate(sorted(self.voc)))

   self.E2I = E2I
   self.A2I = A2I
   self.D2I = D2I

   n = len(self.data_dicts)
   #random.shuffle(self.data_dicts)
  
   self.train = self.data_dicts[:int(0.35*n)]
   self.test  = self.data_dicts[int(0.75*n):int(0.85*n)]


 def get_train_size(self):
	return len(self.train)

 def get_dev_size(self):
	return len(self.test)

 def create_example(self, data_sample):
 	raise NotImplementedError


 def generate(self, is_training):

   """
 	a template method for generating a training example. the abstract method create_example
 	is implemented in the drived class, according to the requierments in each part.

	is_training - a boolean flag indicating training/prediction mode.
   """

   i = 0

   while True: 
      i+=1
      if i%3000 == 0: 
	random.shuffle(self.train)
	random.shuffle(self.test)
	pass

      batch_size = 32
      batch = []

      for k in range(batch_size):
      	if is_training:
      		i = random.choice(range(1, len(self.train)-1))
		source = self.train
      	else:
		i = random.choice(range(1, len(self.test)-1))
		source = self.test

     	data, prev_data, next_data = source[i], source[i-1], source[i+1]

     	x_encoded, y_encoded = self.create_example(data, prev_data, next_data)
	batch.append((x_encoded, y_encoded, data))

      yield batch

