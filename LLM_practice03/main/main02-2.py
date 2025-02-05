import time

# 시작 시간 기록
start_time = time.time()

from transformers import AutoTokenizer, AutoModelForCausalLM

# Llama-2-7b 모델 로드 (원래 텍스트 생성 모델)
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    offload_folder="offload",
    offload_state_dict=True
)

# 입력 메시지
input_text = "How is Korea?"
inputs = tokenizer(input_text, return_tensors="pt")

# 텍스트 생성
outputs = model.generate(**inputs, max_length=50)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"생성된 텍스트: {generated_text}")

# 번역 모델 설정
translation_tokenizer = AutoTokenizer.from_pretrained("Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b")
translation_model = AutoModelForCausalLM.from_pretrained("Translation-EnKo/exaone3-instrucTrans-v2-enko-7.8b")

# 번역을 위한 입력 준비
translation_inputs = translation_tokenizer(generated_text, return_tensors="pt", padding=True, truncation=True)

# 번역 실행
translated_outputs = translation_model.generate(**translation_inputs, max_length=100)
translated_text = translation_tokenizer.decode(translated_outputs[0], skip_special_tokens=True)

# 번역된 텍스트 출력
print(f"번역된 텍스트: {translated_text}")

# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f}초")
