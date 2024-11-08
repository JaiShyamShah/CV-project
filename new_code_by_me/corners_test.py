'''
Testing of the corner and bond detection algorithms.
'''

import os
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import CV_project_SMILES 
from collections import defaultdict

### globals 

THRESH_VAL = 100
LINE_WIDTH = 18 # needs to be even
BORDER = 30
STRUCTURES = [
  #'struct1', 
  #'struct4', 
  #'struct5',
  #'struct8',
  #'struct13',
  #'struct16',
  'struct19',
  'struct20',
  'struct22',
]

PATHS = ['D:/CV_project/stanford_ocsr/chemtype2/data/' + structure + '/sd/' for structure in STRUCTURES]
TEMPLATES = ['D:/CV_project/stanford_ocsr/chemtype2/train/oh/combined.png', 'D:/CV_project/stanford_ocsr/chemtype2/train/or/combined.png', \
'D:/CV_project/stanford_ocsr/chemtype2/train/o/combined.png', 'D:/CV_project/stanford_ocsr/chemtype2/train/h/combined.png', 'D:/CV_project/stanford_ocsr/chemtype2/train/n/combined.png', 'D:/CV_project/stanford_ocsr/chemtype2/train/ro/combined.png']
TEMPLATE_NAMES = ['OH', 'OR', 'O', 'H', 'N', 'RO']

BOND_PATHS = ['D:/CV_project/stanford_ocsr/chemtype2/train/single/', 'D:/CV_project/stanford_ocsr/chemtype2/train/double/', 'D:/CV_project/stanford_ocsr/chemtype2/train/triple/', 'D:/CV_project/stanford_ocsr/chemtype2/train/dashed/', 'D:/CV_project/stanford_ocsr/chemtype2/train/wedge/']
BOND_NAMES = ['single', 'double', 'triple', 'dashed', 'wedge']
COLOR_DICT = {
  'single':[255,0,0],
  'double':[0,0,255],
  'triple':[0,255,0],
  'dashed':[255,165,0],
  'wedge':[128,0,128],
  'none':[0,0,0]
}
COLOR_DICT_OCR = {
  'OH':[255,0,0],
  'OR':[0,255,0],
  'O':[0,0,255],
  'H':[255,255,0],
  'N':[0,255,255],
  'RO':[255,0,255]
}

for path in PATHS:
  corr_t = 0.0
  total = 0.0
  fp_t = 0.0
  fn_t = 0.0
  tp_t = 0.0
  for image in os.listdir(path):
    if image[len(image)-4:len(image)] != '.png':
      continue
    try:
      #corr, fp, fn, tp = chemtype.reimplement_polygon(path+image, image[0:11] + '_tol_eq_0.77_template_bb.pickle')
      corr, fp, fn, tp = CV_project_SMILES.corner_detector(path+image, 'pickles/' + image[0:11] + '_tol_eq_0.77_template_bb.pickle')
      corr_t += corr
      total += 1
      fp_t += fp
      fn_t += fn
      tp_t += tp
    except IOError:
      pass
    try:
      #corr, fp, fn, tp = chemtype.reimplement_polygon(path+image, image[0:10] + '_tol_eq_0.77_template_bb.pickle')
      corr, fp, fn, tp = CV_project_SMILES.corner_detector(path+image, 'pickles/' + image[0:10] + '_tol_eq_0.77_template_bb.pickle')
      corr_t += corr
      total += 1
      fp_t += fp
      fn_t += fn
      tp_t += tp
    except IOError:
      pass
  print (corr_t, total, fp_t, fn_t, tp_t)

for path in PATHS:
  corr_t = 0.0
  total = 0.0
  fp_t = 0.0
  fn_t = 0.0
  tp_t = 0.0
  for image in os.listdir(path):
    if image[len(image)-4:len(image)] != '.png':
      continue
    try:
      corr, fp, fn, tp = CV_project_SMILES.detect_bonds(path+image, 'pickles/' + image[0:11] + '_tol_eq_0.77_template_bb.pickle', image[0:11] + '_corners.pickle')
      corr_t += corr
      total += 1
      fp_t += fp
      fn_t += fn
      tp_t += tp
    except IOError:
      pass
    try:
      corr, fp, fn, tp = CV_project_SMILES.detect_bonds(path+image, 'pickles/' + image[0:10] + '_tol_eq_0.77_template_bb.pickle', image[0:10] + '__corners.pickle')
      corr_t += corr
      total += 1
      fp_t += fp
      fn_t += fn
      tp_t += tp
    except IOError:
      pass
  print (corr_t, total, fp_t, fn_t, tp_t)
