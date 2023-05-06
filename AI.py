# from diffusers import StableDiffusionPipeline
# import torch
#
# model_id = 'dreamlike-art/dreamlike-pohtoreal-2.0'
# pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
#
# pipe = pipe.to('cuda')
#
# prompt = "annoying Student, man, tall, sporty"
#
# pipe(prompt).images[0]

import openai

response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']

print(image_url)