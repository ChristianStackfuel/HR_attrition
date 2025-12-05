# EDA notes
## Overview inspection
* no duplicates
* no missing values
* *Attrition* **(TARGET)**: binary -> [0, 1]
* binary cats: *Attrition, Gender, Over18, OverTime*
* ordinal ints: *Education, EnvironmentSatisfaction, JonInvolvement, JobLevel, JobSatisfaction, NumCompaniesWorked, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TrainingTimesLastYear, WorkLifeBalance*
* **ignore** (no variance): *EmployeeCount, Over18, StandardHours*
* **ignore** (ID): *EmployeeNumber*

## frequency distributions
* done, notes updated
#### columns for value distributions
* *Age* (logarithmic?)
* *BusinessTravel* (transform zu metric)
* *JobInvolvement*
* *JobSatisfaction*
* *MonthlyIncome*
* *MonthlyRate
* *TotalWorkingYears*
## value distributions
* done, notes updated
## Correlations
* no strong immediate correlations ~ *Attrition*
* multicolinearities: 
    * *JobLevel ~ MonthlyIncome*
    * *PerformanceRating ~ PercentSalaryHike*
* Correlation group: *"Years" ~ JobLevel ~ MonthlyIncome*
## Baseline model
* target is unbalanced (84:16 = ~5:1)
### Use columns
#### categorical
* *BusinessTravel*
* *Education*
* *EducationField*
* *EnvironmentSatisfaction*
* *JobLevel*
* *JobRole*
* *JobSatisfaction*
* *MaritalStatus*
* *RelationshipSatisfaction*
* *StockOptionLevel*
* *TrainingTimesLastYear*
* *WorkLifeBalance*
#### metric
* *Age*
* *JobInvolvement*
* *OverTime*
* *TotalWorkingYears*
* *YearsInCurrentRole*
* *MonthlyIncome
* *YearsWithCurrentManager*
* *YearsAtCompany*
## Data cleaning & preparation
* *Attrition, OverTime*: -> [0, 1]
## Model Optimization
### Feature Engineering & Selection
* *BusinessTravel*: Transform to metric
* *MaritalStatus*: Transform to metric
* *YearsAtCompany* < 5
* *Age* < 34
* *YearsWithCurrentManager* < 8
* Test logarithmic rescaling of *Age*
* "*EnvironmentSatisfaction Is 1*"
* "*RelationshipSatisfaction Is 1*"
* "*WorkLifeBalance Is 1*"
* "*NumCompaniesWorked* ==1 or >=5
* *TotalWorkingYears* but grouped
* *MonthlyIncome* vs. "expectedIncome" (linReg *MobthlyIncome ~ TotalWorkingYears*)
* sum("ordinals")
* *JobLevel* vs. *MontthlyIncome*: [both, either, PCA]
* *PercentSalaryHike* vs. *PerformanceRating*: [both, either, PCA]
* *"Years"*: PCA
* *DistanceFromHome*
