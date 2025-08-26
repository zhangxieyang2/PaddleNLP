import json


def stat_metric_single_label(which='iv'):
    gold_labels = []
    for line in open(f'./data/{which}_data/test.txt', 'r', encoding='utf-8'):
        rec = json.loads(line.strip())
        gold_labels.append(rec['labels'][0])
    pred_labels = []
    for line in open(f'./test_result/{which}_test/test_predictions.json', 'r', encoding='utf-8'):
        rec = json.loads(line.strip())
        pred_labels.append(rec['labels'])
    tp, real_p, pred_p = 0, 0, 0
    for g_label, p_label in zip(gold_labels, pred_labels):
        if g_label == p_label == 1:
            tp += 1
        if g_label == 1:
            real_p += 1
        if p_label == 1:
            pred_p += 1
    print(f'precision:{tp}/{pred_p}', tp / pred_p)
    print(f'recall:{tp}/{real_p}', tp / real_p)


def stat_metric_by_request(which='iv'):
    import requests
    from tqdm import tqdm
    if which == 'iv':
        url = "http://0.0.0.0:8892/taskflow/utc"
    else:
        url = "http://0.0.0.0:8893/taskflow/utc"
    headers = {"Content-Type": "application/json"}

    gold_labels = []
    pred_labels = []
    for line in tqdm(open(f'./data/{which}_data/test.txt', 'r', encoding='utf-8')):
        rec = json.loads(line.strip())
        gold_labels.append(rec['labels'][0])
        data = {"data": {"text": [rec['text_a']]}}
        resp = requests.post(url=url, headers=headers, data=json.dumps(data))
        probs = resp.json()['result'][0]['predictions']
        probs = sorted(probs, key=lambda x: x['score'], reverse=True)
        p_label = probs[0]['label']
        pos_val = '失效' if which == 'iv' else '不可用'
        pred_labels.append(1 if p_label == pos_val else 0)
    tp, real_p, pred_p = 0, 0, 0
    for g_label, p_label in zip(gold_labels, pred_labels):
        if g_label == p_label == 1:
            tp += 1
        if g_label == 1:
            real_p += 1
        if p_label == 1:
            pred_p += 1
    print(f'precision:{tp}/{pred_p}', tp / pred_p)
    print(f'recall:{tp}/{real_p}', tp / real_p)


if __name__ == '__main__':
    stat_metric_single_label('iv')
    # stat_metric_single_label('na')

    stat_metric_by_request(which='iv')
    # stat_metric_by_request(which='na')
