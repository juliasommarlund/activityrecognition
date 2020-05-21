# Bachelor thesis project "Activity recognition using IoT and Machine Learning" by Julia Sommarlund and Johanna Olnén. 
Project completed at KTH, Royal Institute of Technology Stockholm. 

Data collected using smartphones, 3-axial linear acceleration, using the accelerometer sampled at the frequency of 50 Hz.
The data was labled in lableData.py, and then preprocesses in file data.m (using slideStats.m and a butterworth-filter with a 0.3 cut-off frequency).
A support vector classifier was created in svc.py and trained using the data. 
