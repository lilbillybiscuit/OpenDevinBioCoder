import json
import os

result_path = (
    'evaluation/evaluation_outputs/outputs/biocoder/CodeActAgent/gpt-4o_maxiter_100'
)


def summarize_results(results):
    succ, fail = 0, 0
    java_succ, java_fail = 0, 0
    for result in results:
        if result['test_result']['result'] == 'pass':
            if result['biocoder_instance']['language'] == 'Java':
                java_succ += 1
            else:
                succ += 1
        else:
            if result['biocoder_instance']['language'] == 'Java':
                java_fail += 1
            else:
                fail += 1
    print('Java Success:', java_succ, 'Java Fail:', java_fail)

    print(f'Success: {succ}, Fail: {fail}')

    costs, costs_java = 0, 0
    for result in results:
        if result['biocoder_instance']['language'] == 'Java':
            costs_java += result['metrics']['accumulated_cost']
        else:
            costs += result['metrics']['accumulated_cost']
    print('Total cost:', costs)
    print('Java cost:', costs_java)


if __name__ == '__main__':
    with open(os.path.join(result_path, 'output.jsonl'), 'r') as f:
        results = [json.loads(line) for line in f]
    results = [x for x in results if 'biocoder_instance' in x]
    print(results[0]['test_result']['result'])
    summarize_results(results)
