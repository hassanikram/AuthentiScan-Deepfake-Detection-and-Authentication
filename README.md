# AUTHENTISCAN: DEEPFAKE DETECTION AND AUTHENTICATION
 
## Project Summary
This project aims to develop a robust deepfake detection system that identifies manipulated video content and provides transparent, interpretable explanations for its decisions. By leveraging advanced deep learning models, the system enhances the trustworthiness and reliability of digital media, addressing the growing challenge posed by deepfake videos. The system utilizes XceptionNet, EfficientNetB4, and EfficientNetAutoAttB4 models, trained and evaluated on the high-quality Celeb-DF v2 dataset, to achieve superior performance in detecting deepfakes.

## Novelty of the Project
The novelty of this project lies in its innovative use of an ensemble of state-of-the-art convolutional neural network (CNN) architectures: XceptionNet, EfficientNetB4, and EfficientNetAutoAttB4. This ensemble approach leverages the unique strengths of each model—XceptionNet's depthwise separable convolutions, EfficientNetB4's efficient compound scaling, and EfficientNetAutoAttB4's automatic attention mechanisms—to capture intricate details and subtle inconsistencies in video frames. This combination, along with the use of the Celeb-DF v2 dataset, ensures high accuracy and robustness, setting new benchmarks in deepfake detection technology.

## Design Diagram 
![image](https://github.com/hassanikram/DeepFakeDetection/assets/45280457/f26e8e33-3f52-466d-9ee3-ecc46d660d74)

•	Celeb-df V2 Dataset: The dataset containing labeled videos for training and testing your models. It contains 590 real videos and 5639 fake videos.
•	Data Preprocessing: During the data preprocessing we first slip the videos into a defined number of frames and detect and extract the facing in the videos and save them as images, split the data into test, train and validation datasets to feed the model.
•	XceptionNet, EfficientNetB4, EfficientNetB4Att: Deep learning models used for video classification. These models are trained on the Celeb-df V2 dataset to detect deepfake videos.
•	Ensemble Model: Combine the outputs of individual models for improved classification performance. This could involve techniques like averaging or weighted voting.
•	Output: Real/Fake: Final output indicating whether the input video is classified as real or fake.

## Results 
The outputs of the three trained models (XceptionNet, EfficientNetB4, and EfficientNetAutoAttB4) were combined using a voting mechanism to improve overall detection accuracy and robustness.

Accuracy:

![image](https://github.com/hassanikram/DeepFakeDetection/assets/45280457/8c166378-fa64-4774-9bef-f080a98b49d1)

## Code Implementation

Download the Celeb-DF v2 Dataset from the following link:
https://drive.google.com/file/d/1iLx76wsbi9itnkxSqz9BVBl4ZvnbIazj/view

Create a new conda environment and install the following libraries:

!pip install efficientnet-pytorch albumentations opencv-python pillow captum timm

Open the notebook using  Jupyter Notebook and run each cell one by one and you not have deepfake detection system. 



