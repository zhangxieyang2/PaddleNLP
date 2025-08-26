python run_eval.py \
    --model_path ./checkpoint/iv_model_best \
    --test_path ./data/iv_data/test.txt \
    --per_device_eval_batch_size 2 \
    --max_seq_len 2048 \
    --output_dir ./test_result/iv_test \
    --single_label True