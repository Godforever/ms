from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from .utils.cnn_model import *
from .utils.image_processing import *
from .utils.calculator import *

cnn_model = model()
cnn_model.load_model('', '')


def main_page(request):
    return render(request, "hand_writing_calculator/index.html")


@csrf_exempt
def get_result(request):
    img_str = request.POST["img_data"]
    img_arr = np.array(img_str.split(',')).reshape(4, 1000, 200)
    img = (img_arr[0] + img_arr[1] + img_arr[2]) / 3
    image_cuts = get_image_cuts(img, data_needed=True)
    equation = ''
    for image in image_cuts:
        predict = cnn_model.predict(image)
        equation += SYMBOL[predict]

    result = calculate(equation)
    return JsonResponse({"status": "{} = {}".format(equation, result)}, safe=False)
