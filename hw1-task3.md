# Homework 1 Task 3

---

Answer the following questions based on exercises from *An Introduction to Statistical Learning with Applications in Python*.

## Chapter 2.4 Exercises

---

### Exercise 1 (ISLP exercise 2)

Explain whether each scenario is a **classification or regression** problem, and indicate whether we are most interested in **inference or prediction**. Finally, provide **n** (size of observation dataset) and **p** (number of predictors).

**(a)**  We collect data on 200 protected marine reserves worldwide. For each reserve we record species richness, reserve size, years since establishment, enforcement budget, and proximity to human settlements. We are interested in understanding which factors affect species richness.

> This is a classification problem because we are attempting to determine **which** factors affect species richness from the list of variables. This is an inference question because we are attempting to understand what factors influence species richness in 200 protected marine reserves worldwide. The observation dataset is 200 and the number of predictors is 4 (reserve size, years since establishment, enforcement budget, and proximity to human settlements).

---

**(b)** A conservation agency wants to know whether a proposed habitat corridor will successfully support wildlife movement or fail to do so. They collect data on 30 previously established corridors. For each corridor they have recorded whether wildlife movement was successful or unsuccessful, corridor width, length, surrounding land use type, and eight other variables.

> This is a classification problem because the outcome answer would be either success or failure. This is a prediction question because we are trying to determine the outcome of a proposed habitat corridor based on the outcomes of existing corridors. The size of the observation dataset is 30 and the number of predictors is 11 (corridor width, length, surrounding land use type, and eight other variables).

---

**(c)** We are interested in predicting weekly average ground-level ozone concentration in a coastal city. We collect weekly data for all of 2019. For each week we record average ozone concentration, sea surface temperature, wind speed, solar radiation, and atmospheric

> This is a regression problem because the question is asking for a correlation between the weekly average ground-level ozone concentration in a coastal city and the given variables. This is a prediction question because this is based on 2019 data presumably being used to predict present a future weekly average ground-level ozone concentration in a coastal city. The size of the observation dataset is the number of weeks in 2019, 52 weeks, and the number of predictors is 4 (sea surface temperature, wind speed, solar radiation, and atmospheric). 

---

### Exercise 2 (ISLP exercise 5)

What are the advantages and disadvantages of a very flexible (versus a a less flexible) approach for regression? Under what circumstances might a more flexible approach be preferred to a less flexible approach? When might a less flexible approach be preferred?

> There is a bias-variance tradeoff between very fleixble and less flexible models. More flexible models have lower bias and higher variance, while less flexible models have higher bias and lower variance. The concept of model flexibility is tied to the fit of a model. Flexible models are better when there is less data while a less flexible model could be better when more data is available. A less flexible model can overfit few data points if there isn't enough points to define true trends. With few data points it is also difficult to determine if any outliers exist which can skew a model. If there is a large amount of data, a less flexible model could provide better detail into true trends. 

> A more flexible model would also be better suited to answering prediction questions as we would be interested in the accuracy of the model for a test dataset which is separated before using the dataset to create the model. A less flexible model could work better to answer an inference question. The model would not need to be run on an additional dataset and could be used to understand the current trend of the data being studied. Models work best on the data from which they are created. A key takeaway to determine whether a very flexible or less model needs to be fit is whether the model needs to be run on data other than the one it is created from. Overall, it is best to find a model where both variance and bias are reasonably low.

---

### Exercise 3 (ISLP exercise 6)

Describe the differences between a **parametric** and a **non-parametric** statistical learning approach. What are the **advantages** of a parametric approach to regression or classification (as opposed to a non-parametric approach)? What are its **disadvantages**?

> Parametric statistical learning is created by first pre-determining what shape or form a function will take. Then the model is fit using the training data. The parametric approach simplifies the task of estimating the function to the task of only needing to estimate parameters. It is simpler to estimate parameters than to estimating an entire function. The pitfall of the parametric approach is that if the assumption of the model is wrong then the estimates can be poor. This pitfall can be overcome by making the model more flexible by adding more parameters. However, using too many parametes can lead to overfitting the data. 

> Non-parametric statistical learning does not assume the model's shape and creates an estimate of the function based on the data. The benefit of a non-parametric approach is that no assumptions need to be made before analyzing the data. This avoids the potential pitfall of the parametric approach that defining a shape as an assumption can mis-predetermine a function's form. The pitfall of a non-parametric statistical learning approach is that it needs much more data to calculate an accurate function. 