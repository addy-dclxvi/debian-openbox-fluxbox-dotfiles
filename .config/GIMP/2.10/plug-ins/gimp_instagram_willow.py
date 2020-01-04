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

#http://www.tricky-photoshop.com/willow-effect

from gimpfu import *

def willow( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()
	current_b=pdb.gimp_context_get_background()

	img.disable_undo()
	
	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Willow Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img,drawCopy,lg,0)
	pdb.gimp_item_set_name(drawCopy,"willowBG")

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#add some noise
	noise = pdb.gimp_layer_new(img,w,h,1,"willowNoise",100.0,0)
	pdb.gimp_image_insert_layer(img, noise, lg, 0)
	pdb.gimp_image_set_active_layer(img,noise)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_fill(noise,0)
	pdb.plug_in_rgb_noise(img,noise,0,0,0.5,0.5,0.5,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(noise,4)
	pdb.gimp_layer_set_opacity(noise,20)

	#turn black and white
	pdb.gimp_desaturate_full(drawCopy,1)

	#add flare
	flare = pdb.gimp_layer_new(img,w,h,1,"willowFlare",100.0,0)
	pdb.gimp_image_insert_layer(img, flare, lg, 0)
	pdb.gimp_image_set_active_layer(img,flare)

	#set color gradient
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_edit_blend(flare,2,0,2,100,0,0,0,0,4,2,1,w/2,h/2,w,h/2)
	pdb.gimp_layer_set_mode(flare,19)


	#add vignette
	l = pdb.gimp_layer_new(img,w,h,1,"sierraVignette",100.0,0)
	pdb.gimp_image_insert_layer(img, l, lg, 0)
	pdb.gimp_image_set_active_layer(img,l)

	delta=80
	pdb.gimp_image_select_round_rectangle(img,0,w/delta,h/delta,w-2*(w/delta),h-2*(h/delta),50,50)
	feather=30
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_selection_invert(img)
	pdb.gimp_edit_fill(l,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(l,19)

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


register( "gimp_instagram_willow",
  "Add Instagram willow effect",
  "Add Instagram willow effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Willow",
  'RGB*',
  [],
  '',
  willow)

main()

