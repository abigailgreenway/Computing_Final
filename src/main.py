# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 09:33:06 2024

@author: Abi
"""
"Intro to Computing Final Project" # ==============================
# Project goals: Use concepts introduced in the class 
# 1. Organize the program into folders
# 2. Section the code into modules for ease of use and debugging
# 3. Batch process files, don't read / process individually
# 4. Optimize, lint, notate (comment), and document (readme) the program

# I want this program to help me quickly understand some things about my
#   cohort's data from SPSS without having to use the program Prism. 

# We need similar behavioral histories (lever presses, infusions) btwn groups
    # to say our manipulation did something, not the rats' inclinations.
# We do this by assigning both high and low responders to each group manually
    # and then comparing means / doing a t-test.
# BUT: A graph is the best way to find individuals making the group uneven.

# We use Prism for graphing and SPSS for statistics, they have different data
#   layouts (grouped vs not, horizontal vs vertical) which is tedious to manage

# I know I originally discussed doing something similar for raw output from
    #

# Things I want this code to do:
    # 1. Read in my .csvs from SPSS correctly, not as strings
    # 2. Recognize groups and sort subjects into them
    # 3. Calculate some basic information about the groups
    # 4. Plot behavior data over time for the groups
    # 5. Output this information to the "plots" folder
# Wishlist of bonus features:
    # Recognize outlier subjects and recommend them for removal from the group
    # Graphs that are really nice to look at 
    # Extremely simple execution (click the python file and it's done)
        # so that my noncoding colleagues can use this
# ==================================================
