#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interactive HTML Preview Generator
交互式HTML预览生成器

Generates a self-contained HTML file that visualizes the design system
with interactive components, color swatches, typography samples, etc.
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any


class PreviewGenerator:
    """Generate interactive HTML preview of a design system."""

    def __init__(self, input_file: Optional[str] = None, output: str = "preview.html",
                 preset: Optional[str] = None, theme: str = "light",
                 title: Optional[str] = None):
        self.input_file = input_file
        self.output = output
        self.preset = preset
        self.theme = theme
        self.title = title

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

    def generate(self) -> str:
        """Generate HTML preview and return output path."""
        data = self._load_tokens()
        tokens = data.get("tokens", {})
        meta = data.get("metadata", {})
        name = data.get("name", "Design System")
        title = self.title or f"{name} Design System Preview"

        colors = tokens.get("colors", [])
        typography = tokens.get("typography", [])
        spacing = tokens.get("spacing", [])
        shadows = tokens.get("shadows", [])
        border_radius = tokens.get("borderRadius", [])
        animations = tokens.get("animations", [])

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Segoe UI', sans-serif;
            background: #f5f5f7;
            color: #1d1d1f;
            line-height: 1.6;
            padding: 0;
        }}
        .header {{
            background: linear-gradient(135deg, {colors[0]['value'] if colors else '#6366F1'}, {colors[1]['value'] if len(colors) > 1 else '#8B5CF6'});
            color: white;
            padding: 48px 24px;
            text-align: center;
        }}
        .header h1 {{ font-size: 32px; font-weight: 700; margin-bottom: 8px; }}
        .header p {{ font-size: 16px; opacity: 0.9; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 32px 24px; }}
        .section {{ margin-bottom: 48px; }}
        .section-title {{
            font-size: 24px; font-weight: 700; margin-bottom: 24px;
            padding-bottom: 12px; border-bottom: 2px solid #e5e5e5;
        }}
        .color-grid {{
            display: grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 16px;
        }}
        .color-swatch {{
            border-radius: 12px; overflow: hidden; background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        }}
        .color-preview {{ height: 80px; }}
        .color-info {{ padding: 12px; }}
        .color-name {{ font-weight: 600; font-size: 14px; margin-bottom: 4px; }}
        .color-value {{ font-family: 'SF Mono', monospace; font-size: 12px; color: #666; }}
        .color-usage {{ font-size: 11px; color: #999; margin-top: 4px; }}
        .color-variants {{ display: flex; gap: 4px; margin-top: 8px; }}
        .color-variant {{
            width: 24px; height: 24px; border-radius: 6px;
            border: 1px solid rgba(0,0,0,0.1);
        }}
        .typo-sample {{ margin-bottom: 24px; padding: 20px; background: white;
            border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }}
        .typo-meta {{ font-size: 12px; color: #999; margin-top: 8px;
            font-family: 'SF Mono', monospace; }}
        .spacing-demo {{ display: flex; align-items: center; gap: 16px;
            margin-bottom: 12px; flex-wrap: wrap; }}
        .spacing-bar {{ background: #6366F1; border-radius: 4px; height: 32px; }}
        .spacing-label {{ font-size: 13px; color: #666; min-width: 120px; }}
        .shadow-card {{
            display: inline-block; padding: 32px; margin: 12px;
            background: white; border-radius: 12px; text-align: center;
        }}
        .radius-demo {{
            display: inline-flex; align-items: center; justify-content: center;
            width: 80px; height: 80px; margin: 8px;
            background: linear-gradient(135deg, #6366F1, #8B5CF6);
            color: white; font-size: 12px;
        }}
        .footer {{ text-align: center; padding: 32px; color: #999; font-size: 13px; }}
        .badge {{
            display: inline-block; padding: 2px 8px; border-radius: 4px;
            font-size: 11px; background: rgba(0,0,0,0.05); color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎨 {name}</h1>
        <p>{data.get('description', '')}</p>
        <p style="margin-top: 8px; font-size: 13px; opacity: 0.7;">
            Generated by DesignPilot v1.0.0
        </p>
    </div>
    <div class="container">"""

        # Colors section
        if colors:
            html += """
        <div class="section">
            <h2 class="section-title">🎨 Color Palette</h2>
            <div class="color-grid">"""
            for c in colors:
                variants_html = ""
                if c.get("variants"):
                    variants_html = '<div class="color-variants">'
                    for vk, vv in c["variants"].items():
                        variants_html += f'<div class="color-variant" style="background:{vv}" title="{vk}: {vv}"></div>'
                    variants_html += "</div>"
                html += f"""
                <div class="color-swatch">
                    <div class="color-preview" style="background:{c.get('value', '#ccc')}"></div>
                    <div class="color-info">
                        <div class="color-name">{c.get('name', '')}</div>
                        <div class="color-value">{c.get('value', '')}</div>
                        <div class="color-usage">{c.get('description', '')}</div>
                        {variants_html}
                    </div>
                </div>"""
            html += "\n            </div>\n        </div>"

        # Typography section
        if typography:
            html += """
        <div class="section">
            <h2 class="section-title">✏️ Typography</h2>"""
            for t in typography:
                size = t.get("size", "14px")
                weight = t.get("weight", "400")
                family = t.get("family", "sans-serif")
                line_height = t.get("line_height", "1.6")
                letter_spacing = t.get("letter_spacing", "0")
                sample_text = "DesignPilot 设计系统" if "heading" in t.get("name", "").lower() else "The quick brown fox jumps over the lazy dog. 设计系统预览文字。"
                html += f"""
            <div class="typo-sample">
                <div style="font-family:{family};font-size:{size};font-weight:{weight};line-height:{line_height};letter-spacing:{letter_spacing};">
                    {sample_text}
                </div>
                <div class="typo-meta">
                    {t.get('name', '')} | {family[:40]} | {size} | {weight} | LH:{line_height}
                </div>
            </div>"""
            html += "\n        </div>"

        # Spacing section
        if spacing:
            html += """
        <div class="section">
            <h2 class="section-title">📐 Spacing Scale</h2>"""
            for s in spacing:
                val = s.get("value", "8px")
                try:
                    num = float(val.replace("px", "").replace("rem", "").replace("em", ""))
                    if "rem" in val:
                        num *= 16
                    width = max(num, 8)
                except (ValueError, TypeError):
                    width = 8
                html += f"""
            <div class="spacing-demo">
                <span class="spacing-label">{s.get('name', '')}: {val}</span>
                <div class="spacing-bar" style="width:{width}px;"></div>
            </div>"""
            html += "\n        </div>"

        # Shadows section
        if shadows:
            html += """
        <div class="section">
            <h2 class="section-title">🌓 Shadows</h2>"""
            for s in shadows:
                html += f"""
            <div class="shadow-card" style="box-shadow:{s.get('value', '')}">
                <div style="font-weight:600;margin-bottom:4px;">{s.get('name', '')}</div>
                <div style="font-size:11px;color:#999;">{s.get('value', '')}</div>
            </div>"""
            html += "\n        </div>"

        # Border Radius section
        if border_radius:
            html += """
        <div class="section">
            <h2 class="section-title">⬜ Border Radius</h2>"""
            for r in border_radius:
                html += f"""
            <div class="radius-demo" style="border-radius:{r.get('value', '0px')}">
                {r.get('value', '')}
            </div>"""
            html += "\n        </div>"

        # Animations section
        if animations:
            html += """
        <div class="section">
            <h2 class="section-title">✨ Animations</h2>
            <table style="width:100%;border-collapse:collapse;background:white;border-radius:12px;overflow:hidden;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                <thead>
                    <tr style="background:#f5f5f5;">
                        <th style="padding:12px;text-align:left;">Name</th>
                        <th style="padding:12px;text-align:left;">Duration</th>
                        <th style="padding:12px;text-align:left;">Easing</th>
                        <th style="padding:12px;text-align:left;">Usage</th>
                    </tr>
                </thead>
                <tbody>"""
            for a in animations:
                html += f"""
                    <tr style="border-top:1px solid #eee;">
                        <td style="padding:12px;font-weight:600;">{a.get('name', '')}</td>
                        <td style="padding:12px;"><code>{a.get('duration', '')}</code></td>
                        <td style="padding:12px;"><code>{a.get('easing', '')}</code></td>
                        <td style="padding:12px;color:#666;">{a.get('usage', '')}</td>
                    </tr>"""
            html += """
                </tbody>
            </table>
        </div>"""

        # AI Prompt section
        if meta.get("ai_prompt_hint"):
            html += f"""
        <div class="section">
            <h2 class="section-title">🤖 AI Prompt</h2>
            <div style="background:white;padding:20px;border-radius:12px;box-shadow:0 2px 8px rgba(0,0,0,0.08);">
                <p style="color:#666;margin-bottom:12px;">Copy this prompt and use it with your AI coding tool:</p>
                <code style="display:block;padding:16px;background:#f5f5f5;border-radius:8px;font-size:13px;line-height:1.6;white-space:pre-wrap;">{meta['ai_prompt_hint']}</code>
            </div>
        </div>"""

        html += f"""
    </div>
    <div class="footer">
        <p>🎨 Generated by <strong>DesignPilot</strong> v1.0.0</p>
        <p>Lightweight AI Design System Extraction & Visualization Engine</p>
    </div>
</body>
</html>"""

        output_path = Path(self.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(html, encoding='utf-8')

        return str(output_path)
