#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Design Document Generator - Generate DESIGN.md from tokens or presets
设计文档生成器

Generates structured DESIGN.md files that AI coding tools can understand
and use to generate pixel-perfect UI components.
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any


class DesignDocGenerator:
    """Generate DESIGN.md documentation from design tokens."""

    def __init__(self, input_file: Optional[str] = None, output: str = "DESIGN.md",
                 preset: Optional[str] = None, lang: str = "zh",
                 include_preview: bool = False):
        self.input_file = input_file
        self.output = output
        self.preset = preset
        self.lang = lang
        self.include_preview = include_preview

    def _load_tokens(self) -> Dict[str, Any]:
        """Load tokens from file or preset."""
        if self.preset:
            from .presets import get_preset
            return get_preset(self.preset)
        elif self.input_file:
            with open(self.input_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            if "tokens" in data:
                return data
            return {"tokens": data}
        else:
            raise ValueError("Either --input or --preset must be provided")

    def _generate_zh(self, data: Dict[str, Any]) -> str:
        """Generate Chinese DESIGN.md."""
        tokens = data.get("tokens", {})
        meta = data.get("metadata", {})
        name = data.get("name", "Design System")
        version = data.get("version", "1.0.0")
        desc = data.get("description", "")

        lines = [
            f"# 🎨 {name} Design System",
            "",
            f"> **版本**: v{version} | **生成工具**: DesignPilot v1.0.0",
            "",
            f"## 📋 概述",
            "",
            f"{desc}",
            "",
        ]

        # Design Philosophy
        if meta.get("design_philosophy"):
            lines.extend([
                "## 💡 设计理念",
                "",
                f'> {meta["design_philosophy"]}',
                "",
            ])

        # AI Prompt Hint
        if meta.get("ai_prompt_hint"):
            lines.extend([
                "## 🤖 AI 提示词",
                "",
                "将以下提示词与 DESIGN.md 一起提供给 AI 编码工具，以获得最佳效果：",
                "",
                "```",
                meta["ai_prompt_hint"],
                "```",
                "",
            ])

        # Colors
        colors = tokens.get("colors", [])
        if colors:
            lines.extend([
                "## 🎨 色彩体系",
                "",
                "| 名称 | 色值 | 变体 | 用途 |",
                "|------|------|------|------|",
            ])
            for c in colors:
                variants = ", ".join(f"{k}:{v}" for k, v in c.get("variants", {}).items())
                lines.append(
                    f"| {c.get('name', '')} | `{c.get('value', '')}` "
                    f"| {variants or '-'} | {c.get('usage', '')} |"
                )
            lines.append("")
            lines.extend([
                "### CSS 变量",
                "",
                "```css",
                ":root {",
            ])
            for c in colors:
                var_name = c.get("name", "").lower().replace(" ", "-")
                lines.append(f"  --color-{var_name}: {c.get('value', '')};")
                for vk, vv in c.get("variants", {}).items():
                    lines.append(f"  --color-{var_name}-{vk}: {vv};")
            lines.extend(["}", "```", ""])

        # Typography
        typo = tokens.get("typography", [])
        if typo:
            lines.extend([
                "## ✏️ 字体排版",
                "",
                "| 名称 | 字体 | 大小 | 字重 | 行高 | 用途 |",
                "|------|------|------|------|------|------|",
            ])
            for t in typo:
                lines.append(
                    f"| {t.get('name', '')} | {t.get('family', '')[:30]} | "
                    f"{t.get('size', '')} | {t.get('weight', '')} | "
                    f"{t.get('line_height', '')} | {t.get('usage', '')} |"
                )
            lines.append("")
            lines.extend([
                "### CSS 变量",
                "",
                "```css",
                ":root {",
            ])
            for t in typo:
                var_name = t.get("name", "").lower().replace(" ", "-")
                if t.get("family"):
                    lines.append(f"  --font-{var_name}-family: {t['family']};")
                if t.get("size"):
                    lines.append(f"  --font-{var_name}-size: {t['size']};")
                if t.get("weight"):
                    lines.append(f"  --font-{var_name}-weight: {t['weight']};")
                if t.get("line_height"):
                    lines.append(f"  --font-{var_name}-line-height: {t['line_height']};")
                if t.get("letter_spacing"):
                    lines.append(f"  --font-{var_name}-letter-spacing: {t['letter_spacing']};")
            lines.extend(["}", "```", ""])

        # Spacing
        spacing = tokens.get("spacing", [])
        if spacing:
            lines.extend([
                "## 📐 间距系统",
                "",
                "| 名称 | 值 | 用途 |",
                "|------|------|------|",
            ])
            for s in spacing:
                lines.append(
                    f"| {s.get('name', '')} | `{s.get('value', '')}` | {s.get('usage', '')} |"
                )
            lines.append("")

        # Shadows
        shadows = tokens.get("shadows", [])
        if shadows:
            lines.extend([
                "## 🌓 阴影系统",
                "",
                "| 名称 | 值 | 用途 |",
                "|------|------|------|",
            ])
            for s in shadows:
                lines.append(
                    f"| {s.get('name', '')} | `{s.get('value', '')}` | {s.get('usage', '')} |"
                )
            lines.append("")

        # Border Radius
        radius = tokens.get("borderRadius", [])
        if radius:
            lines.extend([
                "## ⬜ 圆角系统",
                "",
                "| 名称 | 值 | 用途 |",
                "|------|------|------|",
            ])
            for r in radius:
                lines.append(
                    f"| {r.get('name', '')} | `{r.get('value', '')}` | {r.get('usage', '')} |"
                )
            lines.append("")

        # Breakpoints
        breakpoints = tokens.get("breakpoints", [])
        if breakpoints:
            lines.extend([
                "## 📱 响应式断点",
                "",
                "| 名称 | 值 | 说明 |",
                "|------|------|------|",
            ])
            for b in breakpoints:
                lines.append(
                    f"| {b.get('name', '')} | `{b.get('value', '')}` | {b.get('description', '')} |"
                )
            lines.append("")

        # Animations
        animations = tokens.get("animations", [])
        if animations:
            lines.extend([
                "## ✨ 动效系统",
                "",
                "| 名称 | 时长 | 缓动函数 | 用途 |",
                "|------|------|----------|------|",
            ])
            for a in animations:
                lines.append(
                    f"| {a.get('name', '')} | {a.get('duration', '')} | "
                    f"{a.get('easing', '')} | {a.get('usage', '')} |"
                )
            lines.append("")

        # Footer
        lines.extend([
            "---",
            "",
            f"*由 [DesignPilot](https://github.com/gitstq/DesignPilot) v1.0.0 自动生成*",
            "",
        ])

        return "\n".join(lines)

    def _generate_en(self, data: Dict[str, Any]) -> str:
        """Generate English DESIGN.md."""
        tokens = data.get("tokens", {})
        meta = data.get("metadata", {})
        name = data.get("name", "Design System")
        version = data.get("version", "1.0.0")
        desc = data.get("description", "")

        lines = [
            f"# 🎨 {name} Design System",
            "",
            f"> **Version**: v{version} | **Generated by**: DesignPilot v1.0.0",
            "",
            f"## 📋 Overview",
            "",
            f"{desc}",
            "",
        ]

        if meta.get("design_philosophy"):
            lines.extend([
                "## 💡 Design Philosophy",
                "",
                f'> {meta["design_philosophy"]}',
                "",
            ])

        if meta.get("ai_prompt_hint"):
            lines.extend([
                "## 🤖 AI Prompt",
                "",
                "Use this prompt alongside the DESIGN.md for best results with AI coding tools:",
                "",
                "```",
                meta["ai_prompt_hint"],
                "```",
                "",
            ])

        colors = tokens.get("colors", [])
        if colors:
            lines.extend([
                "## 🎨 Color Palette",
                "",
                "| Name | Value | Variants | Usage |",
                "|------|-------|----------|-------|",
            ])
            for c in colors:
                variants = ", ".join(f"{k}:{v}" for k, v in c.get("variants", {}).items())
                lines.append(
                    f"| {c.get('name', '')} | `{c.get('value', '')}` "
                    f"| {variants or '-'} | {c.get('usage', '')} |"
                )
            lines.append("")
            lines.extend([
                "### CSS Variables",
                "",
                "```css",
                ":root {",
            ])
            for c in colors:
                var_name = c.get("name", "").lower().replace(" ", "-")
                lines.append(f"  --color-{var_name}: {c.get('value', '')};")
                for vk, vv in c.get("variants", {}).items():
                    lines.append(f"  --color-{var_name}-{vk}: {vv};")
            lines.extend(["}", "```", ""])

        typo = tokens.get("typography", [])
        if typo:
            lines.extend([
                "## ✏️ Typography",
                "",
                "| Name | Family | Size | Weight | Line Height | Usage |",
                "|------|--------|------|--------|------------|-------|",
            ])
            for t in typo:
                lines.append(
                    f"| {t.get('name', '')} | {t.get('family', '')[:30]} | "
                    f"{t.get('size', '')} | {t.get('weight', '')} | "
                    f"{t.get('line_height', '')} | {t.get('usage', '')} |"
                )
            lines.append("")

        spacing = tokens.get("spacing", [])
        if spacing:
            lines.extend([
                "## 📐 Spacing Scale",
                "",
                "| Name | Value | Usage |",
                "|------|-------|-------|",
            ])
            for s in spacing:
                lines.append(
                    f"| {s.get('name', '')} | `{s.get('value', '')}` | {s.get('usage', '')} |"
                )
            lines.append("")

        shadows = tokens.get("shadows", [])
        if shadows:
            lines.extend([
                "## 🌓 Shadows",
                "",
                "| Name | Value | Usage |",
                "|------|-------|-------|",
            ])
            for s in shadows:
                lines.append(
                    f"| {s.get('name', '')} | `{s.get('value', '')}` | {s.get('usage', '')} |"
                )
            lines.append("")

        radius = tokens.get("borderRadius", [])
        if radius:
            lines.extend([
                "## ⬜ Border Radius",
                "",
                "| Name | Value | Usage |",
                "|------|-------|-------|",
            ])
            for r in radius:
                lines.append(
                    f"| {r.get('name', '')} | `{r.get('value', '')}` | {r.get('usage', '')} |"
                )
            lines.append("")

        breakpoints = tokens.get("breakpoints", [])
        if breakpoints:
            lines.extend([
                "## 📱 Breakpoints",
                "",
                "| Name | Value | Description |",
                "|------|-------|-------------|",
            ])
            for b in breakpoints:
                lines.append(
                    f"| {b.get('name', '')} | `{b.get('value', '')}` | {b.get('description', '')} |"
                )
            lines.append("")

        animations = tokens.get("animations", [])
        if animations:
            lines.extend([
                "## ✨ Animations",
                "",
                "| Name | Duration | Easing | Usage |",
                "|------|----------|--------|-------|",
            ])
            for a in animations:
                lines.append(
                    f"| {a.get('name', '')} | {a.get('duration', '')} | "
                    f"{a.get('easing', '')} | {a.get('usage', '')} |"
                )
            lines.append("")

        lines.extend([
            "---",
            "",
            f"*Generated by [DesignPilot](https://github.com/gitstq/DesignPilot) v1.0.0*",
            "",
        ])

        return "\n".join(lines)

    def generate(self) -> str:
        """Generate DESIGN.md and return output path."""
        data = self._load_tokens()

        if self.lang == "zh":
            content = self._generate_zh(data)
        elif self.lang == "en":
            content = self._generate_en(data)
        else:
            content = self._generate_en(data)

        output_path = Path(self.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(content, encoding='utf-8')

        return str(output_path)
