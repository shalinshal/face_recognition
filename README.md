# face_recognition
1. dataset - training_data
This folder contains one subfolder for every individual, named with the format: sLabel (e.g. s1, s2) where the label is the integer assigned to that person. For example, the subfolder called s1 means that it contains images for person 1. And all the images within one folder are named numerically. Also all the images must be 'jpg' not even 'JPG'.

2. sds_face_recognition
This file contains the function to train the model on the images by calling sds_face_recognition.main() function. 
This function returns the trained model.

3. sds_face_detection
This file contains function detect_face which detect faces in a live feed from the webcam, and also tries to recognize the face using the model returned from sds_face_recognition.
The output of this a video with a green box across the region of face and the name of the person detected on the top left of the box.
Running this file initially will train the model and then loop indefinitely detecting and recognizing faces.
Press 'q' to quit the program anytime.

For more details visit : https://www.superdatascience.com/opencv-face-recognition/