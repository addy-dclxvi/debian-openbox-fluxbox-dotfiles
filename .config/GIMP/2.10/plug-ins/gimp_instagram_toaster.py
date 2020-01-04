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

#http://www.youtube.com/watch?v=PmWE-FZOgyU

from gimpfu import *

def toaster( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()
	current_b=pdb.gimp_context_get_background()

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Toaster Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"toasterBG")

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#mask layer
	maskL=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, maskL, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"toasterMask")
	pdb.gimp_image_set_active_layer(img,maskL)

	#adjust curves colors
	pdb.gimp_curves_spline(maskL, 0, 4, (25,0, 255,255) )

	#create mask
	lm = pdb.gimp_layer_create_mask(maskL,0)
	pdb.gimp_layer_add_mask(maskL,lm)
	#add vignette
	pdb.gimp_image_select_ellipse(img,0, 0,0, w,h )
	feather=(w/100)*20
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_fill(lm,0)
	pdb.gimp_selection_clear(img)

	#gradient layer
	gradL=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img,gradL,lg,0)
	pdb.gimp_item_set_name(gradL,"toasterGradMap")

	#set color for gradient map
	grad=pdb.gimp_gradient_new("toasterGradient")
	pdb.gimp_context_set_foreground((58,10,89))
	pdb.gimp_context_set_background((254,169,87))
	pdb.gimp_gradient_segment_set_left_color( grad, 0 ,pdb.gimp_context_get_foreground(), 100)
	pdb.gimp_gradient_segment_set_right_color( grad, 0 ,pdb.gimp_context_get_background(), 100)
	pdb.gimp_context_set_gradient(grad)
	pdb.plug_in_gradmap(img,gradL)
	pdb.gimp_gradient_delete(grad)
	pdb.gimp_layer_set_opacity(gradL,70)

	#black layer
	BL = pdb.gimp_layer_new(img,w,h,1,"toasterBlack",100.0,0)
	pdb.gimp_image_insert_layer(img,BL,lg,0)
	pdb.gimp_image_set_active_layer(img,BL)
	pdb.gimp_context_set_foreground((29,29,29))
	pdb.gimp_edit_fill(BL,0)
	pdb.gimp_layer_set_mode(BL,4)
	pdb.gimp_layer_set_opacity(BL,50)
	#create mask
	Blm = pdb.gimp_layer_create_mask(BL,1)
	pdb.gimp_layer_add_mask(BL,Blm)
	#add vignette
	delta=(w/100)*5
	pdb.gimp_image_select_ellipse(img,0, 0-delta,0-delta, w+(delta*2),h+(delta*2) )
	feather=(w/100)*15
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_edit_fill(Blm,0)
	pdb.gimp_selection_clear(img)

	#color layer
	ColL = pdb.gimp_layer_new(img,w,h,1,"toasterCol",100.0,0)
	pdb.gimp_image_insert_layer(img,ColL,lg,0)
	pdb.gimp_image_set_active_layer(img,ColL)
	pdb.gimp_context_set_foreground((210,153,1))
	pdb.gimp_edit_fill(ColL,0)
	pdb.gimp_layer_set_mode(ColL,16)
	pdb.gimp_layer_set_opacity(ColL,50)
	#create mask
	ColM = pdb.gimp_layer_create_mask(BL,1)
	pdb.gimp_layer_add_mask(ColL,ColM)
	#add vignette
	delta=(w/100)*5
	pdb.gimp_image_select_ellipse(img,0, 0+delta,0+delta, w-(delta*2),h-(delta*2) )
	feather=(w/100)*15
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_edit_fill(ColM,0)
	pdb.gimp_selection_clear(img)

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
	pdb.gimp_context_set_background(current_b)


register( "gimp_instagram_toaster",
  "Add Instagram toaster effect",
  "Add Instagram toaster effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Toaster",
  'RGB*',
  [],
  '',
  toaster)

main()

