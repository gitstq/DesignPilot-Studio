#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design System Validator - Validate design system consistency
设计系统验证器

Checks for:
- Token naming consistency
- Color format validity
- Spacing scale regularity
- Typography hierarchy completeness
- Missing essential tokens
"""

import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional


class DesignValidator:
    """Validate design system tokens for consistency and completeness."""

    def __init__(self, input_file: Optional[str] = None):
        self.input_file = input_file

    def _load_data(self) -> Dict[str, Any]:
        """Load design system data."""
        if not self.input_file:
            raise ValueError("Input file is required for validation")

        path = Path(self.input_file)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {self.input_file}")

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Try JSON parse
        try:
            data = json.loads(content)
            if "tokens" in data:
                return data
            return {"tokens": data}
        except json.JSONDecodeError:
            # It's a DESIGN.md file, do basic validation
            return self._parse_design_md(content)

    def _parse_design_md(self, content: str) -> Dict[str, Any]:
        """Basic parsing of DESIGN.md for validation."""
        data = {"tokens": {}, "metadata": {}}

        # Count sections
        sections = re.findall(r'^##\s+.+$', content, re.MULTILINE)
        data["metadata"]["sections_found"] = len(sections)

        # Count tables
        tables = content.count("|---|")
        data["metadata"]["tables_found"] = tables

        # Count code blocks
        code_blocks = content.count("```")
        data["metadata"]["code_blocks"] = code_blocks // 2

        return data

    def _validate_colors(self, colors: List[Dict]) -> List[Dict]:
        """Validate color tokens."""
        issues = []
        hex_pattern = re.compile(r'^#[0-9a-fA-F]{3,8}$')
        rgb_pattern = re.compile(r'^rgba?\([^)]+\)$')
        hsl_pattern = re.compile(r'^hsla?\([^)]+\)$')

        for c in colors:
            name = c.get("name", "")
            value = c.get("value", "")

            if not name:
                issues.append({"level": "warning", "category": "colors",
                               "message": "Color token missing name"})

            if not value:
                issues.append({"level": "error", "category": "colors",
                               "message": f"Color '{name}' missing value"})
                continue

            if not (hex_pattern.match(value) or rgb_pattern.match(value) or
                    hsl_pattern.match(value)):
                issues.append({"level": "warning", "category": "colors",
                               "message": f"Color '{name}' has unusual format: {value}"})

        return issues

    def _validate_typography(self, typography: List[Dict]) -> List[Dict]:
        """Validate typography tokens."""
        issues = []

        for t in typography:
            name = t.get("name", "")
            if not name:
                issues.append({"level": "warning", "category": "typography",
                               "message": "Typography token missing name"})
            if not t.get("family") and not t.get("size"):
                issues.append({"level": "warning", "category": "typography",
                               "message": f"Typography '{name}' has neither family nor size"})

        return issues

    def _validate_spacing(self, spacing: List[Dict]) -> List[Dict]:
        """Validate spacing tokens."""
        issues = []
        value_pattern = re.compile(r'^-?\d+(?:\.\d+)?(?:px|rem|em|%)$')

        for s in spacing:
            name = s.get("name", "")
            value = s.get("value", "")

            if not value:
                issues.append({"level": "error", "category": "spacing",
                               "message": f"Spacing '{name}' missing value"})
                continue

            if not value_pattern.match(value):
                issues.append({"level": "warning", "category": "spacing",
                               "message": f"Spacing '{name}' has unusual value: {value}"})

        return issues

    def _validate_completeness(self, data: Dict[str, Any]) -> List[Dict]:
        """Check for essential tokens."""
        issues = []
        tokens = data.get("tokens", {})

        # Check for essential categories
        categories = ["colors", "typography", "spacing"]
        for cat in categories:
            if not tokens.get(cat):
                issues.append({"level": "warning", "category": "completeness",
                               "message": f"Missing token category: {cat}"})

        # Check for primary color
        colors = tokens.get("colors", [])
        color_names = [c.get("name", "").lower() for c in colors]
        if "primary" not in color_names:
            issues.append({"level": "info", "category": "completeness",
                           "message": "No 'primary' color defined"})

        # Check for body typography
        typo_names = [t.get("name", "").lower() for t in tokens.get("typography", [])]
        if not any("body" in n for n in typo_names):
            issues.append({"level": "info", "category": "completeness",
                           "message": "No 'body' typography defined"})

        return issues

    def validate(self) -> Dict[str, Any]:
        """Run full validation and return report."""
        data = self._load_data()
        tokens = data.get("tokens", {})

        all_issues = []
        all_issues.extend(self._validate_colors(tokens.get("colors", [])))
        all_issues.extend(self._validate_typography(tokens.get("typography", [])))
        all_issues.extend(self._validate_spacing(tokens.get("spacing", [])))
        all_issues.extend(self._validate_completeness(data))

        # Calculate score
        errors = sum(1 for i in all_issues if i["level"] == "error")
        warnings = sum(1 for i in all_issues if i["level"] == "warning")
        infos = sum(1 for i in all_issues if i["level"] == "info")

        score = max(0, 100 - (errors * 20) - (warnings * 5) - (infos * 2))

        return {
            "score": score,
            "total_issues": len(all_issues),
            "errors": errors,
            "warnings": warnings,
            "infos": infos,
            "issues": all_issues,
            "token_summary": {
                "colors": len(tokens.get("colors", [])),
                "typography": len(tokens.get("typography", [])),
                "spacing": len(tokens.get("spacing", [])),
                "shadows": len(tokens.get("shadows", [])),
                "borderRadius": len(tokens.get("borderRadius", [])),
                "breakpoints": len(tokens.get("breakpoints", [])),
                "animations": len(tokens.get("animations", [])),
            },
        }

    def print_report(self, report: Dict[str, Any]):
        """Print validation report to console."""
        print(f"\n{'='*50}")
        print(f"📊 Design System Validation Report")
        print(f"{'='*50}")
        print(f"  Score: {report['score']}/100")
        print(f"  Errors: {report['errors']} | Warnings: {report['warnings']} | Info: {report['infos']}")
        print(f"\n  Token Summary:")
        for cat, count in report["token_summary"].items():
            if count > 0:
                print(f"    {cat}: {count}")

        if report["issues"]:
            print(f"\n  Issues ({len(report['issues'])}):")
            for issue in report["issues"]:
                icon = {"error": "❌", "warning": "⚠️ ", "info": "ℹ️ "}.get(issue["level"], "•")
                print(f"    {icon} [{issue['category']}] {issue['message']}")

        print(f"{'='*50}")
