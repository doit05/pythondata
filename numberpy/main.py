import numpy as np

def main():
    a = np.array([1,2,3])
    b = np.array([[1,3,5],[2,4,6],[7,8,9]])
    print(a.data)
    print(a.shape)
    print(b.shape)
    print(a.dtype)
    print(b)

if __name__ == "__main__":
    main()
