NOT_FIT = 1         # кандидатка не подходит
FIT = 2             # кандидатка подходит


def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

    # TODO: пользуясь информацией, выведенной на экран в процессе построения
    # дерева решений, запрограммируте классификатор, реализующий логику
    # дерева решений. Используйте для этого простые конструкции if-elif-else, а так же
    # конструкции if-elif-else, вложенные одна в другую там, где это необходимо.
    # Пример:
    # if iq_level <= 70:
    #     answer = NOT_FIT
    # else:
    #     ...

    """
    реализуем через If получившееся дерево.
    
    column 0 <= 70.000000, class = 1
    column 0 >  70.000000, 
      column 1 == 1.000000, class = 2
      column 1 == 2.000000, 
        column 3 <= 2.200000, class = 2
        column 3 >  2.200000, class = 1

    """

    if iq_level<=70:
        answer=1
    elif articles_count==1:
        answer=2
    elif articles_count==2:
        if ratio<=2.2:
            answer=2
        else:
            answer=1

    return answer
