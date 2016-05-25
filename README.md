Machine Learning for Bio-inspired Photonics
==================================
### Dr Gen Kamita
### Bio-inspired Photonics group, Cambridge

![alt text](https://dl.dropboxusercontent.com/u/3543207/polliaFruit.png "Fruit of Pollia Condensata")

*Left: Berries of Pollia Condensata. Right: Colourful cells of Polia taken with a microscope.*

Briliant colours found in nature are often not created from pigments, but are results of light interacting with extrodinarily intricate structures that are about 100 times smaller than human hair. Nature's shiniest blue fruit of Pollia Condensata, also known for its ever-lasting colour, uses cellulose microfibrils to make such structure. Inspired by the Pollia fruit, we study cellulos in order to create materials with such structural colour for sensing, security printing and other applications.

Understanding the relationship between colour and structure is important for developing our materials but this turns out to be an extremely difficult task. This is because bio-photonic structures often incoorporates disorder, non-uniformity and irregularity, which makes the optical properties of these materials very complicated and difficult to analise. In order to build an optical model that truely represents our materials, it is important to characterise their structures in small regions and also have an overvie of the entire material at the same time, however conventional methods are practically not useful for this.
This is because we almost always have to manually optimise the parameters of the models, which means we can't automate the modeling process effectively. This means that we don't have access to statistical properties of the material because we can't process large ammounts of data.

This type of difficulties is due to a fundamental limitation of non-linear optimisation, and. It is because the output of the optimisation process relies on constraints 
However, these mathematical methods start to show shortcomings when it is used for analysing photonic structures that has complex structures, for example when they contain multiple domains with different periodicity or when they have defects. In such cases, the number of relevant parameters grows as the complexity of the system increases, which makes the parameter optimisation difficult. This type of problem is common in non-linear optimisation. It is because many variable functions have lots of local minimum, which makes it extremely difficult for conventional optimisation algorithm to find the global minimum, unless the constraints  that are used for the optimisation are finely adjusted prior to the optimisation. This means that analysis of complex data have to rely on manual intervention based on prior knowledge of the structure. Even if a simpler approaches are employed, for example by fitting the data to a simple mathematical function rather than a rigorous model, the fact that the correctness of any optimisation method relies on constraints does not change. Therefore, analysis of complex data will always remain difficult to automate, until the day when quantum computer becomes readily available, which is not expected to happen in the near future.

This may sound as a bad news for natural photonics analysis because in nature, disorder, irregularity, non-uniformity and other factors that introduces variations in the optical response are found very commonly. For a concrete characterisation of such structures, one must investigate the statistical nature of the system without loosing grasp of the detailed structural information, which is difficult because the data analysis process is practically impossible to be automated. This fundamental problem has not been confronted properly in previous studies, but was avoided by resorting to crude treatments. These treatments includes introducing arbitral randomness in layer thicknesses in multilayer systems and averaging over angles in 3D photonic crystals, which improved the agreement of the models with experimental results in a qualitative sense, such as broadening of peaks and loss of side fringes, but were unable to reproduce the experimental results with good quantitative agreement.


In this work, we uncover the complex structure of cnc films by a novel method driven by machine learning. Machine learning is showing very cool developments in the recent years and becoming increasingly popular for applications such as recommendation systems, face detection and spam email filtering. The blooming of machine learning is mainly driven by the increase in available computing power and also because of new methods being developed. For example, alphago is really cool. Machine learning is good at dealing with problems involving pattern recognition and classification. We demonstrate that such strength of machine learning can give a dramatical enhancement to for optimisation problems the shortfalls of conventional optimisation methods. In the field of photonics, this hasn’t been done.
