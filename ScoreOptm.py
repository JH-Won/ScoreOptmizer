import numpy as np
from numpy.core.numeric import NaN
import sympy as sym
from sympy import diff
import math

class ScoreOptimizer:

    # Following constructor has input of score matrix, whose type is numpy.ndarray.
    # Be careful: the scores unassigned should be NaN value. (not 0) 
    def __init__(self, score_matrix):
        assert type(score_matrix) is np.ndarray, "score matrix is not numpy.ndarray!"
        self.score_matrix = score_matrix
        self.n_student = score_matrix.shape[0]
        self.history = []
        
        # set variable symbols.
        self.b_sym, self.y_sym = self.__set_symbols()
        
        # symbolize loss and its partial derivatives w.r.t each variables(i.e., each ys and bs). 
        self.loss = self.__sympify_loss()
        self.db, self.dy = self.__sympify_derivatives()

    # Gradient descent algorithm.
    # If verbose = True, it prints total loss and updated scores(i.e, each ys).
    def gradient_descent(self, learning_rate = 1e-3, n_iteration = 1000, verbose = False):
        # initialize each variables with random values.
        b_numeric = np.random.rand(self.n_student,)
        y_numeric = np.random.rand(self.n_student,)
        self.history.clear()

        # do gradient descent for given iteration, and caculate the total loss.
        total_loss = 0  
        for i in range(n_iteration):
            b_numeric, y_numeric = self.__gradient_descent(b_numeric, y_numeric, learning_rate)
            total_loss = self.__calculate_total_loss(b_numeric, y_numeric)
            self.history.append(total_loss)

            if verbose:
                print(f'iteration {i+1} ======================')
                print(f'total loss    : {total_loss}')
                print(f'updated score : {y_numeric}')

        return b_numeric, y_numeric, total_loss           
    
    # cacluate mean of the original scores from score matrix.
    def caculate_original_mean_score(self):
        mean_scores = []
        # note that each row is a reviewer, each column is a problem.
        for i in range(self.n_student):
            val = 0
            n = 0
            for j in range(self.n_student): 
                if math.isnan(self.score_matrix[j,i]):
                    continue
                n += 1
                val += self.score_matrix[j,i]
            if val <= 0:
                mean_scores.append(0)
            else: 
                mean_scores.append(val / n)
        return mean_scores


    ## Following functions are just helper methods to set functions above. ##
    def __set_symbols(self):
        b_term = ""
        y_term = ""

        for i in range(self.n_student):
            b_term += f"b{i} "
            y_term += f"y{i} "

        return list(sym.symbols(b_term)), list(sym.symbols(y_term))


    def __sympify_loss(self):
        score_mat = self.score_matrix
        y_terms = self.y_sym
        b_terms = self.b_sym

        # symbolize the loss with symbols.
        loss = ""
        for i in range(self.n_student): # i-th problem
            for j in range(self.n_student): # j-th reviewer
                if math.isnan(score_mat[j,i]):
                    continue
                loss += f"+({score_mat[j,i]} - {y_terms[i]} - {b_terms[j]})**2 + {b_terms[j]}**2"
        loss = loss[1:]
        
        return sym.sympify(loss)


    def __sympify_derivatives(self):
        loss = self.loss
        db_list = []
        dy_list = []
        # symbolize derivatives w.r.t each variables using sympy. 
        for term in self.b_sym:
            db_list.append(diff(loss, term))
        for term in self.y_sym:
            dy_list.append(diff(loss, term))
        
        return db_list, dy_list


    def __gradient_descent(self, b_numeric, y_numeric, lr):
        # db, dy are just symbolized derivative lists w.r.t each bs and ys. 
        db = self.db
        dy = self.dy  

        partial_b_val = []
        partial_y_val = []

        # Following codes are important part: apply real value to symbolized derivatives, and evaluate derivatives values.
        # db:
        for i in range(self.n_student):
            free_vals = list(db[i].free_symbols)
            subs_pair = []
            for j in range(self.n_student):
                if self.b_sym[j] in free_vals:
                    subs_pair.append((self.b_sym[j], b_numeric[j]))
                if self.y_sym[j] in free_vals:
                    subs_pair.append((self.y_sym[j], y_numeric[j]))          
            partial_b_val.append(db[i].subs(subs_pair))
        # dy:
        for i in range(len(dy)):
            free_vals = list(dy[i].free_symbols)
            subs_pair = []
            for j in range(self.n_student):
                if self.b_sym[j] in free_vals:
                    subs_pair.append((self.b_sym[j], b_numeric[j]))
                if self.y_sym[j] in free_vals:
                    subs_pair.append((self.y_sym[j], y_numeric[j]))   
            partial_y_val.append(dy[i].subs(subs_pair))

        partial_b_val = np.asfarray(partial_b_val).reshape(-1,)
        partial_y_val = np.asfarray(partial_y_val).reshape(-1,)

        # outputs are updated b values and y values.
        return b_numeric - partial_b_val * lr, y_numeric - partial_y_val * lr


    def __calculate_total_loss(self, b_numeric, y_numeric):
        loss = 0
        score_mat = self.score_matrix
        for i in range(self.n_student): # i-th problem
            for j in range(self.n_student): # j-th reviewer
                if math.isnan(score_mat[j,i]):
                    continue
                loss += (score_mat[j,i] - y_numeric[i] - b_numeric[j])**2 + b_numeric[j]**2
        return loss
