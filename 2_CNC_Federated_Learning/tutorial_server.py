from typing import List, Tuple
import flwr as fl
from flwr.common import Metrics

'''
1. Weighted_average : n명의 Client 평가지표(accuracy)를 가중평균하여 출력해주는 함수.
1-1. List[Tuple[int, Metrics]] 형식의 평가지표(accuracy)를 리스트 형식으로 받아옴 -> "weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:"
1-2. 위에서 받아온 평가지표(accuracy)와 사용한 데이터 수(num_examples)를 곱하여 리스트를 만든 뒤 -> "accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]"
1-3. 총 데이터 수(examples)로 나누어 가중평균을 계산하여 반환 ->    " return {"accuracy": sum(accuracies) / sum(examples)} "
'''

def weighted_average(metrics: List[Tuple[int, Metrics]]) -> Metrics:
    # Multiply accuracy of each client by number of examples used
    accuracies = [num_examples * m["accuracy"] for num_examples, m in metrics]
    examples = [num_examples for num_examples, _ in metrics]
    
    # Aggregate and return custom metric (weighted average)
    return {"accuracy": sum(accuracies) / sum(examples)}


'''
2. FedAVG 클래스를 이용해 Server의 Strategy을 정의 (*커스터마이징 정의)
2-1. evaluate_metrics_aggregation_fn 변수로 위에서 정의한 weighted_average 함수를 Strategy으로 사용
2-2. fl.server.start_server 함수를 사용해 Server를 실행
2-3. server_address, config, strategy을 변수로 전달
2-4. 10회 학습(rounds)을 진행하도록 설정됨
'''

strategy = fl.server.strategy.FedAvg(evaluate_metrics_aggregation_fn=weighted_average)
# Start Flower server
fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=10),
    strategy=strategy
)
