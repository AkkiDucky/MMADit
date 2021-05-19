import numpy as np

NOT_FIT = 1         
FIT = 2            

NUMERICAL = 0       
CATEGORICAL = 1    


def decision_tree(X, Y, scale, level=0):
    
    if len(np.unique(Y))==1:
       print('class = %d' % Y[0])
       return

    print('')

    n = X.shape[1]  
    m = X.shape[0]  

   
    info = Info(Y)

    gain = []
    thresholds = np.zeros(n)

    
    for i in range(n):

        if scale[i] == CATEGORICAL:   

           

            info_s = 0
           
            unique, counts = np.unique(X[:, i], return_counts=True)
            
            uniq_dict = dict(zip(unique, counts))

            
            for uniq in uniq_dict: 
                info_s += (uniq_dict[uniq]/m)*Info(Ycut)
            gain.append(info - info_s)
            #

        else:
            val = np.sort(X[:, i])

            local_gain = np.zeros(m - 1)

            
            for j in range(m - 1):
                threshold = val[j]
                less = sum(X[:, i] <= threshold)  
                greater = m - less  

                # вычисляем информативность признака при данном пороге
                info_s = (less / m) * Info(Y[X[:, i] <= threshold]) + (greater / m) * Info(Y[X[:, i] > threshold])

                local_gain[j] = info - info_s

            gain.append(np.max(local_gain, axis=0))
            idx = np.argmax(local_gain, axis=0)

            thresholds[i] = val[idx]

    
    max_idx = np.argmax(gain)

    if scale[max_idx] == CATEGORICAL:
        
        categories = np.unique(X[:, max_idx])

        for category in categories:
            
            sub_x = X[X[:, max_idx] == category, :]
            sub_y = Y[X[:, max_idx] == category]

            print_indent(level)
            print('column %d == %f, ' % (max_idx, category), end='')

            decision_tree(sub_x, sub_y, scale, level + 1)
    else:
        
        threshold = thresholds[max_idx]

        sub_x = X[X[:, max_idx] <= threshold, :]
        sub_y = Y[X[:, max_idx] <= threshold]

        print_indent(level)
        print('column %d <= %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)

        sub_x = X[X[:, max_idx] > threshold, :]
        sub_y = Y[X[:, max_idx] > threshold]

        print_indent(level)
        print('column %d >  %f, ' % (max_idx, threshold), end='')

        decision_tree(sub_x, sub_y, scale, level + 1)



def Info(set):
    m = len(set)
    info = 0

    if m > 0:
    
        unique,counts =np.unique(set,return_counts=True)
       
        uniq_dict = dict(zip(unique, counts))

       
        for item in uniq_dict:
            
            p= uniq_dict[item]/m
           
            info += (p)*np.log2(p)

    return -info

def print_indent(level):
    print(level * '  ', end='')
