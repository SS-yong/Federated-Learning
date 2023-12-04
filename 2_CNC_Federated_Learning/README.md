# Federated Learning 

dataset_1. CNC-wax machnine process dataset  <br>
dataset_2. CNC-aluminum machine process dataset				

[Dataset information]  
dataset_1 set consists of 18 process data files. <br>
dataset_2 set consists of 25 process data files.	
				
Assume that the wax and aluminum process data are obtained from different process line, but share the target of predicting yield of process machines.
  
<p align="center"> Figure 1. EDA for aluminum process data </p>

![image](https://github.com/SS-yong/Federated-Learning/assets/108441950/0a11d740-b44c-4670-9bb1-cd03a8b976e9)
   
   
<p align="center"> Figure 2. EDA for Wax process data </p>

![image](https://github.com/SS-yong/Federated-Learning/assets/108441950/22e8b017-4350-4fd6-9c88-fc2489b909c0)

   
<p align="center"> Figure 3. Target distribution </p>

![image](https://github.com/SS-yong/Federated-Learning/assets/108441950/221fa888-a29d-4bd0-9f9a-f1b007a237c1)
   
   
<p align="center"> Figure 4. FL result </p>

![image](https://github.com/SS-yong/Federated-Learning/assets/108441950/21d5c170-aa7d-499e-bee0-93a4e3a50350)


The federated learning strategy used **FedAVG**. <br>
"Two" clients was participated, and iterated a total of 10 rounds. <br>
The first round has a loss value of 293, Accuracy 0.73. <br>
In the last round, a Loss value of 263 and Accuracy of 0.747 were extracted. <br>
