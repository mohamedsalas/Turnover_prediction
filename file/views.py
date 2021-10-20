from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer,MultipleFilesUploadSerializer
from PIL import Image

import argparse
import sys
import tensorflow as tf
import pickle
from scipy import misc
import cv2
import numpy as np
from facenet import facenet,detect_face
import tensorflow.compat.v1 as tf 
import os
import time
from facenet.utils import *
import sklearn
from skimage.transform import rescale, resize
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):


    
        
        

        


    