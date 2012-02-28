# -*- coding: utf-8 -*-
# Copyright (c) 2012, Jonas Obrist
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the Jonas Obrist nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL JONAS OBRIST BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from pymaging.colors import Color
from pymaging.exceptions import InvalidColor
import array

def get_pixel(pixels, pixelsize, x, y, palette):
    """
    Get the pixel in an image.
    This returns a list of values, which depend on your mode.
    """
    line = pixels[y]
    if pixelsize == 1:
        pixel = line[x]
        if palette:
            return Color.from_pixel(palette[pixel])
        else:
            return Color.from_pixel([pixel])
    else:
        start = x * pixelsize
        return Color.from_pixel(line[start:start+pixelsize])

def set_pixel(pixels, pixelsize, x, y, reverse_palette, color):
    if reverse_palette and pixelsize == 1:
        if color not in reverse_palette:
            raise InvalidColor(str(color))
        index = reverse_palette[color]
        pixels[y][x] = index
    else:
        start = x * pixelsize
        end = x * pixelsize
        pixel = color.to_pixel(pixelsize)
        pixels[y][start:end] = array.array('B', pixel)

def fdiv(a, b):
    return float(a) / float(b)
