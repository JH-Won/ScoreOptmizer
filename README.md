# ScoreOptmizer
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

4. 기타 util:
- ScoreOptmizer.caculate_original_mean_score() := score_matrix의 기존 problem별 평균을 계산한다.
```python
original_mean = myOptmizer.caculate_original_mean_score()
```
- ScoreOptmizer.history := iteration마다의 loss를 기록한 list.
```python
loss_history = myOptmizer.history
```

### 예시
- 폴더 내 test_example 노트북 파일 참고(ScoreOptmizer/test_example.ipynb)


### 업데이트 현황
- 2021.03.12: 초안 완성 (테스트 진행)
