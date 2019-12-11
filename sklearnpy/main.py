from sklearn import linear_model

def main():
    reg = linear_model.LinearRegression()
    reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
    # linear_model.LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
    reg.coef_
    print(reg.coef_)
if __name__ == "__main__":
    main()  
