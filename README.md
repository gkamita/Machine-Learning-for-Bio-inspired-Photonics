Machine Learning for Bio-inspired Photonics
==================================
### Dr Gen Kamita
### Bio-inspired Photonics group, Cambridge

![alt text](https://dl.dropboxusercontent.com/u/3543207/polliaFruit.png "Fruit of Pollia Condensata")

*Left: Berries of Pollia Condensata. Right: Colourful cells of Polia taken with a microscope.*

Briliant colours found in nature are often not created from pigments, but are results of light interacting with extrodinarily intricate structures that are about 100 times smaller than human hair. Nature's shiniest blue fruit of Pollia Condensata, also known for its ever-lasting colour, uses cellulose microfibrils to make such structure. Inspired by the Pollia fruit, we study cellulos in order to create materials with such structural colour for sensing, security printing and other applications.

Understanding the relationship between colour and structure is important for developing our materials, but this turns out to be an extremely difficult task. This is because bio-photonic structures often incoorporates features that are difficult to model, which makes the optical response of these materials very complicated and difficult to analise. In order to build optical models that truely represents our materials, it is important to characterise their structures in small regions and also get an overview of the entire material at the same time. However, conventional methods are practically not useful for solving this problem, because they are difficult to automate effectively. This means that we cannot access the statistical properties of our materials without losing the detailed information of the structure, because we cannot analyse large ammount of data.

This type of difficulty is caused by a fundamental limitation of non-linear optimisation, which is the fact that the output of the optimisation processes heavily relies on constraints and starting points. Because there is no general method to automaticaly produce good constraints and starting points (except for simple problems), the optimisation program can easily fall into a "local minimum" rather than a "global minimum", i.e. the true solution that we are looking for. Quantum computers are expected to be able to find the "global minimum" very effectively, however they are not expected to be available in the near future.

To solve this, I developed a machine-learning technique. 
