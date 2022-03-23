# 代码规范测试
import pylint.lint

pylint_opts = ["-ry","./max_subarray_solve.py"]

pylint.lint.Run(pylint_opts)