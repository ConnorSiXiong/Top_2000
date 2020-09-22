import numpy as np

def reverseBits(n: int) -> int:
    return 0


sizes = [[0.2, 0.272], [0.37, 0.447], [0.54, 0.619], [0.71, 0.79], [0.88, 0.961]]
ratios = [[1, 0.5]] * 5

pairs = []  # pair of (size, sqrt(ratio))

for r in ratios:
    pairs.append([sizes[0], np.sqrt(r)])
for s in sizes[1:]:
    pairs.append([s, np.sqrt(ratios[0])])

pairs = np.array(pairs)

ss1 = pairs[:, 0] * pairs[:, 1]  # size * sqrt(ration)
ss2 = pairs[:, 0] / pairs[:, 1]  # size / sqrt(retion)
print('ss1', ss1)
print('ss2', ss2)
base_anchors = np.stack([-ss1, -ss2, ss1, ss2], axis=1) / 2
print(base_anchors)

np.meshgrid
np.add
np.argmax