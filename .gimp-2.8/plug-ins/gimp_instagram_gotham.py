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

#http://www.youtube.com/watch?v=V_0BR_yaY_w

from gimpfu import *

def gotham( img, draw ):
	

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Gotham Effect")

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"gothamBG")
	pdb.gimp_desaturate_full(drawCopy,0)

	drawCopy2=pdb.gimp_layer_new_from_drawable(drawCopy,img)
	pdb.gimp_image_insert_layer(img, drawCopy2, lg, 0)
	pdb.gimp_item_set_name(drawCopy2,"gothamBG2")

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy2, 3, 10, (0,0, 63,98, 128,128, 189,159, 255,255) )
	pdb.gimp_layer_set_mode(drawCopy2,18)

	#add some blur and noise
	drawCopy3=pdb.gimp_layer_new_from_drawable(drawCopy,img)
	pdb.gimp_image_insert_layer(img, drawCopy3, lg, 0)
	pdb.gimp_item_set_name(drawCopy3,"gothamBG3")
	pdb.plug_in_mblur(img,drawCopy3,0,256,0,0,0)
	pdb.gimp_layer_set_mode(drawCopy3,4)
	pdb.gimp_layer_set_opacity(drawCopy3,30)
	pdb.plug_in_rgb_noise(img,drawCopy3,0,1,0.10,0.10,0.10,0)

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


register( "gimp_instagram_gotham",
  "Add Instagram Gotham effect",
  "Add Instagram Gotham effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Gotham",
  'RGB*',
  [],
  '',
  gotham)

main()

