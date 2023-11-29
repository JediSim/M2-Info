import cv2 as cv
import math
import numpy as np
import sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-g', '--use_gpu', action='store_true', help='Use GPU')
args = vars(ap.parse_args())

# start webcam
cap = cv.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load names of classes and get random colors
classes = open('coco.names').read().strip().split('\n')
np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(classes), 3), dtype='uint8')

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
if args["use_gpu"]:
    net.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA)
else:
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

while True:
    success, img = cap.read()
    # construct a blob from the image
    blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
    r = blob[0, 0, :, :]

    # Analyse l'image en la mettant en entrée dans le réseau.
    net.setInput(blob)
    outputs = net.forward(ln_out)

    r0 = blob[0, 0, :, :]
    r = r0.copy()
    cv.imshow('blob', r)
    # cv.createTrackbar('confidence', 'blob', 50, 101, trackbar2)
    # trackbar2(50)
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



    # img = ResizeWithAspectRatio(img, width=448)
    cv.imshow('window', img)
    # cv.imwrite('output.jpg', img)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()