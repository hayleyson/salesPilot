from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-13b-v1.5")
model = AutoModelForCausalLM.from_pretrained("lmsys/vicuna-13b-v1.5")

def predict(input, history=[]):
    new_user_input_ids = tokenizer.encode(
        input+tokenizer.eos_token, return_tensors="pt"
    )
    
    bot_input_ids = torch.cat([torch.LongTensor(history), new_use_input_ids], dims=-1)
    
    history = model.generate(
        bot_input_ids, max_length=4000, pad_token_id=tokenizer.eos_token_id
    ).tolist()
    
    response = tokenizer.decode(history[0]).split("<|endoftext|>")
    response = [
        (response[i], response[i+1]) for i in range(0, len(response) - 1, 2)
    ]
    
    return response, history