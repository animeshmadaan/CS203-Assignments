# Generalized Monty Hall Problem

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
python monty.py
```
A surface plot of $n$, $k$ versus $\frac{P(win | W)}{P(win | T)}$ is displayed, where $n$ is the number of doors and $k$ is the number of cars. 
$W$ denotes switching whereas $T$ denoted sticking. 

### Simulation
The simulation goes in the following steps &rarr;

1. Gates are build as array of $n-k$ $G's$ (goats) and $k$ $C's$ (cars).
2. Person from audience picks any gate out of the $n$ gates. So a random number less than $n$ is picked.
3. Host Opens a gate that contains a goat.(Chooses randomly from the $n-k$ gates).
4. Person from audience is given the choice of switiching to a different gate (obviously other than the first chosen gate and the gate opened by the host).
5. A random number less than $n$ excluding the first two choices is chosen, signifying the new choice of the person, if they wish to switch.
6. If originally chosen gate had a car, `win_og` is increased, signifying a win in the condition of not switching.
7. If newly chosen gate contains a car then, `win_sw` is increased, signifying a win in the condition of switching.
8. This experiment is repeated for $num$ iterations for every combination of $n$ and $k$
9. In both the cases, the corresponding probability is number of wins by number of trials

### Logic

Here, the probability $P(win | W)$ is calculated as follows -
$$P(win | W) = P(C) * P(win | W | C) + P( \overline{C} ) * P(win | W | \overline{C})$$
$$P(win | W) = \frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}$$
where $C$ denoted the event of choosing a door with car behind it before switching.
$W$ denotes switching whereas $T$ denoted sticking. 

The probability $P(win | T)$ can be calculated trivially as follows -
$$P(win | T) = P(C) = \frac{k}{n}$$

Therefore,
$$\frac{P(win | W)}{P(win | T)} = \frac{\frac{k}{n} * \frac{k - 1}{n - 2} + \frac{n - k}{n} * \frac{k}{n - 2}}{\frac{k}{n}}$$
$$\frac{P(win | W)}{P(win | T)} = \frac{n - 1}{n - 2}$$