# DFD: Adversarial Learning-based Approach to Defend Against Website Fingerprinting

This project provides the implementation of DFD, website fingerprinting defense by introducing perturbation to the packets sequence.

The project is implemented on top of Deep Fingerprinting: Undermining Website Fingerprinting Defenses with Deep Learning (https://github.com/deep-fingerprinting/df), using the same baseline models and representation. 

### Reference Format
```
Abusnaina, A., Jang, R., Khormali, A., Nyang, D., & Mohaisen, D. 
DFD: Adversarial Learning-based Approach to Defend Against Website Fingerprinting.
IEEE International Conference on Computer Communications (INFOCOM), 2020.
```

The defense propose of the following steps:
1- After sending every burst of packets, defined as packets in the same direction,record the length of the burst.
2- Replay previously sent packets or send dummy packets to the destination. The number of send packets are equal to the perturbation parameter multiplied by the length of the last burst (prior to the one currently appending to). 
3- Periodically, e.g., after each burst or after time window, change the perturbation rate following a normal distribution. This is user configurable parameter.


> The code read the data as represented by (https://github.com/deep-fingerprinting/df), and modifies the traces on the direction-level representation. 
> Note: This code provides only a proof-of-concept, and may or may not work for other data representations. 


