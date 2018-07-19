from cnn_model import *
import sys
import tensorflow as tf

tf.app.flags.DEFINE_integer(
    'batch_size',
    64,
    '批次大小'
)

tf.app.flags.DEFINE_integer(
    'hidden_size',
    1024,
    '隐层大小'
)

tf.app.flags.DEFINE_integer(
    'EPOCH',
    201,
    '训练轮次'
)
tf.app.flags.DEFINE_float(
    'learning_rate',
    1e-4,
    '学习率'
)
tf.app.flags.DEFINE_float(
    'regular_coef',
    5e-4,
    '正则项系数'
)
tf.app.flags.DEFINE_string(
    'model_dir',
    'C:\static\model',
    '模型保存的目录'
)
tf.app.flags.DEFINE_string(
    'model_name',
    'model',
    '模型保存的名称'
)
FLAGS = tf.app.flags.FLAGS

def main(_):
    my_model = model(batch_size=FLAGS.batch_size, hidden_size=FLAGS.hidden_size)
    my_model.train_model(EPOCH=FLAGS.EPOCH, learning_rate=FLAGS.learning_rate,
                         regular_coef=FLAGS.regular_coef, model_dir=FLAGS.model_dir, model_name=FLAGS.model_name)
    
if __name__ == '__main__':
    np.random.seed(0)
    tf.set_random_seed(0)
    tf.app.run()
