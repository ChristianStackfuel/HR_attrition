# Project notes
## EDA
### Notes for EDA
* no duplicates
* no missing values
* *Attrition* **(TARGET)**: binary -> [0, 1]
* binary cats: *Attrition, Gender, Over18, OverTime*
* ordinal ints: *Education, EnvironmentSatisfaction, JonInvolvement, JobLevel, JobSatisfaction, NumCompaniesWorked, PerformanceRating, RelationshipSatisfaction, StockOptionLevel, TrainingTimesLastYear, WorkLifeBalance*
* **ignore** (no variance): *EmployeeCount, Over18, StandardHours*
* **ignore** (ID): *EmployeeNumber*

## Baseline model
* target is unbalanced (84:16 = ~5:1)
### Use columns
### Data CLeaning
* *Attrition, OverTime*: -> [0, 1]

## Model Optimization
#### Try columns
