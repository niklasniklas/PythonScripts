"""
Demonstrate the use of layouts to control placement of multiple plots / views /
labels


"""

## Add path to library (just for examples; you do not need this)
#import initExample

from pyqtgraph.Qt import QtGui, QtCore
import pyqtgraph as pg
import numpy as np
import sys
import cv2
from PIL import Image, ImageDraw
import matplotlib.cm as cm

import face.align.detect_face as detect_face
import face.facenet as facenet
from scipy import misc
import tensorflow as tf

pg.setConfigOptions(antialias=True)

iod_data = []
dist_data = []

def updateData():
    global img, data, p6, p6curve, iod_data, i, updateTime, fps, feat_stat, feat_vect, frame, p3, p3curve #, p7, p7curve

    ret, frame = cap.read()
    frame = frame[...,[2,1,0]]

    image = Image.fromarray(frame)
    width, height = image.size
    resize_ratio = 1.0
    #resize_ratio = 1.0 * self.INPUT_SIZE / max(width, height)
    target_size = (int(resize_ratio * width), int(resize_ratio * height))
    res_im = image.convert('RGB').resize(target_size, Image.ANTIALIAS)

    bounding_boxes, lms = detect_face.detect_face(np.array(res_im), minsize, pnet, rnet, onet, threshold, factor)
    if len(bounding_boxes) > 0: #om ansikte(n)
        #det.face_status = 'Face'
        #print('Found face...', end='')
        #ymax, xmax = img_det.shape[0:2]

        # ta fram bästa ansikte, går på conf
        #best_box = np.argmax([bb[4] for bb in bounding_boxes])
        #box = bounding_boxes[best_box]
        box = bounding_boxes[0]
        #lm = lms[best_box]


        xmax, ymax = res_im.size

        x1m, x2m, y1m, y2m = int(box[0]), int(box[2]), int(box[1]), int(box[3])
        x1m = int(np.maximum(x1m, 0))
        y1m = int(np.maximum(y1m, 0))
        x2m = int(np.minimum(x2m, xmax))
        y2m = int(np.minimum(y2m, ymax))

        margin = int((x2m-x1m)*margin_fraction)

        x1 = int(np.maximum(box[0] - margin, 0))
        y1 = int(np.maximum(box[1] - margin, 0))
        x2 = int(np.minimum(box[2] + margin, xmax))
        y2 = int(np.minimum(box[3] + margin, ymax))

        cropped = np.array(res_im)[y1:y2, x1:x2, :]
        aligned = misc.imresize(cropped, (image_size, image_size), interp='bilinear')
        box_face = facenet.prewhiten(aligned)
        feed_dict = { images_placeholder: [box_face], phase_train_placeholder:False }
        feat_vect = sess.run(embeddings, feed_dict=feed_dict).T#[0,:]#.tolist()

        draw = ImageDraw.Draw(res_im)

        draw.rectangle((x1m, y1m, x2m, y2m), outline=(200,200,0))
        draw.point([(lms[0][0], lms[5][0]), (lms[1][0], lms[6][0])], fill=(255, 0 , 0))

        iod = ((lms[0][0]-lms[1][0])**2 + (lms[0][0]-lms[1][0])**2)**0.5
        iod_data.append(iod)
        p6curve.setData(iod_data)


        frame = np.array(res_im)
        frame = np.rot90(frame, -1, (0,1))
        img0.setImage(frame)


        img1.setImage(np.hstack([feat_stat, feat_vect]))

        dist=np.sum((feat_vect-feat_stat)[:,0]**2)**0.5
        #print(dist)
        dist_data.append(dist)

        p3curve.setData( dist_data )
        if len(iod_data)>100:
            del iod_data[0]
            del dist_data[0]


    #img1.setImage(np.random.normal(size=(128,1)))


    QtCore.QTimer.singleShot(1, updateData)

def onClick(event):
    global img1, frame, feat_stat, feat_vect
    #items = view.scene().items(event.scenePos())
    #print('Mouse', items)

    ##ret, frame = cap.read()
    #frame = frame[...,[2,1,0]]
    #frame = np.rot90(frame, -1, (0,1))
    feat_stat = feat_vect.copy()
    img2.setImage(frame)



#-------------FaceNET---------------
minsize = 20 # minimum size of face
threshold = [ 0.6, 0.7, 0.7 ]  # three steps's threshold
factor = 0.709 # scale factor

#-----FaceDetector-----------------
config_find = tf.ConfigProto()
#config_find.gpu_options.allow_growth = True
config_find.gpu_options.per_process_gpu_memory_fraction = 0.4
#config_find = tf.ConfigProto(device_count = {'GPU': 0})

print('Loading face detector...  ', end='')
with tf.Graph().as_default() as g1:
    sess_detect = tf.Session(config=config_find)

    with sess_detect.as_default():
        pnet, rnet, onet = detect_face.create_mtcnn(sess_detect, None)
    print('OK')


