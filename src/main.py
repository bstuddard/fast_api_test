import torch
from scipy.special import softmax
from fastapi import FastAPI, Security
from src.preprocess_helpers import preprocess
from src.setup_model import download_model
from src.api_schemas import TextClassificationInput, ResponseDict
from src.security import auth_api_key

# Start up app
app = FastAPI()

# Ready model - model download cached during docker build
tokenizer, model = download_model()

# Label values from repo, hardcoded for runtime
labels=['negative', 'neutral', 'positive']


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post('/score/', response_model=ResponseDict)
def score(input_data: TextClassificationInput, api_key: str = Security(auth_api_key)):

    # Process user input strings - make required string subs and tokenize
    user_input_list = input_data.input_text_list
    processed_user_input_list = [preprocess(single_input_string) for single_input_string in user_input_list]
    encoded_input = tokenizer(processed_user_input_list, padding=True, return_tensors='pt')

    # Run through model and normalize
    with torch.no_grad():
        scores = model(**encoded_input)[0].detach().numpy()
    scores_normalized = softmax(scores, axis=1).tolist()

    # Bind to original data (input text after processing: scores)
    output_dict = {}
    for text, scores in zip(processed_user_input_list, scores_normalized):
        scores_dict = {k:v for k,v in zip(labels, scores)}
        output_dict[text] = scores_dict

    return {'output': output_dict}