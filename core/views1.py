import os
import replicate
# Create your views here.

os.environ["REPLICATE_API_TOKEN"] = "r8_Qh7fOYo4OpiJKo5wkKKFSLwLaj9DBtM2e9Nfo"
file_url = "https://firebasestorage.googleapis.com/v0/b/djangoimggen.appspot.com/o/file%2Foutput-onlinepngtools.png?alt=media&token=6a5de7cf-9471-44c9-b0eb-75c919e19966"
model_id = 'jagilley/controlnet-canny:aff48af9c68d162388d230a2ab003f68d2638d88307bdaf1c2f1ac95079c9613'

def run_replicate(model_id, prompt, num_samples, image_resolution, low_threshold, high_threshold, ddim_steps, scale, eta, a_prompt, n_prompt):
  try:
    response = replicate.run(model_id, input={
                                  'image': file_url,
                                  'prompt': prompt,
                                  'num_samples': num_samples,
                                  'image_resolution': image_resolution,
                                  'low_threshold': low_threshold,
                                  'high_threshold': high_threshold,
                                  'ddim_steps': ddim_steps,
                                  'scale': scale,
                                  'eta': eta,
                                  'a_prompt': a_prompt,
                                  'n_prompt': n_prompt
                              })
    output_mask = response[0]
    output_img = response[1]
    print("mask: ", output_mask)
    print("Generated img: ", output_img)
    
  except Exception as e:
    print("<== Exception ==> ")
    print(e)


image_instance = request.FILES['image']

# model_id 
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

response = run_replicate(file_url, prompt, num_samples, image_resolution, low_threshold, high_threshold, ddim_steps, scale, eta, a_prompt, n_prompt)