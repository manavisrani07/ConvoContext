from transformers import BertTokenizer, BertForQuestionAnswering, pipeline

class QAModel:
    def __init__(self, model, tokenizer, tqa):
        self.tokenizer = tokenizer
        self.model = model
        self.qa_pipeline = pipeline('question-answering', model=self.model, tokenizer=self.tokenizer)
        self.tqa = tqa

    def answer_question(self, question, context):
        answer = self.qa_pipeline({
            'question': question,
            'context': context
        })
        return answer

    def answer_csv(self, question, context):
        if self.tqa is not None:
            answer = self.tqa(table=context, query=question)
            return answer
        else:
            return "tqa pipeline not provided."

class ContentExtractor:
    @staticmethod
    def extract_context(content, start_index, end_index):
        # Move the start index backward until a period (".") is found or the start of the content
        while start_index > 0 and content[start_index] != '.':
            start_index -= 1

        # Extend the end index until a period (".") is found or the end of the content
        while end_index < len(content) and content[end_index] != '.':
            end_index += 1

        # Extract the identified content
        extracted_content = content[start_index:end_index]  # +1 to exclude the period

        # Split the content into multiple lines
        max_line_length = 80  # Adjust the line length as needed
        lines = [extracted_content[i:i + max_line_length] for i in range(0, len(extracted_content), max_line_length)]

        return "\n".join(lines)
