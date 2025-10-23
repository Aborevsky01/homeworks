%%R
library(readxl)

patients <- read_excel("./Пациенты.xlsx")

str(patients$Возраст)
str(patients$глюкоза)

patients$Пол <- factor(patients$Пол, levels = c("м", "ж"))
print(levels(patients$Пол))

patients$возраст_группа <- ifelse(patients$Возраст <= 60, "Молодые", "Старшие")

print(patients[patients$Возраст > 75, ])

head(patients$лейкоциты)
head(patients$глюкоза)
summary(patients$лейкоциты)
summary(patients$глюкоза)

aggregate(глюкоза ~ Пол, data = patients, FUN = mean)

aggregate(лейкоциты ~ Пол + возраст_группа, data = patients, FUN = mean)

aggregate(глюкоза ~ Пол, data = patients, 
          FUN = function(x) c(среднее = mean(x), отклонение = sd(x), наблюдения = length(x)))

boxplot(глюкоза ~ Пол, data = patients,
        main = "Глюкоза по полу", xlab = "Пол", ylab = "глюкоза")

test_result <- t.test(лейкоциты ~ Пол, data = patients)
print(test_result)

patients_task <- patients
patients_task$глюкоза[c(3, 15, 45)] <- NA

print(sum(is.na(patients_task)))

print(which(is.na(patients_task$глюкоза)))

patients_full <- na.omit(patients_task)
print(dim(patients_task))
print(dim(patients_full))

patients_task$глюкоза[is.na(patients_task$глюкоза)] <- median(patients_task$глюкоза, na.rm = TRUE)

print(aggregate(лейкоциты ~ Пол, data = patients_task, FUN = mean, na.rm = TRUE))
print(aggregate(лейкоциты ~ Пол, data = patients_full, FUN = mean))

hemoglobin_stats <- aggregate(гемоглобин ~ возраст_группа, data = patients, 
                             FUN = function(x) c(среднее = mean(x),станд_отклонение = sd(x)))

result_table <- data.frame(
  возраст_группа = hemoglobin_stats$возраст_группа,
  гемоглобин_среднее = hemoglobin_stats$гемоглобин[, "среднее"],
  гемоглобин_отклонение = hemoglobin_stats$гемоглобин[, "станд_отклонение"]
)

write.csv(result_table, "анализ_гемоглобина.csv", row.names = FALSE)