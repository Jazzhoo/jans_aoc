import numpy as np

with open("input_files/input.txt", "r") as f:
    heatmap = f.readlines()

heatmap_array = []

for line in heatmap:
    heatmap_array.append([int(a) for a in line.strip()])
ha = np.array(heatmap_array)

shape = ha.shape
result = 0

for i in range(shape[0]):
    for j in range(shape[1]):
        if i == 0:
            if j == 0:
                if ha[i, j] > ha[i, j+1] or ha[i, j] > ha[i+1, j]:
                    result += (1 + ha[i, j])
            elif j == shape[1] - 1:
                if ha[i, j] < ha[i, j-1] and ha[i, j] < ha[i+1, j]:
                    result += (1 + ha[i, j])
            else:
                if ha[i, j] < ha[i, j+1] and ha[i, j] < ha[i, j-1] and ha[i, j] < ha[i+1, j]:
                    result += (1 + ha[i, j])
        elif i == shape[0] - 1:
            if j == 0:
                if ha[i, j] < ha[i, j+1] and ha[i, j] < ha[i-1, j]:
                    result += (1 + ha[i, j])
            elif j == shape[1] - 1:
                if ha[i, j] < ha[i, j-1] and ha[i, j] < ha[i-1, j]:
                    result += (1 + ha[i, j])
            else:
                if ha[i, j] < ha[i, j+1] and ha[i, j] < ha[i, j-1] and ha[i, j] < ha[i-1, j]:
                    result += (1 + ha[i, j])
        else:
            if j == 0:
                if ha[i, j] < ha[i, j+1] and ha[i, j] < ha[i+1, j] and ha[i, j] < ha[i-1, j]:
                    result += (1 + ha[i, j])
            elif j == shape[1] - 1:
                if ha[i, j] < ha[i, j - 1] and ha[i, j] < ha[i + 1, j] and ha[i, j] < ha[i - 1, j]:
                    result += (1 + ha[i, j])
            else:
                if ha[i, j] < ha[i, j - 1] and ha[i, j] < ha[i, j + 1] and ha[i, j] < ha[i + 1, j] and ha[i, j] < ha[i - 1, j]:
                    result += (1 + ha[i, j])
        pass ## TODO: continue with i iter

print(f"The result is: {result}")

