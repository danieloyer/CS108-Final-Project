"""CS 108 Final Project

This module implements a model for an individual gif.

@author: Daniel Oyer
@date: Fall, 2021"""


class Gif:
    """This class implements a model for an individual gif."""

    def __init__(self, gif, caption, rating=None):
        """stores the type of gif, caption, and rating of the gif as instance variables. The rating will be None type
        until updated"""
        self.gif = gif
        self.caption = caption
        self.rating = rating

    def __str__(self):
        """returns a string of the type of gif and the caption. example:
        Drakesupport.gif
        me when I finally figure out my project
        3"""
        return "{}\n{}\n{}\n".format(str(self.gif), str(self.caption), str(self.rating))

    def save(self):
        """writes a string method of a gif object to the saved gif file"""
        saved_gifs = open('saved_gifs.txt', 'a')
        saved_gifs.write(self.__str__())

    def update_rating(self, new_rating):
        """updates the current rating to the new_rating parameter"""
        self.rating = new_rating
