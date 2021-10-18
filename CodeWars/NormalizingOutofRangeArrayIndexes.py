
# Kata = https://www.codewars.com/kata/5285bf61f8fc1b181700024c


def norm_index_test(seq, ind):
    return None if len(seq)== 0  else seq[ind%len(seq)]