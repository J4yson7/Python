if __name__ == "__main__":
    n,m = input().split()

    i = input().split()

    A_like = input().split() 
    B_dlike = input().split()
    like,dlike = 0,0
    for j in range(int(m)):
        if A_like[j] in i:
            like += 1
        if B_dlike[j] in i:
            dlike += 1
    
    print(like - dlike)
    print()