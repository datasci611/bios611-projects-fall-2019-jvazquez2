# This code creates the comparative distributions graph

library(tidyverse)
library(ggplot2)

my_tax_data = read_csv("tax_data_graph.csv")

tax_plot = ggplot(data=my_tax_data, aes(x=Number, y=value, fill=variable)) +
  geom_bar(stat="identity", color="black", position=position_dodge()) + theme_minimal() +
  labs(title = "Urban Ministries of Durham - 2006-2018 Tax Fraud Analysis", subtitle = 'Net-Income', y = 'Percentage (%)', fill = "Group") +
  scale_x_continuous("Digit", labels = as.character(my_tax_data$Number), breaks = my_tax_data$Number)

ggsave('taxplot.png', tax_plot)