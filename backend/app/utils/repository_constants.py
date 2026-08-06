IMPORTANT_FILES = {
    # Python
    "requirements.txt",
    "pyproject.toml",
    "poetry.lock",
    "uv.lock",

    # JavaScript / TypeScript
    "package.json",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",

    # Java
    "pom.xml",
    "build.gradle",
    "build.gradle.kts",

    # Go
    "go.mod",

    # Rust
    "cargo.toml",
    "cargo.lock",

    # Environment & Configuration
    ".env",
    ".env.example",
    "application.properties",
    "application.yml",
    "application.yaml"
}

IGNORE_FOLDERS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    "node_modules"
}

DATABASE_KEYWORDS = {
            "PostgreSQL": [
                "psycopg2",
                "postgresql://",
                "postgresql+psycopg2"
            ],
            "MySQL": [
                "pymysql",
                "mysql://",
                "mysql"
            ],
            "SQLite": [
                "sqlite3",
                ".db"
            ],
            "MongoDB": [
                "pymongo",
                "mongodb://",
                "mongo"
            ],
            "Redis": [
                "import redis",
                "redis://",
                "redis.Redis("
            ]
        }

API_KEYWORDS = {

            "FastAPI": [
                "fastapi",
                "@app.get",
                "@app.post",
                "@app.put",
                "@app.delete",
                "APIRouter"
            ],

            "Flask": [
                "flask",
                "@app.route",
                "Blueprint"
            ],

            "Django": [
                "django",
                "urlpatterns",
                "path(",
                "re_path("
            ],

            "Express.js": [
                "express",
                "app.get(",
                "app.post(",
                "router.get(",
                "router.post("
            ],

            "Spring Boot": [
                "@RestController",
                "@GetMapping",
                "@PostMapping",
                "@RequestMapping"
            ],

            "ASP.NET Core": [
                "[ApiController]",
                "[HttpGet]",
                "[HttpPost]",
                "MapGet(",
                "MapPost("
            ]
        }

ARCHITECTURE_KEYWORDS = {

    "MVC": [
        "controllers",
        "controller",
        "models",
        "model",
        "views",
        "view"
    ],

    "Clean Architecture": [
        "domain",
        "application",
        "infrastructure",
        "presentation"
    ],

    "Layered": [
        "controller",
        "service",
        "repository",
        "entity"
    ],

    "Microservices": [
        "gateway",
        "discovery",
        "config-server",
        "service-registry"
    ],

    "Monolithic": [
        "app",
        "routes",
        "templates",
        "static"
    ]
}

AUTHENTICATION_KEYWORDS = {

            "JWT": [
                "jwt.encode",
                "jwt.decode",
                "pyjwt",
                "jsonwebtoken",
                "jjwt",
                "jwtbearer",
                "bearer ",
                "authorization: bearer",
                "bearer token"
            ],

            "OAuth": [
                "oauth2passwordbearer",
                "oauth2",
                "oauth",
                "authlib",
                "passport-google-oauth20",
                "spring-security-oauth2",
                "microsoft.aspnetcore.authentication",
                "google.oauth",
                "github.oauth"
            ],

            "Session": [
                "flask_login",
                "login_user",
                "@login_required",
                "request.session",
                "httpsession",
                "express-session",
                "cookie-session",
                "sessionmiddleware"
            ],

            "API Key": [
                "x-api-key",
                "x-auth-token",
                "api_key",
                "apikey",
                "api-token"
            ]
        }

TESTING_KEYWORDS = {

            "pytest": [
                "pytest",
                "import pytest",
                "@pytest"
            ],

            "unittest": [
                "import unittest",
                "unittest.TestCase"
            ],

            "nose": [
                "nose",
                "nosetest"
            ],

            "JUnit": [
                "org.junit",
                "@Test",
                "JUnit"
            ],

            "TestNG": [
                "org.testng",
                "@Test"
            ],

            "Jest": [
                "jest",
                "describe(",
                "test("
            ],

            "Mocha": [
                "mocha",
                "describe(",
                "it("
            ],

            "Vitest": [
                "vitest",
                "describe(",
                "expect("
            ],

            "NUnit": [
                "nunit",
                "[Test]"
            ],

            "xUnit": [
                "xunit",
                "[Fact]"
            ],

            "Go Testing": [
                "testing",
                "func Test"
            ],

            "Cargo Test": [
                "cargo test"
            ]
        }

LICENSE_KEYWORDS = {

            "MIT": [
                "mit license",
                "permission is hereby granted"
            ],

            "Apache 2.0": [
                "apache license",
                "apache license, version 2.0",
                "version 2.0, january 2004"
            ],

            "BSD 3-Clause": [
                "redistribution and use in source and binary forms",
                "neither the name of",
                "all rights reserved"
            ],

            "BSD 2-Clause": [
                "redistribution and use in source and binary forms",
                "this list of conditions and the following disclaimer"
            ],

            "GPL v3": [
                "gnu general public license",
                "version 3"
            ],

            "GPL v2": [
                "gnu general public license",
                "version 2"
            ],

            "LGPL": [
                "gnu lesser general public license"
            ],

            "MPL 2.0": [
                "mozilla public license",
                "version 2.0"
            ],

            "ISC": [
                "isc license"
            ],

            "Unlicense": [
                "this is free and unencumbered software released into the public domain"
            ]
        }

HEALTH_SCORE_WEIGHTS = {

    "readme": 15,

    "architecture": 15,

    "database": 10,

    "api_framework": 15,

    "authentication": 15,

    "testing": 10,

    "docker": 10,

    "cicd": 10,

    "license": 10

}
