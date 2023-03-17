# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    laiks = [0] * n
    idx = 0
    while idx < m:
        next = 0
        for i in range (1, n):
            if laiks[i] < laiks[next]:
                next = i
        output.append((next, laiks[next]))
        laiks[next] = laiks[next] + data[idx]
        idx = idx + 1
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for pair in result:
        print(pair[0], pair[1])



if __name__ == "__main__":
    main()
