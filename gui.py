"""CS 108 Final Project

This module implements a GUI for the gif maker.

@author: Daniel Oyer
@date: Fall, 2021"""

from guizero import Picture, App, Box, PushButton, Window, TextBox, Text, ButtonGroup
from gif import Gif
from helpers import saved_gifs, scroll_right, scroll_left


class MemeGUI:
    """MemeGUI runs a GUI of the gif maker."""

    def __init__(self, app):
        """builds the interface of each of the windows. There is a window for the gif selector, the caption input, the
        created gif, the filter window, and the interface for the saved gifs."""
        self.gif_list = ['drakesupport.gif', 'puppet.gif', 'manatee.gif', 'cat.gif', 'dwight.gif', 'kermit.gif',
                         'obama.gif', 'michaeljackson.gif', 'zootopia_sloth.gif', 'michaelscott.gif']
        self.saved_gif_list = saved_gifs()
        app.title = 'Gif Caption Generator'
        self.unit = 700
        app.height = self.unit
        app.width = self.unit
        self.gif_index = 0
        self.saved_gif_index = 0

        # Home Gif Selector GUI layout
        self.box = Box(app, layout='grid', width=self.unit, height=self.unit + 100)
        PushButton(self.box, text='view saved', grid=[0, 0], align='left', command=self.view_saved)
        PushButton(self.box, text='quit', grid=[2, 0], align='right', command=app.destroy)
        PushButton(self.box, text='choose', grid=[0, 3], align='left', command=self.choose)
        PushButton(self.box, text='-->', grid=[2, 3], align='right', command=self.scroll_right_home)
        PushButton(self.box, text='<--', grid=[2, 3], command=self.scroll_left_home)
        self.picture = Picture(self.box, width=self.unit, height=self.unit - 100, grid=[0, 1, 3, 1],
                               image=self.gif_list[self.gif_index])

        # Gif Caption Maker Window
        self.text_app = Window(app, visible=False, title='Caption Maker')
        self.text_app.width = 600
        self.text_app.height = 50
        self.gif_text = TextBox(self.text_app, height='fill', width=50, align='left', text='enter caption')
        PushButton(self.text_app, text='make', align='right', command=self.make)
        PushButton(self.text_app, text='save', align='right', command=self.save)
        self.rate_gif = TextBox(self.text_app, height='fill', width=15, align='left', text='rating: (1-5)')
        PushButton(self.text_app, text='rate', align='right')

        # Created Gif Window
        self.gif_app = Window(app, visible=False, title='new gif')
        created_gif_box = Box(self.gif_app, height=self.unit, width=self.unit, layout='grid')
        self.gif = Picture(created_gif_box, image=self.gif_list[self.gif_index], height=self.unit - 50, width=self.unit,
                           grid=[0, 0])
        self.caption_text = Text(created_gif_box, text=self.gif_text.value, grid=[0, 1], align='left', width='fill')

        # View Saved Window
        self.saved_app = Window(app, visible=False)
        self.saved_app.height = self.unit
        self.saved_app.width = self.unit
        saved_box = Box(self.saved_app, layout='grid', width=self.unit, height=self.unit + 100)
        PushButton(saved_box, text='filter', grid=[0, 0], command=self.open_filter_window)
        PushButton(saved_box, text='back', grid=[0, 0], align='left', command=self.back)
        self.current_rating_displayed = Text(saved_box,
                                             text='rating: {}'.format(self.saved_gif_list[self.saved_gif_index].rating),
                                             grid=[0, 0], align='right')
        self.rating_input_box = TextBox(saved_box, text='rate gif: (1-5)', grid=[1, 0], width='fill')
        PushButton(saved_box, text='Rate', grid=[1, 0], align='right', command=self.rate)
        PushButton(saved_box, text='<--', grid=[2, 0], command=self.scroll_left_saved)
        PushButton(saved_box, text='-->', grid=[2, 0], align='right', command=self.scroll_right_saved)
        self.saved_gif_displayed = Picture(saved_box, width=self.unit, height=self.unit - 100, grid=[0, 1, 3, 1],
                                           image=self.gif_list[self.gif_index])
        self.caption_text_saved = Text(saved_box, text='placeholder', grid=[0, 3, 3, 1], align='left')

        # Filter Gif Window
        self.filter_window = Window(app, visible=False)
        filter_box = Box(self.filter_window, layout='grid', height=self.filter_window.height,
                         width=self.filter_window.width)
        self.filter_window.text_size = 12
        self.gif_choice = ButtonGroup(filter_box, options=[i for i in self.gif_list], grid=[1, 1])
        PushButton(filter_box, text='filter type', grid=[1, 2], command=self.filter_type)
        self.keyword_search_box = TextBox(filter_box, text='filter by keyword: ', grid=[2, 1], width='fill',
                                          align='top')
        PushButton(filter_box, text='search keyword', grid=[3, 1], align='top', command=self.search_keyword)
        self.rating_search_box = TextBox(filter_box, text='filter by rating: (1-5)', grid=[2, 1], width='fill',
                                         align='bottom')
        PushButton(filter_box, text='search rating', grid=[3, 1], align='bottom', command=self.search_rating)
        PushButton(filter_box, text='RESET ALL FILTERS', grid=[2, 3], command=self.reset)

    def scroll_right_home(self):
        """replaces the displayed image on the choose gif page with the gif image to the right of the current gif in the
        gif list."""
        self.picture.image = self.gif_list[scroll_right(self.gif_index, self.gif_list)]  # updates picture
        self.gif_index = scroll_right(self.gif_index, self.gif_list)  # updates index value of gif shown

    def scroll_left_home(self):
        """replaces the displayed image on the choose gif page with the gif image to the left of the current gif in the
        gif list."""
        self.picture.image = self.gif_list[scroll_left(self.gif_index, self.gif_list)]
        self.gif_index = scroll_left(self.gif_index, self.gif_list)

    def choose(self):
        """opens two windows, the caption input window and the created gif window. Also resets the text input, caption,
        and rating input values when creating a new gif after creating at list one gif after running the program"""
        self.gif_text.value = 'enter caption'
        self.rate_gif.value = 'Rate gif: (1-5)'
        self.caption_text.value = ''
        self.text_app.visible = True
        self.gif_app.visible = True
        self.gif_app.height = self.unit
        self.gif_app.width = self.unit
        self.gif.image = self.gif_list[self.gif_index]

    def make(self):
        """updates the text value in the created gif window to the value of what is entered in the text input box"""
        self.caption_text.value = self.gif_text.value

    def save(self):
        """saves the created gif by instantiating a gif object with the entered caption, gif type, and rating. closes
        the created gif and caption input windows"""
        self.caption_text.value = self.gif_text.value
        new_gif = Gif(str(self.gif_list[self.gif_index]), str(self.caption_text.value), self.rate_gif.value)
        new_gif.save()
        self.saved_gif_list = saved_gifs()
        self.gif_app.visible = False
        self.text_app.visible = False

    def update_saved_gui(self):
        """updates the image, caption, and value of the saved gif GUI to the first gif of the filtered gif list"""
        self.saved_gif_displayed.image = self.saved_gif_list[0].gif
        self.caption_text_saved.value = self.saved_gif_list[0].caption
        self.current_rating_displayed.value = self.saved_gif_list[0].rating

    def view_saved(self):
        """opens a window of saved gifs and their corresponding captions"""
        if len(self.saved_gif_list) == 0:
            pass
        else:
            app.visible = False
            self.saved_app.visible = True
            self.saved_app.height = self.unit
            self.saved_gif_list = saved_gifs()
            self.update_saved_gui()

    def back(self):
        """returns the user to the gif selector interface from the saved gif interface window"""
        self.saved_app.visible = False
        app.visible = True

    def scroll_right_saved(self):
        """replaces the displayed caption and image on the saved gif page with the gif caption and image of the gif
        object and index to the right of the previous gif in the saved gif list"""
        if len(self.saved_gif_list) < 2:  # does nothing if less than two gifs are saved
            pass
        else:
            self.saved_gif_displayed.image = self.saved_gif_list[scroll_right(self.saved_gif_index,
                                                                              [i.gif for i in self.saved_gif_list])].gif  # updates image
            self.caption_text_saved.value = self.saved_gif_list[scroll_right(self.saved_gif_index,
                                                                             [i.caption for i in self.saved_gif_list])].caption  # updates caption
            self.saved_gif_index = scroll_right(self.saved_gif_index, self.saved_gif_list)  # updates index of saved gif displayed
            self.current_rating_displayed.value = self.saved_gif_list[self.saved_gif_index].rating  # updates rating displayed

    def scroll_left_saved(self):
        """replaces the displayed caption and image on the saved gif page with the gif caption and image of the gif
                object and index to the left of the previous gif in the saved gif list"""
        if len(self.saved_gif_list) < 2:  # does nothing if less than two gifs are saved
            pass
        else:
            self.saved_gif_displayed.image = self.saved_gif_list[scroll_left(self.saved_gif_index,
                                                                             [i.gif for i in self.saved_gif_list])].gif
            self.caption_text_saved.value = self.saved_gif_list[scroll_left(self.saved_gif_index,
                                                                            [i.caption for i in
                                                                             self.saved_gif_list])].caption
            self.saved_gif_index = scroll_left(self.saved_gif_index, self.saved_gif_list)
            self.current_rating_displayed.value = self.saved_gif_list[self.saved_gif_index].rating

    def rate(self):
        """saves the rating entered into the rating textbox to the rating attribute for the displayed gif,
        updates the gui so that the new rating is displayed"""
        self.saved_gif_list[self.saved_gif_index].update_rating(self.rating_input_box.value)  # updates the rating attribute of the displayed gif to the entered rating
        self.current_rating_displayed.value = self.saved_gif_list[self.saved_gif_index].rating  # updates the rating displayed

    def open_filter_window(self):
        """opens the window that allows the user to filter through the displayed saved gifs based on type of gif"""
        self.filter_window.visible = True
        self.filter_window.height = 500

    def search_keyword(self):
        """searches the captions of all the saved gif objects for the entered keyword, then updates the list of saved
        gifs so that the list only contains gifs that contain the keyword in their caption. Then the function updates
        the gui so that the new saved gif list is displayed."""
        search_input = self.keyword_search_box.value.split()
        keyword_gif_list = []
        '''iterates through each gif, searches if the keyword is in the gif, adds the gif to the list if it has the
        keyword in the caption'''
        for gif in self.saved_gif_list:
            for keyword in search_input:
                if keyword.lower() in gif.caption.lower().split():
                    keyword_gif_list.append(gif)
        self.saved_gif_list = keyword_gif_list
        if len(self.saved_gif_list) == 0:  # if none of the gifs in the saved gif list have the keyword
            pass
        else:
            self.update_saved_gui()

    def search_rating(self):
        """filters through each saved gif and creates a new saved gif list of only those gifs whose rating matches the
         rating entered in the search box"""
        rating_gif_list = []
        '''loops through each gif in the saved gif list, appends those gifs whose rating match the entered rating to the
        rating gif list'''
        for gif in self.saved_gif_list:
            if gif.rating is None:
                pass
            else:
                if self.rating_search_box.value == gif.rating:
                    rating_gif_list.append(gif)
        self.saved_gif_list = rating_gif_list
        if len(self.saved_gif_list) == 0:
            pass
        else:
            self.update_saved_gui()

    def filter_type(self):
        """filters the saved gifs displayed by updating the list of saved gifs so that the only gifs displayed to the
        user are those which the user specified in the filter window button group"""
        self.saved_gif_list = [i for i in saved_gifs() if i.gif == self.gif_choice.value_text]  # list of gifs whose gif type matches the specified type
        if len(self.saved_gif_list) == 0:
            pass
        else:
            self.update_saved_gui()

    def reset(self):
        """clears any filters on the saved gif selection window"""
        self.saved_gif_list = saved_gifs()
        self.update_saved_gui()


app = App()
gui = MemeGUI(app)
app.display()
