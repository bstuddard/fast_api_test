from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

def download_model():
    task='sentiment'
    MODEL = f"cardiffnlp/twitter-roberta-base-{task}"

    tokenizer = AutoTokenizer.from_pretrained(MODEL, cache_dir='./pretrained')
    model = AutoModelForSequenceClassification.from_pretrained(MODEL, cache_dir='./pretrained')

    return tokenizer, model


if __name__ == '__main__':
    tokenizer, model = download_model()
    print('main download completed.')