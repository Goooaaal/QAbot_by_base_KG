import synonyms
import input_QA
import pandas
import nltk



def question():
    return input('您的问题是:')

def answer():
    answer_sequence = input_QA.input_file(file_path='crawler.csv')
    return answer_sequence


if __name__ == '__main__':
    question_sequence = question()
    answer_sequence = answer()
    score_dict = dict()
    for i in answer_sequence.keys():
        value = synonyms.compare(question_sequence, i, seg=True)
        score_dict[i] = value
        new_scoredict = sorted(score_dict.items(), key=lambda item: item[1])[-1]
    print(type(new_scoredict))
    #     list = list(new_scoredict)[0]
    #     answer_sequence_sub = answer_sequence[list]
    # print(answer_sequence_sub)
