# Analysis on Secure Triplet Loss

Bora Jeong, Sunpill Kim, Seunghun Paik and Jae Hong Seo

*Department of Mathematics & Research Institute for Natural Sciences, Hanyang University, Seoul 04763, Republic of Korea*

Contact: jbr915@hanyang.ac.kr





# Abstract

Major improvements in biometric authentication have been made in recent years due to the advancements in deep learning. Through the use of a deep learning-based facial recognition model with metric learning, more discriminative facial features can be extracted from faces. A large threat to user privacy could result from the disclosure of more discriminatory feature vectors related to biometric information. Among many biometric template protection (BTP) schemes, there have been studies that have attempted to protect feature vectors from the learning process of facial recognition models, while considering security requirements. One of them is secure triplet loss (STL) based BTP, which is an end-to-end BTP scheme using deep learning model that merges an additional layer on a pre-trained facial recognition model. STL-based BTP takes a pre-defined key and an image as inputs, and it is designed to become closer only when both the identity and the key are matched simultaneously. In this paper, we propose an efficient impersonation attack algorithm on STL-based BTP and our impersonation attack algorithm is conducted in a black-box setting using only the similarity scores between a target template and the template from the queried image and key pair. We have succeed in the impersonation attack using approximately 329.59 and 256.57 queries for the two types of black-box target systems. Furthermore, we conduct an analysis of our impersonation attack algorithm along with the implementation code.





# Setup

1. Prepare target models: https://github.com/jtrpinto

                            face_prepare_ytfdb.py
                            face_train_triplet_model.py
                            face_train_securetl_model.py
                            face_train_securetl_linkability_model.py
                            face_test_triplet_model.py
                            face_test_secure_model.py (get the predefined threshold)
   We recommend saving the file name of the trained model as STL_C or STL_L.                  

2. Open *AttackSTL.ipynb* file and follow the steps.





# Reference

[1] Pinto, J. R., Correia, M. V., & Cardoso, J. S. (2020). Secure triplet loss: Achieving cancelability and non-linkability in end-to-end deep biometrics. IEEE Transactions on Biometrics, Behavior, and Identity Science, 3(2), 180-189.

[2] B. Jeong, S. Kim, S. Paik and J. H. Seo, "Attack on Secure Triplet Loss," in IEEE Access, 2022, doi: 10.1109/ACCESS.2022.3225430.
