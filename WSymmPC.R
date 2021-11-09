# Weighted Symmetric pivot coordinates 
# date: '7/23/2021'
# author: 'XuCpeng'

require("compositions")

weightSymmPivotCoord = function(x_o, pivotvar1 = 1, pivotvar2 = 2) {

    D = ncol(x_o)

    # Sort, put pivotvar1 in column 1 and pivotvar2 in column 2
    x = cbind(x_o[, pivotvar1], x_o[, pivotvar2], x_o[, c(-pivotvar1, -pivotvar2)])

    # Using classical variation matrix
    var = compositions::variation(acomp(x))
    tj1 = var[, 1]
    tj2 = var[, 2]

    # a～
    a_v = 1/tj1[c(-1, -2)]^2
    # b～
    b_v = 1/tj2[c(-1, -2)]^2

    # a*
    a_ = a_v/sum(a_v)
    # b*
    b_ = b_v/sum(b_v)

    # y*
    y_ = sum(a_ * b_)/2

    # c
    c = (-1 + sqrt(1 + 4 * y_))/(2 * y_)

    # y
    y = (c^2) * y_

    # a
    a = c * a_
    # b
    b = c * b_

    # A1
    A1 = 1/sqrt(1 + (y^2) + sum(a^2))
    # A2
    A2 = 1/sqrt(1 + (y^2) + sum(b^2))

    # ws1
    p1 = x[, 2]^y
    for (i in (3:D)) {
        p1 = p1 * (x[, i]^a[i - 2])
    }

    ws1 = A1 * log(x[, 1]/p1)

    # ws2
    p2 = x[, 1]^y
    for (i in (3:D)) {
        p2 = p2 * (x[, i]^b[i - 2])
    }

    ws2 = A2 * log(x[, 2]/p2)

    return(list(ws1 = ws1, ws2 = ws2))
}


