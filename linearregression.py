import tensorflow as tf

#neuron: y=W*x
x = tf.constant(1.0, name='input')
w = tf.Variable(0.8, name='weight')
y = tf.mul(w, x, name='output')

#label
y_ = tf.constant(0.0, name='correct_value')

#learning
loss = tf.pow(y - y_, 2, name='loss')
train_step = tf.train.GradientDescentOptimizer(0.025).minimize(loss)

#run the program
sess = tf.Session()
sess.run(tf.global_variables_initializer())

for i in range(100):
	#execute
    sess.run(train_step)
    print "Weight = ", sess.run(w), "\tLoss =", sess.run(loss)
sess.close()