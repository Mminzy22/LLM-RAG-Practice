# Transformer 모델

Transformer 모델은 텍스트 데이터와 같은 순차 데이터를 처리하기 위해 만들어진 딥러닝 모델입니다. Google이 2017년에 발표한 논문 [*Attention Is All You Need*](https://arxiv.org/abs/1706.03762)에서 처음 소개되었으며, 현재 가장 인기 있는 언어 모델인 GPT와 BERT의 기반이 되는 구조입니다.


## Transformer 모델이란?
Transformer는 **문장에서 중요한 단어를 찾고, 각 단어의 의미를 문맥에 맞게 이해**할 수 있는 모델입니다. RNN과 같은 기존 모델은 문장을 순차적으로 처리했지만, Transformer는 병렬로 데이터를 처리하기 때문에 훨씬 빠르고 효율적입니다.


## Transformer의 주요 특징

### 1. Self-Attention 메커니즘
- Self-Attention은 문장 안의 단어들이 서로 어떤 관련이 있는지 계산하는 과정입니다.
- 예를 들어, "고양이가 매트 위에 앉아 있다"라는 문장에서, "고양이"와 "앉아"라는 단어가 서로 밀접한 관련이 있다는 것을 모델이 학습합니다.

### 2. 순서 정보 반영 (Positional Encoding)
- Transformer는 단어의 순서를 자연스럽게 이해하지 못하기 때문에, **단어의 위치 정보**를 추가로 입력해줍니다.
- 이를 통해 모델이 단어의 순서도 고려할 수 있습니다.

### 3. Encoder와 Decoder 구조
Transformer는 두 부분으로 나뉩니다:
- **Encoder**: 입력 문장을 읽고 중요한 정보를 추출합니다.
- **Decoder**: Encoder에서 추출한 정보를 바탕으로 출력 문장을 만듭니다.
- 예를 들어, 영어 문장을 프랑스어로 번역하는 작업에서 Encoder는 영어 문장을 이해하고, Decoder는 프랑스어 문장을 생성합니다.

### 4. Multi-Head Attention
- 한 번의 Attention 계산만으로는 부족할 수 있기 때문에, 여러 번 병렬로 계산합니다.
- 이를 통해 모델이 문장의 다양한 측면을 동시에 이해할 수 있습니다.


## Transformer의 장점

1. **빠른 처리 속도**
   - 데이터를 한 번에 처리하기 때문에 RNN보다 훨씬 빠릅니다.

2. **긴 문맥도 잘 이해**
   - 문장이 길어도 중요한 단어들 간의 관계를 잘 파악합니다.

3. **다양한 활용 가능성**
   - 언어 처리뿐만 아니라 이미지 처리, 음성 인식 등에도 사용됩니다.


## Transformer의 활용 예

1. **BERT**
   - 문장을 양방향으로 이해하여 질문 답변, 문서 분류와 같은 작업에서 뛰어난 성능을 보이는 모델입니다.

2. **GPT**
   - 글을 쓰거나 대화를 생성하는 데 특화된 모델로, 자연스러운 문장을 만듭니다.

3. **Vision Transformer (ViT)**
   - 텍스트가 아닌 이미지 데이터를 처리하기 위해 Transformer를 사용한 모델입니다.

