from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("distilgpt2")
# print(tokenizer.eos_token)
tokenizer.pad_token = tokenizer.eos_token
model = AutoModelForCausalLM.from_pretrained("distilgpt2", pad_token_id=tokenizer.eos_token_id)

def predict(input, history=[]):
    # print(input)
    new_user_input_ids = tokenizer.encode(
        input+tokenizer.eos_token, return_tensors="pt"
    )
    # print(new_user_input_ids)
    
    bot_input_ids = torch.cat([torch.LongTensor(history), new_user_input_ids], dim=-1)
    
    history = model.generate(
        bot_input_ids, pad_token_id=tokenizer.eos_token_id, max_length = max(len(bot_input_ids)+25, 1024)
    ).tolist()

    history[0] = [ x for x in history[0] if x != 198]

    response = tokenizer.decode(history[0]).split("<|endoftext|>")[-1]
    response = response.rstrip()

    # response = [
    #     (response[i], response[i+1]) for i in range(0, len(response) - 1, 2)
    # ]
    
    return response, history

if __name__ == "__main__":
    
    print(predict("hello"))