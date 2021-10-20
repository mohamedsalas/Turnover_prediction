from django.shortcuts import render
import os 



def align(request):
    os.system('python facenet/align/align_dataset_yolo_gpu.py')
    return render(request,"home.html")
def hello(request):

    return render(request, "default.html")