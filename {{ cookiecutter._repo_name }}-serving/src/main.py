# import tensorflow as tf
# from tensorflow.examples.tutorials.mnist import input_data
# import numpy as np

class TrainedModel:
    
    def __init__(self, model_dir):
        # self.graph = tf.Graph()
        # self.sess = tf.Session(graph=self.graph)
        # tf.saved_model.loader.load(self.sess, [tf.saved_model.tag_constants.SERVING], model_dir)
        # self.mnist = input_data.read_data_sets("/tmp/data/", one_hot=True)
        pass

    def predict(self, request):
        # num = int(request.form['num'])
        # img = self.mnist.test.images[num]
        # expected_result = self.mnist.test.labels[num]
        # x = self.graph.get_tensor_by_name('x-input:0')
        # y = self.graph.get_tensor_by_name('Softmax:0')
        # classification = self.sess.run(y, feed_dict={x: [img]})
        # print("classification prob:", classification)
        # classification = tf.argmax(classification, 1)
        # return 'predicted result: ' + str(classification) + "( expected result = " + str(np.argmax(expected_result))
        pass

    def health(self):
        return '200 OK'
        