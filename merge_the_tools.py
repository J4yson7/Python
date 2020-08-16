if __name__ == "__main__":
    n = int(input())

    alp = "abcdefghijklmnopqrstuvwxyz"

    rang = [alp[n-i:n][::-1] + alp[(n-1)-i:n] for i in range(n)]

    rang2 = ["-".join(i).center(len("-".join(rang[n-1])), "-") for i in list(rang + list(rang.__reversed__())[1:])] 
    print("\n".join(rang2))

    
    
