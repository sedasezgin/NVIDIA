#!/usr/bin/env python
# coding: utf-8

# ## Working with Amazon Textract
# In this exercise, you will use Amazon Textract to extract text from handwritten movie-review cards.
# 
# ## Task 1: Running the application
# In this task, you use the sample Amazon Textract application for the first time.
# 
# 1. If you didn’t complete the first exercise, install the AWS SDK for Python (Boto3) and extract the exercise source:

# In[1]:


pip install boto3
wget https://aws-tc-largeobjects.s3.amazonaws.com/DEV-AWS-MO-MachineLearning/downloads/exercise-source.zip
unzip exercise-source.zip


# 2. Next, run the application that’s in main.py.

# In[2]:


cd exercise-textract
python3 main.py


# The application will run, process the files in the raw_images directory, and display comma-separated values (CSV) output with placeholder data.
# 
# ## Task 2: Updating the application
# In this task, you complete the missing code in main.py. This task is an open challenge.
# 
# 1. Locate the placeholder in main.py:

# In[3]:


#####
# Replace this code with a solution to populate a dictionary with the results from textract
#####
csv_row["ResponseId"] = "Sample-123"
csv_row["Notes"] = "Sample-I liked the movie."


# 1. Update the two lines of code with the ResponseId and Notes that are returned from the analyze_document API operation.
# 
# 2. Run the application again.
# 
# Do you see the text that was extracted from the images by Amazon Textract?
# 
# If you get stuck, see the working solution in the solution-textract folder.
