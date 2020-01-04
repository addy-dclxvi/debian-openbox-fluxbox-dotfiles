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

#http://www.gramoftheday.com/#!hudson-filter/cken

from gimpfu import *

def hudson( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()
	current_b=pdb.gimp_context_get_background()

	img.disable_undo()
	
	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Hudson Effect")

	#copy image
	drawCopy2=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img,drawCopy2,lg,0)
	pdb.gimp_item_set_name(drawCopy2,"hudsonBG")

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy2, 0, 4, (0,25, 255,255) )
	pdb.gimp_curves_spline(drawCopy2, 1, 10, (0,34, 29,49, 130,162, 201,217, 255,255) )
	pdb.gimp_curves_spline(drawCopy2, 2, 14, (0,0, 67,88, 126,159, 154,178, 201,220, 226,235, 255,255) )
	pdb.gimp_curves_spline(drawCopy2, 3, 12, (0,0, 67,91, 138,191, 204,231, 255,255) )

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#add color level
	pdb.gimp_context_set_foreground((128,153,190))
	pdb.gimp_context_set_background((47,27,27))

	l = pdb.gimp_layer_new(img,w,h,1,"hudsonColor",100.0,0)
	pdb.gimp_image_insert_layer(img, l, lg, 0)
	pdb.gimp_image_set_active_layer(img,l)

	pdb.gimp_edit_blend(l,0,0,2,100,0,0,0,0,4,2,1,w/2,h/2,w+(w/2),h/2)

	pdb.gimp_layer_set_opacity(l,75)
	pdb.gimp_layer_set_mode(l,5)

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


register( "gimp_instagram_hudson",
  "Add Instagram hudson effect",
  "Add Instagram hudson effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Hudson",
  'RGB*',
  [],
  '',
  hudson)

main()

