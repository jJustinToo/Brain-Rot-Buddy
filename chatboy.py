from transformers import pipeline

# Initialize a text generation pipeline with a model like GPT-2
generator = pipeline('text-generation', model='gpt2')

# Generate text
response = generator("Hello, how are you?", max_length=50, num_return_sequences=1)
print(response[0]['generated_text'])