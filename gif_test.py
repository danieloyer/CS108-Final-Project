"""CS 108 Final Project

This module implements tests of the saved_gifs function, the functions for scrolling left and scrolling right, and
testing individual gif objects.

@author: Daniel Oyer
@date: Fall, 2021"""
from helpers import saved_gifs, scroll_right, scroll_left
from gif import Gif

# tests the scrolling functions and the saved gifs function
my_list = [1, 2, 3, 4, 5]
assert scroll_left(1, my_list) == 0
assert scroll_right(2, my_list) == 3
assert saved_gifs()[0].caption == 'when I finally figure out how to buy 80 watermelons on amazon'
assert saved_gifs()[0].gif == 'drakesupport.gif'

# tests the saving to a file feature
saved_gif_file = open('saved_gifs.txt', 'r')
lines = saved_gif_file.readlines()
assert lines[0] == saved_gifs()[0].gif + '\n'
assert lines[1] == saved_gifs()[0].caption + '\n'
assert lines[2] == str(saved_gifs()[0].rating) + '\n'
assert lines[3] == saved_gifs()[1].gif + '\n'
assert lines[4] == saved_gifs()[1].caption + '\n'
assert lines[5] == str(saved_gifs()[1].rating) + '\n'

# tests an individual gif object with the save method and the text file
gif1 = Gif('manatee.gif', 'face go smushy smush')
assert gif1.caption == 'face go smushy smush'
assert gif1.gif == 'manatee.gif'
# gif1.save()
# lines = saved_gif_file.readlines()
# assert lines[-2:] == [str((gif1.gif + '\n')), str((gif1.caption + '\n'))], '\n'
assert gif1.__str__() == 'manatee.gif\nface go smushy smush\nNone\n'

# test rating system
gif2 = Gif('manatee.gif', 'when I\'m a manatee and I run into a wall')
assert gif2.rating is None
gif2.rating = 4
assert gif2.rating == 4
