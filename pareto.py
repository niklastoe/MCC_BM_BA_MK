import numpy as np

def all_elements_are_pos_or_neg_1(vector):
    sign_check = [x in [-1, 1] for x in vector]
    if sum(sign_check) == len(sign_check):
        return True
    else:
        return False

def pareto_frontier_multi(sel_array, sign_vector=None):
    """return the pareto front for an array.
    sign vector denotes if better means bigger or smaller
    taken and extended from http://code.activestate.com/recipes/578287-multidimensional-pareto-front/
    Input must be of shape (entries, dimensions)

    # >>> pareto_frontier(np.array([0,]))
    """

    # sign vector determines which pareto front is determined
    dimensionality = sel_array.shape[1]

    if sign_vector != None:
        if len(sign_vector) != dimensionality:
            raise ValueError(
                'The sign vector passed must correspond to the %s dimensions of the array!' % str(dimensionality))
        elif not all_elements_are_pos_or_neg_1(sign_vector):
            raise ValueError('Sign vector may only contain -1 and +1!!')
    else:
        sign_vector = [1] * dimensionality

    sign_vector[0] = sign_vector[0] * -1
    sel_array = sel_array * sign_vector

    # Sort on first dimension, descending
    first_dimension_sorted_max_to_min = sel_array[:, 0].argsort()
    sel_array = sel_array[first_dimension_sorted_max_to_min]

    # Add first row to pareto_frontier
    pareto_frontier = sel_array[0:1, :]
    # Test next row against the last row in pareto_frontier
    for row in sel_array[1:, :]:
        evaluation_vector = [row[x] >= pareto_frontier[-1][x] for x in range(len(row))]
        # in the first dimension, it will always be smaller. If it is better on all other features,
        # add the row to pareto_frontier
        if sum(evaluation_vector) == dimensionality:
            pareto_frontier = np.concatenate((pareto_frontier, [row]))

    # restore original output by multiplying with sign vector
    pareto_frontier = pareto_frontier * sign_vector

    return pareto_frontier
