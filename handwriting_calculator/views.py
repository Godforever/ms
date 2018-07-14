from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.templatetags.static import static
from .utils.cnn_model import *
from .utils.image_processing import *
from .utils.calculator import *
from PIL import Image

meta = static("./model/model-200.meta")
path = static("./model/")

def main_page(request):
    return render(request, "hand_writing_calculator/index.html")

def save_img(img_arr: np.ndarray, file_path: str) -> None:
    img = Image.fromarray(img_arr, 'L')
    img.save(file_path)

@csrf_exempt
def get_result(request):
    img_str = request.POST["img_data"]
    global cnn_model
    img_arr = np.array(img_str.split(',')).reshape(200, 1000, 4).astype(np.uint8)
    binary_img_arr = img_arr[:, :, 3]
    save_img(binary_img_arr, "./target.png")
    data = cv2.imread('./target.png', 2)
    data = 255 - data
    images = get_image_cuts(data, is_data=True, n_lines=1, data_needed=True)
    equation = ''
    cnn_model = model()
    cnn_model.load_model(meta, path)
    digits = list(cnn_model.predict(images))
    for d in digits:
        equation += SYMBOL[d]
    print(equation)
    result = calculate(equation)
    return JsonResponse({"status": "{} = {}".format(equation, result)}, safe=False)