# Copyright (c) 2023 PaddlePaddle Authors. All Rights Reserved.
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

import textwrap

from apibase import APIBase

obj = APIBase("torch.nn.Moudle.register_module")


def test_case_1():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1., 2., 3.])
        module1 = torch.nn.Module()
        module1.register_buffer('buffer', x)
        module2 = torch.nn.Module()
        module2.register_module('submodule', module1)
        result = module2.submodule.buffer
        """
    )
    obj.run(pytorch_code, ["result"])


def test_case_2():
    pytorch_code = textwrap.dedent(
        """
        import torch
        x = torch.tensor([1., 2., 3.])
        module1 = torch.nn.Module()
        module1.register_buffer('buffer', x)
        module2 = torch.nn.Module()
        module2.register_module(name='submodule', module=module1)
        result = module2.submodule.buffer
        """
    )
    obj.run(pytorch_code, ["result"])
