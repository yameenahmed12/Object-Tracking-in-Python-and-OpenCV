# Object-Tracking-in-Python-and-OpenCV
**Simple Introduction to Object Tracking**

**Project Overview**

This project is a demo for a Highway Traffic Monitoring System which uses computer vision functions from the library of OpenCV which helps in the detection and tracking of parametrically-defined objects in the given 'traffic.mp4' file which is a surveillance footage of a typical highway with trucks and other vehicles alike. If refined and trained to an extensive degree, this system can be used in traffic management and surveillance systems. 

**Core Features**

- Vehicle Detection: Relies on the Background Subtraction method from OpenCV(MOG2) which is key in differentiating moving vehicles from the static background (this can of course be modified if the .mp4 file in question is non-statc)

- Vehicle Tracking: Uses a custom tracking alogrithim from the tracking file to utulize Euclidean distance for the sake of tracking vehicles across different frames

- Shadow Detection: Allows freedom in enabling or disabling shadow detection for object segmentation

  **Resources Used**
  - PyCharm
  - OpenCV Library
  - NumPy Library
 
  
