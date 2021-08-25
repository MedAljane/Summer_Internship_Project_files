import torch
import os
# Insert the directory for the CUDA binary files if you got a warning implying that TesorFlow can't use CUDA
# because of missing library Files
os.add_dll_directory("C:/Program Files/NVIDIA GPU Computing Toolkit/CUDA/v11.4/bin")

from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Set the 'model_name' variable's velue to the path of the folder containing the files of the model
# or set it to 'tuner007/pegasus_paraphrase' if you wish to download the files each time the script is run
model_name = 'C:\\Users\\mhmda\\Desktop\\Project files\\Paraphraser files\\'

# check if CUDA is available and if the available VRAM is equal to or higher than 6Gb (8Gb is recommended)
torch_device = 'cuda' if torch.cuda.is_available() and torch.cuda.get_device_properties(0).total_memory >= 6442450944 else 'cpu'
tokenizer = PegasusTokenizer.from_pretrained(model_name)
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)

def get_response(input_text,num_return_sequences,num_beams):
  batch = tokenizer([input_text],truncation=True,padding='longest',max_length=60, return_tensors="pt").to(torch_device)
  translated = model.generate(**batch,max_length=60,num_beams=num_beams, num_return_sequences=num_return_sequences, temperature=1.5)
  tgt_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
  return tgt_text