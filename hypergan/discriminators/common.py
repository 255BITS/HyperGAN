import tensorflow as tf
import hyperchamber as hc

def repeating_block(ops, net, config, depth):
   batch_norm = config['layer_regularizer']
   activation = config['activation']
   filter_size_w = 2
   filter_size_h = 2
   filter = [1,filter_size_w,filter_size_h,1]
   stride = [1,filter_size_w,filter_size_h,1]
   for i in range(config.block_repeat_count-1):
     if batch_norm is not None:
         net = batch_norm(int(net.get_shape()[0]), momentum=config.batch_norm_momentum, epsilon=config.batch_norm_epsilon, name=prefix+'_hidden_bn_'+str(i))(net)
     net = conv2d(net, depth, name=prefix+'_hidden_layer_'+str(i), k_w=3, k_h=3, d_h=1, d_w=1, regularizer=None,gain=config.orthogonal_initializer_gain)
     net = activation(net)
     print("[discriminator] hidden layer", net)

   net = conv2d(net, depth, name=prefix+'_expand_layer_last', k_w=3, k_h=3, d_h=1, d_w=1, regularizer=None,gain=config.orthogonal_initializer_gain)
   net = tf.nn.avg_pool(net, ksize=filter, strides=stride, padding='SAME')
   print('[discriminator] layer', net)
   return net

def standard_block(ops, net, config, depth):
   filter_size_w = 2
   filter_size_h = 2
   filter = [1,filter_size_w,filter_size_h,1]
   stride = [1,filter_size_w,filter_size_h,1]

   net = ops.conv2d(net, 3, 3, 1, 1, depth)
   #TODO
   net = tf.nn.avg_pool(net, ksize=filter, strides=stride, padding='SAME')
   print('[discriminator] layer', net)
   return net

def strided_block(ops, net, config, depth):
   net = ops.conv2d(net, 3, 3, 2, 2, depth)
   print('[discriminator] layer', net)
   return net
