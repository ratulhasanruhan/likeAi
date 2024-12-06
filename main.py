import json
from difflib import get_close_matches


def load_data() -> dict:
    with open('brain.json') as file:
        data = json.load(file)
    return data


def save_knowledge(data: dict):
    with open('brain.json', 'w') as file:
        json.dump(data, file, indent=4)


def find_matches(user_input: str, questions: list[str]) -> str or None:
    matches: list = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    if matches:
        return matches[0]
    return None


def main():
    data = load_data()
    questions = list(data.keys())

    while True:
        user_input = input('You: ')
        if user_input.lower() == 'exit':
            break

        match = find_matches(user_input, questions)
        if match:
            print(f'Bot: {data[match]}')
        else:
            print('Bot: Sorry, I don\'t know the answer to that question. Please teach me. Or enter "Skip" to skip.')
            answer = input('You: ')
            if answer.lower() == 'skip':
                continue
            else:
                data[user_input] = answer
                questions.append(user_input)
                save_knowledge(data)


if __name__ == '__main__':
    main()
