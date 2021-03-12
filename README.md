# ScoreOptmizer
### 구현방법
1. bias, y term을 모두 symbolize하여 loss function을 정의한다. (sympy를 이용)
2. loss function에 대해 각 bias (ex. 1,2,...12) 및 y에 대한 미분식을 구한다. (sympy.diff() 이용)
3. 각 미분식에 random value로 초기화한다.
4. 이렇게 구한 미분값에 주어진 learning rate 곱하여 -방향으로 미분값을 업데이트한다. ([__gradient_descent 함수](https://github.com/JH-Won/ScoreOptmizer/blob/main/ScoreOptm.py#L104))


### 사용방법
1. impot ScoreOptmizer class.
```python
from ScoreOptm import ScoreOptimizer
```

2. ScoreOptimizer 객체를 생성.
```python
myOptmizer = ScoreOptimizer(score_matrix) # score_matrix is ndarray.
```

3. gradient_descent 메서드를 호출.
```python
bias_updated, y_updated, total_loss = myOptmizer.gradient_descent(learnin_rate=1e-3, n_iteration=1000, verbose=True) 
# If verbose = True, it prints total loss and updated scores(i.e, each ys).
```

### 기타 util:
- ScoreOptmizer.caculate_original_mean_score() := score_matrix의 기존 problem별 평균을 계산한다.
```python
original_mean = myOptmizer.caculate_original_mean_score()
```
- ScoreOptmizer.history := iteration마다의 loss를 기록한 list.
```python
loss_history = myOptmizer.history
```

### 예시
- 폴더 내 test_example 노트북 파일 참고([ScoreOptmizer/test_example.ipynb](https://github.com/JH-Won/ScoreOptmizer/blob/main/test_example.ipynb))


### 업데이트 현황
- 2021.03.12: 초안 완성 (테스트 진행)
