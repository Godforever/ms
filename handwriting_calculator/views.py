from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static

meta = static("./model/model-200.meta")
path = static("./model/")

from django.conf import settings
import numpy as np
from .utils.cnn_model import *
from .utils.image_processing import *
from .utils.calculator import *
import os


def main_page(request):
    return render(request, "hand_writing_calculator/index.html")


@csrf_exempt
def get_result(request):
    img_str = request.POST["img_data"]

    print(os.path.abspath(meta))
    cnn_model = model()
    cnn_model.load_model(meta, path)
    img_arr = np.array(img_str.split(',')).reshape(4, 1000, 200).astype(np.float)
    # img = (img_arr[0] + img_arr[1] + img_arr[2]) / 3
    img = img_arr[0]
    print(img)
    img = img.T
    cv2.imwrite('img.jpg', img)
    image_cuts = get_image_cuts(img, is_data=True, data_needed=True)
    equation = ''
    for image in image_cuts:
        predict = cnn_model.predict(image)
        equation += SYMBOL[predict]

    result = calculate(equation)
    return JsonResponse({"status": "{} = {}".format(equation, result)}, safe=False)
