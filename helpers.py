"""CS 108 Final Project

This module implements a function that reads the data from the saved gif file and returns a list of gif objects based on
the kind of gif, caption, and rating in the file. It also contains functions that return the index above and below an
index in a given list (returns the index of the item to the right or the left of the received index).

@author: Daniel Oyer
@date: Fall, 2021"""

from gif import Gif


def saved_gifs():
    """This function opens the saved gif text file, reads the data values, and returns a list of gif objects that have
    corresponding type of gif, caption, and rating values"""
    fin = open('saved_gifs.txt', 'r')
    gif_list = []
    saved_gif_objects = []
    for i in fin.readlines():
        gif_list.append(i[0:-1])  # this line is necessary to remove the \n at the end of the line in the save file
    '''loops through every third item in the list, creates a gif object of the first line as the gif type, the second
    line as the caption, and the third line as the rating'''
    for i in range(0, len(gif_list), 3):
        saved_gif_objects.append(Gif(gif_list[i], gif_list[i + 1], gif_list[i + 2]))
    return saved_gif_objects


def scroll_left(index, list):
    """algorithm that receives an index from an item in a list and returns the index below it"""
    if index > 0:
        index -= 1
        return index
    else:
        return len(list) - 1


def scroll_right(index, list):
    """algorithm tha receives the index of an item in a list and returns the index above it"""
    if index < len(list) - 1:
        index += 1
        return index
    else:
        return 0
