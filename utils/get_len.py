import operator

def get_len(matrix, command='vector', channel=0):
    # row
    if command == 'row':
        index_max, max_ =  max(enumerate(matrix[channel]), key=operator.itemgetter(1))
        index_min, min_ =  min(enumerate(matrix[channel]), key=operator.itemgetter(1))
        return [index_min, index_max], [min_, max_], ((max_ - min_))
    # col
    if command == 'col':
        index_max, max_ =  max(enumerate(matrix[:, channel]), key=operator.itemgetter(1))
        index_min, min_ =  min(enumerate(matrix[:, channel]), key=operator.itemgetter(1))
        return [index_min, index_max], [min_, max_], ((max_ - min_))

    # vector
    if command == 'vector':
        index_max, max_ =  max(enumerate(matrix), key=operator.itemgetter(1))
        index_min, min_ =  min(enumerate(matrix), key=operator.itemgetter(1))
        return [index_min, index_max], [min_, max_], ((max_ - min_))
        
    return False