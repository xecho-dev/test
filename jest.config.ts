  collectCoverage: true,
  coverageThreshold: {
    global: {
      branches: 80,
      functions: 80,
      lines: 80,
      statements: 80
    }
  },
  coverageDirectory: "coverage",
  coveragePathIgnorePatterns: ["/node_modules/", "/dist/"],
  coverageProvider: "v8",
  collectCoverageFrom: ["src/**/*.{ts,tsx}", "!src/**/*.d.ts", "!src/**/index.ts"]