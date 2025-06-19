from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    # Load tokenizer and model from Hugging Face Hub
    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-mini-instruct")
    model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-mini-instruct")
    model.eval()

    # Example prompt
    prompt = "describe about youtube channel @djnikmumabi"
    inputs = tokenizer(prompt, return_tensors="pt")

    # Generate output
    outputs = model.generate(**inputs, max_new_tokens=100)

    # Decode and print the output text
    print(tokenizer.decode(outputs[0], skip_special_tokens=True))

if __name__ == "__main__":
    main()
