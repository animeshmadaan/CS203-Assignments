# CS203 Assignment#1

## Simulation of Bertrand’s Paradox

### Content
1. First way (Mid-Point) of sampling is to take mid-point of the chord from a uniform random distribution over the 2D space.
2. Second way (End-Point) is to fix one point on the perimeter of the circle and pick the other one from a uniform random distribution over the periphery of the circle.
3. Third way (Radial) is to take the distance of the chord from the centre of the circle from a uniform random distribution over the range [0,radius].


### Instructions
First of all install the requirements using the following command
```bash
pip install -r requirements.txt
```

For seeing the results, run 
```bash
python main.py <method_name>
``` 
Where method name can be any of the following 
1. `mid_point` - sample the chord over the location of its mid-point. 
2. `end_point` - sample the chord over the angle from the triangle side
3. `radial` - sample the chord by uniform distribution over the distance of chord from centre.
4. `all` - simulate all the methods in the above order

