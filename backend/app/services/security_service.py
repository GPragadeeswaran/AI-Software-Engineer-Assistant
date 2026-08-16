from app.utils.repository_scanner import RepositoryScanner
from app.utils.source_detector import SourceDetector    
from app.utils.repository_filter import RepositoryFilter


class SecurityService:

    SECURITY_PATTERNS = {
        "hardcoded_password": [
            "password=",
            "passwd=",
            "pwd="
        ],
        "hardcoded_secret": [
            "secret=",
            "api_key=",
            "apikey=",
            "access_token="
        ],
        "dangerous_eval": [
            "eval("
        ],
        "dangerous_exec": [
            "exec("
        ],
        "debugger": [
            "breakpoint(",
            "pdb.set_trace("
        ]
    }

    def detect_security_issues(self, repository_path: str):

        issues = []

        for file in RepositoryScanner.scan_files(repository_path):
            
            if not RepositoryFilter.is_valid_file(file):
                continue

            if not SourceDetector.is_source_file(file):
                continue

            try:
                content = file.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()

            except Exception:
                continue

            for issue_type, patterns in self.SECURITY_PATTERNS.items():

                for pattern in patterns:

                    if pattern in content:

                        relative_path = file.relative_to(
                            repository_path
                        )

                        issues.append({
                            "type": issue_type,
                            "file": str(relative_path),
                            "pattern": pattern
                        })

        return {
            "risk_count": len(issues),
            "issues": issues
        }