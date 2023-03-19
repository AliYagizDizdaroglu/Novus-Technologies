1) Train to Model (train2modelJupyter.ipynb)

Loads the GPT-2 model and tokenizer, loads the training data from a file, sets up the training parameters, optimizer(AdamW), and scheduler, and trains the model on the text data using batched gradient descent. After training, the fine-tuned model and tokenizer are saved to disk.

Decision: Had to slice the batches into smaller pieces since max sequence length is 1024. So defined a distinct function for this purpose.

Result: Model file created (finetuned_gpt2) with average loss: 8.87


2) Model to Deployment (main.py)

Utilizing the model file via a FastAPI app, input is taken and output is given via get and post methods.

Decision: Added an html input box to better visualize the operation.

Result: Created both .sh and .bat files for both Unix and Windows platforms. App runs on host="127.0.0.1", port=8000

 
Note: Might take up to 30 seconds to produce an output text, please be aware.

