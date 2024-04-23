import sys

from transformers import AutoTokenizer, T5ForConditionalGeneration

tokenizer = AutoTokenizer.from_pretrained("grammarly/coedit-large")
model = T5ForConditionalGeneration.from_pretrained("grammarly/coedit-large")
input_text = 'Fix grammatical errors in this sentence: When I grow up I start to understand what he said is quite right.'
input_ids = tokenizer(input_text, return_tensors="pt").input_ids
outputs = model.generate(input_ids, max_length=256)
edited_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(edited_text)


sys.exit()
import re
from transformers import pipeline


text = "I am XYZ I want to execute I have a doubt"

punct_model = pipeline("text-generation", model="lvwerra/bert-imdb")
punctuated_text = punct_model(text)[0]['generated_text']
print(f"Punctuated text: \n{punctuated_text}")

punctuated_text = re.sub(r'\b([A-Z][a-z]*)\b', r'\1,', text)
print(punctuated_text)



