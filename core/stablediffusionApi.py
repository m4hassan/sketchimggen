import requests
import json

def sd_Api():

    url = "https://stablediffusionapi.com/api/v3/img2img"
    key = 'ZdOA7vtrmg20hLElq4wXnjt8theMOrJSGKXlkH2dLRYDtwI6beT942gIedCr'
    payload = json.dumps({
    "key": key,
    "prompt": "a cat sitting on a bench",
    "negative_prompt": None,
    "init_image": "https://raw.githubusercontent.com/CompVis/stable-diffusion/main/data/inpainting_examples/overture-creations-5sI6fQgYIuo.png",
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
        else:
            print(f"Error: {response.status_code} - {response.text}")
    
    except requests.RequestException as e:
        print(f"Request Failed: {e}")


# sd_Api()