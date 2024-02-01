def get_min_flow(mat, tmpPath):
    return min([mat[tmpPath[i]][tmpPath[i+1]] for i in range(len(tmpPath)-1)])


def update_matrice(mat, tmpPath, tmpFlow):
    for i in range(len(tmpPath)-1):
        mat[tmpPath[i]][tmpPath[i+1]] -= tmpFlow
        mat[tmpPath[i+1]][tmpPath[i]] += tmpFlow


def get_one_path(mat):
    """
    Algorithme de recherche de chemin
    """
    visited = [False for i in range(len(mat))]
    visited[0] = True
    tmpPath = [0]
    while tmpPath:
        tmp = tmpPath[-1]
        if tmp == len(mat)-1:
            return tmpPath
        for i in range(len(mat)):
            if mat[tmp][i] > 0 and not visited[i]:
                tmpPath.append(i)
                visited[i] = True
                break
        else:
            tmpPath.pop()
    return None


def get_flow(mat):
    maxFlow = 0
    tmpPath = get_one_path(mat)
    while tmpPath is not None:
        tmpFlow = get_min_flow(mat, tmpPath)
        maxFlow += tmpFlow
        update_matrice(mat, tmpPath, tmpFlow)
        tmpPath = get_one_path(mat)
    return maxFlow


if __name__ == "__main__":
    """
    Algorithme de Ford-Fulkerson
    """
    mat = [[0, 6, 8, 0, 0, 0], [0, 0, 0, 6, 3, 0], [0, 0, 0, 3, 3, 0], [0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0]]
    print(get_flow(mat))