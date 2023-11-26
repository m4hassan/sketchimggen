import replicate
import requests
import json
import time

def run_sd_api(file_url, prompt, negative_prompt, image_size, samples, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength):

    url = "https://stablediffusionapi.com/api/v3/img2img"
    key = 'ZdOA7vtrmg20hLElq4wXnjt8theMOrJSGKXlkH2dLRYDtwI6beT942gIedCr'
    payload = json.dumps({
    "key": key,
    "prompt": prompt,
    "negative_prompt": negative_prompt,
    "init_image": file_url,
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "guidance_scale": 7.5,
    "strength": 0.7,
    "seed": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        if response.status_code == 200:
            json_response = response.json()
            output = json_response.get('output',[])[0]
            print("Output Image Url: ", output)
            return output
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.RequestException as e:
        print(f"Request Failed: {e}")


def fetch_generated_result(key, request_id):
    try:
        url = 'https://stablediffusionapi.com/api/v3/fetch'
        payload = json.dumps({
        "key": key,
        "request_id": request_id
        })

        headers = {
        'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            json_response = response.json()
            output = json_response.get('output', [])[0]
            if output:
                print("<== Fetched Image Url: ==>", output)
                return output
            else:
                print("Error: Fetched output is empty.")
        else:
            print(f"Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Exception: {e}")


def control_net_canny(file_url, prompt, negative_prompt, image_size, samples, num_inference_steps, safety_checker, enhance_prompt, guidance_scale, strength):

    negative_prompt = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), (text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck), "
    url = "https://stablediffusionapi.com/api/v5/controlnet"
    # key = "ZdOA7vtrmg20hLElq4wXnjt8theMOrJSGKXlkH2dLRYDtwI6beT942gIedCr" #mashudhassandev api key
    key = "QvoLwzfxnp0geSBtODlTnP99ptJ5zvFD5dkbToRUnyhIBYGnaN0E9mFNewsu" #Nyalee.Littles@FreeMailOnline.us
    payload = json.dumps({
    "key": key,
    "controlnet_model": "canny",
    "controlnet_type": "canny",
    "model_id": "midjourney",
    "auto_hint": "yes",
    "guess_mode": "no",
    "prompt": prompt,
    # "a model mugshot, ultra high resolution, 4K image"
    "negative_prompt": negative_prompt + "cartoon, illustration, 3d render, cgi, anime, drawing, grayscale, sketch, painting, animation, low resolution, low detail",
    "init_image": file_url,
    "mask_image": None,
    "width": "512",
    "height": "512",
    "samples": "1",
    "scheduler": "UniPCMultistepScheduler",
    "num_inference_steps": "30",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "guidance_scale": 7.5,
    "strength": 0.55,
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "embeddings_model": None,
    "seed": None,
    "webhook": None,
    "track_id": None
    })

    headers = {
    'Content-Type': 'application/json'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)

        json_response = response.json()
        output = json_response.get('output', '')

        if output:
            print("<== Generated Image Url: ==>", output)
            return output
        else:
            print("Output is empty. Trying to fetch result...")
            print("<== JsonResponse ==> ", json_response)
            fetch_result_id = json_response.get('id', '')
            if fetch_result_id:
                wait_time = json_response.get('eta', 0) + 10  # Adding 10 seconds buffer
                print(f"Waiting for {wait_time} seconds before fetching result...")
                time.sleep(wait_time)
                return fetch_generated_result(key, fetch_result_id)
            else:
                print("Error: fetch_result ID is not available in the response.")
    
    except requests.RequestException as e:
        print(f"Request Failed: {e}")


def run_replicate(file_url, prompt, num_samples, image_resolution, low_threshold, high_threshold, ddim_steps, scale, eta, a_prompt, n_prompt):

    print("inside replicate function...")
    model_id = 'jagilley/controlnet-canny:aff48af9c68d162388d230a2ab003f68d2638d88307bdaf1c2f1ac95079c9613'
    response = replicate.run(model_id, input={
                                  'image': file_url,
                                  'prompt': prompt,
                                  'num_samples': "1",
                                  'image_resolution': image_resolution,
                                  'low_threshold': low_threshold,
                                  'high_threshold': high_threshold,
                                  'ddim_steps': ddim_steps,
                                  'scale': scale,
                                  'eta': eta,
                                  'a_prompt': a_prompt,
                                  'n_prompt': n_prompt
                              })

    return response
