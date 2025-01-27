import time

start_time = time.time()

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

model= AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b-chat-hf",
    device_map="cpu",
    offload_folder="offload",
    offload_state_dict=True
    )

# 입력 메시지
input_text = "How is korea?"
inputs = tokenizer(input_text, return_tensors="pt")

# 텍스트 생성
outputs = model.generate(**inputs, max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))


# 종료 시간 기록
end_time = time.time()

# 실행 시간 출력
execution_time = end_time - start_time
print(f"실행 시간: {execution_time:.6f}초")
# auto : 398.860001초 / 6.65분
# CPU: 1097.478652초 / 18.29분