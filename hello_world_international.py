# Created by: Saad Shabir
# Created on: Sept 2017
# Created for: IC3U
# This program is the Hello, World program, but in three different languages

import ui

def english_touch_up_inside(sender):
	# displays the english version
	view['hello_world_label'].text = ('Hello, World!')
def german_touch_up_inside(sender):
	# displays the german version
	view['hello_world_label'].text = ('Hallo Welt!')
	
def japanese_touch_up_inside(sender):
	# displays the japanese version
	view['hello_world_label'].text = ('Kon nichiwa sekai!')


# note that now the app runs in full screen
view = ui.load_view()
view.present('full_screen')
