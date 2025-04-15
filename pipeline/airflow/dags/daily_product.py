from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import datetime

# DAG에서 실행할 함수 정의
def print_hello():
    print("Hello, Airflow!")

# 기본 인자 설정 (DAG의 설정값)
default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 4, 16),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5)
}

# DAG 정의: 이름, 기본 인자, 실행 주기 등 설정
with DAG(
    'example_hello_dag',            # DAG 이름
    default_args=default_args,       # 기본 인자
    description='간단한 Hello 메시지를 출력하는 DAG ',
    schedule_interval='@daily',      # 매일 실행하도록 설정
    catchup=False                    # 과거 실행 이력을 무시
) as dag:
    
    # PythonOperator를 사용하여 print_hello 함수 실행
    hello_task = PythonOperator(
        task_id='hello_task',
        python_callable=print_hello
    )

    # DAG 내에서 단일 태스크이므로 의존성 설정은 생략 가능
    hello_task