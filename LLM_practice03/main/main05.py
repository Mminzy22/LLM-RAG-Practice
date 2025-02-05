import os
import time
from transformers import AutoTokenizer, AutoModelForCausalLM
from dotenv import load_dotenv

# 시작 시간 기록
start_time = time.time()

# .env 파일 로드
load_dotenv()
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

if not HUGGINGFACE_TOKEN:
    raise ValueError("Hugging Face Access Token이 .env 파일에 저장되어 있어야 합니다.")

# 모델과 토크나이저 불러오기
print("모델 로드 중...")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    offload_folder="offload",
    offload_state_dict=True
)
print("모델 로드 완료!")

# 프롬프트 템플릿
prompt_template = """
You are a cafe worker.

Question: {question}

Answer: 
"""

# 입력 데이터 정의
input_data = {
    "question": "What is your favorite drink?"
}

# 프롬프트 생성
prompt = prompt_template.format(**input_data)

# 함수 정의: 입력에 따른 텍스트 생성
def generate_text(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=50)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 텍스트 생성 실행
print("결과 생성 중...")
result = generate_text(prompt)
print("생성된 텍스트:", result)

# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f}초")

print("모든 작업 완료!")
