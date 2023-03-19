1) Train to Model (train2model.py)

Loads the GPT-2 model and tokenizer, loads the training data from a file, sets up the training parameters, optimizer, and scheduler, and trains the model on the text data using batched gradient descent. After training, the fine-tuned model and tokenizer are saved to disk.

Decision: Had to slice the batches into smaller pieces since max sequence length is 1024. So defined a distinct function for this purpose.

