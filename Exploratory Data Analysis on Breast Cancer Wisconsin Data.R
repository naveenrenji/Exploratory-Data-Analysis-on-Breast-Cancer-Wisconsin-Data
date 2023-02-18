rm(list=ls())

library(dplyr)
library(readr)
library(ggplot2)
library(tidyr)
library(GGally)


# Load dataset and remove rows with missing values
df <- read_csv("breast-cancer-wisconsin.csv") %>%
  drop_na()

num_rows <- nrow(df)
cat("Number of rows:", num_rows, "\n")

# Summarize each column
df$F6 <- as.numeric(df$F6)
summary(df)

summary(df$F2)
summary(df$F3)
summary(df$F4)
summary(df$F5)
summary(df$F6)
summary(df$F7)
summary(df$F8)
summary(df$F9)
summary(df$Class)

# Replace missing values with mean of column
df$F6[is.na(df$F6)] <- mean(df$F6, na.rm = TRUE)

# Frequency table of Class vs F6
freq_table <- table(df$Class, df$F6)
freq_table

# Scatter plot of F1 to F6
columns <- c('F1', 'F2', 'F3', 'F4', 'F5', 'F6')
scatter_matrix <- ggpairs(df[columns])
scatter_matrix

# Box plot for columns F7 to F9
df[,7:9] %>%
  gather %>%
  ggplot(aes(key, value)) +
  geom_boxplot()

# Histogram plot for columns F7 to F9
df[,7:9] %>%
  gather %>%
  ggplot(aes(value)) +
  geom_histogram()

