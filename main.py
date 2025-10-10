from tqdm.notebook import tqdm
import itertools

def experiment_and_analyze(seq1, seq2, match_values, mismatch_values, gap_values):
    results = []

    param_combinations = itertools.product(match_values, mismatch_values, gap_values)

    for match, mismatch, gap in tqdm(param_combinations):
        align1, align2, dp = needleman_wunsch(seq1, seq2, match, mismatch, gap)

        matches, mismatches, gaps = 0, 0, 0
        for i in range(len(align1)):
            if align1[i] == align2[i]:
                matches += 1
            else:
                if align1[i] == '-' or align2[i] == '-':
                    gaps += 1
                else:
                    mismatches +=1 

        results.append({
            "match": match,
            "mismatch": mismatch,
            "gap": gap,
            "score": dp,
            "matches": matches,
            "mismatches": mismatches,
            "gaps": gaps,
            "alignment": (align1, align2) 
        })
    return results 



seq1 = "GATTACA"
seq2 = "GCATGCU"
match_values = [2, 1, 0]
mismatch_values = [-1, -2]
gap_values = [-1, -2, -3]

results = experiment_and_analyze(seq1, seq2, match_values, mismatch_values, gap_values)


print("Results:")
for result in results:
    print(f"Match: {result['match']}, Mismatch: {result['mismatch']}, Gap: {result['gap']}, Score: {result['score']}, Matches: {result['matches']}, Mismatches: {result['mismatches']}, Gaps: {result['gaps']}")
    print(f"Alignment: {result['alignment']}")


# 2. Используя numpy создайте матрицу 7 на 7

import numpy as np

empty_arr = np.empty((7, 7))
zeros_arr = np.zeros((7, 7))
ones_arr = np.ones((7, 7))
random_arr = np.random.randint(0, 100, (7, 7))

print(empty_arr, zeros_arr, ones_arr, random_arr, sep='\n\n')

# 3. NumPy: создайтие диагональную матрицу, где по главной диагонали идут числа от 1 до 5

diag_mat = np.diag(np.arange(1, 6))
diag_mat


def is_identity_matrix_np(matrix):
    return np.array_equal(matrix, np.eye(len(matrix)))

print(f'Для единичной матрицы: {is_identity_matrix_np(np.eye(5))}')
print(f'Для НЕ единичной матрицы: {is_identity_matrix_np(np.random.randint(0, 100, (7, 7)))}')