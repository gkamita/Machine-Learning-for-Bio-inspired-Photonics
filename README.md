Machine Learning for Bio-inspired Photonics
==================================
### Dr Gen Kamita
### Bio-inspired Photonics group, Cambridge

![alt text](https://dl.dropboxusercontent.com/u/3543207/polliaFruit.png "Fruit of Pollia Condensata")

*Left: Berries of Pollia Condensata. Right: Colourful cells of Pollia taken with a microscope.*

Brilliant colours found in nature are often not created from pigments, but are results of light interacting with extraordinarily intricate structures that are about 100 times smaller than human hair. Nature's shiniest blue fruit of Pollia Condensata, also known for its ever-lasting colour, uses cellulose microfibrils to make such structure. Inspired by the Pollia fruit, we study cellulose in order to create materials with such structural colour for sensing, security printing and other applications.

Understanding the relationship between colour and structure is important for developing our materials, but this turns out to be an extremely difficult task. This is because bio-photonic structures often incorporate complicated features, which makes the materials difficult to analyse optically. In order to build optical models that truly represent our materials, it is important to understand their structures in small regions and also characterise the overall trend of the material. However, conventional methods are not very useful for solving this problem, because they are difficult to automate. 

This type of difficulty is caused by a fundamental limitation of non-linear optimisation, which is the fact that the output of the optimisation processes heavily relies on constraints (and starting points). Because there is no general method that can automatically produce good constraints except for simple problems, an optimisation program always has the possibility of falling into a "local minimum", a false solution, rather than a "global minimum", the true solution that we are looking for. Quantum computers are considered to be able to find global minima very effectively, however they are not expected to be available in the near future. This means that we cannot access the statistical properties of our materials without losing the detailed information of the structure, even though the necessary optical data are available. 

To solve this dilemma, I developed a simple and powerful machine-learning technique that allows automatic analysis of complicated optical data. Unlike other mathematical methods, machine-learning algorithms excel in pattern recognition. Considering our optical signals as patterns, a machine-learning algorithm can classify the signals based on the features they have. For example, an artificial neural network, which is an algorithm that is used in this study, can be trained to recognise the difference between signals that have one peak and two peaks, without being fooled by less important features such as noise and small amplitude oscillations. Based on the determined classification, we can generate constraints that can be used for the optimisation process that follows afterwards.

The following picture shows results of machine learning driven peak detection. It can be seen that only pronounced peaks are picked up regardless of where it appears, even when there are two peaks that are merging (for more details, please see DetectionProcess.mp4 in this repo). Based on these results, we can create maps and histograms that show the detailed optical character and the statistical character of our sample. A clear correlation is seen between the features in the photograph and the maps, from which we can understand the underlying structural properties in great detail.

We believe that this study is going to be the first example that shows how machine learning can be used for optical data analysis and how it can have a dramatic impact on the output. This technique can be applied for many other problems that are difficult to solve by conventional methods, for example for time series analysis.

