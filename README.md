# StringAlignmentProblem
Dynamic Programming + Divide &amp; Conquer approach to String Alignment Problem


![image](https://user-images.githubusercontent.com/39965156/172039357-9f67659a-7664-4f30-b5e7-deba9c2e2b77.png)


![image](https://user-images.githubusercontent.com/39965156/172039197-29be6e76-9e34-4a64-a699-6e19bae8f4ad.png)
Nature of the Graph
Basic: Polynomial
Efficient: Linear
Explanation:
The space requirement for the basic Dynamic Programming algorithm for the sequence alignment problem is 𝑶(𝑴∗𝑵). 
The space complexity grows polynomially with the increase in the input size (The input size is M+N, where M and N are the lengths of two input strings). 
This polynomial nature of the graph is due to the fact that the computation of optimal alignment between two input strings of length M and N, 
respectively requires building-up a 2-dimensional M-by-N array of optimal solutions to the subproblems (Also, each of the 𝑀∗𝑁 cells of the 2-D array take constant space).The space requirement for the efficient algorithm (Divide and Conquer coupled with Dynamic Programming) is 𝑶(𝑴+𝑵). 
The space complexity grows linearly with the increase in the input size (The input size is M+N, where M and N are the lengths of two input strings). 
The memory consumption is efficient due to the fact that the problem is being solved recursively thereby reusing the working space from one call to the next.

![image](https://user-images.githubusercontent.com/39965156/172039244-70d41669-7d8e-4d40-8767-8fe6778f8ed2.png)
Nature of the Graph
Basic: Polynomial
Efficient: Polynomial
Explanation:
The running time or the time complexity for the basic dynamic programming algorithm for the sequence alignment problem is 𝑶(𝑴∗𝑵).
It can be observed from the above graph that the running time grows polynomially with the increase in the input size (The input size is M+N).
This polynomial nature of the graph is due to the fact that the computation of optimal alignment between two input strings of length M and N, 
respectively requires building-up a 2-dimensional M-by-N array of optimal solutions to the subproblems (Also, it takes constant time to fill each of the 𝑀∗𝑁 cells of the 2-D array).
The efficient solution (Divide and Conquer coupled with Dynamic Programming) has a time complexity of 𝑶(𝑴∗𝑵).
It is clear from the above graph that the running time grows polynomially with the increase in the input size (The input size is M+N).
This polynomial nature can be easily identified by analysing the algorithm summing up the times at every level:
Σ(𝐶∗𝑀∗𝑁+𝐶∗𝑀∗𝑁2+ 𝐶∗𝑀∗𝑁4+⋯)=2∗𝑀∗𝑁= 𝑂(𝑀∗𝑁)
