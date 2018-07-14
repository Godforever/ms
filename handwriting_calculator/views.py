from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from .utils.cnn_model import *
from .utils.image_processing import *
from .utils.calculator import *

cnn_model = model()
cnn_model.load_model('')