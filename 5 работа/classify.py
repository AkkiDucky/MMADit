NOT_FIT = 1         
FIT = 2             


def classify(X):
    answer = 0
    iq_level, articles_count, has_education, ratio = X

   

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
