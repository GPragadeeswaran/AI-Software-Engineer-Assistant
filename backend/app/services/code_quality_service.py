import ast

from app.utils.repository_scanner import RepositoryScanner
from app.utils.source_detector import SourceDetector
from app.utils.repository_filter import RepositoryFilter


class CodeQualityService:

    LARGE_FILE_LIMIT = 500
    LARGE_FUNCTION_LIMIT = 50

    def detect_code_quality(self, repository_path: str):

        total_lines = 0
        large_files = []
        large_functions = []
        high_complexity_functions = []
        todo_count = 0
        debug_count = 0

        for file in RepositoryScanner.scan_files(repository_path):

            if not RepositoryFilter.is_valid_file(file):
               continue

            if not SourceDetector.is_source_file(file):
                continue

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception:
                continue

            lines = content.splitlines()
            line_count = len(lines)

            total_lines += line_count

            # Large file detection
            if line_count > self.LARGE_FILE_LIMIT:

                relative_path = file.relative_to(repository_path)

                large_files.append({
                    "file": str(relative_path),
                    "lines": line_count
                })

            # Python function analysis
            if file.suffix.lower() == ".py":

                try:
                    tree = ast.parse(content)

                except SyntaxError:
                    continue

                for node in ast.walk(tree):

                    if isinstance(
                        node,
                        (ast.FunctionDef, ast.AsyncFunctionDef)
                    ):

                        if not node.body:
                            continue

                        start_line = node.lineno
                        end_line = node.end_lineno

                        function_lines = end_line - start_line + 1

                        complexity = self.calculate_complexity(node)

                        relative_path = file.relative_to(
                            repository_path
                        )

                        if function_lines > self.LARGE_FUNCTION_LIMIT:

                            large_functions.append({
                                "file": str(relative_path),
                                "function": node.name,
                                "lines": function_lines
                            })

                        if complexity > 10:

                            high_complexity_functions.append({
                                "file": str(relative_path),
                                "function": node.name,
                                "complexity": complexity
                            })
            # TODO / FIXME and debug detection
            for line in lines:

                line_lower = line.lower()

                if "todo" in line_lower or "fixme" in line_lower:
                    todo_count += 1

                if (
                    "print(" in line_lower
                    or "breakpoint(" in line_lower
                    or "pdb.set_trace(" in line_lower
                ):
                    debug_count += 1

        return {
            "total_lines": total_lines,
            "large_files": large_files,
            "large_functions": large_functions,
            "high_complexity_functions": high_complexity_functions,
            "todo_count": todo_count,
            "debug_count": debug_count
        }

    def calculate_complexity(self, tree):

        complexity = 1

        for node in ast.walk(tree):

            if isinstance(
                node,
                (
                    ast.If,
                    ast.For,
                    ast.While,
                    ast.Try,
                    ast.With
                )
            ):
                complexity += 1

            elif isinstance(
                node,
                ast.BoolOp
            ):
                complexity += len(node.values) - 1

            elif isinstance(
                node,
                ast.ExceptHandler
            ):
                complexity += 1

        return complexity