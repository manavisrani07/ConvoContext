from transformers import pipeline

class QAModel:
    def __init__(self, tqa, ext, question, content):
        self.tqa = tqa
        self.ext = ext
        self.question = question
        self.content = content

    def answer_question(self):
        answer = self.tqa({
            'question': self.question,
            'context': self.content
        })
        return answer

    def answer_csv(self):
        if self.tqa is not None:
            answer = self.tqa(table=self.content, query=self.question)
            return answer
        else:
            return "tqa pipeline not provided."

    def extract_context(self, start_index, end_index):
        content = self.content  # Assuming context is stored in self.context
        while start_index > 0 and content[start_index] != '.':
            start_index -= 1

        while end_index < len(content) and content[end_index] != '.':
            end_index += 1

        extracted_content = content[start_index:end_index]
        max_line_length = 80
        lines = [extracted_content[i:i + max_line_length] for i in range(0, len(extracted_content), max_line_length)]

        return "\n".join(lines)

    def run(self):
        if self.ext == ".csv":
            return None, self.answer_csv()
        else:
            answer = self.answer_question()
            return answer, self.extract_context(answer['start'],answer['end'])
