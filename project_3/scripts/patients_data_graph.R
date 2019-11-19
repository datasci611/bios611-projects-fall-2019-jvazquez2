# This code creates the distributions age per disability attainted while at UMD

library(tidyverse)
library(ggplot2)

my_patient_data = read_csv("patients_data_graph.csv")

patient_plot = ggplot(my_patient_data, aes(x=my_patient_data$`Disability Type`, y = my_patient_data$`Client Age at Entry`)) +
  geom_boxplot(fill='#00BFC4') +
  theme_minimal() +  
  labs(title = "Distributions of Age for Patients who got a Disability while at UMD", subtitle = 'Per type of Disability', y = 'Age', x = 'Disability Type') +
  theme(axis.text.x = element_text(angle = 45, hjust = 1))

ggsave('agedist.png', patient_plot)
