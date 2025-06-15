# Data Dictionary

This table summarizes the attributes used for training the classification model, including their descriptions, statistical test used, and the corresponding test significance (in `−log₁₀(p-value)` form for better readability).

| **Attribute**              | **Description**                                                            | **Test**       | **−log₁₀(p-value)** |
|---------------------------|-----------------------------------------------------------------------------|----------------|----------------------|
| Race                      | Ethnicity of the patient                                                   | Chi-square     | ∞                    |
| milk_consumption          | Milk consumption habit                                                     | Chi-square     | 66.88                |
| MeanCellVolumn            | Mean corpuscular volume (MCV)                                              | t-test         | 39.80                |
| BMI                       | Body Mass Index                                                            | t-test         | 39.37                |
| PIR                       | Poverty Income Ratio                                                       | t-test         | 38.81                |
| RedCellDistributionWidth | Red cell distribution width                                                | t-test         | 36.75                |
| Hemoglobin                | Hemoglobin concentration                                                   | t-test         | 30.21                |
| Age                       | Age of the patient                                                         | t-test         | 15.55                |
| Triglycerides             | Triglyceride level in blood                                                | t-test         | 14.65                |
| FastingGlucose            | Fasting blood glucose level                                                | t-test         | 8.12                 |
| Creatinine                | Serum creatinine concentration                                             | t-test         | 6.31                 |
| HDLCholesterol            | High-density lipoprotein cholesterol level                                 | t-test         | 4.20                 |
| SmokeFam                  | Family members who smoke                                                   | Chi-square     | 2.78                 |
| Gender                    | Gender of the patient                                                      | Chi-square     | 1.65                 |

> **Note:** Tests are chosen based on variable type and comparison groups.  
> The value of `−log₁₀(p-value)` is used to represent the p-value in a more readable logarithmic form.
