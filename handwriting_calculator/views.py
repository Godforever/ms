from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import numpy as np
from PIL import Image


def main_page(request):
    return render(request, "hand_writing_calculator/index.html")


@csrf_exempt
def get_result(request):
    img_str = request.POST["img_data"]
    img_arr = np.array(img_str.split(',')).reshape(200, 1000, 4).astype(np.uint8)
    binary_img_arr = img_arr[:, :, 3]
    save_img(binary_img_arr, "./target.png")
    return JsonResponse({"status": "Not Implemented!"}, safe=False)


def save_img(img_arr: np.ndarray, file_path: str) -> None:
    img = Image.fromarray(img_arr, 'L')
    img.save(file_path)
