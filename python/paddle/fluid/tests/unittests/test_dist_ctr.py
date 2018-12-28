#   Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
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
from __future__ import print_function

import os
import unittest
from test_dist_base import TestDistBase


# FIXME(tangwei): sum op can not handle when inputs is empty.
class TestDistCTR2x2(TestDistBase):
    def _setup_config(self):
        self._sync_mode = True
        self._enforce_place = "CPU"

    def test_dist_ctr(self):
        self.check_with_place("dist_ctr.py", delta=1e-7, check_error_log=False)


class TestDistCTR2x2WithL2Decay(TestDistBase):
    def _setup_config(self):
        self._sync_mode = True
        self._enforce_place = "CPU"

    def test_dist_ctr(self):
        self.check_with_place(
            "dist_ctr_with_l2_decay.py", delta=1e-7, check_error_log=False)


if __name__ == "__main__":
    unittest.main()
