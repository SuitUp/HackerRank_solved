if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    # length_dictionary for mpping name with count of marks
    length_student_marks = {name: len(scores) for name, scores in student_marks.items()}

    for key, values in student_marks.items():
        if key == query_name:
            #avg = 0
            sum_scores = 0
            for value in values:
                sum_scores += value 
            len_scores = length_student_marks[query_name]
            avg = sum_scores/len_scores
            print('{0:.2f}'.format(avg))
