install.packages("rlang")
library(C50)

m1 <- C5.0(output_oversampled[1:3257,-7], output_oversampled[1:3257,7])
m1
summary (m1)
p1 <-predict (m1, output_oversampled[3258:4653,])
p1
table(output_oversampled[3258:4653,7], predicted = p1)
