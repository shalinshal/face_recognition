# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 19:49:15 2018

@author: Shalin
"""
#%%
#OpenCV module
import cv2
#os module for reading training data directories and paths
import os
#numpy to convert python lists to numpy arrays as it is needed by OpenCV face recognizers
import numpy as np

#function to detect face using OpenCV
def detect_face(img):
#convert the test image to gray scale as opencv face detector expects gray images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#load OpenCV face detector, I am using LBP which is fast
#there is also a more accurate but slow: Haar classifier
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')

#let's detect multiscale images(some images may be closer to camera than others)
#result is a list of faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

#if no faces are detected then return original img
    if (len(faces) == 0):
        return None, None

#under the assumption that there will be only one face,
#extract the face area
    x, y, w, h = faces[0]

#return only the face part of the image
    return gray[y:y+w, x:x+h], faces[0]

#this function will read all persons' training images, detect face from each image
#and will return two lists of exactly same size, one list 
#of faces and another list of labels for each face
def prepare_training_data(data_folder_path):
 
#------STEP-1--------
#get the directories (one directory for each subject) in data folder
    dirs = os.listdir(data_folder_path)
 
#list to hold all subject faces
    faces = []
#list to hold labels for all subjects
    labels = []

#let's go through each directory and read images within it
    for dir_name in dirs:
#our subject directories start with letter 's' so
#ignore any non-relevant directories if any
        if not dir_name.startswith("s"):
            continue;
 
#------STEP-2--------
#ext    ract label number of subject from dir_name
#format of dir name = slabel
#, so removing letter 's' from dir_name will give us label
        label = int(dir_name.replace("s", ""))
 
#build path of directory containing images for current subject subject
#sample subject_dir_path = "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name
 
#get the images names that are inside the given subject directory
        subject_images_names = os.listdir(subject_dir_path)
 
#------STEP-3--------
#go through each image name, read image, 
#detect face and add face to list of faces
        for image_name in subject_images_names: 
#build image path
#sample image path = training-data/s1/1.pgm
            image_path = subject_dir_path + "/" + image_name

#read image
            image = cv2.imread(image_path)
 
##display an image window to show the image 
#            cv2.imshow("Training on image...", image)
#            cv2.waitKey(100)
 
#detect face
            face, rect = detect_face(image)
 
#------STEP-4--------
#for the purpose of this tutorial
#we will ignore faces that are not detected
            if face is not None:
#add face to list of faces
                faces.append(face)
#add label for this face
                labels.append(label)
 
                cv2.destroyAllWindows()
                cv2.waitKey(1)
                cv2.destroyAllWindows()
 
    return faces, labels


#function to draw rectangle on image 
#according to given (x, y) coordinates and 
#given width and heigh
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
#function to draw text on give image starting from
#passed (x, y) coordinates. 
def draw_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)

#%%
#print("Predicting images...")
#
##load test images
#test_img1 = cv2.imread("dataset/test_data/s1/jayesh.jpg")
#test_img2 = cv2.imread("dataset/test_data/s2/kanan.jpg")
#test_img3 = cv2.imread("dataset/test_data/s3/shalin.jpg")
#test_img4 = cv2.imread("dataset/test_data/s4/vandana.jpg")
#
##perform a prediction
#predicted_img1 = predict(test_img1)
#
#predicted_img2 = predict(test_img2)
#predicted_img3 = predict(test_img3)
#predicted_img4 = predict(test_img4)
#print("Prediction complete")

##display both images
#cv2.imshow(subjects[1], predicted_img1)
#cv2.imshow(subjects[2], predicted_img2)
#cv2.imshow(subjects[3], predicted_img3)
#cv2.imshow(subjects[4], predicted_img4)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
    
#%%
def main():
#let's first prepare our training data
#data will be in two lists of same size
#one list will contain all the faces
#and the other list will contain respective labels for each face
    print("Preparing data...")
    faces, labels = prepare_training_data("dataset/training_data")
    print("Data prepared")

#print total faces and labels
    print("Total faces: ", len(faces))
    print("Total labels: ", len(labels))

#create our LBPH face recognizer 
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

#train our face recognizer of our training faces
    face_recognizer.train(faces, np.array(labels))
    return face_recognizer