#-----Feature vector extraction-----------
config_match = tf.ConfigProto()
#config_match.gpu_options.allow_growth = True
config_match.gpu_options.per_process_gpu_memory_fraction = 0.4
#config_match = tf.ConfigProto(device_count = {'GPU': 0})

model='./face/20170512-110547/'
margin_fraction=0.2
image_size=160

print('Loading face feature extrator...  ')
print('')




app = QtGui.QApplication([])
view = pg.GraphicsView()
l = pg.GraphicsLayout(border=(100,100,100))
view.setCentralItem(l)
view.show()
view.setWindowTitle('pyqtgraph example: GraphicsLayout')
view.resize(800,600)

## Title at top
text = """
This example demonstrates the use of GraphicsLayout to arrange items in a grid.<br>
The items added to the layout must be subclasses of QGraphicsWidget (this includes <br>
PlotItem, ViewBox, LabelItem, and GrphicsLayout itself).
"""
#l.addLabel(text, colspan=5)
l.addLabel('Hejsan1', colspan=1)
l.addLabel('Hejsan1', colspan=1)
l.addLabel('Hejsan1', colspan=1)
#l.addLabel('Hejsan1', colspan=1)

l.nextRow()

## Put vertical label on left side
#l.addLabel('Long Vertical Label', angle=-90, col=1, rowspan=3)

## Add 3 plots into the first row (automatic position)
#p1 = l.addPlot(title="Plot 1", colspan=1)
l.addLabel('Live', angle=-90)
vb0 = l.addViewBox(colspan=1, lockAspect=True)
feat_vect = np.zeros((128,1))
feat_stat = np.zeros((128,1))
img0 = pg.ImageItem(np.hstack([feat_vect, feat_stat]))
vb0.addItem(img0)
#vb0.autoRange()

vb1 = l.addViewBox(colspan=2)#lockAspect=True)

img1 = pg.ImageItem(np.zeros((128,2)))
h=cm.get_cmap('coolwarm')
h_arr= h(range(255))
img1.setLookupTable(h_arr*255)
vb1.addItem(img1)
vb1.scaleBy(y=2)

l.nextRow()
l.addLabel('Capture', angle=-90)
vb2 = l.addViewBox(colspan=1, lockAspect=True)
img2 = pg.ImageItem(np.random.normal(size=(200,200)))
vb2.addItem(img2)
#vb0.autoRange()

p3 = l.addPlot(title="Feature vector difference", colspan=1)
#p3.enableAutoRange('y', False)
#p3.setYRange(-0.1, 0.1, padding=0)
p3curve = p3.plot(pen='y')



#vb3 = l.addViewBox(colspan=2)#lockAspect=True)
#img3 = pg.ImageItem(np.random.normal(size=(128,1)))
#h=cm.get_cmap('coolwarm')
#h_arr= h(range(255))
#img3.setLookupTable(h_arr*255)
#vb3.addItem(img3)
#vb3.scaleBy(y=2)

#l.nextRow()



## Add 2 more plots into the third row (manual position)
#l.nextRow()
#iod_plot = pg.PlotCurveItem()#pen=(i,nPlots*1.3))
#l.addItem(iod_plot)
p6 = l.addPlot(title="Eye distance")
p6curve = p6.plot(pen='y')

#p7 = l.addPlot(title="Eye distance")

#p7.disableAutoRange()
#p7.setYRange(-1, 1, padding=0)
#p7.enableAutoRange('y', False)
#p7curve = p7.plot(pen='y')

#iod_vb = pg.ViewBox()

#iod_plot = pg.PlotDataItem()
#iod_vb.addItem(iod_plot)

#iod_plot = l.addPlot(colspan=1)
#p5 = l.addPlot(colspan=2)

## show some content in the plots
#p1.plot([1,3,2,4,3,5])
#p2.plot([1,3,2,4,3,5])
#iod_plot.plot(np.array([1,3,2,4,3,5]))
#p5.plot([1,3,2,4,3,5])


cap = cv2.VideoCapture(0)



#    h=cm.get_cmap('hot')
#    h_arr= h(range(255))
#    img1.setLookupTable(h_arr*255)
    #print "Plots:", [x for x in items if isinstance(x, pg.PlotItem)]

view.scene().sigMouseClicked.connect(onClick)

#updateData()


with tf.Graph().as_default() as g2:
    with tf.Session(config=config_match) as sess:
        # Load the model
        facenet.load_model(model)

        # Get input and output tensors
        images_placeholder = tf.get_default_graph().get_tensor_by_name("input:0")
        embeddings = tf.get_default_graph().get_tensor_by_name("embeddings:0")
        phase_train_placeholder = tf.get_default_graph().get_tensor_by_name("phase_train:0")
        updateData()
        if __name__ == '__main__':
            if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
                QtGui.QApplication.instance().exec_()
