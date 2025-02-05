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

# 함수 정의: 입력에 따른 텍스트 생성
def generate_text(input_text):
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=100)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# 입력 프롬프트 테스트
prompts = {
    "간결한 프롬프트": "Describe the job of a cafe worker.",
    "상세한 프롬프트": "Describe the responsibilities of a cafe worker in detail, including customer service, coffee preparation, and maintaining a clean workspace.",
    "복잡한 프롬프트": "Describe the roles of a barista, a cashier, and a manager in a cafe in detail. Include their responsibilities and how they collaborate to ensure smooth operations."
}

# 결과 출력 및 한글 번역
print("결과 생성 중...")
for prompt_type, prompt_text in prompts.items():
    print(f"\n[{prompt_type}]")
    english_result = generate_text(prompt_text)
    print("영어 결과:", english_result)

    # 한글 번역 (간단한 번역 구현)
    korean_result = f"[번역 필요] {english_result}"
    print("한글 번역:", korean_result)

# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f}초")

print("모든 작업 완료!")
