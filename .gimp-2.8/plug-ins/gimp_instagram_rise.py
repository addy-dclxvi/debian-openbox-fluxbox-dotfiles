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

#http://www.tricky-photoshop.com/create-rise-effect/

from gimpfu import *

def rise( img, draw ):
	
	current_f=pdb.gimp_context_get_foreground()
	current_b=pdb.gimp_context_get_background()

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Rise Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"riseBG")

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]

	#Add vignette layer
	vignette = pdb.gimp_layer_new(img,w,h,1,"riseVignette",100.0,0)
	pdb.gimp_image_insert_layer(img, vignette, lg, 0)

	#add some noise
	noise = pdb.gimp_layer_new(img,w,h,1,"riseNoise",100.0,0)
	pdb.gimp_image_insert_layer(img, noise, lg, 0)
	pdb.gimp_image_set_active_layer(img,noise)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_fill(noise,0)
#	pdb.plug_in_rgb_noise(img,noise,1,0,0.20,0.20,0.20,0)
	pdb.plug_in_rgb_noise(img,noise,0,0,0.50,0.50,0.50,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(noise,4)
	pdb.gimp_layer_set_opacity(noise,20)

	#add warming level
	warm = pdb.gimp_layer_new(img,w,h,1,"riseWarming",100.0,0)
	pdb.gimp_image_insert_layer(img, warm, lg, 0)
	pdb.gimp_image_set_active_layer(img,warm)
	pdb.gimp_context_set_foreground((237,138,0))
	pdb.gimp_edit_fill(warm,0)
	pdb.gimp_layer_set_mode(warm,5)
	pdb.gimp_layer_set_opacity(warm,50)

	#adjust hue saturation of bg
	pdb.gimp_hue_saturation(drawCopy,0, 20,0,-50)

	#add vignette
	pdb.gimp_image_set_active_layer(img,vignette)
	nParti=6
	wBorder=int( (h/100)*5 )
	feather=(w/100)*10
	pdb.gimp_image_select_ellipse(img,0, 0-(w/nParti), 0+wBorder, w+(w/nParti)*2, h-(wBorder*2) )
	pdb.gimp_selection_invert(img)
	pdb.gimp_selection_feather(img,feather)
	#set color gradient
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_blend(vignette,2,0,2,100,0,0,1,0,4,2,1,w/2,h/2,w+(w/2),h/2)
	pdb.gimp_layer_set_mode(vignette,5)
	pdb.gimp_selection_clear(img)
	pdb.gimp_levels(drawCopy,0,0,255,1.23,0,255)

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


register( "gimp_instagram_rise",
  "Add Instagram rise effect",
  "Add Instagram rise effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Rise",
  'RGB*',
  [],
  '',
  rise)

main()

