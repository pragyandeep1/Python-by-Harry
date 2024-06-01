content = True
i = 0
with open('log.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print("\n"+content)
            print(f"There is python on line number {i}\n")
        i+=1