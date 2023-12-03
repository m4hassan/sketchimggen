import os
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .forms import *
from .firebase import FIREBASE_CONFIG, fb_storage
from .stablediffusionApi import run_sd_api, control_net_canny

os.environ["REPLICATE_API_TOKEN"] = "r8_Qh7fOYo4OpiJKo5wkKKFSLwLaj9DBtM2e9Nfo"

def home(request):
    return render(request, 'switch/index.html')


@login_required(login_url='/accounts/login/')
def sdIndex(request):
    form = SdForm()
    return render(request, 'core/stablediffusion.html', {'form': form})


@login_required(login_url='/accounts/login/')
def sd_view(request):
    if request.method == 'POST':
        form = SdForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = request.FILES['init_img']
            prompt = request.POST['prompt']
            negative_prompt = request.POST['negative_prompt']
            image_size = request.POST['image_size']
            samples = request.POST['samples']
            num_inference_steps = request.POST['num_inference_steps']
            safety_checker = request.POST['safety_checker']
            enhance_prompt = request.POST['enhance_prompt']
            guidance_scale = request.POST['guidance_scale']
            strength = request.POST['strength']

            file_url = fb_storage(FIREBASE_CONFIG, image_instance)
            try:
                response = control_net_canny(file_url, prompt, negative_prompt, image_size, samples, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength)
                error_msg = response.get('message', '')
                if error_msg:
                    return JsonResponse({"error": error_msg})
                
                return JsonResponse({'output_url': response})
            
            except Exception as e:
                print("<== cmd exception ==>", e)
                error_messege = str(e)
                return JsonResponse({"error": error_messege}) 
            
    return JsonResponse({'error': 'Invalid input form. Please try again. error at /stablediffuse'})


@login_required(login_url='/accounts/login/')
def replicateIndex(request):
    form = ImageUploadForm()
    return render(request, 'core/index.html', {'form': form})


@login_required(login_url='/accounts/login/')
def replicate_view(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = request.FILES['image']
            prompt = request.POST['prompt']
            num_samples = request.POST['num_samples']
            image_resolution = request.POST['image_resolution']
            low_threshold = request.POST['low_threshold']
            high_threshold = request.POST['high_threshold']
            ddim_steps = request.POST['ddim_steps']
            scale = request.POST['scale']
            eta = request.POST['eta']
            a_prompt = request.POST['a_prompt']
            n_prompt = request.POST['n_prompt']

            file_url = fb_storage(FIREBASE_CONFIG, image_instance)
            try:
                response = run_replicate(file_url, prompt, num_samples, image_resolution, low_threshold, high_threshold, ddim_steps, scale, eta, a_prompt, n_prompt)
                
                print("original response: ", response)
                output_url = response[1]
                return JsonResponse({'output_url': output_url})
            except Exception as e:
                print("<== cmd exception ==>", e)
                error_messege = str(e)
                return JsonResponse({"error": error_messege})
            
    return JsonResponse({'error': 'Invalid input form. Please try again. error at /process_upload'})

