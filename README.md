# ScoreOptmizer
### Introduction
ScoreOptimizer is an algorithm for reducing biases and getting the most likely scores students should get (i.e., students' unbiased scores). Here, the assumption is that each student has a bias, and scores the problems with that. The algorithm is based on following objective function, ~ . Note that all {b_i} and {y_i} are the parameters which we should find. 


### Implementation steps
Here's how it was implemented:
1. In order to take the partial derivatives for each parameters, we symbolized all parameters and loss function using [python sympy](https://www.sympy.org/en/index.html).
2. We then, took partial derivatives of loss function with respect to each parameters, and kept them in the list.
4. In order to optimize the parameters, the gradient descent was implemented. ([ScoreOptimizer.__gradient_descent](https://github.com/JH-Won/ScoreOptmizer/blob/main/ScoreOptm.py#L104))
5. All of these are included in [ScoreOptimizer class](https://github.com/JH-Won/ScoreOptmizer/blob/main/ScoreOptm.py#L7).


### How to use
1. Download this repository and place ScoreOptm.py into your workspace.
2. Impot ScoreOptmizer class.
```python
from ScoreOptm import ScoreOptimizer
```

2. Create ScoreOptimizer object with score matrix. This will set the loss function from the score matrix.
```python
myOptmizer = ScoreOptimizer(score_matrix) # score_matrix is ndarray.
```

3. Call the gradient_descent mathod to find optimal parameters. You can set the learning rate, iteration number, and verbose.
```python
bias_updated, y_updated, total_loss = myOptmizer.gradient_descent(learnin_rate=1e-3, n_iteration=1000, verbose=True) 
# If verbose = True, it prints total loss and updated scores(i.e, each ys).
```

### Utils
- ScoreOptmizer.caculate_original_mean_score()
:= Calculate the average scores of the problem.
```python
original_mean = myOptmizer.caculate_original_mean_score()
```
- ScoreOptmizer.history
:= The list that tracked loss for each iteration.
```python
loss_history = myOptmizer.history
```

### Example
- Sample score matrix file and [notebook](https://github.com/JH-Won/ScoreOptmizer/blob/main/test_example.ipynb) are in the repository.


### Updates 
- 2021.03.12: first draft.
- 2021.03.23: README.md edited.
