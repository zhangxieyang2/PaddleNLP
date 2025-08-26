# Copyright (c) 2022 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from paddlenlp import SimpleServer, Taskflow

# The schema changed to your defined schema
schema = ['未失效', '失效']
# The task path changed to your best model path
pred_threshold = 0
max_seq_len = 2048
utc = Taskflow(
    "zero_shot_text_classification", model="utc-base", task_path="../../checkpoint/iv_model_best/plm", schema=schema,
    pred_threshold=pred_threshold, max_seq_len=max_seq_len
)
# If you want to define the finetuned utc service
app = SimpleServer()
app.register_taskflow("taskflow/utc", utc)
