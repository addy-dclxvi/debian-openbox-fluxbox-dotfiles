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

#http://www.tricky-photoshop.com/mayfair-effect/

from gimpfu import *

def mayfair( img, draw ):
	

	img.disable_undo()

	lg=pdb.gimp_layer_group_new(img)
	pdb.gimp_image_insert_layer(img, lg, None, 0)
	pdb.gimp_item_set_name(lg,"Mayfair Effect")

	#copy image
	drawCopy=pdb.gimp_layer_new_from_drawable(draw,img)
	pdb.gimp_image_insert_layer(img, drawCopy, lg, 0)
	pdb.gimp_item_set_name(drawCopy,"mayfairBG")

	pdb.gimp_selection_all
	sel_size=pdb.gimp_selection_bounds(img)
	w=sel_size[3]-sel_size[1]
	h=sel_size[4]-sel_size[2]
	pdb.gimp_selection_clear(img)

	#add some noise
	noise = pdb.gimp_layer_new(img,w,h,1,"mayfairNoise",100.0,0)
	pdb.gimp_image_insert_layer(img, noise, lg, 0)
	pdb.gimp_image_set_active_layer(img,noise)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_fill(noise,0)
#	pdb.plug_in_rgb_noise(img,noise,1,0,0.20,0.20,0.20,0)
	pdb.plug_in_rgb_noise(img,noise,0,0,0.20,0.20,0.20,0)
	pdb.gimp_selection_clear(img)
	pdb.gimp_layer_set_mode(noise,4)
	pdb.gimp_layer_set_opacity(noise,20)

	#central selection
	pdb.gimp_image_set_active_layer(img,drawCopy)
	nParti=6
	feather=(w/100)*10
	pdb.gimp_image_select_rectangle(img,0, (w/2)-(w/nParti), (h/2)-(h/nParti), (w/nParti)*2, (h/nParti)*2 )
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_edit_copy(drawCopy)
	sel = pdb.gimp_layer_new(img,w,h,1,"mayfairSel",100.0,0)
	pdb.gimp_image_insert_layer(img, sel, lg, 0)
	pdb.gimp_image_set_active_layer(img,sel)
	lSel = pdb.gimp_edit_paste(sel, 1)
	pdb.gimp_floating_sel_attach(lSel, sel)
	pdb.gimp_selection_clear(img)

	#adjust brightness contrast
	pdb.gimp_brightness_contrast(sel, 0, 25)

	#lateral selection
	latSel = pdb.gimp_layer_new(img,w,h,1,"mayfairLatSel",100.0,0)
	pdb.gimp_image_insert_layer(img, latSel, lg, 0)
	pdb.gimp_image_set_active_layer(img,latSel)
	wSel=(w/100)*10
	pdb.gimp_image_select_rectangle(img,0, w-wSel, 0, w, h )
	pdb.gimp_image_select_rectangle(img,0, 0, 0, wSel, h )
	feather=(w/100)*10
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_context_set_foreground((0,0,0))
	pdb.gimp_edit_fill(latSel,0)
	pdb.gimp_layer_set_mode(latSel,19)
	pdb.gimp_layer_set_opacity(latSel,70)
	pdb.gimp_selection_clear(img)

	#circular selection
	cSel = pdb.gimp_layer_new(img,w,h,1,"mayfairCSel",100.0,0)
	pdb.gimp_image_insert_layer(img, cSel, lg, 0)
	pdb.gimp_image_set_active_layer(img,cSel)
	pdb.gimp_layer_set_opacity(cSel,80)
	pdb.gimp_image_select_ellipse(img,0, (w/2)-(w/nParti), 0-(h/nParti), (w/nParti)*2, (h/nParti)*2 )
	pdb.gimp_image_select_ellipse(img,0, (w/2)-(w/nParti), h-(h/nParti), (w/nParti)*2, (h/nParti)*2 )
	feather=(w/100)*10
	pdb.gimp_selection_feather(img,feather)
	pdb.gimp_context_set_foreground((255,255,255))
	pdb.gimp_edit_fill(cSel,0)
	pdb.gimp_layer_set_mode(cSel,19)
	pdb.gimp_layer_set_opacity(cSel,55)
	pdb.gimp_selection_clear(img)

	#adjust curves colors
	pdb.gimp_curves_spline(drawCopy, 0, 8, (0,0, 65,60, 185,190, 255,255) )
	pdb.gimp_curves_spline(sel, 0, 8, (0,0, 65,60, 185,190, 255,255) )

	#adjust levels colors
	pdb.gimp_levels(drawCopy, 0, 0, 255, 0.83, 0, 255)
	pdb.gimp_levels(sel, 0, 0, 255, 0.83, 0, 255)

	#adjust hue saturation of bg
	pdb.gimp_hue_saturation(drawCopy,0, 0,0,-20)
	pdb.gimp_hue_saturation(sel,0, 0,0,-20)
	
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


register( "gimp_instagram_mayfair",
  "Add Instagram mayfair effect",
  "Add Instagram mayfair effect",
  "Marco Crippa",
  "(©) 2013 Marco Crippa",
  "2013-01-08",
  "<Image>/Filters/Instagram/Mayfair",
  'RGB*',
  [],
  '',
  mayfair)

main()

