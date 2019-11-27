import operator

def get_len(axises, channel, row_or_col=0):
    # row
    if row_or_col == 0:
        index_max, max_ =  max(enumerate(axises[channel]), key=operator.itemgetter(1))
        index_min, min_ =  min(enumerate(axises[channel]), key=operator.itemgetter(1))
    # col
    if row_or_col == 1:
        index_max, max_ =  max(enumerate(axises[channel]), key=operator.itemgetter(1))
        index_min, min_ =  min(enumerate(axises[channel]), key=operator.itemgetter(1))

    return [index_min, index_max], [min_, max_], ((max_ - min_))