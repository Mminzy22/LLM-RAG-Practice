import time
from transformers import AutoTokenizer, AutoModelForCausalLM, MarianMTModel, MarianTokenizer

# 시작 시간 기록
start_time = time.time()

# Llama-2-7b 모델 로드
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="auto",
    offload_folder="offload",
    offload_state_dict=True
)

# 번역 모델 설정 (영어 -> 한국어)
src_lang = "en"
tgt_lang = "ko"
translation_model_name = f"Helsinki-NLP/opus-mt-tc-big-{src_lang}-{tgt_lang}"
translation_tokenizer = MarianTokenizer.from_pretrained(translation_model_name)
translation_model = MarianMTModel.from_pretrained(translation_model_name)

# 입력 메시지
input_text = "How is Korea?"
inputs = tokenizer(input_text, return_tensors="pt")

# 텍스트 생성
outputs = model.generate(**inputs, max_length=50)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(f"생성된 텍스트: {generated_text}")

# 번역 함수
def translate_text(text, src_lang="en", tgt_lang="ko"):
    inputs = translation_tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = translation_model.generate(**inputs)
    return translation_tokenizer.decode(translated[0], skip_special_tokens=True)

# 생성된 텍스트를 번역
translated_text = translate_text(generated_text)
print(f"번역된 텍스트: {translated_text}")

# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f}초")
