motifs2 <- matrix(c(
  "a", "C", "g", "G", "T", "A", "A", "t", "t", "C", "a", "G",
  "t", "G", "G", "G", "C", "A", "A", "T", "t", "C", "C", "a",
  "A", "C", "G", "t", "t", "A", "A", "t", "t", "C", "G", "G",
  "T", "G", "C", "G", "G", "G", "A", "t", "t", "C", "C", "C",
  "t", "C", "G", "a", "A", "A", "A", "t", "t", "C", "a", "G",
  "A", "C", "G", "G", "C", "G", "A", "a", "t", "T", "C", "C",
  "T", "C", "G", "t", "G", "A", "A", "t", "t", "a", "C", "G",
  "t", "C", "G", "G", "G", "A", "A", "t", "t", "C", "a", "C",
  "A", "G", "G", "G", "T", "A", "A", "t", "t", "C", "C", "G",
  "t", "C", "G", "G", "A", "A", "A", "a", "t", "C", "a", "C"
), nrow = 10, byrow = TRUE)

z <- toupper(motifs2)

cat(z)

f <- function(x) {
  sapply(c("A","C","G","T"), function(y) sum(x==y))
}

cnt_matrix <- do.call(rbind, lapply(1:ncol(z), function(j) f(z[,j])))
prf_matrix <- cnt_matrix / nrow(z)

scr <- function(m) {
  sum(sapply(1:ncol(m), function(j) max(f(m[,j]))))
}

sc <- scr(z)

cs <- function(m) {
  sapply(1:ncol(m), function(j) {
    u <- c("A","C","G","T")
    x <- m[,j]
    w <- sapply(u, function(y) sum(x==y))
    u[which.max(w)]
  })
}

cns <- cs(z)
cat(paste(cns, collapse=""), "\n")

bp <- table(z[,1])
barplot(bp, col="skyblue", main="Частоты нуклеотидов в 1-м столбце")
