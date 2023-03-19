from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from transformers import GPT2LMHeadModel, GPT2Tokenizer

app = FastAPI()

# Load the fine-tuned GPT-2 model and tokenizer
model = GPT2LMHeadModel.from_pretrained("finetuned_gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("finetuned_gpt2")

# Set the maximum sequence length
MAX_LENGTH = 1024

@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
        <html>
            <body>
                <h1>Text Generation with GPT-2</h1>
                <form action="/generate_text/" method="post">
                    <label for="prompt">Prompt:</label><br>
                    <input type="text" id="prompt" name="prompt" required><br><br>
                    <input type="submit" value="Generate Text">
                </form>
            </body>
        </html>
    """

@app.post("/generate_text/")
async def generate_text(prompt: str = Form(...)):
    # Encode the prompt using the tokenizer
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    
    # Create the attention mask
    attention_mask = input_ids.ne(tokenizer.eos_token_id).long()

    # Generate text with the model
    output = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_length=MAX_LENGTH,
        pad_token_id=tokenizer.eos_token_id,
        temperature=0.7,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.0,
        num_return_sequences=1,
    )

    # Decode the generated text and return it
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return {"generated_text": generated_text}

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)