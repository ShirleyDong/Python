#!/usr/bin/env python

# Hello World in GIMP Python

from gimpfu import *

def poster(file1, file2, file3 , file4):
              # make an empty image
              posterW, posterH = 800,1200
              posterImage = gimp.Image(posterW,posterH,RGB)

              #make a background layer
              backLayer = gimp.Layer(posterImage, "Background", posterW,posterH,RGB_IMAGE,100,NORMAL_MODE)

              #setup the back and foreground color
              pdb.gimp_context_set_background((0, 0, 0))
              pdb.gimp_context_set_foreground((255,255,255))

              backLayer.fill(BACKGROUND_FILL)
              posterImage.add_layer(backLayer,1)

              # make a text layer
              textLayer = pdb.gimp_text_fontname(posterImage, None, posterW/2, posterH/15, "Best Of Beers In Cork", True, 1, 60, PIXELS, "Courier")
              textLayer.translate(-textLayer.width/2, -textLayer.height/2)

              # load the 5 images
              image0 = pdb.file_png_load(file1, file1)
              image1 = pdb.file_png_load(file2, file2)
              image2 = pdb.file_png_load(file3, file3)
              image3 = pdb.file_png_load(file4, file4)

              # resize the 5 images
              pdb.gimp_image_resize(image0, 400, 550, 0, 0)
              pdb.gimp_image_resize(image1, 400, 550, 0, 0)
              pdb.gimp_image_resize(image2, 400, 550, 0, 0)
              pdb.gimp_image_resize(image3, 400, 550, 0, 0)

              # make layer 0
              layer0 = gimp.Layer(posterImage, "Layer 0", 400, 550, RGB_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(layer0, 0)
              pdb.gimp_edit_copy(image0.layers[0])
              layer0.update(0, 0, 400, 550)
              layer0.translate(0, 100)
              pdb.gimp_edit_paste(layer0, True)

              # make layer 1
              layer1 = gimp.Layer(posterImage, "Layer 1", 400, 550, RGB_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(layer1, 0)
              pdb.gimp_edit_copy(image1.layers[0])
              layer1.update(0, 0, 400, 550)
              layer1.translate(400, 100)
              pdb.gimp_edit_paste(layer1, True)

              # make layer 2
              layer2 = gimp.Layer(posterImage, "Layer 2", 400, 550, RGB_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(layer2, 0)
              pdb.gimp_edit_copy(image2.layers[0])
              layer2.update(0, 0, 400, 550)
              layer2.translate(0, 650)
              pdb.gimp_edit_paste(layer2, True)

              # make layer 3
              layer3 = gimp.Layer(posterImage, "Layer 3", 400, 550, RGB_IMAGE, 100, NORMAL_MODE)
              posterImage.add_layer(layer3, 0)
              pdb.gimp_edit_copy(image3.layers[0])
              layer3.update(0, 0, 400, 550)
              layer3.translate(400, 650)
              pdb.gimp_edit_paste(layer3, True)
              
            
            
              #display the image
              gimp.Display(posterImage)
             

register(
              "python_fu_poster",
              "Make a poster",
              "Create a poster from 4 images about the best of cork",
              "ST",
              "Copyright@ST",
              "2018",
              "Poster(Python)",
              "", # Create a new image, don't work on an existing one
              [
              #place parameter inputs
                (PF_FILE, "file0", "Choose Image 1", ""),
                (PF_FILE, "file1", "Choose Image 2", ""),
                (PF_FILE, "file2", "Choose Image 3", ""),
                (PF_FILE, "file3", "Choose Image 4", "")
            
              ],
              [],
              poster, menu="<Image>/File/_DTX"
)

main()
