Machine Learning for Bio-inspired Photonics
==================================
### Dr Gen Kamita
### Bio-inspired Photonics group, Cambridge

![alt text](https://dl.dropboxusercontent.com/u/3543207/polliaFruit.png "Fruit of Pollia Condensata")

*Left: Berries of Pollia Condensata. Right: Colourful cells of Polia taken with a microscope.*

Briliant colours found in nature are often not created from pigments, but are results of light interacting with extrodinarily intricate structures that are about 100 times smaller than human hair. Nature's shiniest blue fruit of Pollia Condensata, also known for its ever-lasting colour, uses cellulose microfibrils to make such structure. Inspired by the Pollia fruit, we study cellulos in order to create materials with such structural colour for sensing, security printing and other applications.

Understanding the relationship between colour and structure is important for developing our materials, but this turns out to be an extremely difficult task. This is because bio-photonic structures often incoorporates complicated features, which makes the materials difficult to analise opticaly. In order to build optical models that truely represents our materials, it is important to understand their structures in small regions and also characterise the overall trend of the material. However, conventional methods are not very useful for solving this problem, because they are difficult to automate. 

This type of difficulty is caused by a fundamental limitation of non-linear optimisation, which is the fact that the output of the optimisation processes heavily relies on constraints (and starting points). Because there is no general method to automaticaly produce good constraints (except for simple problems), an optimisation program can easily fall into a "local minimum", a false solution, rather than a "global minimum", the true solution that we are looking for. Quantum computers are expected to be able to find global minima very effectively, however they are not expected to be available in the near future. This means that we cannot access the statistical properties of our materials without losing the detailed information, eventhough we do have the necesary optical data for that. 

To solve this dilemma, I developed a simple and powerful machine-learning technique that allows automatic analysis of optical data. This method can be applied for other problems.
