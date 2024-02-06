##output before smote 90:10
library(C50)


m1 <- C5.0(output[1:4188,-7], output[1:4188,7])
m1
summary (m1)
p1 <-predict (m1, output[4189:4653,])
p1
table(output[4189:4653,7], predicted = p1)
