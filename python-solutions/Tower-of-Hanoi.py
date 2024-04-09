def towerOfHanoi(n: int, src: str, helper: str, dest: str ) -> None:
    if(n == 1):
        print(f"Transfer disk {n} :: From {src} to {dest}")
        return
    
    towerOfHanoi(n-1, src, dest, helper)
    print(f"Transfer disk {n} :: From {src} to {dest}")
    towerOfHanoi(n-1, helper, src, dest)


# Driver Code
n = 4;
towerOfHanoi(n, "S", "H", "D")