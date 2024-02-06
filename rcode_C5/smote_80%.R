##output after smote 80:30
library(C50)
output_oversampled2$LeaveOrNot <- as.factor(output_oversampled2$LeaveOrNot)
m1 <- C5.0(output_oversampled2[1:3430,-7], output_oversampled2[1:3430,7] , trials = 15)
m1
summary (m1)
p1 <-predict (m1, output_oversampled2[3431:4288,])
p1
table(output_oversampled2[3431:4288,7], predicted = p1)

