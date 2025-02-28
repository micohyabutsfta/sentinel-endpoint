import runpod
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

# Load model from Hugging Face
repo_id = "micohyabutsfta/Sentinel-2.0"
model_path = snapshot_download(repo_id)

model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# Define inference function for RunPod
def generate_text(job):
    prompt = job["input"]["prompt"]
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"response": response}

# Register function with RunPod
runpod.serverless.start({"handler": generate_text})
