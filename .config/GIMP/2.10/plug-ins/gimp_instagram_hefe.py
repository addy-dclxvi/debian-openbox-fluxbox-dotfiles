#!/usr/bin/env python
# -*- coding: utf8 -*-

# *************************************************************************** #
#                                                                             #
#      Version 0.1 - 2013-08-01                                               #
#      Copyright (C) 2013 Marco Crippa                                        #
#                                                                             #
#      This program is free software; you can redistribute it and/or          #
#      modify it under the terms of the GNU General Public License            #
#      as published by the Free Software Foundation; either version 2         #
#      of the License, or (at your option) any later version.                 #
#                                                                             #
#      This program is distributed in the hope that it will be useful,        #
#      but WITHOUT ANY WARRANTY; without even the implied warranty of         #
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
#      GNU General Public License for more details.                           #
#                                                                             #
#      You should have received a copy of the GNU General Public License      #
#      along with this program; if not, write to the                          #
#      Free Software Foundation, Inc.,                                        #
#      51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA           #
#                                                                             #
# *************************************************************************** #

#http://www.dreevoo.com/content.php?id=744

from gimpfu import *

def hefe( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()

	img.disable_undo()
	
	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Hefe Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img,drawCopy,lg,0)
	pdb.gimp_item_set_name(drawCopy,"hefeBG")

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, 15, 25)
	
	#adjust hue saturation
	pdb.gimp_hue_saturation(drawCopy,0,5,0,-20)

	o=pdb.gimp_layer_new_from_drawable(drawCopy,img)
	pdb.gimp_image_insert_layer(img, o, lg, 0)
	pdb.gimp_item_set_name(o,"hefeOverlay")
	pdb.gimp_layer_set_mode(o,5)
	pdb.gimp_layer_set_opacity(o,40)

	ml=pdb.gimp_image_merge_down(img,o,1)

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(ml, -15, 5)

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#add vignette
	l = pdb.gimp_layer_new(img,w,h,1,"hefeVignette",100.0,0)
	pdb.gimp_image_insert_layer(img, l, lg, 0)
	pdb.gimp_image_set_active_layer(img,l)

	newW=int( (w/100)*90 )
	newH=int( (h/100)*90 )
	pdb.gimp_image_select_rectangle(img,0,int((w-newW)/2),int((h-newH)/2),newW,newH)
	if w>=h:
		rd=int(w/3)
	else:
		rd=int(h/3)
	pdb.gimp_selection_feather(img,rd)
	pdb.gimp_selection_invert(img)
	pdb.gimp_context_set_foreground((181,181,181))
	pdb.gimp_edit_fill(l,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(l,3)

	#add white border
	Wborder = pdb.gimp_layer_new(img,w,h,1,"whiteBorder",100.0,0)
	pdb.gimp_image_insert_layer(img, Wborder, lg, 0)
	pdb.gimp_image_set_active_layer(img,Wborder)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_image_select_rectangle(img, 0, 0,0, w,h )
	dimBorder=int( (w/100)*2 )
	if dimBorder<5:
		dimBorder=5
	pdb.gimp_selection_shrink(img, dimBorder)
	pdb.gimp_selection_invert(img)
	pdb.gimp_edit_fill(Wborder,0)
	pdb.gimp_selection_clear(img)
	
	#add black border
	Bborder = pdb.gimp_layer_new(img,w,h,1,"blackBorder",100.0,0)
	pdb.gimp_image_insert_layer(img, Bborder, lg, 0)
	pdb.gimp_image_set_active_layer(img,Bborder)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_image_select_rectangle(img, 0, 0,0, w,h )
	dimBorder=int( (w/100)*2 )
	if dimBorder<5:
		dimBorder=5
	pdb.gimp_selection_shrink(img, dimBorder)
	pdb.gimp_selection_invert(img)
	pdb.gimp_edit_fill(Bborder,0)
	pdb.gimp_selection_clear(img)

	img.enable_undo()

	pdb.gimp_context_set_foreground(current_f)


register( "gimp_instagram_hefe",
  "Add Instagram Hefe effect",
  "Add Instagram Hefe effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Hefe",
  'RGB*',
  [],
  '',
  hefe)

main()

