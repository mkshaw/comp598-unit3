
def generate_fib_sequence(seq_length):
    """
    Produce a list of length seq_length that contains
    the start of the fibonacci sequence.

    seq_length has minimum length 2.
    """

    if seq_length <= 1:
            raise Exception('seq_length must be > 1')

    values = [1, 1]
    for i in range(seq_length - 2):
        values.append(values[-1] + values[-2])

    return values
