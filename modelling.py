from transformers import BertTokenizer, BertForQuestionAnswering, pipeline

class ModelSelector:
    def __init__(self, file_extension):
        self.file_extension = file_extension
        self.tqa = None
        self.model_name = None
        self.tokenizer = None
        self.model = None

        if self.file_extension == ".csv":
            self.initialize_csv_model()
        else:
            self.initialize_other_model()

    def initialize_csv_model(self):
        self.model_name = "google/tapas-base-finetuned-wtq"
        self.tqa = pipeline(task="table-question-answering", model=self.model_name)

    def initialize_other_model(self):
        self.model_name = 'deepset/bert-base-cased-squad2'
        self.tokenizer = BertTokenizer.from_pretrained(self.model_name)
        self.model = BertForQuestionAnswering.from_pretrained(self.model_name)
        self.tqa = pipeline("question-answering", model=self.model, tokenizer=self.tokenizer)

    def get_tqa_model(self):
        return self.tqa

    def get_model_name(self):
        return self.model_name

    def get_tokenizer(self):
        return self.tokenizer

    def get_model(self):
        return self.model

