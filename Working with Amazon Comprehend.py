#!/usr/bin/env python
# coding: utf-8

# ## Working with Amazon Comprehend
# In this exercise, you will use Amazon Comprehend to process the movie-feedback comma-separated values (CSV) file to retrieve the sentiment for each movie review.
# 
# ## Task 1: Running the application
# In this task, you use the sample Amazon Comprehend application for the first time.
# 
# 1. If you didn’t complete the first exercise, install the AWS SDK for Python (Boto3) and extract the exercise source:

# In[1]:


pip install boto3
wget https://aws-tc-largeobjects.s3.amazonaws.com/DEV-AWS-MO-MachineLearning/downloads/exercise-source.zip
unzip exercise-source.zip


# 2. Next, run the application that’s in main.py.

# In[2]:


cd exercise-comprehend
python3 main.py


# The application exits with two Missing required parameter in input errors.
# 
# ## Task 2: Updating the application.
# In this task, you complete the missing code in main.py. This task is an open challenge.
# 
# 1. Read the documentation for batch_detect_sentiment.
# 
# 2. Update the call to batch_detect_sentiment with all the required parameters.
# 
# 3. Run the application again.
# 
# Do you see the sentiment results that were returned from Amazon Textract?
# 
# If you get stuck, see the working solution in the solution-comprehend folder.
