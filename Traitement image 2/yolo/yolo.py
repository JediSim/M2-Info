import cv2 as cv
import numpy as np
import time
import sys

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv.resize(image, dim, interpolation=inter)

# charge l'image 'horse' ou une image donnée sur la ligne de commande
filename = 'horse.jpg'
if ( len( sys.argv ) > 1 ):
    filename = sys.argv[ 1 ]
img = cv.imread( filename )
img = ResizeWithAspectRatio(img, width=448)
cv.imshow('window',  img)
cv.waitKey(1)

# Load names of classes and get random colors
classes = open('coco.names').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)

# determine the output layer
ln = net.getLayerNames()
print(ln)
Out = [i for i in net.getUnconnectedOutLayers()]
ln_out = []
for j in range( len( Out ) ):
    print( Out[ j ] - 1, ' ', ln[ Out[ j ] - 1 ] )
    ln_out.append( ln[ Out[ j ] - 1 ] );
print( ln_out )

# construct a blob from the image
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]
# si vous voulez l'afficher.
cv.imshow('blob', r )
cv.waitKey(1)

# Analyse l'image en la mettant en entrée dans le réseau.
net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln_out)
t = time.time()
print('time=', t-t0)

print(len(outputs))
for out in outputs:
    print(out.shape)


def trackbar2(x):
    confidence = x/100
    r = r0.copy()
    for output in np.vstack(outputs):
        if output[4] > confidence:
            x, y, w, h = output[:4]
            p0 = int((x-w/2)*416), int((y-h/2)*416)
            p1 = int((x+w/2)*416), int((y+h/2)*416)
            cv.rectangle(r, p0, p1, 1, 1)
    rdisplay = r.copy()
    text = f'Bbox confidence={confidence}'
    # displayText( rdisplay, text, (20, 20), scale=1.0 )
    cv.imshow('blob', rdisplay)
    # cv.displayOverlay('blob', text)

r0 = blob[0, 0, :, :]
r = r0.copy()
cv.imshow('blob', r)
cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)
trackbar2(50)
boxes = []
confidences = []
classIDs = []
h, w = img.shape[:2]

for output in outputs:
    for detection in output:
        scores = detection[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > 0.5:
            box = detection[:4] * np.array([w, h, w, h])
            (centerX, centerY, width, height) = box.astype("int")
            x = int(centerX - (width / 2))
            y = int(centerY - (height / 2))
            box = [x, y, int(width), int(height)]
            boxes.append(box)
            confidences.append(float(confidence))
            classIDs.append(classID)

indices = cv.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
if len(indices) > 0:
    for i in indices.flatten():
        (x, y) = (boxes[i][0], boxes[i][1])
        (w, h) = (boxes[i][2], boxes[i][3])
        color = [int(c) for c in colors[classIDs[i]]]
        cv.rectangle(img, (x, y), (x + w, y + h), color, 2)
        text = "{}: {:.4f}".format(classes[classIDs[i]], confidences[i])
        cv.putText(img, text, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)



img = ResizeWithAspectRatio(img, width=448)
cv.imshow('window', img)
cv.imwrite('output.jpg', img)
cv.waitKey(0)
cv.destroyAllWindows()