for i  in range(2,26):
    with open(f"D:/Python by Harry/Ch9 - File IO/tables/Multiplication table of {i}","w") as f:
        for j in range(1,11):
            f.write(f"{i} * {j} = {i*j}")
            if j!=10:
                f.write('\n')