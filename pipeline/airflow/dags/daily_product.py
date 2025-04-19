from airflow import DAG
from dotenv import load_dotenv
from airflow.operators.python_operator import PythonOperator
import datetime

# 환경 설정 
load_dotenv()

# 함수 정의
def get_subway_data():
    pass    

# 기본 인자 설정 (DAG의 설정값)
default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 4, 16),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5)
}

# DAG 정의: 이름, 기본 인자, 실행 주기 등 설정
with DAG(
    'daily_get_api_dag',            
    default_args=default_args,       
    description='매일 API를 통해 데이터 적재 DAG ',
    schedule_interval='@daily',      # Daily
    catchup=False                    # 과거 실행 무시
) as dag:
    
    # 함수
    get_subway_api = PythonOperator(
        task_id='subway',
        python_callable=print_hello
    )

    # 의존성 주입
    get_subway_api