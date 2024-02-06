##output before smote 80:20
library(C50)


m1 <- C5.0(output[1:3722,-7], output[1:3722,7])
m1
summary (m1)
p1 <-predict (m1, output[3723:4653,])
p1
table(output[3723:4653,7], predicted = p1)
