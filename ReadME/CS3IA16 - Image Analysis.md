Module Code: CS3IA16

Assignment report Title: Image Analysis

Student number:  28003801, 29007309

Date: 28/10/2022

Actual hrs spent for the assignment: 45

Assignment evaluation (3 key points): Good, Challenging, Informative

# Table of Contents
[Abstract	1](#_Toc117809426)

[Introduction	2](#_Toc117809427)

[Methodology	2](#_Toc117809428)

[Process overview	2](#_Toc117809429)

[Frequency Domain	2](#_Toc117809430)

[FFT & DFT	2](#_Toc117809431)

[High-Pass Filter	4](#_Toc117809432)

[Low-Pass Filter	5](#_Toc117809433)

[Bandpass Filter	6](#_Toc117809434)

[Band Stop Filter	8](#_Toc117809435)

[Fourier Transform Results and Discussions	9](#_Toc117809436)

[Spatial Domain	9](#_Toc117809437)

[Mean Filter	10](#_Toc117809438)

[Median Filter	10](#_Toc117809439)

[Bilateral Filter	11](#_Toc117809440)

[Spatial Domain Results and Discussion	11](#_Toc117809441)

[Mean Squared Error (MSE)	11](#_Toc117809442)

[Conclusion	12](#_Toc117809443)

[References	13](#_Toc117809444)

[Appendix	14](#_Toc117809445)

[Frequency domain code	14](#_Toc117809446)

[Spatial domain code	16](#_Toc117809447)

[MSE code	17](#_Toc117809448)




# Abstract
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.001.png)
# Introduction 
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.002.png)

# Methodology
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.003.png)

## Process overview
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.004.png)

![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.005.png)
## Frequency Domain
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.006.png)

### FFT & DFT
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.007.png)

![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.008.png)


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.010.png)                  ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.011.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.012.png)|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.013.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.014.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.015.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.016.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.017.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.018.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.011.png)|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.019.png)|
| :- | :-: |


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.020.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.020.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.021.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.021.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.021.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.013.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.015.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.016.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.014.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.011.png)                 ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.022.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.023.png)|
### High-Pass Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.024.png)


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.025.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.026.png)                  ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.027.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.028.png)|



|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.027.png)               ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.029.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.030.png)|



|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.031.png)              ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.032.jpeg) |
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.033.png)|



### Low-Pass Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.034.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.025.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.035.png)              ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.036.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.037.png)|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.036.png)               ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.038.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.039.png)|



|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.040.png)            ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.041.png) |
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.042.png)|











### Bandpass Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.043.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.025.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.044.png)             ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.045.png)|
| :- |
|<p>![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.046.png)</p><p>![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.047.png)</p>|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.045.png)               ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.048.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.049.png)|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.050.png)            ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.051.png)             |
| :-: |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.052.png)|


### Band Stop Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.053.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.025.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.054.png)                  ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.055.png)|
| :-: |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.056.png)|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.009.png)![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.055.png)                     ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.057.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.058.png)|


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.059.png)                      ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.060.png)                        |
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.061.png)|


### Fourier Transform Results and Discussions

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.059.png)                        ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.062.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.063.png)|








## Spatial Domain
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.064.png)


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.059.png)                        ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.065.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.066.png)|



### Mean Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.067.png)


|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.068.png)                          ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.069.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.070.png)|


### Median Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.071.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.072.jpeg)                         ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.073.jpeg)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.074.png)|


### Bilateral Filter
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.075.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.076.png)                                 ![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.077.png)|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.078.png) |

### Spatial Domain Results and Discussion

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.077.png)|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.079.png)|
| :- | :- |

## Mean Squared Error (MSE)
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.080.png)

|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.081.png)|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.082.png)|
| :- | :- |


# Conclusion
![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.083.png)














# References
[1] - homepages.inf.ed.ac.uk. (n.d.). *Digital Filters - Frequency Filters*. [online] Available at: <https://homepages.inf.ed.ac.uk/rbf/HIPR2/freqfilt.htm>.

[2] - Alaa, A. (n.d.). *Week 3: Images in Frequency Domain*. [online] Tutorials for SBME Students. Available at: <https://sbme-tutorials.github.io/2018/cv/notes/3_week3.html>.

[3] - Ed.ac.uk. (2020). *Spatial Filters - Median Filter*. [online] Available at: <https://homepages.inf.ed.ac.uk/rbf/HIPR2/median.htm>.

[4] - www.l3harrisgeospatial.com. (n.d.). *BANDPASS\_FILTER*. [online] Available at: <https://www.l3harrisgeospatial.com/docs/bandpass_filter.html>.

[5] - Wikipedia Contributors (2019). *Mean squared error*. [online] Wikipedia. Available at: <https://en.wikipedia.org/wiki/Mean_squared_error>.

‌

‌


‌

‌

‌








# Appendix
## Frequency domain code

|<p>1.1 - The code includes: low pass, high pass, band pass and band stop filters code.</p><p>CS GitLab Link: <https://csgitlab.reading.ac.uk/xy003801/cs3ia16-image-analysis.git> </p>|
| :- |
|<p>![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.084.png)</p><p></p><p>![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.085.png)</p><p></p>|

























## Spatial domain code

|<p>1.2 – The code includes: mean, media and bilateral filters code.</p><p>`   `CS GitLab Link: <https://csgitlab.reading.ac.uk/xy003801/cs3ia16-image-analysis.git></p>|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.086.png)|



## MSE code

|<p>1.3 – The code includes: code to calculate MSE.</p><p>`          `CS GitLab Link: <https://csgitlab.reading.ac.uk/xy003801/cs3ia16-image-analysis.git></p>|
| :- |
|![](Aspose.Words.7c9835c4-be89-4407-b02f-a04bbb44ced5.087.png)|


