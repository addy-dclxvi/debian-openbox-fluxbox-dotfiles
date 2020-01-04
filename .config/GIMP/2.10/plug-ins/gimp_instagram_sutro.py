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

#http://www.youtube.com/watch?v=2GwOi1lJYPo

from gimpfu import *

def sutro( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Sutro Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"sutroBG")

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, 55, 38)
#	pdb.gimp_brightness_contrast(drawCopy, 10, 38)

	#adjust hue, saturation and lightness
	pdb.gimp_hue_saturation(drawCopy,0,0,0,-36)

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy, 1, 4, (11,14, 255,241) )
	pdb.gimp_curves_spline(drawCopy, 2, 4, (0,4, 255,247) )
	pdb.gimp_curves_spline(drawCopy, 3, 8, (0,33, 44,53, 114,120, 252,231) )

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(drawCopy, -30, 5)

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#create vignette
	v = pdb.gimp_layer_new(img,w,h,1,"sutroVignette",100.0,17)
	pdb.gimp_image_insert_layer(img, v, lg, 0)
	pdb.gimp_image_set_active_layer(img,v)
	pdb.gimp_image_select_rectangle(img,0,int((w/100)*10),int((h/100)*10),int((w/100)*80),int((h/100)*80))
	feather=50
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_selection_invert(img)
	pdb.gimp_context_set_foreground((168,168,168))
	pdb.gimp_edit_fill(v,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(v,17)
	pdb.gimp_layer_set_opacity(v,30)

	#add warming level
	warm = pdb.gimp_layer_new(img,w,h,1,"sutroWarming",100.0,0)
	pdb.gimp_image_insert_layer(img, warm, lg, 0)
	pdb.gimp_image_set_active_layer(img,warm)
	pdb.gimp_context_set_foreground((237,138,0))
	pdb.gimp_edit_fill(warm,0)
	pdb.gimp_layer_set_mode(warm,10)
	pdb.gimp_layer_set_opacity(warm,10)

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


register( "gimp_instagram_sutro",
  "Add Instagram sutro effect",
  "Add Instagram sutro effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Sutro",
  'RGB*',
  [],
  '',
  sutro)

main()

