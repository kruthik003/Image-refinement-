{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 Courier;}
{\colortbl;\red255\green255\blue255;\red131\green0\blue165;\red245\green245\blue245;\red0\green0\blue0;
\red15\green112\blue1;\red0\green0\blue255;\red86\green65\blue25;\red0\green0\blue109;\red19\green85\blue52;
\red31\green99\blue128;\red144\green1\blue18;}
{\*\expandedcolortbl;;\cssrgb\c59216\c13725\c70588;\cssrgb\c96863\c96863\c96863;\cssrgb\c0\c0\c0;
\cssrgb\c0\c50196\c0;\cssrgb\c0\c0\c100000;\cssrgb\c41569\c32157\c12941;\cssrgb\c0\c6275\c50196;\cssrgb\c6667\c40000\c26667;
\cssrgb\c14510\c46275\c57647;\cssrgb\c63922\c8235\c8235;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 from\cf0 \strokec4  os \cf2 \strokec2 import\cf0 \strokec4  listdir\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  numpy \cf2 \strokec2 import\cf0 \strokec4  asarray,savez_compressed,load,zeros,ones\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  numpy.random \cf2 \strokec2 import\cf0 \strokec4  random,randint\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras.preprocessing.image \cf2 \strokec2 import\cf0 \strokec4  load_img, img_to_array\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras.initializers \cf2 \strokec2 import\cf0 \strokec4  RandomNormal\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras.layers \cf2 \strokec2 import\cf0 \strokec4  Conv2D, Add, Activation, Conv2DTranspose,LeakyReLU, Concatenate\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras.models \cf2 \strokec2 import\cf0 \strokec4  Input,Model\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras.optimizers \cf2 \strokec2 import\cf0 \strokec4  Adam\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Loading the Images\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 load_images\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 path\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 size\cf0 \cb3 \strokec4  = (\cf9 \cb3 \strokec9 256\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 256\cf0 \cb3 \strokec4 )):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   data_list = \cf10 \cb3 \strokec10 list\cf0 \cb3 \strokec4 ()\cb1 \
\cb3   \cf2 \strokec2 for\cf0 \strokec4  filename \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  listdir(path):\cb1 \
\cb3     pixels = load_img(path + filename, target_size = size)\cb1 \
\cb3     pixels = img_to_array(pixels)\cb1 \
\cb3     data_list.append(pixels)\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  asarray(data_list)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 from\cf0 \strokec4  google.colab \cf2 \strokec2 import\cf0 \strokec4  drive\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 drive.mount(\cf11 \cb3 \strokec11 '/content/drive'\cf0 \cb3 \strokec4 )\cb1 \
\cb3 path1 = \cf11 \cb3 \strokec11 '/content/drive/MyDrive/input/Haze/'\cf0 \cb1 \strokec4 \
\cb3 dataA = load_images(path1)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 'Loaded indoor data :'\cf0 \cb3 \strokec4 ,dataA.shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 path2 = \cf11 \cb3 \strokec11 '/content/drive/MyDrive/input/deHaze/'\cf0 \cb1 \strokec4 \
\cb3 dataB = load_images(path2)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 'Loaded Outdoor data :'\cf0 \cb3 \strokec4 ,dataB.shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 filename = \cf11 \cb3 \strokec11 'input.npz'\cf0 \cb1 \strokec4 \
\cb3 savez_compressed(filename,dataA,dataB)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # load and plot the prepared dataset\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 import\cf0 \strokec4  matplotlib.pyplot \cf2 \strokec2 as\cf0 \strokec4  plt\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 data = load(\cf11 \cb3 \strokec11 'input.npz'\cf0 \cb3 \strokec4 )\cb1 \
\cb3 dataA , dataB = data[\cf11 \cb3 \strokec11 'arr_0'\cf0 \cb3 \strokec4 ], data[\cf11 \cb3 \strokec11 'arr_1'\cf0 \cb3 \strokec4 ]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 'Loaded'\cf0 \cb3 \strokec4 ,dataA.shape,dataB.shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # plotting source images\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 n_samples = \cf9 \cb3 \strokec9 3\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  i \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 range\cf0 \cb3 \strokec4 (n_samples):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   plt.rcParams[\cf11 \cb3 \strokec11 'figure.figsize'\cf0 \cb3 \strokec4 ] = (\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.subplot(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,n_samples,\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 +i)\cb1 \
\cb3   plt.axis(\cf11 \cb3 \strokec11 'off'\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.title(\cf11 \cb3 \strokec11 'Distorted_images'\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.imshow(dataA[i].astype(\cf11 \cb3 \strokec11 'uint8'\cf0 \cb3 \strokec4 ))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # plotting target images\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 for\cf0 \strokec4  i \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 range\cf0 \cb3 \strokec4 (n_samples):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   plt.rcParams[\cf11 \cb3 \strokec11 'figure.figsize'\cf0 \cb3 \strokec4 ] = (\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.subplot(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,n_samples,n_samples+\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 +i)\cb1 \
\cb3   plt.axis(\cf11 \cb3 \strokec11 'off'\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.title(\cf11 \cb3 \strokec11 'Refined_images'\cf0 \cb3 \strokec4 )\cb1 \
\cb3   plt.imshow(dataA[i].astype(\cf11 \cb3 \strokec11 'uint8'\cf0 \cb3 \strokec4 ))\cb1 \
\cb3 plt.show\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 !\cf0 \cb3 \strokec4 pip install git+https://www.github.com/keras-team/keras-contrib.git\cb1 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 from\cf0 \strokec4  keras_contrib.layers.normalization.instancenormalization \cf2 \strokec2 import\cf0 \strokec4  InstanceNormalization\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 layer = InstanceNormalization(axis = \cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Cycle GAN Architecture\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # Discriminator model Architecture\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 discriminator\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 image_shape\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \cb3 \strokec5 # weight initialization\cf0 \cb1 \strokec4 \
\cb3     init = RandomNormal(stddev=\cf9 \cb3 \strokec9 0.02\cf0 \cb3 \strokec4 ,seed = \cf9 \cb3 \strokec9 42\cf0 \cb3 \strokec4 )\cb1 \
\cb3     \cf5 \cb3 \strokec5 # source image input\cf0 \cb1 \strokec4 \
\cb3     in_image = Input(shape=image_shape)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # C64\cf0 \cb1 \strokec4 \
\cb3     d = Conv2D(\cf9 \cb3 \strokec9 64\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(in_image)\cb1 \
\cb3     d = LeakyReLU(alpha=\cf9 \cb3 \strokec9 0.2\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # C128\cf0 \cb1 \strokec4 \
\cb3     d = Conv2D(\cf9 \cb3 \strokec9 128\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(d)\cb1 \
\cb3     d = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     d = LeakyReLU(alpha=\cf9 \cb3 \strokec9 0.2\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # C256\cf0 \cb1 \strokec4 \
\cb3     d = Conv2D(\cf9 \cb3 \strokec9 256\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(d)\cb1 \
\cb3     d = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     d = LeakyReLU(alpha=\cf9 \cb3 \strokec9 0.2\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # C512\cf0 \cb1 \strokec4 \
\cb3     d = Conv2D(\cf9 \cb3 \strokec9 512\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(d)\cb1 \
\cb3     d = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     d = LeakyReLU(alpha=\cf9 \cb3 \strokec9 0.2\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # second last output layer\cf0 \cb1 \strokec4 \
\cb3     d = Conv2D(\cf9 \cb3 \strokec9 512\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(d)\cb1 \
\cb3     d = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     d = LeakyReLU(alpha=\cf9 \cb3 \strokec9 0.2\cf0 \cb3 \strokec4 )(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # patch output\cf0 \cb1 \strokec4 \
\cb3     patch_out = Conv2D(\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 4\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(d)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # define model\cf0 \cb1 \strokec4 \
\cb3     model = Model(in_image, patch_out)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # compile model\cf0 \cb1 \strokec4 \
\cb3     model.\cf7 \cb3 \strokec7 compile\cf0 \cb3 \strokec4 (loss=\cf11 \cb3 \strokec11 'mse'\cf0 \cb3 \strokec4 , optimizer=Adam(learning_rate=\cf9 \cb3 \strokec9 0.0002\cf0 \cb3 \strokec4 , beta_1=\cf9 \cb3 \strokec9 0.5\cf0 \cb3 \strokec4 ), loss_weights=[\cf9 \cb3 \strokec9 0.5\cf0 \cb3 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  model\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Generator (Resnet block)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 resnet_block\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 n_filters\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 input_layer\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   init = RandomNormal(stddev = \cf9 \cb3 \strokec9 0.02\cf0 \cb3 \strokec4 ,seed = \cf9 \cb3 \strokec9 42\cf0 \cb3 \strokec4 )\cb1 \
\cb3   \cf5 \cb3 \strokec5 # CNN 1\cf0 \cb1 \strokec4 \
\cb3   g = Conv2D(n_filters,(\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ),padding = \cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 ,kernel_initializer = init)(input_layer)\cb1 \
\cb3   g = InstanceNormalization(axis = \cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3   g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3   \cf5 \cb3 \strokec5 # CNN 2\cf0 \cb1 \strokec4 \
\cb3   g = Conv2D(n_filters,(\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ),padding = \cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 ,kernel_initializer = init)(g)\cb1 \
\cb3   g = InstanceNormalization(axis = \cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3   g = Add()([g,input_layer])\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  g\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # define the standalone generator model\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 generator\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 image_shape\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 n_resnet\cf0 \cb3 \strokec4 =\cf9 \cb3 \strokec9 9\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \cb3 \strokec5 # weight initialization\cf0 \cb1 \strokec4 \
\cb3     init = RandomNormal(stddev=\cf9 \cb3 \strokec9 0.02\cf0 \cb3 \strokec4 ,seed = \cf9 \cb3 \strokec9 42\cf0 \cb3 \strokec4 )\cb1 \
\cb3     \cf5 \cb3 \strokec5 # image input\cf0 \cb1 \strokec4 \
\cb3     in_image = Input(shape=image_shape)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # c64\cf0 \cb1 \strokec4 \
\cb3     g = Conv2D(\cf9 \cb3 \strokec9 64\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 7\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 7\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(in_image)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # d128-downsample\cf0 \cb1 \strokec4 \
\cb3     g = Conv2D(\cf9 \cb3 \strokec9 128\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(g)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # d256\cf0 \cb1 \strokec4 \
\cb3     g = Conv2D(\cf9 \cb3 \strokec9 256\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(g)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # R256-ResNet\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  _ \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 range\cf0 \cb3 \strokec4 (n_resnet):\cb1 \
\cb3         g = resnet_block(\cf9 \cb3 \strokec9 256\cf0 \cb3 \strokec4 , g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # u128-upsample\cf0 \cb1 \strokec4 \
\cb3     g = Conv2DTranspose(\cf9 \cb3 \strokec9 128\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(g)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # u64\cf0 \cb1 \strokec4 \
\cb3     g = Conv2DTranspose(\cf9 \cb3 \strokec9 64\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 ), strides=(\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 2\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(g)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     g = Activation(\cf11 \cb3 \strokec11 'relu'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # c3\cf0 \cb1 \strokec4 \
\cb3     g = Conv2D(\cf9 \cb3 \strokec9 3\cf0 \cb3 \strokec4 , (\cf9 \cb3 \strokec9 7\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 7\cf0 \cb3 \strokec4 ), padding=\cf11 \cb3 \strokec11 'same'\cf0 \cb3 \strokec4 , kernel_initializer=init)(g)\cb1 \
\cb3     g = InstanceNormalization(axis=\cf9 \cb3 \strokec9 -1\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     out_image = Activation(\cf11 \cb3 \strokec11 'tanh'\cf0 \cb3 \strokec4 )(g)\cb1 \
\cb3     \cf5 \cb3 \strokec5 # define model\cf0 \cb1 \strokec4 \
\cb3     model = Model(in_image, out_image)\cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  model\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Composite model that updates the generators based on the losses\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 composite_model\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 g_model_1\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 d_model\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 g_model_2\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 image_shape\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   g_model_1.trainable = \cf6 \cb3 \strokec6 True\cf0 \cb1 \strokec4 \
\cb3   d_model.trainable = \cf6 \cb3 \strokec6 False\cf0 \cb1 \strokec4 \
\cb3   g_model_trainable = \cf6 \cb3 \strokec6 False\cf0 \cb1 \strokec4 \
\cb3   input_gen = Input(shape = image_shape)\cb1 \
\cb3   gen1_out = g_model_1(input_gen)\cb1 \
\cb3   output_d = d_model(gen1_out)\cb1 \
\cb3   input_id = Input(shape = image_shape)\cb1 \
\cb3   output_id = g_model_1(input_id)\cb1 \
\cb3   output_f = g_model_2(gen1_out)\cb1 \
\cb3   gen2_out = g_model_2(input_id)\cb1 \
\cb3   output_b = g_model_1(gen2_out)\cb1 \
\cb3   model = Model([input_gen,input_id],[output_d,output_id,output_f,output_b])\cb1 \
\cb3   opt = Adam(learning_rate = \cf9 \cb3 \strokec9 0.0002\cf0 \cb3 \strokec4 , beta_1 = \cf9 \cb3 \strokec9 0.5\cf0 \cb3 \strokec4 )\cb1 \
\cb3   model.\cf7 \cb3 \strokec7 compile\cf0 \cb3 \strokec4 (loss=[\cf11 \cb3 \strokec11 'mse'\cf0 \cb3 \strokec4 ,\cf11 \cb3 \strokec11 'mae'\cf0 \cb3 \strokec4 ,\cf11 \cb3 \strokec11 'mae'\cf0 \cb3 \strokec4 ,\cf11 \cb3 \strokec11 'mae'\cf0 \cb3 \strokec4 ],loss_weights=[\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 5\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 10\cf0 \cb3 \strokec4 ],optimizer = opt)\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  model\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 load_real_samples\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 filename\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   data = load(filename)\cb1 \
\cb3   x1,x2 = data[\cf11 \cb3 \strokec11 'arr_0'\cf0 \cb3 \strokec4 ],data[\cf11 \cb3 \strokec11 'arr_1'\cf0 \cb3 \strokec4 ]\cb1 \
\cb3   x1 = (x1 - \cf9 \cb3 \strokec9 127.5\cf0 \cb3 \strokec4 )/\cf9 \cb3 \strokec9 127.5\cf0 \cb1 \strokec4 \
\cb3   x2 = (x2 - \cf9 \cb3 \strokec9 127.5\cf0 \cb3 \strokec4 )/\cf9 \cb3 \strokec9 127.5\cf0 \cb1 \strokec4 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  [x1,x2]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 generate_real_samples\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 dataset\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 n_samples\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 patch_shape\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   ix = randint(\cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 ,dataset.shape[\cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 ],n_samples)\cb1 \
\cb3   x = dataset[ix]\cb1 \
\cb3   y = ones((n_samples,patch_shape,patch_shape,\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ))\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  x,y\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 generate_fake_samples\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 g_model\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 dataset\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 patch_shape\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   x = g_model.predict(dataset)\cb1 \
\cb3   y = zeros((\cf7 \cb3 \strokec7 len\cf0 \cb3 \strokec4 (x),patch_shape,patch_shape,\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ))\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  x,y\cb1 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 save_models\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 step\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 g_model_AtoB\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 g_model_BtoA\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   f1 = \cf11 \cb3 \strokec11 'g_model_AtoB_%06d.h5'\cf0 \cb3 \strokec4  %(step+\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 )\cb1 \
\cb3   g_model_AtoB.save(f1)\cb1 \
\cb3   f2 = \cf11 \cb3 \strokec11 'g_model_BtoA_%06d.h5'\cf0 \cb3 \strokec4  %(step+\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 )\cb1 \
\cb3   g_model_BtoA.save(f2)\cb1 \
\cb3   \cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 '>Saved: %s and %s'\cf0 \cb3 \strokec4 %(f1,f2))\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # update image pool for fake images\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 update_image_pool\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 pool\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 images\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 max_size\cf0 \cb3 \strokec4  = \cf9 \cb3 \strokec9 50\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   selected = \cf10 \cb3 \strokec10 list\cf0 \cb3 \strokec4 ()\cb1 \
\cb3   \cf2 \strokec2 for\cf0 \strokec4  image \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  images:\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  \cf7 \cb3 \strokec7 len\cf0 \cb3 \strokec4 (pool) < max_size:\cb1 \
\cb3       pool.append(image)\cb1 \
\cb3       selected.append(image)\cb1 \
\cb3     \cf2 \strokec2 elif\cf0 \strokec4  random()<\cf9 \cb3 \strokec9 0.5\cf0 \cb3 \strokec4 :\cb1 \
\cb3       selected.append(image)\cb1 \
\cb3     \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3       ix = randint(\cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 ,\cf7 \cb3 \strokec7 len\cf0 \cb3 \strokec4 (pool))\cb1 \
\cb3       selected.append(pool[ix])\cb1 \
\cb3       pool[ix] = image\cb1 \
\cb3   \cf2 \strokec2 return\cf0 \strokec4  asarray(selected)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Train Cycle-Gan models\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf6 \cb3 \strokec6 def\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 train\cf0 \cb3 \strokec4 (\cf8 \cb3 \strokec8 d_model_A\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 d_model_B\cf0 \cb3 \strokec4 , \cf8 \cb3 \strokec8 g_model_AtoB\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 g_model_BtoA\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 c_model_AtoB\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 c_model_BtoA\cf0 \cb3 \strokec4 ,\cf8 \cb3 \strokec8 dataset\cf0 \cb3 \strokec4 ):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3   n_epochs,n_batch = \cf9 \cb3 \strokec9 40\cf0 \cb3 \strokec4 ,\cf9 \cb3 \strokec9 1\cf0 \cb1 \strokec4 \
\cb3   n_patch =  d_model_A.output_shape[\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ]\cb1 \
\cb3   trainA,trainB = dataset\cb1 \
\cb3   poolA,poolB = \cf10 \cb3 \strokec10 list\cf0 \cb3 \strokec4 (),\cf10 \cb3 \strokec10 list\cf0 \cb3 \strokec4 ()\cb1 \
\cb3   bat_per_epo = \cf10 \cb3 \strokec10 int\cf0 \cb3 \strokec4 (\cf7 \cb3 \strokec7 len\cf0 \cb3 \strokec4 (trainA)/n_batch)\cb1 \
\cb3   n_steps = bat_per_epo*n_epochs\cb1 \
\cb3   \cf2 \strokec2 for\cf0 \strokec4  i \cf6 \cb3 \strokec6 in\cf0 \cb3 \strokec4  \cf7 \cb3 \strokec7 range\cf0 \cb3 \strokec4 (n_steps):\cb1 \
\cb3     x_realA,y_realA = generate_real_samples(trainA,n_batch,n_patch)\cb1 \
\cb3     x_realB,y_realB = generate_real_samples(trainB,n_batch,n_patch)\cb1 \
\cb3     x_fakeA,y_fakeA = generate_fake_samples(g_model_BtoA,x_realB,n_patch)\cb1 \
\cb3     x_fakeB,y_fakeB = generate_fake_samples(g_model_AtoB,x_realA,n_patch)\cb1 \
\cb3     x_fakeA = update_image_pool(poolA,x_fakeA)\cb1 \
\cb3     x_fakeB = update_image_pool(poolB,x_fakeB)\cb1 \
\cb3     g_loss2,_,_,_,_ =c_model_BtoA.train_on_batch([x_realB,x_realA],[y_realA,x_realA,x_realB,x_realA])\cb1 \
\cb3     dA_loss1 = d_model_A.train_on_batch(x_realA,y_realA)\cb1 \
\cb3     dA_loss2 = d_model_A.train_on_batch(x_fakeA,y_fakeA)\cb1 \
\cb3     g_loss1,_,_,_,_ = c_model_AtoB.train_on_batch([x_realA,x_realB],[y_realB,x_realB,x_realA,x_realB])\cb1 \
\cb3     dB_loss1 = d_model_B.train_on_batch(x_realB,y_realB)\cb1 \
\cb3     dB_loss2 = d_model_B.train_on_batch(x_fakeB,y_fakeB)\cb1 \
\cb3     \cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 '>%d, dA[%.3f,%.3f] dB[%.3f,%.3f] g[%.3f,%.3f]'\cf0 \cb3 \strokec4  % (i+\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 , dA_loss1,dA_loss2, dB_loss1,dB_loss2, g_loss1,g_loss2))\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  (i+\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ) % (bat_per_epo * \cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ) == \cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 :\cb1 \
\cb3     \cf5 \cb3 \strokec5 # save the models\cf0 \cb1 \strokec4 \
\cb3       save_models(i, g_model_AtoB, g_model_BtoA)\cb1 \
\cb3 dataset = load_real_samples(\cf11 \cb3 \strokec11 'input.npz'\cf0 \cb3 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf7 \cb3 \strokec7 print\cf0 \cb3 \strokec4 (\cf11 \cb3 \strokec11 'Loaded'\cf0 \cb3 \strokec4 , dataset[\cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 ].shape, dataset[\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 ].shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # define input shape based on the loaded dataset\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 image_shape = dataset[\cf9 \cb3 \strokec9 0\cf0 \cb3 \strokec4 ].shape[\cf9 \cb3 \strokec9 1\cf0 \cb3 \strokec4 :]\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # generator: A -> B\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 g_model_AtoB = generator(image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # generator: B -> A\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 g_model_BtoA = generator(image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # discriminator: A -> [real/fake]\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 d_model_A = discriminator(image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # discriminator: B -> [real/fake]\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 d_model_B = discriminator(image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # composite: A -> B -> [real/fake, A]\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 c_model_AtoB = composite_model(g_model_AtoB, d_model_B, g_model_BtoA, image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # composite: B -> A -> [real/fake, B]\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 c_model_BtoA = composite_model(g_model_BtoA, d_model_A, g_model_AtoB, image_shape)\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # train models\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 train(d_model_A, d_model_B, g_model_AtoB, g_model_BtoA, c_model_AtoB, c_model_BtoA, dataset)\cb1 \
}