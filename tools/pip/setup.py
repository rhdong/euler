# Copyright 2020 Alibaba Group Holding Limited. All Rights Reserved.
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
# ==============================================================================

import setuptools
import sys

from wheel.bdist_wheel import bdist_wheel as _bdist_wheel


if '--tf_version' in sys.argv:
    tf_version_idx = sys.argv.index('--tf_version')
    tf_version = sys.argv[tf_version_idx + 1]
    sys.argv.remove('--tf_version')
    sys.argv.pop(tf_version_idx)
else:
    import tensorflow as tf
    tf_version = tf.VERSION

print(tf_version)
required_packages = ['ttensorflow=={}'.format(tf_version), 'tqdm', 'scipy==1.1.0', 'networkx==1.11', 'scikit-learn==0.19.1']


class bdist_wheel(_bdist_wheel):
    def finalize_options(self):
        _bdist_wheel.finalize_options(self)
        self.root_is_pure = False


setuptools.setup(name='euler2-gl',
                 version='1.0.0',
                 description='A toolset for network representation learning.',
                 url='https://github.com/alibaba/euler',
                 author='Alibaba Group Holding Limited',
                 author_email='euler-opensource@list.alibaba-inc.com',
                 license='Apache License 2.0',
                 packages=setuptools.find_packages(),
                 package_data={'': ['*.so']},
                 include_package_data=True,
                 install_requires=required_packages,
                 cmdclass={'bdist_wheel': bdist_wheel})
