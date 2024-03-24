# Birthday Paradox

### Instructions
This is a source code written in `python`. This can be run on any machine having a python interpreter installed. 

Ensure that the aforementioned interpreter is added to `PATH`

- Go to the directory in which the code is saved 
- Install the requirements
```bash 
pip install -r requirements.txt
```
- Run the following command in the *terminal* 
```bash
python birthday_paradox.py
```
- You will get a prompt to enter the probability `p` and enter required value in the form of a **percentage value**
- The output `k` will be printed in the terminal

If you want to see a plot of probabilty of atleast two people having the same birthday as number of people increases then run the following command in the *terminal*
```bash
python birthday_paradox.py graph
```

### Logic

In the class it was already derived that the probability of no two students having the same birthday is given by 

$$p_k = \frac{^{365}P_k}{365^k}$$
where $k$ is the number of students in the class

This can be simplified as 
$$p_k = \frac{365!}{(365-k)! \cdot 365^k}$$

we can write this recursively as 
$$p_k = p_{k-1} \cdot \frac{365-k}{365}$$

Hence by starting with $p_1 = 1$, we can recursively get the next $p_k$ and compare to find the smallest such $k$ for which $p_k$ is less than $p_n$, i.e the smallest number of students for which probabilty of having at least two students with the same birthday ( $1-p_k$ ) is greater than the given probability ( $1-p_n$)