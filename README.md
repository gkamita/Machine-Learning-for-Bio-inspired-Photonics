Machine Learning for Bio-inspired Photonics
==================================
### Dr Gen Kamita
### Bio-inspired Photonics group, Cambridge

![alt text](https://dl.dropboxusercontent.com/u/3543207/polliaFruit.png "Fruit of Pollia Condensata")

*Left: Berries of Pollia Condensata. Right: Colourful cells of Polia taken with a microscope.*

Briliant colours found in nature are often not created from pigments, but are results of light interacting with extrodinarily intricate structures that are about 100 times smaller than human hair. Nature's shiniest blue fruit of Pollia Condensata, also known for its ever-lasting colour, uses cellulose microfibrils to make such structure. Inspired by the Pollia fruit, we study cellulos in order to create materials with such structural colour for sensing, security printing and other applications.

Understanding the relationship between colour and structure is important for developing our materials, but this turns out to be an extremely difficult task. This is because bio-photonic structures often incoorporates complicated features, which makes the materials difficult to analise opticaly. In order to build optical models that truely represents our materials, it is important to understand their structures in small regions and also characterise the overall trend of the material. However, conventional methods are not very useful for solving this problem, because they are difficult to automate. 

This type of difficulty is caused by a fundamental limitation of non-linear optimisation, which is the fact that the output of the optimisation processes heavily relies on constraints (and starting points). Because there is no general method to automaticaly produce good constraints (except for simple problems), an optimisation program can easily fall into a "local minimum", a false solution, rather than a "global minimum", the true solution that we are looking for. Quantum computers are expected to be able to find global minima very effectively, however they are not expected to be available in the near future. This means that we cannot access the statistical properties of our materials without losing the detailed information of the structure, eventhough the necesary optical data are accessible. 

To solve this dilemma, I developed a simple and powerful machine-learning technique that allows automatic analysis of complicated optical data. Unlike other mathematical methods, machine learing algorythms excel in pattern recognition. If we concider our optical signals as patterns, a machine leraning algorythm can clasify the signals depending on the features they have. Based on the determined classification, we can generate constraints that can be used for the following optimisation process. We use an artificial neural networkr algorythm for the classification or example,  to recognise optical data that have one peak and two peaks. The label produced by this neural network is used for generating constraints for the next step of the analysis. The following picture shows a peak detection result which used the label. It is clear
an example in which is used in the following This method can be applied for other problems.
